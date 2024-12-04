import cv2

source = "/home/abby/Documents/Projects/Pyhton Intermediate Projects/2. Image Resizer/Batman.jpg"
destination = "/home/abby/Documents/Projects/Pyhton Intermediate Projects/2. Image Resizer/Batman_Again.jpg"
percent = 50

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
new_width = int(image.shape[1] * percent / 100)
new_height = int(image.shape[0] * percent / 100)

desize = (new_width, new_height)
output = cv2.resize(image, desize)

cv2.imwrite(destination, output)
