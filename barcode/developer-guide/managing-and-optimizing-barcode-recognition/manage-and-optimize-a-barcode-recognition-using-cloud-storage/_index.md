---
title: "Manage and Optimize a Barcode Recognition Using Cloud Storage"
type: docs
url: /manage-and-optimize-a-barcode-recognition-using-cloud-storage/
weight: 10
---

## **Introduction**
Aspose.BarCode for Cloud has provided the simplest API to recognize a barcode and save it on Aspose Cloud Storage.

## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/{name}/recognize|GET|Recognize barcode from a file on server|[GetBarcodeRecognize](https://apireference.aspose.cloud/barcode/#/Barcode/GetBarcodeRecognize)|

### **cURL Example**
{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token
// Get App Key and App SID from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant_type=client_credentials&client_id=XXXXXXXXX&client_secret=XXXXXXXXX' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

```
```java

// cURL example to recognize a barcode

curl -v "https://api.aspose.cloud/v3.0/barcode/sample-barcode.png/recognize?type=Code128&format=png" -X GET -H "Content-Type: application/json" -H "Accept: application/json" 

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
#### **Read Barcode from Aspose Cloud Storage**
{{< tabs tabTotal="6" tabID="4" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "6870ff02a0a2f99a9206163f5e6df7e2" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "7478c19a65c3463f5aee7cf4455f7beb" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-RecognizeBarcodeFromStorage.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "6275bcdea343576fc9dd39c66d8b92e5" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-RecognizeBarcodeFromStorage.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "6cd164837c89ec2bae69022d847eac51" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Read Barcode from Specific Region of Image**
{{< tabs tabTotal="6" tabID="5" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "831a237fc1340791fe99fac370250491" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "3f5d042567f7853c4ae3dc39af7f2454" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-ReadBarcodeFromSpecificRegion.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "183dbbf55f51d5227c22d887fbf7691c" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-ReadBarcodeFromSpecificRegion.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "cb77f0513d354454cb992cfbb5107d3d" >}}

{{< /tab >}}

{{< /tabs >}}
