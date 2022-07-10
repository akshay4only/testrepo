import cv2
image = cv2.imread("galaxy.jpg",0) #reads image, pass 0 for b&w and 1 for colour
print(type(image))
print(image.shape)#size of number (m,n)
print(image.ndim)#what dimension array is the image

cv2.imshow("galaxy",image)#open img in new window "name",img_variable
cv2.waitKey(0) #wait for an key like getch(), put 0 for close by any key or milisec 2000
cv2.destroyAllWindows() #closes window
#above code dont resize img properly so writing resize code
resized_img = cv2.resize(image,(500,900)) #by manualy rezizing we strech the image
cv2.imshow("galaxy",resized_img)
cv2.waitKey(0)

resized_img2 = cv2.resize(image,(int(image.shape[1]/2),int(image.shape[0]/2)))#shape uses size
cv2.imshow("galaxy",resized_img2)
cv2.imwrite("galaxy_resize.jpg",resized_img2)#saves resized image
cv2.waitKey(0)
cv2.destroyAllWindows