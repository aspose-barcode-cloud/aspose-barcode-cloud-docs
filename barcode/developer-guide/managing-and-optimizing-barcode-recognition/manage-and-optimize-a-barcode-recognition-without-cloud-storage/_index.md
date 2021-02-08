---
title: "Manage and Optimize a Barcode Recognition Without Cloud Storage"
type: docs
url: /manage-and-optimize-a-barcode-recognition-without-cloud-storage/
weight: 20
---

## **Introduction**
Aspose.BarCode for Cloud provided the simplest API which lets you recognize a barcode from file on the server with parameters in the request body. This API can be used with any language: .NET, Java, PHP, Ruby, Rails, Python, jQuery and many more.

## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/recognize|POST|Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image or encoded with base64|[PostBarcodeRecognizeFromUrlOrContent](https://apireference.aspose.cloud/barcode/#/Barcode/PostBarcodeRecognizeFromUrlOrContent)|


### **cURL Example**

{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token
// Get Client Secret and Client Id from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant_type=client_credentials&client_id=XXXXXXXXX&client_secret=XXXXXXXXX' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-ReadBarcodeFromLocal.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "ef70cc3af72d10f6d35f34abd0ecb0a6" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-ReadBarcodeFromLocal.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-ReadBarcodeFromUrl.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "d7dfea1d3c77064f52bde8dc63bebad3" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-ReadBarcodeFromUrl.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-ReadBarcodeFromRequestBody.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "008ac62a87353fdd28c9628d2ac05d34" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-ReadBarcodeFromRequestBody.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-RecogniseBarcodeWithChecksumOption.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "cf5fa5b7a6fc21327aaa76f1dfc8ef45" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-RecogniseBarcodeWithChecksumOption.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "5a60e4bca5c318b9d43319fb9933192a" >}}

{{< /tab >}}

{{< /tabs >}}




