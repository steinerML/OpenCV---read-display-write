import cv2
#print(cv2.__version__) #Prints OpenCV version

#Reads image as unchanged -1
img_unchanged = cv2.imread('image.jpg', -1)

#Reads image as grayscale 0
img_grayscale = cv2.imread('image.jpg', 0)

#Reads image as Colour 1
img_color = cv2.imread('image.jpg',1)

#Shows Unchanged, Grayscale and Color images.
cv2.imshow('Unchanged Image:',img_unchanged)
cv2.imshow('Grayscale Image:',img_grayscale)
cv2.imshow('Color Image:', img_color)

#Writes grayscale image to working folder
cv2.imwrite('gray2_flower.jpg', img_grayscale)

#Waits for 2 seconds (If 0 is passed will wait indefinitely)
cv2.waitKey(0)

#Destroys specific window, in this case the Grayscale one.
cv2.destroyWindow('Grayscale_Image')

#Destroys ALL windows
cv2.destroyAllWindows()