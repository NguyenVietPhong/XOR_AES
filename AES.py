import numpy as np
from cypher import cipher
from inv_cypher import inv_cipher
def en_AES(plaintext_hex,s_box, inv_s_box, w, poly_mat, inv_poly_mat):
    plaintext = np.zeros((1, len(plaintext_hex)), dtype='int16')
    for i in range(len(plaintext_hex)):
        plaintext[0, i] = int(plaintext_hex[i], 16)
    ciphertext = cipher(plaintext, w, s_box, poly_mat, 1)
    return ciphertext
def de_AES(ciphertext_hex,s_box, inv_s_box, w, poly_mat, inv_poly_mat):
    ciphertext = np.zeros((1, len(ciphertext_hex)), dtype='int16')
    for i in range(len(ciphertext_hex)):
        ciphertext[0, i] = int(ciphertext_hex[i], 16)
    re_plaintext = inv_cipher (ciphertext, w, inv_s_box, inv_poly_mat, 1)
    return re_plaintext

# if __name__ == '__main__':
#     a = en_AES(plaintext_hex, key_hex)
#     b = de_AES(a, key_hex)