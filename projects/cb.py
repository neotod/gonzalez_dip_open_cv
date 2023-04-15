import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread('./cb.png'), cv2.COLOR_BGR2GRAY)
w_sol = img[520:580, 15:65]
h_steps, w_steps = w_sol.shape

res = np.zeros(img.shape)
cv2.namedWindow(winname='window')

for i in range(0, img.shape[0], h_steps):
    for j in range(0, img.shape[0], w_steps):
        img_crop = img[i:i+h_steps, j:j+w_steps]
        
        # try:
        #     res[i:i+h_steps, j:j+w_steps] = img_crop - w_sol
        # except ValueError:
        #     pass

        cv2.imshow('window', img_crop)


res[res < 0] = 0