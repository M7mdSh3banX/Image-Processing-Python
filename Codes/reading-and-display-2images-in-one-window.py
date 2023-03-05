import cv2
import numpy as np

cat_and_dog = cv2.imread("images/cat and dog.jpg")
cat_and_dog2 = cv2.imread("images/cat and dog.jpg")

gumball = cv2.imread("images/gumball.jpg")
gumball2 = cv2.imread("images/gumball.jpg")

# Display two images in the same window
# concatenate image Horizontally
horizontal = np.concatenate((cat_and_dog, cat_and_dog2), axis=1)

# concatenate image Vertically
vertical = np.concatenate((gumball, gumball2), axis=0)

cv2.imshow("Horizontal Screen", horizontal)
cv2.imshow("Vertical Screen", vertical)

cv2.waitKey(0)
cv2.destroyAllWindows()
