def key_expansion(key, s_box, rcon,  x):
    import numpy as np
    from sub_bytes import sub_bytes
    from rot_word import rot_word
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0

    w = np.reshape(key, (4, 4), 'F').T
    temp = np.zeros((1, 4), dtype='int16')
    r = np.zeros((1, 4), dtype='int16')

    for i in range (4, 44):
        temp[0, :] = w[i - 1, :]
        for j in range (4):
            temp[0, j] = w[i-4, j] ^ temp[0, j]
        w = np.vstack((w, temp))
    return w








