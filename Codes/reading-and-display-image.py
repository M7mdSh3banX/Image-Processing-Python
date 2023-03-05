import cv2

# imread(): this method loads an image from the specified file
img = cv2.imread("images/gumball.jpg")

# Seeing the shape width and height and channels of the image using shape attribute.
print(img.shape)

# imshow(): creating GUI window to display an image on screen
# first Parameter: is windows title (should be in string format)
# Second Parameter: is image array
cv2.imshow("Gumball", img)

# waitKey(): To hold the window on screen
# First Parameter: is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass as a parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)

# destroyAllWindows(): for removing/deleting created GUI window from screen and memory
cv2.destroyAllWindows()
