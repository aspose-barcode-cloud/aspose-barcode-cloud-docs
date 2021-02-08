---
title: "Generate, Format and Manipulate a Barcode using Cloud Storage"
type: docs
url: /generate-format-and-manipulate-a-barcode-using-cloud-storage/
weight: 10
---
## **Introduction**
Aspose.BarCode for Cloud has provided the simplest API to generate a barcode and save it on Aspose Cloud Storage. This API can be used with any language: .NET, Java, PHP, Ruby, Rails, Python, jQuery and many more.

## **API Information**

|**API**|**Type**|**Description**|**Resource Link**|
| :- | :- | :- | :- |
|/barcode/{name}/generate|PUT|Generate barcode and save on server (from query params or from file with json or xml content)|[PutBarcodeGenerateFile](https://apireference.aspose.cloud/barcode/#/Barcode/PutBarcodeGenerateFile)|

### **cURL Example**

{{< tabs tabTotal="2" tabID="1" tabName1="Request" tabName2="Response" >}}

{{< tab tabNum="1" >}}

```java

// First get Access Token
// Get Client Secret and Client Id from https://dashboard.aspose.cloud/

curl -v "https://api.aspose.cloud/oauth2/token" -X POST -d 'grant_type=client_credentials&client_idXXXXXXXXX&client_secret=XXXXXXXXX' -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: application/json"

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-PutBarcodeGenerateFileOnCloudStorage.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "2b8815d9eb48bd894bb6867318f7a523" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-PutBarcodeGenerateFileOnCloudStorage.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-GenerateASpecificBarcode.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "7cb3914bc920c70957935e37e85d2b30" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-GenerateASpecificBarcode.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SetBarcodeImageResolution.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "69f6584b4b39d83cadca465f24acd4e8" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SetBarcodeImageResolution.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SpecifyCodetextAndSymbology.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "1bcab1b8617ad088346f1a1355af25c6" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SpecifyCodetextAndSymbology.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "1d155d4cbbedd2898c382db5439df41a" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Set Dimensions of a Barcode**
{{< tabs tabTotal="6" tabID="8" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "87c09d903641d7127c37ebb9ad17bbd3" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "dfa661053da885296d7182096c47a48d" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SetDimensionOfBarcode.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "56ea289c7dcbf846f0995886f70f1f06" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SetDimensionOfBarcode.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "92daf1433e28ca9a9a4bf424ed1a6c16" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Specify Barcode Image Save Format**
{{< tabs tabTotal="6" tabID="9" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "00aa785de274e93ed594421576848787" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "c11c9809fd43e635a90e56eda15bc60e" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SpecifyBarcodeImageSaveFormat.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "2bf0dab342dc89961a43b99eba86996e" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SpecifyBarcodeImageSaveFormat.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SpecifyBarcodeTextLocation.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "f478a05c708536f537b7481010c7857e" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SpecifyBarcodeTextLocation.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-GenerateBarcodeWithChecksumOption.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "7ded5cb4e3949cb670d18b483b1add11" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-GenerateBarcodeWithChecksumOption.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-RotateBarcodeImage.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "5619fe4173276f678ea166485a85800a" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-RotateBarcodeImage.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SetBarcodeImageSize.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "51dc8a405c5b330b6ca16e29592bdaca" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SetBarcodeImageSize.ts" >}}

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

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-SetBarcodeBarsHeight.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "4209447b0c6300039b843e34274cdc3e" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-SetBarcodeBarsHeight.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "45b4909a5b5e3a98edce44c5d54217f2" >}}

{{< /tab >}}

{{< /tabs >}}
#### **Generate Multiple Barcodes**
{{< tabs tabTotal="5" tabID="15" tabName1="C#" tabName2="Java" tabName3="PHP" tabName4="Python" tabName5="Node.js" tabName6="Go" >}}

{{< tab tabNum="1" >}}

{{< gist "aspose-cloud" "13492976d5104a07cda07b7fc04b886f" >}}

{{< /tab >}}

{{< tab tabNum="2" >}}

{{< gist "aspose-cloud" "30e0597a7b1ba6ff88a4489c97e32cde" >}}

{{< /tab >}}

{{< tab tabNum="3" >}}

{{< gist "aspose-cloud" "7dd7c6f477aeb4eabd1afc57e6913ccd" "Example-GenerateMultipleBarcodes.php" >}}

{{< /tab >}}

{{< tab tabNum="4" >}}

{{< gist "aspose-cloud" "0aa6c08db374c01e73733544e6c7d2b1" >}}

{{< /tab >}}

{{< tab tabNum="5" >}}

{{< gist "aspose-cloud" "3d80ec0b502975afa622577a2ca7bf0a" "Example-GenerateMultipleBarcodes.ts" >}}

{{< /tab >}}

{{< tab tabNum="6" >}}

{{< gist "aspose-cloud" "fe445405c2505fad3da886bb2a1c5811" >}}

{{< /tab >}}

{{< /tabs >}}
