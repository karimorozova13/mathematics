import numpy as np

# TASK1

a =np.array([[1,2,3,4,5]])
b= np.array([[1/2,1,2,3,4]])

# transpose 
transpose_b= np.transpose(b)
print( a+ transpose_b)
print(np.dot(a,transpose_b))
print(a / transpose_b)


# TASK 2

import cv2 as cv
import urllib
import numpy as np
from google.colab.patches import cv2_imshow as cv_imshow

# Read an image
def read_image_by_url(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)
    return img

url = 'https://a-z-animals.com/media/2021/11/cute-tabby-kittens-sleeping-and-hugging-picture-id480615728.jpg'
url2 = 'https://a-z-animals.com/media/2021/11/cute-kitten-licking-glass-table-with-copy-space-picture-id1293763250-1024x535.jpg'

img = read_image_by_url(url)
img1 = read_image_by_url(url2)

height, width = img.shape[:2]

resized_image = cv.resize(img1, (width // 4, height // 4))

x_pos = (width - resized_image.shape[1]) //2
y_pos = (height - resized_image.shape[0]) //2

combined_image = img.copy()
combined_image[y_pos:y_pos + resized_image.shape[0], x_pos:x_pos + resized_image.shape[1]] = resized_image

M = np.float32([[1, 0, 50], [0, 1, -50]])
transformed_img =cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

rotation_matrix = np.array([[np.cos(np.radians(42)), -np.sin(np.radians(42)),0],
                            [np.sin(np.radians(42)), np.cos(np.radians(42)),0]])
rotated_img = cv.warpAffine(img, rotation_matrix, (width, height))

scale = 1.2
scale_matrix = np.array([[scale,0,0], [0,scale,0]])
scaled_img = cv.warpAffine(img,scale_matrix,(int(width*scale),int(height*scale)))

horizontal_scale = 1.2 
vertical_scale = 1.3
horizontal_matrix = np.array([[horizontal_scale, 0, 0], [0, vertical_scale, 0], [0, 0, 1]])
perspective_img = cv.warpPerspective(img, horizontal_matrix, (width, height))


moved_matrix = np.float32([[1, 0, 50], [0, 1, 50],[0, 0, 1]])
perspective_moved_img = cv.warpPerspective(img, moved_matrix, (width, height))

shear_matrix = np.float32([[1, -np.tan(np.radians(5)),0], [-np.tan(np.radians(10)),1,0],[0, 0, 1]])
shear_img = cv.warpPerspective(img, shear_matrix, (width, height))

rotate_matrix = np.array([[np.cos(np.radians(10)), -np.sin(np.radians(10)),0],
                            [np.sin(np.radians(10)), np.cos(np.radians(10)),0],[0, 0, 1]])
rotate_img = cv.warpPerspective(img, rotate_matrix, (width, height))

common_matrix= horizontal_matrix @ moved_matrix @ shear_matrix @ rotate_matrix
common_img = cv.warpPerspective(img, common_matrix, (width, height))
