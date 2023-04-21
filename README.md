# OpenCV Read, Display, Write.
Read, Display and Write an Image using OpenCV.
## Contents:

Reading, displaying, and writing images are basic to image processing and computer vision.  Even when cropping, resizing, rotating, or applying different filters to process images, you’ll need to first read in the images

I have used these three built-in functions, let’s find out what exactly each one does:

| Function     |Action                                     |
|-------------:|-------------------------------------------|
|     imread() |   helps us read an image                  |
|     imshow() |   displays an image in a window           |
|     imwrite()|  writes an image into the file directory  |

## Test Images used: 
Below the images I used to execute the aforementioned functions:

![Source Image](https://github.com/steinerML/OpenCV-Read-Display-Write-/blob/main/image.jpg) ![Source Image](https://github.com/steinerML/OpenCV-Read-Display-Write-/blob/main/gray2_flower.jpg)


## Summary:

```python
#Reads image as Colour 1
cv2.imread('image.jpg',1)
```
```python
#Shows Unchanged, Grayscale and Color images.
cv2.imshow('Unchanged Image:',img_unchanged)
```

```python
#Writes grayscale image to working folder
cv2.imwrite('gray2_flower.jpg', img_grayscale)
```
