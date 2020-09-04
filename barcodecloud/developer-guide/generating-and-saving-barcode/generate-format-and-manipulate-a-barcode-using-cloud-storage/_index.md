---
title: "Generate, Format and Manipulate a Barcode using Cloud Storage"
type: docs
url: /generate-format-and-manipulate-a-barcode-using-cloud-storage/
weight: 10
---

# **Introduction**
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
|Text|` `String|Text to encode|
|TwoDDisplayText|` `String|<p>Optional parameter</p><p>Text that will be displayed instead of codetext in 2D barcodes.<br>Used for: Aztec, Pdf417, DataMatrix, QR, MaxiCode, DotCode</p>|
|TextLocation|` `Below, Above, None|<p>(Optional parameter)</p><p>Displaying Text Location</p>|
|TextAlignment|` `Left, Center, Right|<p>(Optional parameter)</p><p>Text alignment</p>|
|TextColor|` `Default value: Color.Black|<p>(Optional parameter)</p><p>Displaying CodeText's Color</p>|
|FontSizeMode|` `Auto, Manual|<p>(Optional parameter)</p><p>If FontSizeMode is set to Auto, font size will be calculated automatically based on xDimension value.<br>It is recommended to use FontSizeMode.Auto especially in AutoSizeMode.Nearest or AutoSizeMode.Interpolation</p>|
|Resolution|` `Number|<p>(Optional parameter)</p><p>Resolution of the BarCode image.<br>One value for both dimensions.<br>Default value: 96 dpi.</p>|
|DimensionX|` `Number|<p>(Optional parameter)</p><p>The smallest width of the unit of BarCode bars or spaces. Increase this will increase the whole barcode image width. Ignored if AutoSizeMode property is set to AutoSizeMode.Nearest or AutoSizeMode.Interpolation</p>|
|TextSpace|` `Number|<p>(Optional parameter)</p><p>Space between the CodeText and the BarCode in Unit value<br>Default value: 2pt<br>Ignored for EAN8, EAN13, UPCE, UPCA, ISBN, ISMN, ISSN, UpcaGs1DatabarCoupon</p>|
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
**Output File:** [sample-barcode.png](attachments/4391166/4555175.png)

{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token

// Get App Key and App SID from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" \

-X POST \

-d 'grant\_type=client\_credentials&client\_idXXXXXXXXX&client\_secret=XXXXXXXXX' \

-H "Content-Type: application/x-www-form-urlencoded" \

-H "Accept: application/json"

// cURL example to generate barcode and save on server

curl -v "https://api.aspose.cloud/v3.0/barcode/sample-barcode.png/generate?text=AsposeBarCode&type=Code128&format=png" \

-X PUT \

-H "Content-Type: application/json" \

-H "Accept: application/json" \

-H "Authorization: Bearer BQNPIzh7T8mj6f0O7fuYm87IAUyjhSu0kb\_WeIeigZFU\_yXb7\_kwojehxNGyVQWuc9hXGvuMfxcY7AXPkSykKCUPcrjt\_tpEMIrMhavTz3rcw4oStXzReI1thSmoHsYosDQ4SMtmEISbII7wu7-ld\_HDKirl\_3YpU8bRqVRQ1aBq79X0JbOvi2gJ-6\_G8vGO\_zI02tAc6FcLhF2UJT5J0DPRUJ2OgyLRFnn7h1fQExbJGIS8fn1El2EgkhzRixsZYVpm6ey2Is6NAWBy75KVSZt3ICH3g7X0V6PCL3OJWi0ZU-WeKNXAyQfm3cUEehP1XZocjmhh2E8sL-3liEKZkw8IBBPmyryDKjPZMm0-K3Zjx\_XrLcp\_nYPMV9353LpqMEEmyF2atAG1eEVa0Hh12REPzeDc82AhpVwzFsI3HqIqTbD3"

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
# **SDKs**
Using an SDK (API client) is the quickest way for a developer to speed up the development. An SDK takes care of a lot of low-level details of making requests and handling responses and lets you focus on writing code specific to your particular project. Checkout our [GitHub repository](https://github.com/aspose-barcode-cloud) for a complete list of Aspose.BarCode SDKs along with working examples, to get you started in no time.
## **SDK Examples**
#### **Generate a Barcode on Aspose Cloud Storage**
{{< tabs tabTotal="6" tabID="4" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-create-barcode-and-save-asposecloudstorage-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-create-barcode-and-save-asposecloudstorage-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate a CodablockF Type Barcode**
{{< tabs tabTotal="6" tabID="5" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-a-codablockf-type-barcode-.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-GenerateCodablockFBarCode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Barcode Image Resolution**
{{< tabs tabTotal="6" tabID="6" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-barcode-image-resolution-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-barcode-image-resolution-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Specify Codetext and Symbology for barcode**
{{< tabs tabTotal="6" tabID="7" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-specify-codetext-and-symbology-for-barcode-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-specify-codetext-and-symbology-for-barcode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Dimensions of a Barcode**
{{< tabs tabTotal="6" tabID="8" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Node.js" tabName5="Python" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-x-and-y-dimensions-of-barcode-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-x-and-y-dimensions-of-barcode-1.js" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Specify Barcode Image Save Format**
{{< tabs tabTotal="6" tabID="9" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Node.js" tabName5="Python" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-specify-barcode-image-save-format-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-specify-barcode-image-save-format-1.js" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Barcode with Appropriate Code Text Location**
{{< tabs tabTotal="6" tabID="10" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-barcode-with-appropriate-codetext-location-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-barcode-with-appropriate-codetext-location-1.js" >}}



{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Barcode with Checksum Option**
{{< tabs tabTotal="6" tabID="11" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-generate-barcode-with-checksum-option-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-barcode-with-checksum-option-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Rotate Barcode Image with Suitable Angle**
{{< tabs tabTotal="6" tabID="12" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-rotate-barcode-image-with-suitable-angle-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-rotate-barcode-image-with-suitable-angle-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Barcode Image Size**
{{< tabs tabTotal="6" tabID="13" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-barcode-image-height-width-quality-settings-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-barcode-image-height-width-quality-settings-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Height of the Bars in the Barcode Image**
{{< tabs tabTotal="6" tabID="14" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-cloud-storage-set-bars-height-in-barcodeimage-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-set-bars-height-in-barcodeimage-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Multiple Barcodes**
{{< tabs tabTotal="5" tabID="15" tabName1="C#" tabName2="Java" tabName3="Node.js" tabName4="Python" tabName5="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-cloud-storage-generate-multiple-barcodes-1.js" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< /tab >}}

{{< /tabs >}}
