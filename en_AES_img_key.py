import numpy as np
import itertools
# from read_txt import read_img1
from AES import en_AES
from aes_init import aes_init
import cv2
def en_AES_img_key(img_path, img_cipher, key_hex):
    A = cv2.imread(img_path, 0)
    C = A.copy()
    l = []
    for i in range(512):
       for j in range(512):
           l.append(A[i][j])
    h = []
    for i in range(16384):
        new = []
        for j in range(16):
            new.append(hex(l[16*i+j]))
        h.append(new)

    l3 = []
    ciphertext_hex = h[1]
    ciphertext = np.zeros((1, len(ciphertext_hex)), dtype='int16')
    for i in range(len(ciphertext_hex)):
        ciphertext[0, i] = int(ciphertext_hex[i], 16)
    l1 = []
    [s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init(key_hex)
    for i in range(16384):
    	l1.append(en_AES(h[i],s_box, inv_s_box, w, poly_mat, inv_poly_mat).tolist())
    del h
    l3 = list(itertools.chain(*l1))
    del l1
    l4 = list(itertools.chain(*l3))
    del l3 

    for i in range(512):
        for j in range(512):
            C[i][j] = l4[512*i+j]
    cv2.imwrite(img_cipher, C)
    # cv2.imshow('file', C)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    del l4
if __name__ == "__main__":
    # x =  "/home/phong/LTMM/XOR-AES/XOR-AES/Image_txt_cipher/0002_cipher.txt"
    x = "/home/phong/LTMM/XOR-AES/XOR-AES/Image/0002.png"
    img_cipher = "/home/phong/LTMM/XOR-AES/XOR-AES/Image_cipher/0002.png"
    key_hex = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    en_AES_img_key(x, img_cipher, key_hex)