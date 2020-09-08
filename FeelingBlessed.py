import numpy as np
import cv2


img = cv2.imread('MasjidPicture.jpeg', 1)

 
print(img)

cv2.imshow("MasjidPicture.jpeg", img)
cv2.waitKey(0)
count = 0
rcount = 0

for i in range(len(img)):
	for j in range(len(img[i])):
		print(img[i][j])# = 255

print("\n",img)

cv2.imshow("CurrentStatus.jpeg", img)

cv2.waitKey(0)