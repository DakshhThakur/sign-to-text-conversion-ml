import os
import cv2
import string

cap = cv2.VideoCapture(0)
directory = 'Image/'

# ✅ Ensure all subdirectories exist
for ch in string.ascii_uppercase:
    path = os.path.join(directory, ch)
    if not os.path.exists(path):
        os.makedirs(path)

while True:
    ret, full_frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # ROI: (x1=0, y1=40) to (x2=300, y2=400)
    roi = full_frame[40:400, 0:300]

    # ✅ Count files in each folder
    count = {ch.lower(): len(os.listdir(os.path.join(directory, ch))) for ch in string.ascii_uppercase}

    # Draw rectangle on original frame
    cv2.rectangle(full_frame, (0, 40), (300, 400), (255, 255, 255), 2)

    # Show full frame and ROI
    cv2.imshow("data", full_frame)
    cv2.imshow("ROI", roi)

    # Wait for key press
    key = cv2.waitKey(10) & 0xFF

    # Save ROI to corresponding folder if a-z key is pressed
    if ord('a') <= key <= ord('z'):
        ch = chr(key)
        path = os.path.join(directory, ch.upper(), f"{count[ch]}.png")
        cv2.imwrite(path, roi)
        print(f"Saved {path}")

    # Press ESC to exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
