import cv2

gray_img = cv2.imread("gumball.jpg", 0)
cv2.imshow("The image in gray scale mode", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
