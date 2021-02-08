---
title: "Generate, Format and Manipulate a Barcode Without Cloud Storage"
type: docs
url: /generate-format-and-manipulate-a-barcode-without-cloud-storage/
weight: 20
---
## **Introduction**
Aspose.BarCode for Cloud has provided the simplest API to generate a barcode and get image as a stream object in an easy way without using any cloud storage operation. This API can be used with any language: .NET, Java, PHP, Ruby, Rails, Python, jQuery and many more.

## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/generate|GET|Generate barcode|[GetBarcodeGenerate](https://apireference.aspose.cloud/barcode/#/Barcode/GetBarcodeGenerate)|

### **cURL Example**
{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token
// Get Client Secret and Client Id from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant_type=client_credentials&client_id=0B17F60A-6D69-426B-9ABD-79F35A6E9F7B&client_secret=53b8b19adffa41a3e87dbbd8858977ae' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

```

```java

// cURL example to generate barcode and get image as a stream object

curl -v "https://api.aspose.cloud/v3.0/barcode/generate?text=AsposeBarCode&type=QR&format=png&enableChecksum=NO&resolution=96&dimensionX=0.7" -X GET -H "Content-Type: application/json" -H "Accept: multipart/form-data" -o sample-barcode.png

```

{{< /tab >}}

{{< tab tabNum="2" >}}

![todo:image_alt_text](generate-format-and-manipulate-a-barcode-without-cloud-storage_1.png)

{{< /tab >}}

{{< /tabs >}}
## **SDKs**
Using an SDK (API client) is the quickest way for a developer to speed up the development. An SDK takes care of a lot of low-level details of making requests and handling responses and lets you focus on writing code specific to your particular project. Checkout our [GitHub repository](https://github.com/aspose-barcode-cloud) for a complete list of Aspose.BarCode SDKs along with working examples, to get you started in no time.
### **SDK Examples**
#### **Generate a Barcode and Get Image as Stream**
{{< tabs tabTotal="6" tabID="3" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "8204b108d4966f58bae08dec977ea1c6" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "86ca3b2412bd9a512b62bb078b093b80" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-GenerateABarcodeAndGetImageStream.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "bba7dc746bffe92c6388f0f156ba5f58" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-GenerateABarcodeAndGetImageStream.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "a148ff358c2ccc42d1a12691b01a2424" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate a Barcode and Save Image to Local Disk**
{{< tabs tabTotal="5" tabID="4" tabName1="C#" tabName2="Java" tabName3="Python" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "a42ed26a4fa09288bc1c307447715c23" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "ba7461ee97f8e3a65b07b86a9a01a873" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-GenerateBarcodeAndSaveImageToLocalDisk.php" >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "706b16f43ebbc5289518eef1d8ba4899" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-GenerateBarcodeAndSaveImageToLocalDisk.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "a63947a5e7dfb70d5967d2ea2fbeea47" >}}

{{< /tab >}}

{{< /tabs >}}
