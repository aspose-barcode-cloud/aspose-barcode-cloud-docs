import os
import re
from collections import namedtuple
import operator
from typing import List

RELEASE_NOTES_RE = re.compile(r'release-notes-(?P<key>\d+)')
BARCODE_VERSION_RE = re.compile(r'aspose-barcode(?:-for)?-cloud-(\d+)-(\d+)(?:-(\d+))?-release-notes')

WEIGHT_RE = re.compile(r'^\s*weight:\s*(?P<weight>\d+)\s*$')

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

RELEASE_NOTES_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', 'barcode', 'release-notes'))
assert os.path.isdir(RELEASE_NOTES_DIR)

Item = namedtuple('Item', ('key', 'weight', 'memo'))


def list_dirs(root: str):
    return [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]


def get_weight_from_index(index_filename: str) -> int:
    with open(index_filename, 'rt') as f:
        for line in f.readlines():
            match = WEIGHT_RE.match(line)
            if match:
                return int(match.groupdict()['weight'])
        else:
            raise Exception(f"Pattern {WEIGHT_RE.pattern} not found in '{index_filename}'")


def get_dir_weight(dirname: str) -> int:
    index = os.path.join(dirname, '_index.md')
    return get_weight_from_index(index)


def extract_version(s: str, regex: re.Pattern) -> tuple[int]:
    match = regex.match(s)
    assert match, f"String {s} doesn't match '{regex.pattern}'"
    return tuple(int(d) for d in match.groups() if d is not None)


def assert_sorted(items: List[Item]) -> bool:
    reverse_sorted_items = sorted(items, key=operator.attrgetter('key'), reverse=True)
    prev_item = None
    for item in reverse_sorted_items:
        if prev_item is None:
            prev_item = item
            continue

        assert item.weight > prev_item.weight, f"'{item.memo}.weight' should be greater than '{prev_item.memo}.weight'"
        return False
    return True


def check_sorted(root, regex):
    items = []
    for dir_name in list_dirs(root):
        version = extract_version(dir_name, regex)
        weight = get_dir_weight(os.path.join(root, dir_name))
        items.append(Item(key=version, weight=weight, memo=dir_name))

    return assert_sorted(items)


def main():
    items = []
    for rn in list_dirs(RELEASE_NOTES_DIR):
        check_sorted(os.path.join(RELEASE_NOTES_DIR, rn), BARCODE_VERSION_RE)
        key = extract_version(rn, RELEASE_NOTES_RE)
        weight = get_dir_weight(os.path.join(RELEASE_NOTES_DIR, rn))
        items.append(Item(key=key, weight=weight, memo=rn))
    assert_sorted(items)
    print("All release notes sorted!")


if __name__ == '__main__':
    main()
