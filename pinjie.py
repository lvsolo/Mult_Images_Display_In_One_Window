import cv2
#from matplotlib import pyplot as plt
import numpy as np

#images:list of image
def mult_display(images, output_width = 700):
    assert len(images)
    image_num = len(images)
    sqrt_num =  int(np.sqrt(image_num))
    height_num = sqrt_num 
    width_num = int(np.ceil(image_num/height_num))
    #resize the images 
    resized_w = output_width / width_num 
    resized_h = images[0].shape[1] * resized_w / float(images[0].shape[0])
    resize = tuple(map(int, (resized_h, resized_w)))
    resized_imgs = []
    for image in images:
       tmp = cv2.resize(image, resize)
       resized_imgs.append(tmp)
    total_imgs = np.zeros((1,1))
    for h in range(height_num):
        if h == height_num - 1:
            w_imgs = np.hstack(resized_imgs[h*width_num:])
            remainder = (height_num*width_num)%image_num
            tmp = np.zeros([int(resized_h),int(resized_w),3])
            zeros = tmp 
            for _ in range(remainder):
                #print('w',w_imgs.shape)
                w_imgs = np.hstack([w_imgs, zeros])
        else:
            w_imgs = np.hstack(resized_imgs[h*width_num:(h+1)*width_num])
        if total_imgs.shape[0] == 1:
            total_imgs = w_imgs
        else:
            total_imgs = np.vstack([total_imgs,w_imgs])
    print(total_imgs.shape)
    win_name = 'mult_display'
    #cv2.imshow(win_name,total_imgs)
    #cv2.waitKey(0)
    #plt.imshow(total_imgs)
    #plt.show()
    return total_imgs

import sys
import os 
images1 = os.listdir(sys.argv[1])
images2 = os.listdir(sys.argv[2])

for i in range(1, len(images1)+1):
    image1 = cv2.imread(sys.argv[1]+"/"+str(i)+".jpg")/255.
    image2 = cv2.imread(sys.argv[2]+"/"+str(i)+".jpg")/255.
    imgs = [image1, image2]
    tmp = mult_display(imgs)
    #cv2.imshow('w',tmp)
    #cv2.waitKey(0)
    cv2.imwrite(sys.argv[3]+"/"+str(i) + '.jpg',tmp*255.)

