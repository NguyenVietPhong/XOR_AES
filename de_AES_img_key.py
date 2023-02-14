import numpy as np
import itertools
# from read_txt import read_txt
from AES import de_AES
from aes_init import aes_init
import cv2
def de_AES_img_key(img_path, img_plant, key_hex):
    A = cv2.imread(img_path, 0)
    P = A.copy()
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
    count = 0 
    l1 = []
    [s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init(key_hex)
    for i in range(16384):
    	l1.append(de_AES(h[i],s_box, inv_s_box, w, poly_mat, inv_poly_mat).tolist())
    del h
    l3 = list(itertools.chain(*l1))
    del l1
    l4 = list(itertools.chain(*l3))
    del l3

    for i in range(512):
        for j in range(512):
            P[j][i] = l4[512*j+i]
    cv2.imwrite(img_plant, P)
   
    del l4
if __name__ == "__main__":
    x = "/home/phong/LTMM/XOR-AES/XOR-AES/Image_cipher/0002.png"
    img_plant = "/home/phong/LTMM/XOR-AES/XOR-AES/Images_plant/0002.png"
    key_hex = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    de_AES_img_key(x, img_plant, key_hex)