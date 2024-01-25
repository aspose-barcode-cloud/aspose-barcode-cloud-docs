---
title: Authorization in Cloud SDK for PHP
linktitle: Authorization
type: docs
url: /cloud-php/authorization/
weight: 10
---

## **Overview**
Aspose.BarCode Cloud prioritizes data security by adhering to industry standards and implementing best practices. The REST API communication employs JWT authentication, ensuring a secure and standardized method for information exchange.

## **Get Access Token**
To obtain time-limited JWT tokens, follow these specific steps using Client ID and Client Secret credentials unique to each application:

1. Sign in to the [Aspose Cloud API Dashboard](https://dashboard.aspose.cloud/)
2. Navigate to page [Applications](https://dashboard.aspose.cloud/applications)
3. Click the **Create New Application** button
4. Assign an easily recognizable name and an optional detailed description to the application
5. Create cloud storage by clicking the plus icon and following the required steps. You can also reuse existing storage if available
6. Click the **Save** button
7. Access the newly created application and copy the values from the **Client Id** and **Client Secret** fields

To request an access token, send a POST request to https://api.aspose.cloud/connect/token with the following parameters in the request body (x-www-form-urlencoded):

- *grant_type*: must be client_credentials
- *client_id*: the value from the **Client Id** field
- *client_secret*: the value from the **Client Secret** field


## **Authorize REST API Requests**
To authorize your requests to Aspose.BarCode Cloud API, pass the access token in the authorization header of each request:

```csharp
curl --request POST --location 'https://api.aspose.cloud/v3.0/barcode' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...l8v7jUV-mLjEdQ'

```

## **Authorize SDK Requests**
The Cloud SDK facilitates the process of obtaining an access token and authorizing requests by simplifying these operations. When initializing the API, you only need to provide the values from the "Client ID" and "Client Secret" fields. The SDK takes care of the entire process on your behalf.

```java
Configuration.setAPP_SID("CLIENT-ID-VALUE");
Configuration.setAPI_KEY("CLIENT-SECRET-VALUE");

```