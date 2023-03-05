import cv2

# Reading an image in grayscale mode with 2 ways
gumball = cv2.imread("gumball.jpg", 0)
shaun_the_sheep = cv2.imread("shaun the sheep.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Gumball in gray scale mode", gumball)
cv2.imshow("Shaun the sheep in gray scale mode", shaun_the_sheep)

cv2.waitKey(0)
cv2.destroyAllWindows()
