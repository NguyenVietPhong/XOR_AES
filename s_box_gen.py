def s_box_gen(x):
    import numpy as np
    from find_inverse import find_inverse
    from aff_trans import aff_trans
    from s_box_inversion import s_box_inversion
    inverse = np.zeros((1, 256), dtype='int16')
    s_box = np.zeros((1, 256), dtype='int16')
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    mod_pol = int('100011011', 2)
    inverse[0,0] = 0
    for i in range (1, 256):
        inverse[0, i] = find_inverse(i, mod_pol)
    for i in range (256):
        s_box[0, i] = aff_trans(inverse[0, i])
    inv_s_box = s_box_inversion(s_box)
    if verbose_mode == 1:
        s_box_mat = np.reshape(s_box, (16, 16), 'F').T
        inv_s_box_mat = np.reshape(inv_s_box, (16, 16), 'F').T
    return s_box, inv_s_box


