import cv2
import os
import matplotlib.pyplot as plt


# PATH
__PATH__ = os.path.abspath(os.getcwd())
print(__PATH__)
_PATH_IMG_I = os.path.join(__PATH__,"Image")
_PATH_IMG_C = os.path.join(__PATH__,"Image_cipher")
_PATH_IMG_P = os.path.join(__PATH__,"Images_plant")

def visual_image(image_name):
    img_c = os.path.join(_PATH_IMG_C, image_name)
    img_p = os.path.join(_PATH_IMG_P, image_name)
    img_i = os.path.join(_PATH_IMG_I, image_name)
    # print(img)
    img_path = [img_i, img_c, img_p]

    fig = plt.figure(figsize=(30, 10))
    columns = 1
    rows = 3
    for i in range(1, columns*rows +1):
        img = cv2.imread(img_path[i-1])
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
    plt.show()

visual_image("0002.png")