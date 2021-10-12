---
title: "Aspose.BarCode Cloud 21.10 Release Notes"
type: docs
url: /aspose-barcode-cloud-21-10-release-notes/
weight: 60
---

{{% alert color="primary" %}}

The page contains release notes for Aspose.BarCode for Cloud 21.10 – [API Reference](https://apireference.aspose.cloud/barcode/)

{{% /alert %}}

## **Complete List of Changes Covered in this Release**

- Update Aspose.BarCode for .Net to version 21.9 (previous version was 21.6):
  - [Aspose.BarCode for .Net to version 21.7 Release Notes](https://docs.aspose.com/barcode/net/aspose-barcode-for-net-21-7-release-notes/)
  - [Aspose.BarCode for .Net to version 21.8 Release Notes](https://docs.aspose.com/barcode/net/aspose-barcode-for-net-21-8-release-notes/)
  - [Aspose.BarCode for .Net to version 21.9 Release Notes](https://docs.aspose.com/barcode/net/aspose-barcode-for-net-21-9-release-notes/)

- Default font changed to support more characters

### **New Recognize parameters**

- **FastScanOnly** Allows engine for 1D barcodes to quickly recognize middle slice of an image and return result without using any time-consuming algorithms. Default value: False.

- **IgnoreEndingFillingPatternsForCTable** The flag which force AustraliaPost decoder to ignore last filling patterns in Customer Information Field during decoding as CTable method. CTable encoding method does not have any gaps in encoding table and sequnce "333" of filling paterns is decoded as letter "z".
