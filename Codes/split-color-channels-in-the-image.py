import cv2

mickey_img = cv2.imread("images/mickey.jpeg")
# Colors stores in the BGR format
B, G, R = cv2.split(mickey_img)

cv2.imshow("Original Image", mickey_img)
cv2.waitKey(0)

cv2.imshow("Image with blue channel", B)
cv2.waitKey(0)

cv2.imshow("Image with green channel", G)
cv2.waitKey(0)

cv2.imshow("Image with red channel", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
