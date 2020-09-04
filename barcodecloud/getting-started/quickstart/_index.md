---
title: "Quickstart"
type: docs
url: /quickstart/
weight: 30
---

## **Create an account**
The first thing you need to do to get started with Aspose for Cloud is sign up for a [free account](https://docs.aspose.cloud/display/storagecloud/Creating+and+Managing+Account).
## **Create an API client app**
Before you can make any requests to Aspose for Cloud API you need to [create an API client app](https://docs.aspose.cloud/display/storagecloud/Create+New+App+and+Get+App+Key+and+SID).

This will give you **App SID** and **App key (secret key)** which you can use to invoke Aspose.Barcode for Cloud API. 
## **Install the SDK of your choice**
We provide and support API SDKs in many development languages in order to make it easier for you to integrate your application with us.

**.NET**

```java

nuget install Aspose.BarCode-Cloud

```

**PHP**

```java

composer require aspose/barcode-cloud-php

```

**Node.js**

```java

npm install aspose-barcode-cloud-node --save

```
## **Make an API request from the SDK of your choice**
Use the **App SID** and **App key (secret key)** from the API app client you created in step one and replace in the corresponding code.

**C#**

```java

var barCodeApi = new BarCodeApi(AppKey, AppSid);

using (Stream response = api.BarCodeGetBarCodeGenerate(new BarCodeGetBarCodeGenerateRequest("Sample text", "Code128", "jpg")))

using (FileStream stream = File.Create("out.jpg"))

{

   response.CopyTo(stream);

}

```

**PHP**

```php

var barCodeApi = new BarCodeApi(AppKey, AppSid);

using (Stream response = api.BarCodeGetBarCodeGenerate(new BarCodeGetBarCodeGenerateRequest("Sample text", "Code128", "jpg")))

using (FileStream stream = File.Create("out.jpg"))

{

   response.CopyTo(stream);

} 

```

**Node.js**

```javascript

const { barcode, fs } = require("aspose-barcode-cloud-node", "fs");

var api = new barcode.BarCodeApi(AppSid, AppKey);

api.barCodeGetBarCodeGenerate("Aspose.BarCode for Cloud Sample", "Pdf417", "png").then((apiResult) => {

       if (apiResult.response.statusCode == 200) {

           fs.writeFile("out.png", apiResult.body);

           console.log("Saved to out.png ");

       }

   });

```
