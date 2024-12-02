import cv2
import numpy as np
from PIL import Image

# Load the map image and custom PNG
map_image_path = "/mnt/data/Screenshot 2024-11-24 at 23.06.41.png"
custom_ball_path = "/mnt/data/ball_white.png"
output_image_path = "/mnt/data/map_with_replacements.png"

map_img = cv2.imread(map_image_path)
custom_ball = cv2.imread(custom_ball_path, cv2.IMREAD_UNCHANGED)  # Load with alpha channel

# Convert the map image to grayscale
gray = cv2.cvtColor(map_img, cv2.COLOR_BGR2GRAY)

# Detect circles using Hough Transform
circles = cv2.HoughCircles(
    gray, 
    cv2.HOUGH_GRADIENT, 
    dp=1.2, 
    minDist=50, 
    param1=50, 
    param2=30, 
    minRadius=10, 
    maxRadius=100
)

# Ensure some circles are detected
if circles is not None:
    circles = np.uint16(np.around(circles))
    
    for circle in circles[0, :]:
        x, y, radius = circle
        diameter = 2 * radius
        
        # Resize the custom ball to match the circle size
        resized_ball = cv2.resize(custom_ball, (diameter, diameter), interpolation=cv2.INTER_AREA)
        
        # Extract the alpha channel for transparency
        alpha_ball = resized_ball[:, :, 3] / 255.0
        alpha_background = 1.0 - alpha_ball

        # Define the region of interest (ROI) on the map
        x1, y1 = max(0, x - radius), max(0, y - radius)
        x2, y2 = x1 + diameter, y1 + diameter

        # Safeguard for image boundaries
        if x2 > map_img.shape[1] or y2 > map_img.shape[0]:
            continue

        roi = map_img[y1:y2, x1:x2]

        # Blend the custom ball into the ROI
        for c in range(3):  # Apply to each color channel
            roi[:, :, c] = (
                alpha_ball * resized_ball[:, :, c] + alpha_background * roi[:, :, c]
            )

# Save the resulting image
cv2.imwrite(output_image_path, map_img)

print(f"Image saved at {output_image_path}")
