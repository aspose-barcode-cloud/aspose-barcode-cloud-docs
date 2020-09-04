---
title: "Generate, Format and Manipulate a Barcode Without Cloud Storage"
type: docs
url: /generate-format-and-manipulate-a-barcode-without-cloud-storage/
weight: 20
---

# **Introduction**
Aspose.BarCode for Cloud has provided the simplest API to generate a barcode and get image as a stream object in an easy way without using any cloud storage operation.
## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/generate|GET|Generate barcode|[GetBarcodeGenerate](https://apireference.aspose.cloud/barcode/#/Barcode/GetBarcodeGenerate)|
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
|format|String|<p>(Optional parameter)</p><p>The image format</p>|
## **cURL Example**
{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token

// Get App Key and App SID from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" \

-X POST \

-d 'grant\_type=client\_credentials&client\_id=0B17F60A-6D69-426B-9ABD-79F35A6E9F7B&client\_secret=53b8b19adffa41a3e87dbbd8858977ae' \

-H "Content-Type: application/x-www-form-urlencoded" \

-H "Accept: application/json"

// cURL example to generate barcode and get image as a stream object

curl -v "https://api.aspose.cloud/v3.0/barcode/generate?text=AsposeBarCode&type=QR&format=png&enableChecksum=NO&resolution=96&dimensionX=0.7" \

-X GET \

-H "Content-Type: application/json" \

-H "Accept: multipart/form-data" \

-o sample-barcode.png \

-H "Authorization: Bearer BQNPIzh7T8mj6f0O7fuYm87IAUyjhSu0kb\_WeIeigZFU\_yXb7\_kwojehxNGyVQWuc9hXGvuMfxcY7AXPkSykKCUPcrjt\_tpEMIrMhavTz3rcw4oStXzReI1thSmoHsYosDQ4SMtmEISbII7wu7-ld\_HDKirl\_3YpU8bRqVRQ1aBq79X0JbOvi2gJ-6\_G8vGO\_zI02tAc6FcLhF2UJT5J0DPRUJ2OgyLRFnn7h1fQExbJGIS8fn1El2EgkhzRixsZYVpm6ey2Is6NAWBy75KVSZt3ICH3g7X0V6PCL3OJWi0ZU-WeKNXAyQfm3cUEehP1XZocjmhh2E8sL-3liEKZkw8IBBPmyryDKjPZMm0-K3Zjx\_XrLcp\_nYPMV9353LpqMEEmyF2atAG1eEVa0Hh12REPzeDc82AhpVwzFsI3HqIqTbD3"

```

{{< /tab >}}

{{< tab tabNum="2" >}}

![todo:image\_alt\_text](generate-format-and-manipulate-a-barcode-without-cloud-storage_1.png)

{{< /tab >}}

{{< /tabs >}}
# **SDKs**
Using an SDK (API client) is the quickest way for a developer to speed up the development. An SDK takes care of a lot of low-level details of making requests and handling responses and lets you focus on writing code specific to your particular project. Checkout our [GitHub repository](https://github.com/aspose-barcode-cloud) for a complete list of Aspose.BarCode SDKs along with working examples, to get you started in no time.
## **SDK Examples**
#### **Generate a Barcode and Get Image as Stream**
{{< tabs tabTotal="6" tabID="3" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "" "8882af24a0597b7c756eaa5186ee8125" "Examples-PHP-generating-saving-without-cloud-storage-generate-barcode-and-get-image-as-stream-1.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-without-cloud-storage-create-barcode-and-get-image-as-stream-1.js" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate a Barcode and Save Image to Local Disk**
{{< tabs tabTotal="5" tabID="4" tabName1="C#" tabName2="Java" tabName3="Python" tabName4="Node.js" tabName5="Go" >}}

{{< tab tabNum="1" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-barcode" "831958079e7a6ee3d9d4cca9be305966" "Examples-Node.js-generating-saving-without-cloud-storage-create-barcode-and-saveimage-to-localdisk-1.js" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< /tab >}}

{{< /tabs >}}






