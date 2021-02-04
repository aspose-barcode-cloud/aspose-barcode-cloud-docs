---
title: "Aspose.BarCode Cloud 21.2 Release Notes"
type: docs
url: /aspose-barcode-cloud-21-2-release-notes/
weight: 8
---

{{% alert color="primary" %}}

The page contains release notes for Aspose.BarCode for Cloud 21.2 – [API Reference](https://apireference.aspose.cloud/barcode/)

{{% /alert %}}

## Complete List of Changes Covered in this Release

- Update Aspose.BarCode for .Net to version 21.1 (previous version was 20.12):
  - [Aspose.BarCode for .Net to version 21.1 Release Notes](https://docs.aspose.com/barcode/net/aspose-barcode-for-net-21-01-release-notes/)

## SDK Changes

### Aspose.BarCode Cloud SDKs ( .NET, Java, Node.js, Python, PHP, Go)

Update to new [Aspose.BarCode Cloud 21.2](/barcode/aspose-barcode-cloud-21-2-release-notes/)

### New parameters

#### Recognize barcode

- **CheckMore1DVariants** Allows engine to recognize 1D barcodes with checksum by checking more recognition variants. Default value: False

#### Generate barcode

- Barcode type **Pdf417**
  - **MacroTimeStamp** Macro Pdf417 barcode time stamp
  - **MacroSender** Macro Pdf417 barcode sender name
  - **MacroFileSize** Macro Pdf417 file size. The file size field contains the size in bytes of the entire source file
  - **MacroChecksum** Macro Pdf417 barcode checksum. The checksum field contains the value of the 16-bit (2 bytes) CRC checksum using the CCITT-16 polynomial
  - **MacroFileName** Macro Pdf417 barcode file name
  - **MacroAddressee** Macro Pdf417 barcode addressee name
  - **MacroECIEncoding** Extended Channel Interpretation Identifiers. Applies for Macro PDF417 text fields
