import os
from xor_img import xor_img
from en_AES_img_key import en_AES_img_key
from de_AES_img_key import de_AES_img_key
from visual_image import visual_image
# from dec_xor_img import 
# PATH
__PATH__ = os.path.abspath(os.getcwd())
_PATH_IMG_I = os.path.join(__PATH__,"Image")
_PATH_IMG_C = os.path.join(__PATH__,"Image_cipher")
_PATH_IMG_P = os.path.join(__PATH__,"Images_plant")


def main(key_hex, folder):
    file_name = []
    for i in os.listdir(folder):
        file_name.append(os.path.join(folder, i))
    # first image encryption
    img_cipher_key = os.path.join(_PATH_IMG_C, file_name[0].split('/')[-1])
    en_AES_img_key(file_name[0],img_cipher_key ,key_hex)
    
    # encrypt image not key image
    for i in range(1,len(file_name)):
        img_cipher = os.path.join(_PATH_IMG_C, file_name[i].split('/')[-1])
        xor_img(file_name[0], file_name[i], img_cipher)
    
    # decrypt key image encryption
    img_plant_key = os.path.join(_PATH_IMG_P, img_cipher_key.split('/')[-1])
    print(img_cipher_key)
    de_AES_img_key(img_cipher_key, img_plant_key, key_hex)

    # decrypt image not key image
    for i in range(1,len(file_name)):
        img_plant = os.path.join(_PATH_IMG_P, file_name[i].split('/')[-1])
        img_cipher = os.path.join(_PATH_IMG_C, file_name[i].split('/')[-1])
        xor_img(img_plant_key, img_cipher, img_plant)

    # visual processing key image
    visual_image(file_name[0].split('/')[-1])

    # visual processing not key image 
    for i in range(1,len(file_name)):
        visual_image(file_name[i].split('/')[-1])


if __name__=='__main__':
    folder = _PATH_IMG_I
    key_hex = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    main(key_hex, folder)



