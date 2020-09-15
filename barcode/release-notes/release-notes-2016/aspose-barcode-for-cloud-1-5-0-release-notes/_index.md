---
title: "Aspose.BarCode for Cloud 1.5.0 Release Notes"
type: docs
url: /aspose-barcode-for-cloud-1-5-0-release-notes/
weight: 40
---

{{% alert color="primary" %}} 

The page contains release notes for Aspose.BarCode for Cloud update 1.5.0 – [API Version 1.1](http://api.aspose.com/v1.1/swagger/ui/index)

{{% /alert %}} 
## **Full List of Issues Covering all Changes in this Release**

|**Key** |**Summary** |**Category** |
| :- | :- | :- |
|BARCODENET-33812 |Support GS1QR code |Feature |
|BARCODENET-3426 |Add MaxiCode implementation |Feature |
### **Public API and Backward Incompatible Changes**
###### **New values of ManualHints have been added**
MedianSmoothing - Starts recognition barcodes with the special form of cells. Example: dot peen datamatrix. The MaxQuality mode includes this flag by default. 
SpecialFormOfCells - MedianSmoothing. This value deals with the MedianSmoothingWindowSize property. The MaxQuality mode includes this flag by default. 
UseRegular - Starts recognition using algorithms from MaxPerfomance mode. It maybe helpful in the combination with the other hints. 
UseRestoration - Starts recognition using only the restoration algorithms from MaxQuality mode. 
###### **BinarizationHints have been excluded**
BinarizationHints are obsolete and have been removed.
