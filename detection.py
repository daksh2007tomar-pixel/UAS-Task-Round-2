import cv2
import numpy as np
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Error: Image not found")
    exit()

image = cv2.resize(image, (800, 600))
output = image.copy()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)


_, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)


contours, _ = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)


camps = []

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 600:
        continue

    perimeter = cv2.arcLength(cnt, True)
    if perimeter == 0:
        continue

    circularity = 4 * np.pi * area / (perimeter * perimeter)

    if circularity > 0.7:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)

        cv2.circle(output, center, radius, (0, 255, 0), 2)
        cv2.circle(output, center, 3, (0, 0, 255), -1)

        camps.append(center)

camp_info = []

for (x, y) in camps:
    b, g, r = image[y, x]

    if b > 150 and g < 120 and r < 120:
        color = "Blue"
        capacity = 4
    elif r > 150 and g < 130:
        color = "Pink"
        capacity = 3
    else:
        color = "Grey"
        capacity = 2

    camp_info.append({
        "center": (x, y),
        "color": color,
        "capacity": capacity
    })


for camp in camp_info:
    text = f"{camp['color']} | Cap: {camp['capacity']}"
    x, y = camp["center"]

    cv2.putText(
        output,
        text,
        (x - 60, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 255),
        2
    )

cv2.imshow("Rescue Camp Detection", output)
cv2.imwrite("images/output/rescue_camps_detected.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
