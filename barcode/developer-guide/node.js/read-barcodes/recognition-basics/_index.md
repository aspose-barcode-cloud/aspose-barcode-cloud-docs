---
title: Barcode Recognition Basics
type: docs
description: "This Article Describes How to Read Barcodes of Different Symbologies from Images or Stream and How to Detect All 1D Barcodes Presented in an Image"
keywords: "Read barcode, Read Barcode from Stream, Scan Barcode from Image, Many Barcodes in One Image, Read PDF417 Barcode, Aspose.BarCode, Read Barcodes in Cloud"
weight: 10
url: /cloud-nodejs/barcode-recognition-basics/

---

## **Overview**
Model *ReaderParams* represents *BarCodeReader* objects in ***Aspose.BarCode for Cloud***. First, it is necessary to indentify a barcode source that can be represented as a file, a stream, or a bitmap object. After that, target barcode types need to be specified using values from the *DecodeType* enum. By default, the library uses the *DecodeType.ALL_SUPPORTED_TYPES* setting that implies iterating over all supported barcode types to check for their presence in the source image. In this case, barcode scanning and recognition takes much more time. Developers can specify explicitly not only the desired symbologies but also a target region or regions in the source image. This allows optimizing the scanning process by avoiding areas without barcodes. Target regions can be determined using a system class called *Rectangle*.


## **Main Recognition Parameters**
In ***Aspose.BarCode for Cloud***, barcode reading is performed according to the following steps:
-	Determine the barcode source (image file, stream, or bitmap), e.g. set the path to a source image
-	Select target barcode types. *DecodeType* is set to *DecodeType.ALL_SUPPORTED_TYPES* by default meaning that the sources image will be scanned to search for all supported barcode types; in this case, time required to finish the barcode detection process will increase.  
  
***Aspose.BarCode for Cloud*** contains the *ReadBarCodes* metho that returns the result of barcode reading in an array of the *BarCodeResult* type.  
    
<p align="center"><img src="multiple_codes.png" hight="50%" width="50%"></p>  
  
## **Getting Recognition Results**
To load barcode recognition outputs, it is needed to call the *ReadBarCodes* method that provides a *BarCodeResult* array. Moreover, the current recognition output can be accessed through the *getFoundBarCodes* method that enables fetching decoding results or the *getFoundCount* method that returns the number of detected barcodes.  
  

## **Barcode Recognition Source**
In ***Aspose.BarCode for Cloud***, there are three ways to set the barcode recognition source: from an image file, from a bitmap, or from a stream. The following five raster image formats are supported: PNG, JPEG, BMP, TIFF, or GIF. Three options to set the source for barcodes reading are explained further. 

### **Read Barcodes from Files**
First of all, barcodes can be scanned and recognized from image files. The full or relative path to the source needs to be specified in the *BarCodeReader* constructor. Alternatively, the *setBarCodeImage* method can be used to pass the path to the existing object of class *BarCodeReader*.  
  
### **Read Barcodes from Bitmap Objects**
It is possible to use a graphical object or a bitmap as a source for barcode reading. Bitmap objects allow working with images consisting of pixel data. To read barcodes from a bitmap, the created bitmap object needs to be passed to the *BarCodeReader()* constructor or the *setBarCodeImage* method.  
  
### **Read Barcodes from Streams**
A stream (in a binary format) can be also used as a source for barcode recognition. This option can be useful in some situations owing to its versatility and accessibility without file systems. A stream to read barcodes from needs to be passed to the *BarCodeReader()* constructor or the *setBarCodeImage* method.
  

## **Setting Target Barcode Types**
***Aspose.BarCode for Cloud*** supports barcode recognition for 60+ various barcode types. To improve the efficiency of the recognition process and optimize its timing, it is recommended to set target symbologies in advance. Otheriwse, the *DecodeType.ALL_SUPPORTED_TYPES* setting of the *DecodeType* enum will be used by default meaning that the library will look over all supported barcode types to check for their presence in the source image. Using this setting will increase the time needed to complete barcode recognition. 

### **Listing Target Barcode Types in DecodeType**
Target barcode types can be specified by grouping them in a list and passing it to the *BarCodeReader()* constructor or the *setBarCodeReadType* method.  
  
### Using ***MultyDecodeType* Mode**
The other way to specify target barcode types is to determine them using a constructor of class *MultyDecodeType* and then pass it to class *BarCodeReader* or the *setBarCodeReadType* method.  
  
### **Using Predefined Barcode Type Sets**
Class *DecodeType* provides the following symbology setsfor barcode reading:
-	*ALL_SUPPORTED_TYPES* - all available barcode types
-	*TYPES_1D* - all supported 1D types
-	*TYPES_2D* - all supported 2D types
-	*POSTAL_TYPES* - all available postal types
-	*MOST_COMMON_TYPES* - a set of most widespread barcode types defined according to Aspose recommendations

The required set can be specified in the *BarCodeReader* constructor or passed to the *setBarCodeReadType* method.
  

## **Setting Target Barcode Regions**
Target areas for barcode detection can be specified by creating one or several objects of the *Rectangle* type. Setting target regions allows improving recognition efficiency and avoiding the regions without any barcodes. Target areas have to be determined accurately as the Aspose library apply heuristic approaches to identify target barcode detection areas. Focusing on too many image regions can lead to recognition efficiency deterioration.

### **Unique Target Region**
To set one target area for barcode recognition, it is necessary to create an object of the *Rectangle* type and then pass it to the *BarCodeReader* constructor or the *setBarCodeImage* method.    

### **Several Target Regions**
It is also possible to set several target areas for barcode detection within the one source image. This can be done in the same way as described above for one target region, i.e., using the *BarCodeReader* constructor or the *setBarCodeImage* method.  
  
## **Recognition Abortion through Manual and Timeout Methods**
Class *BarCodeReader* enables two special methods to stop the recognition process if it becomes unfeasible to complete. The first one is the *setTimeOut* method that can be called to interrupt the barcode reading process immediately after the timeout value gets exceeded. By default, the *TimeOut* value is set to 0.  
  
The second way is to use the *abort()* method. This option is used if the recognition process has been launched in the other thread. This method does not stop the entire process and returns controls immediately.  
  
Both aforementioned methods throw an exception called *RecognitionAbortedException* if the recognition process could not be finished successfully.
  