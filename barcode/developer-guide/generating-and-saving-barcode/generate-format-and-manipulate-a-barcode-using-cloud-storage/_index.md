---
title: "Generate, Format and Manipulate a Barcode using Cloud Storage"
type: docs
url: /generate-format-and-manipulate-a-barcode-using-cloud-storage/
weight: 10
---

Aspose.BarCode for Cloud has provided the simplest API to generate a barcode and save it on Aspose Cloud Storage.
## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/{name}/generate|PUT|Generate barcode and save on server (from query params or from file with json or xml content)|[PutBarcodeGenerateFile](https://apireference.aspose.cloud/barcode/#/Barcode/PutBarcodeGenerateFile)|
The description of important API parameters and their valid values are given below:

|**Parameter**|**Valid values**|**Description**|
| :- | :- | :- |
|name|String|The image file name|
|Type|Codabar, Code11, Code39Standard, Code39Extended, Code93Standard, Code93Extended, <br>Code128, GS1Code128, EAN8, EAN13, EAN14, SCC14, SSCC18, UPCA, UPCE, ISBN, ISSN, <br>ISMN, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, ITF14, <br>ITF6, MSI, VIN, DeutschePostIdentcode, DeutschePostLeitcode, OPC, PZN, Code16K, <br>Pharmacode, DataMatrix, QR, Aztec, Pdf417, MacroPdf417, AustraliaPost, Postnet, <br>Planet, OneCode, RM4SCC, DatabarOmniDirectional, DatabarTruncated, DatabarLimited, <br>DatabarExpanded, SingaporePost, GS1DataMatrix, AustralianPosteParcel, <br>SwissPostParcel, PatchCode, DatabarExpandedStacked, DatabarStacked, <br>DatabarStackedOmniDirectional, MicroPdf417, GS1QR, MaxiCode, Code32, DataLogic2of5, <br>DotCode, DutchKIX, UpcaGs1Code128Coupon, UpcaGs1DatabarCoupon, CodablockF, GS1CodablockF|Type of barcode to generate|
|Text|String|Text to encode|
|TwoDDisplayText|String|<p>Optional parameter</p><p>Text that will be displayed instead of codetext in 2D barcodes.<br>Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode</p>|
|TextLocation|Below, Above, None|<p>(Optional parameter)</p><p>Displaying Text Location</p>|
|TextAlignment|Left, Center, Right|<p>(Optional parameter)</p><p>Text alignment</p>|
|TextColor|Default value: Color.Black|<p>(Optional parameter)</p><p>Displaying CodeText's Color</p>|
|FontSizeMode|Auto, Manual|<p>(Optional parameter)</p><p>If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value.<br>It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation</p>|
|Resolution|Number|<p>(Optional parameter)</p><p>Resolution of the BarCode image.<br>One value for both dimensions.<br>Default value: 96 dpi.</p>|
|DimensionX|Number|<p>(Optional parameter)</p><p>The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation</p>|
|TextSpace|Number|<p>(Optional parameter)</p><p>Space between the CodeText and the BarCode in Unit value<br>Default value: 2pt<br>Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon</p>|
|Units|Pixel, Point, Inch, Millimeter|<p>(Optional parameter)</p><p>Common Units for all measuring in query. Default units: pixel</p>|
|SizeMode|None, Nearest, Interpolation|<p>(Optional parameter)</p><p>Specifies the different types of automatic sizing modes.<br>Default value: AutoSizeMode.None</p>|
|BarHeight|Number|<p>(Optional parameter)</p><p>Height of the barcode in given units. Default units: pixel</p>|
|ImageHeight|Number|<p>(Optional parameter)</p><p>Height of the barcode image in given units. Default units: pixel</p>|
|ImageWidth|Number|<p>(Optional parameter)</p><p>Width of the barcode image in given units. Default units: pixel</p>|
|RotationAngle|Number|<p>(Optional parameter)</p><p>BarCode image rotation angle, measured in degree, e.g. RotationAngle = 0 or RotationAngle = 360 means no rotation.<br>If RotationAngle NOT equal to 90, 180, 270 or 0, it may increase the difficulty for the scanner to read the image.<br>Default value: 0</p>|
|BackColor|String|<p>(Optional parameter)</p><p>Background color of the barcode image.<br>Default value: Color.White</p>|
|BarColor|String|<p>(Optional parameter)</p><p>Bars color.<br>Default value: Color.Black</p>|
|BorderColor|String|<p>(Optional parameter)</p><p>Border color.<br>Default value: Color.Black</p>|
|BorderWidth|Number|<p>(Optional parameter)</p><p>Border width.<br>Default value: 0<br>Ignored if Visible is set to false</p>|
|BorderDashStyle|Solid, Dash, Dot, DashDot, DashDotDot|<p>(Optional parameter)</p><p>Border dash style.<br>Default value: BorderDashStyle.Solid</p>|
|BorderVisible|Boolean|<p>(Optional parameter)</p><p>Border visibility. If false than parameter Width is always ignored (0).<br>Default value: false</p>|
|EnableChecksum|Default, Yes, No|<p>(Optional parameter)</p><p>Enable checksum during generation 1D barcodes.<br>Default is treated as Yes for symbology which must contain checksum, as No where checksum only possible.<br>Checksum is possible: Code39 Standard/Extended, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, DeutschePostIdentcode, DeutschePostLeitcode, VIN, Codabar<br>Checksum always used: Rest symbology</p>|
|EnableEscape|Boolean|<p>(Optional parameter)</p><p>Indicates whether explains the character "" as an escape character in CodeText property. Used for Pdf417, DataMatrix, Code128 only<br>If the EnableEscape is true, "" will be explained as a special escape character. Otherwise, "" acts as normal characters.<br>Aspose.BarCode supports input decimal ascii code and mnemonic for ASCII control-code characters. For example, \013 and \CR stands for CR</p>|
|FilledBars|Boolean|<p>(Optional parameter)</p><p>Value indicating whether bars are filled.<br>Only for 1D barcodes.<br>Default value: true</p>|
|AlwaysShowChecksum|Boolean|<p>(Optional parameter)</p><p>Display checksum digit in the human readable text for Code128 and GS1Code128 barcodes</p>|
|WideNarrowRatio|Number|<p>(Optional parameter)</p><p>Wide bars to Narrow bars ratio.<br>Default value: 3, that is, wide bars are 3 times as wide as narrow bars.<br>Used for ITF, PZN, PharmaCode, Standard2of5, Interleaved2of5, Matrix2of5, ItalianPost25, IATA2of5, VIN, DeutschePost, OPC, Code32, DataLogic2of5, PatchCode, Code39Extended, Code39Standard</p>|
|ValidateText|Boolean|<p>(Optional parameter)</p><p>Only for 1D barcodes.<br>If codetext is incorrect and value set to true - exception will be thrown. Otherwise codetext will be corrected to match barcode's specification.<br>Exception always will be thrown for: Databar symbology if codetext is incorrect.<br>Exception always will not be thrown for: AustraliaPost, SingapurePost, Code39Extended, Code93Extended, Code16K, Code128 symbology if codetext is incorrect</p>|
|SupplementData|String|<p>(Optional parameter)</p><p>Supplement parameters.<br>Used for Interleaved2of5, Standard2of5, EAN13, EAN8, UPCA, UPCE, ISBN, ISSN, ISMN</p>|
|SupplementSpace|String|<p>(Optional parameter)</p><p>Space between main the BarCode and supplement BarCode</p>|
|storage|String|<p>(Optional parameter)</p><p>Image's storage</p>|
|folder|String|<p>(Optional parameter)</p><p>Image's folder</p>|
|format|String|<p>(Optional parameter)</p><p>The image format</p>|
## **cURL Example**

{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token

// Get App Key and App SID from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant\_type=client\_credentials&client\_idXXXXXXXXX&client\_secret=XXXXXXXXX' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

```
```java
// cURL example to generate barcode and save on server

curl -v "https://api.aspose.cloud/v3.0/barcode/sample-barcode.png/generate?text=AsposeBarCode&type=Code128&format=png" -X PUT -H "Content-Type: application/json" -H "Accept: application/json"

```

{{< /tab >}}

{{< tab tabNum="2" >}}

```java

{
  "Code": 200,
  "Status": "OK"
}

```

{{< /tab >}}

{{< /tabs >}}
## **SDKs**
Using an SDK (API client) is the quickest way for a developer to speed up the development. An SDK takes care of a lot of low-level details of making requests and handling responses and lets you focus on writing code specific to your particular project. Checkout our [GitHub repository](https://github.com/aspose-barcode-cloud) for a complete list of Aspose.BarCode SDKs along with working examples, to get you started in no time.
### **SDK Examples**
#### **Generate a Barcode on Aspose Cloud Storage**
{{< tabs tabTotal="6" tabID="4" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "f91d1296e69f11f26d20907fdf662e59" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "0e0cdae72b99c579ed0da982b0e9cea7" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-create-barcode-and-save-asposecloudstorage-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "2b8815d9eb48bd894bb6867318f7a523" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-create-barcode-and-save-asposecloudstorage-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "0083aa4036f686740cf547e3d4e3e3ff" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate a CodablockF Type Barcode**
{{< tabs tabTotal="6" tabID="5" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "6f99b0df41428285ecc1dd47931fdb6d" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "083785d2dfd82560e773d1433ec1d6e0" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-a-codablockf-type-barcode-.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "7cb3914bc920c70957935e37e85d2b30" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-GenerateCodablockFBarCode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "867bd62c2f27641a3267466cd00d6158" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Barcode Image Resolution**
{{< tabs tabTotal="6" tabID="6" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "1616f2ec2735967b12099f9fbd715d9b" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "e8c0728375d651e6662f23f52d17ccce" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-barcode-image-resolution-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "69f6584b4b39d83cadca465f24acd4e8" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-barcode-image-resolution-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "b39d9265412e2af2dd87679ab9e27693" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Specify Codetext and Symbology for barcode**
{{< tabs tabTotal="6" tabID="7" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "aa3772dc829ab43231036710dbe26b67" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "44d3bd980fa221c7683fda99eb1bb6b0" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-specify-codetext-and-symbology-for-barcode-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "1bcab1b8617ad088346f1a1355af25c6" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-specify-codetext-and-symbology-for-barcode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "1d155d4cbbedd2898c382db5439df41a" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Dimensions of a Barcode**
{{< tabs tabTotal="6" tabID="8" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Node.js" tabName5="Python" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "87c09d903641d7127c37ebb9ad17bbd3" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "dfa661053da885296d7182096c47a48d" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-x-and-y-dimensions-of-barcode-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-x-and-y-dimensions-of-barcode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "56ea289c7dcbf846f0995886f70f1f06" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "92daf1433e28ca9a9a4bf424ed1a6c16" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Specify Barcode Image Save Format**
{{< tabs tabTotal="6" tabID="9" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Node.js" tabName5="Python" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "00aa785de274e93ed594421576848787" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "c11c9809fd43e635a90e56eda15bc60e" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-specify-barcode-image-save-format-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-specify-barcode-image-save-format-1.js" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "2bf0dab342dc89961a43b99eba86996e" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "56e198264c14c4f9173d5f06686e8f84" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Barcode with Appropriate Code Text Location**
{{< tabs tabTotal="6" tabID="10" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "962506b187e5584f4801fe8a9a644e77" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "b82ff58823e2c68936a4b2575c982c66" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-barcode-with-appropriate-codetext-location-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "f478a05c708536f537b7481010c7857e" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-barcode-with-appropriate-codetext-location-1.js" >}}



{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "7c1061c4d8b910345765c588bf34dbb3" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Barcode with Checksum Option**
{{< tabs tabTotal="6" tabID="11" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "38a10ffc2c1cc8625efff80d38edcbdf" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "cf419b15f68fe257ca6bd58db9c92379" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-barcode-with-checksum-option-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "7ded5cb4e3949cb670d18b483b1add11" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-barcode-with-checksum-option-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "c3455052499bd7c7f3b885fef094b651" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Rotate Barcode Image with Suitable Angle**
{{< tabs tabTotal="6" tabID="12" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "c53e6fad8f71a6653f3964d024c21bfc" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "3377124ef5054ed1093da6c769119207" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-rotate-barcode-image-with-suitable-angle-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "5619fe4173276f678ea166485a85800a" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-rotate-barcode-image-with-suitable-angle-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "e88cbf3e20e492d78d9f01df45b6b0c6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Barcode Image Size**
{{< tabs tabTotal="6" tabID="13" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "d7a0051b3a2233655922cd27638d915b" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "5d7eb1a5ca3f1d0a310ab722a84cdcda" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-barcode-image-height-width-quality-settings-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "51dc8a405c5b330b6ca16e29592bdaca" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-barcode-image-height-width-quality-settings-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "97012194b6b8a9a00117308b00f870fc" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Height of the Bars in the Barcode Image**
{{< tabs tabTotal="6" tabID="14" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "a548ca2f6321e366663c6f10ed7e54e0" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "ed619486e1815e1d36cadd2ffd5abe46" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-bars-height-in-barcodeimage-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "4209447b0c6300039b843e34274cdc3e" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-bars-height-in-barcodeimage-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "45b4909a5b5e3a98edce44c5d54217f2" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Multiple Barcodes**
{{< tabs tabTotal="5" tabID="15" tabName1="C#" tabName2="Java" tabName3="Node.js" tabName4="Python" tabName5="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "13492976d5104a07cda07b7fc04b886f" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "30e0597a7b1ba6ff88a4489c97e32cde" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-multiple-barcodes-1.js" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "0aa6c08db374c01e73733544e6c7d2b1" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "fe445405c2505fad3da886bb2a1c5811" >}}

{{< /tab >}}

{{< /tabs >}}
