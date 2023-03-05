import cv2

# Convert the gumball image to gray scale mode
gumball_in_gray = cv2.imread("images/gumball.jpg", 0)
cv2.imshow("Gumball in gray mode", gumball_in_gray)

# imwrite(): save the image according to the specified format
# First Parameter: string representing the file name
# Second Parameter: the image that is to be saved
cv2.imwrite("images/gumball in gray mode.jpg", gumball_in_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
