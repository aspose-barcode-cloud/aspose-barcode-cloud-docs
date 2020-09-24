---
title: "Aspose.BarCode for Cloud 1.6.0 Release Notes"
type: docs
url: /aspose-barcode-for-cloud-1-6-0-release-notes/
weight: 30
---

{{% alert color="primary" %}} 

The page contains release notes for Aspose.BarCode for Cloud update 1.6.0 – [API Version 1.1](http://api.aspose.com/v1.1/swagger/ui/index). Codebase has been upgraded to Aspose.Barcode for .NET version: 7.8.0.0 in this release.

{{% /alert %}} 
## **Full List of Issues Covering all Changes in this Release**

|**Key** |**Summary** |**Category** |
| :- | :- | :- |
|BARCODENET-34363 |Add new BarCode type: Code32 |Feature |
|BARCODENET-34364 |Add new BarCode type: Datalogic2of5 |Feature |
|BARCODENET-34368 |Add new BarCode type: MICR (only reader) |Feature |
|BARCODENET-34399 |Add a manual hint "SkipRotatedBarcodes" |Feature |
### **Public API and Backward Incompatible Changes**
#### **Add a manual hint "SkipRotatedBarcodes"**
SkipRotatedBarCodes - Switches off rotation algorithms when BarCode recognition is in process.
This allows BarCodeReader to increase the recognition speed.
It is applicable only to Datamatrix and 1D-barcodes. 
