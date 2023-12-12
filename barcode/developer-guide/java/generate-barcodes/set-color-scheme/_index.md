---
title: Customize Barcode Color
type: docs
weight: 60
description: "How to Adjust Color Schemes of Barcode Elements in Aspose.BarCode for Cloud"
keywords: "Generate Barcodes, Customize Barcode Image, Change Barcode Color, Set Barcode Color, Generate Colored Barcodes, Barcode Color in Aspose.BarCode for Cloud, Work with Barcode Image in Aspose.BarCode for Cloud, Generate Barcodes in Aspose.BarCode"
url: /cloud-java/manage-barcode-color/
---
In this article, the options available in ***Aspose.BarCode for Cloud*** to manage barcode color scheme and its key elements are described.

## **Overview**
Usually, barcode images have a black-and-white color scheme. To provide the possibility of modifying barcode colors, ***Aspose.BarCode for Cloud*** enables customizing system RGB colors for key barcode elements, including the following:
- Bars
- Background
- Text label
- Top and bottom captions
- Borders

## **Background Color**
Barcode background color can be modified through the *setBackColor* method of *BaseGenerationParameters* class. The default value of background color is *White*.  
  
The barcode image with background color set to *Color.Green* is provided below.
   
<p align="center"><image src="colorbackground.png"></p>
  
## **Bar Color**
To manage the color of bars, the *setBarColor* method of *BarcodeParameters* class needs to be used. By default, the bar color is set to *Black*.  
  
The barcode image below has been generated with the bar color setting *Color.Green*.
  
<p align="center"><image src="colorbarcode.png"></p>
  
## **Border Color**
Barcode border color can be adjusted through the *setColor* method of class *BorderParameters*. The default border color is *Black*. The barcode image below has been generated with border color set to *Color.Green*.
  
<p align="center"><image src="colorborder.png"></p>
  

## **Main Text Color**
***Aspose.BarCode for Cloud*** provides the possibility to customize the color of the main text label displayed on a barcode image. It can be done by calling the *setColor* method of class *CodeTextParameters*. The default setting of the main text color is *Black*. The sample barcode image shown below has been generated with the customized barcode text color setting (*Color.Green*).
  
<p align="center"><image src="colorcodetext.png"></p>
  

## **Caption Color**
In ***Aspose.BarCode for Cloud***, barcode images can be generated with top and bottom captions. Caption color can be customized using the *setTextColor* method of class *CaptionParameters*. Sample images below have been created with the color setting set to *Color.Green*.
  
|Caption Color|   |
|:--| :-: |
|<image src="colorcaptionabove.png">|<image src="colorcaptionbelow.png">|
  