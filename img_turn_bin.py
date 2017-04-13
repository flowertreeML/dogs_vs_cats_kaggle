import cv2
import numpy as np

dir_path = "/home/fuyan/kaggle/dogs_vs_cats/resize_train/"

for j in range(5):
	if j != 4:
		f = file('batch_' + str(j + 1) + '.bin', 'wb')
	else:
		f = file("test_batch.bin", 'wb')
	for cat in range(j * 2500, j * 2500 + 2500):
		label = 0
		img = cv2.imread(dir_path + "cat." + str(cat) + '.jpg')
		l = np.transpose(img, [2, 0, 1])
		l = np.reshape(l, [3072])
		f.write(chr(label))
		for temp in l:
			f.write(chr(temp))
	for dog in range(j * 2500, j * 2500 + 2500):
		label = 1
		img = cv2.imread(dir_path + 'dog.' + str(dog) + '.jpg')
		l = np.transpose(img, [2, 0, 1])
		l = np.reshape(l, [3072])
		f.write(chr(label))
		for temp in l:
			f.write(chr(temp))
		print dog
	f.close()