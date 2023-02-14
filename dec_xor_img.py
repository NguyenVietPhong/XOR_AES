import pandas as pd
import cv2
def de_xor_img(img1, img2, filename):
    A1 = cv2.imread(img1, 0)
    B1 = cv2.imread(img2, 0)
    C = A1.copy()
    # print(B1)
    # print("A1", A1[0][0])

    for i in range(512):
        for j in range(512):
            C[i][j] = A1[i][j]^B1[i][j]
    cv2.imwrite(filename, C)


if __name__ == '__main__':
    img1 = "/home/phongnv/Desktop/phongnv/XOR-AES/Image_cipher/0009.png"
    img2 = "/home/phongnv/Desktop/phongnv/XOR-AES/Images_plant/0012.png"
    filename = "/home/phongnv/Desktop/phongnv/XOR-AES/Images_plant/0009.png"
    de_xor_img(img2, img1, filename)