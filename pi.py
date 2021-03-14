import cv2
import numpy as np
import random
from decimal import *

center = (500,500)

estimates = []

def dist(p1,p2):
	return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


for j in range(100):
	img = np.zeros((1000,1000,3),dtype='uint8');

	img = cv2.circle(img,center,500,(255,0,0),1)

	random.seed()

	outside = 0
	inside = 0
	for i in range(2000000):
		p = (random.randrange(1000),random.randrange(1000))
		d = dist(p,center)

		if d <= 500:
			img[p[0],p[1]] = [0,255,0]
			inside += 1
		elif d > 500:
			img[p[0],p[1]] = [0,0,255]
			outside += 1

		if (i%10000 == 0):
			cv2.waitKey(1)
			show = cv2.resize(img,(600,600))
			cv2.imshow('frame',show)
			print('Pi =',Decimal(4)*Decimal(inside)/Decimal(inside+outside),end = '\r')
	pi = Decimal(4)*Decimal(inside)/Decimal(inside+outside)
	print('Pi =',pi)
	estimates.append(pi)
	cv2.waitKey(1)

print('Mean =',np.mean(estimates))
print('Stdev =',np.std(estimates))