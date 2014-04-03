import numpy as np
import cv2


def kmeans(frame, K):
#K means
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	#K = 3
	Z = np.float32(frame) #change for kmeans
	
	ret,label,center = cv2.kmeans(Z,K,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	#print center.dtype #center is float32
	center = np.uint8(center)
	#center = center.view(uint8)
	res = center[label.flatten()]
	res2 = res.reshape(frame.shape)
	return res2