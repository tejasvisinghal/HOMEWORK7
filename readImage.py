import cv2
img=cv2.imread("butterfly.jpg")
cv2.putText(img,"BUTTERFLY",(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,0,0))
cv2.imshow("BUTTERFLY",img)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2NGRAY)
cv2.imshow("GRAY",gray)
print(img)
cv2.waitKey(0)
