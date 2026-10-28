
import numpy as np

# Create a grayscale image matrix
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Image:")
print(image)

# 1. Reshape the image
reshaped = image.reshape(2, 8)
print("\nReshaped Image:")
print(reshaped)

# 2. Slice a region of the image
region = image[0:2, 1:3]
print("\nSliced Region:")
print(region)

# 3. Adjust brightness using broadcasting
bright_image = np.clip(image + 20, 0, 255)
print("\nBrightened Image:")
print(bright_image)

# 4. Matrix multiplication for transformation
transform = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

transformed = np.dot(image, transform)
print("\nTransformed Image:")
print(transformed)
