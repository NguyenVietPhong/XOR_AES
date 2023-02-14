//Ảnh gốc sẽ đưuọc lưu tại Folder Image
//Sử dụng hàm read_img để đọc ảnh rồi lưu các giá trị pixels vào Folder Image_txt
//Phía bên mật mã hóa:
chọn 1 ảnh key 
mã hóa XOR bằng hàm enc_xor_img giữa ảnh key và các ảnh còn lại lưu vào Folder Image_txt_cipher
mã hóa ảnh key bằng AES qua hàm en_AES_img_key lưu vài Folder Image_txt_cipher
//Phía bên giải mật mã hóa:
giải mật mã hóa AES ảnh key bằng hàm de_AES_img_key rồi lưu lại Folder Image_txt_plant
giải mật mã hóa XOR bằng hàm de_xor_img rồi lưu lại Folder Image_txt_plant (xor giữa ảnh key vừa giải mật mã hóa với các ảnh cipher còn lại)
//Hiện thị ảnh
Sử dụng hàm show_img từ show_img_from_txt.py 