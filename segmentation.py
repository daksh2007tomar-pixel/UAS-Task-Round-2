import cv2
import numpy as np

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Error: Image not found. Check the path.")
    exit()

image = cv2.resize(image, (800, 600))
output = image.copy()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_water = np.array([90, 50, 50])
upper_water = np.array([130, 255, 255])

lower_land = np.array([15, 40, 40])
upper_land = np.array([85, 255, 255])

water_mask = cv2.inRange(hsv, lower_water, upper_water)
land_mask = cv2.inRange(hsv, lower_land, upper_land)

output[water_mask > 0] = [255, 0, 0]
output[land_mask > 0] = [0, 255, 0]

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", output)

cv2.imwrite("images/output/segmented_output.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
