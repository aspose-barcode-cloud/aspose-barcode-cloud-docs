---
title: "Manage and Optimize a Barcode Recognition Without Cloud Storage"
type: docs
url: /manage-and-optimize-a-barcode-recognition-without-cloud-storage/
weight: 20
---

## **Introduction**
This API lets you recognize a barcode from file on the server with parameters in the request body.

## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/recognize|POST|Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image or encoded with base64|[PostBarcodeRecognizeFromUrlOrContent](https://apireference.aspose.cloud/barcode/#/Barcode/PostBarcodeRecognizeFromUrlOrContent)|
The description of important API parameters and their valid values are given below:

|**Parameter**|**Valid values**|**Description**|
| :- | :- | :- |
|Type|Codabar, Code11, Code39Standard, Code39Extended, Code93Standard, Code93Extended,<br>Code128, GS1Code128, EAN8, EAN13, EAN14, SCC14, SSCC18, UPCA, UPCE, ISBN, ISSN,<br>ISMN, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, ITF14,<br>ITF6, MSI, VIN, DeutschePostIdentcode, DeutschePostLeitcode, OPC, PZN, Code16K,<br>Pharmacode, DataMatrix, QR, Aztec, Pdf417, MacroPdf417, AustraliaPost, Postnet,<br>Planet, OneCode, RM4SCC, DatabarOmniDirectional, DatabarTruncated, DatabarLimited,<br>DatabarExpanded, SingaporePost, GS1DataMatrix, AustralianPosteParcel,<br>SwissPostParcel, PatchCode, DatabarExpandedStacked, DatabarStacked,<br>DatabarStackedOmniDirectional, MicroPdf417, GS1QR, MaxiCode, Code32, DataLogic2of5,<br>DotCode, DutchKIX, UpcaGs1Code128Coupon, UpcaGs1DatabarCoupon, CodablockF, GS1CodablockF|<p>(Optional parameter)</p><p>Type of barcode to generate</p>|
|ChecksumValidation|Default, On, Off|<p>(Optional parameter)</p><p>Enable checksum validation during recognition for 1D barcodes.<br>Default is treated as Yes for symbologies which must contain checksum, as No where checksum only possible.<br>Checksum never used: Codabar<br>Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN<br>Checksum always used: Rest symbologies</p>|
|DetectEncoding|Boolean|<p>(Optional parameter)</p><p>A flag which force engine to detect codetext encoding for Unicode</p>|
|Preset|HighPerformance, NormalQuality, HighQualityDetection, MaxQualityDetection, HighQuality, MaxBarCodes|<p>(Optional parameter)</p><p>Preset allows to configure recognition quality and speed manually.<br>You can quickly set up Preset by embedded presets: HighPerformance, NormalQuality,<br>HighQuality, MaxBarCodes or you can manually configure separate options.<br>Default value of Preset is NormalQuality</p>|
|RectX|Integer|<p>(Optional parameter)</p><p>Set X for area for recognition</p>|
|RectY|Integer|<p>(Optional parameter)</p><p>Set Y for area for recognition</p>|
|RectWidth|Integer|<p>(Optional parameter)</p><p>Set Width of area for recognition</p>|
|RectHeight|Integer|<p>(Optional parameter)</p><p>Set Height of area for recognition</p>|
|StripFNC|Boolean|<p>(Optional parameter)</p><p>Value indicating whether FNC symbol strip must be done</p>|
|Timeout|Integer|<p>(Optional parameter)</p><p>Timeout of recognition process</p>|
|MedianSmoothingWindowSize|Integer|<p>(Optional parameter)</p><p>Window size for median smoothing. Typical values are 3 or 4. Default value is 3. AllowMedianSmoothing must be set</p>|
|AllowMedianSmoothing|Boolean|<p>(Optional parameter)</p><p>Allows engine to enable median smoothing as additional scan. Mode helps to recognize noised barcodes</p>|
|AllowComplexBackground|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize color barcodes on color background as additional scan. Extremely slow mode</p>|
|AllowDatamatrixIndustrialBarcodes|Boolean|<p>(Optional parameter)</p><p>Allows engine for Datamatrix to recognize dashed industrial Datamatrix barcodes. Slow mode which helps only for dashed barcodes which consist from spots</p>|
|AllowDecreasedImage|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize decreased image as additional scan. Size for decreasing is selected by internal engine algorithms. Mode helps to recognize barcodes which are noised and blurred but captured with high resolutio</p>|
|AllowDetectScanGap|Boolean|<p>(Optional parameter)</p><p>Allows engine to use gap between scans to increase recognition speed. Mode can make recognition problems with low height barcodes</p>|
|AllowIncorrectBarcodes|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize barcodes which has incorrect checksum or incorrect values. Mode can be used to recognize damaged barcodes with incorrect text</p>|
|AllowInvertImage|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize inverse color image as additional scan. Mode can be used when barcode is white on black background</p>|
|AllowMicroWhiteSpotsRemoving|Boolean|<p>(Optional parameter)</p><p>Allows engine for Postal barcodes to recognize slightly noised images. Mode helps to recognize slightly damaged Postal barcodes</p>|
|AllowOneDFastBarcodesDetector|Boolean|<p>(Optional parameter)</p><p>Allows engine for 1D barcodes to quickly recognize high quality barcodes which fill almost whole image. Mode helps to quickly recognize generated barcodes from Internet</p>|
|AllowOneDWipedBarsRestoration|Boolean|<p>(Optional parameter)</p><p>Allows engine for 1D barcodes to recognize barcodes with single wiped/glued bars in pattern</p>|
|AllowQRMicroQrRestoration|Boolean|<p>(Optional parameter)</p><p>Allows engine for QR/MicroQR to recognize damaged MicroQR barcodes</p>|
|AllowRegularImage|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize regular image without any restorations as main scan. Mode to recognize image as is</p>|
|AllowSaltAndPepperFiltering|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize barcodes with salt and pepper noise type. Mode can remove small noise with white and black dots</p>|
|AllowWhiteSpotsRemoving|Boolean|<p>(Optional parameter)</p><p>Allows engine to recognize image without small white spots as additional scan. Mode helps to recognize noised image as well as median smoothing filtering</p>|
|RegionLikelihoodThresholdPercent|Number|<p>(Optional parameter)</p><p> </p><p>Sets threshold for detected regions that may contain barcodes.</p><p> </p><p>Value 0.7 means that bottom 70% of possible regions are filtered out and not processed further.<br>Region likelihood threshold must be between [0.05, 0.9]<br>Use high values for clear images with few barcodes.<br>Use low values for images with many barcodes or for noisy images.<br>Low value may lead to a bigger recognition time</p>|
|ScanWindowSizes|array[integer]|<p>(Optional parameter)</p><p> </p><p>Scan window sizes in pixels.</p><p> </p><p>Allowed sizes are 10, 15, 20, 25, 30.<br>Scanning with small window size takes more time and provides more accuracy but may fail in detecting very big barcodes.<br>Combining of several window sizes can improve detection quality</p>|
|Similarity|Number|<p>(Optional parameter)</p><p> </p><p>Similarity coefficient depends on how homogeneous barcodes are.</p><p> </p><p>Use high value for for clear barcodes.<br>Use low values to detect barcodes that ara partly damaged or not lighten evenly.<br>Similarity coefficient must be between [0.5, 0.9]</p>|
|SkipDiagonalSearch|Boolean|<p>(Optional parameter)</p><p>Allows detector to skip search for diagonal barcodes. Setting it to false will increase detection time but allow to find diagonal barcodes that can be missed otherwise. Enabling of diagonal search leads to a bigger detection time</p>|
|AustralianPostEncodingTable|CTable, NTable, Other|<p>(Optional parameter)</p><p>Interpreting Type for the Customer Information of AustralianPost BarCode.Default is CustomerInformationInterpretingType.Other</p>|
|RectangleRegion|String|(Optional parameter)|
|url|String|The image file url|
|image|file|Image data|


cURL Example

{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token

// Get App Key and App SID from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant\_type=client\_credentials&client\_id=XXXXXXXXX&client\_secret=XXXXXXXXX' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

```
```java

// cURL example to generate barcode and recognize a barcode from file on the server with parameters in the request body

curl -v "https://api.aspose.cloud/v3.0/barcode/recognize?Type=Code128&ChecksumValidation=On&url=http%3A%2F%2Fwww.barcoding.com%2Fimages%2FBarcodes%2Fcode93.gif" -X POST -H "Content-Type: application/json" -H "Accept: application/json" 

```

{{< /tab >}}

{{< tab tabNum="2" >}}

```java

{
  "Barcodes": [
    {
      "BarcodeValue": "AsposeBarCode",
      "BarcodeType": "Code128",
      "Region": [
        "16, 4",
        "371, 4",
        "371, 60",
        "16, 60"
      ],
      "Checksum": ""
    }
  ],
  "Code": 200,
  "Status": "OK"
}

```

{{< /tab >}}

{{< /tabs >}}
## **SDKs**
Using an SDK (API client) is the quickest way for a developer to speed up the development. An SDK takes care of a lot of low-level details of making requests and handling responses and lets you focus on writing code specific to your particular project. Checkout our [GitHub repository](https://github.com/aspose-barcode-cloud) for a complete list of Aspose.BarCode SDKs along with working examples, to get you started in no time.
### **SDK Examples**
#### **Read Barcode from Local Image**
{{< tabs tabTotal="6" tabID="4" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "45a0fda4a2cee116f1bf7a1a7f428b3a" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "bffef2dcfc12bd403e4d35809df515e8" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-managing-recognition-without-cloud-storage-read-barcode-from-localfile-.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "ef70cc3af72d10f6d35f34abd0ecb0a6" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-managing-recognition-without-cloud-storage-read-barcode-from-localfile-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "48e56cabb3323df86d69082a42512b98" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Read Barcode from External Image URL**
{{< tabs tabTotal="6" tabID="5" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "4d57ffcac82bc9571cdfa40994757bb4" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "70c0a032b99f2c41a528f2fe88c9d134" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-managing-recognition-without-cloud-storage-read-barcode-from-external-image-url-.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "d7dfea1d3c77064f52bde8dc63bebad3" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-managing-recognition-without-cloud-storage-read-barcode-from-external-image-url-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "ce263f7e28965768eac8f21050b5e317" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Read Barcode from Request Body**
{{< tabs tabTotal="6" tabID="6" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "81d865a9f2bbb9638c114c5ab38ef7ac" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "a812f6afdbadc829ba3b73676e3d0d88" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-managing-recognition-without-cloud-storage-post-barcode-recognize-from-request-body-.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "008ac62a87353fdd28c9628d2ac05d34" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-managing-recognition-without-cloud-storage-ReadBarcodeFromRequestBody-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "63423e8931bc044d5545ac47af66c173" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Recognise Barcode with Checksum Option**
{{< tabs tabTotal="6" tabID="7" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "5b3e55e129c0801c263914e35b99dcf7" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "376700bda6dba920c4df0809e4b12452" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-barcode-with-checksum-option-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "cf5fa5b7a6fc21327aaa76f1dfc8ef45" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-managing-recognition-without-cloud-storage-read-barcodes-with-checksum-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "5a60e4bca5c318b9d43319fb9933192a" >}}

{{< /tab >}}

{{< /tabs >}}




