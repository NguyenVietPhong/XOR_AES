def inv_cipher(ciphertext, w, inv_s_box, inv_poly_mat, x):
    import numpy as np
    from add_round_key import add_round_key
    from inv_shift_rows import inv_shift_rows
    from mix_columns import mix_columns
    from sub_bytes import sub_bytes
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    [row, col] = ciphertext.shape
    [row2, col2] = w.shape
    state = np.reshape(ciphertext, (4, 4), 'F')
    round_key = np.zeros((4, 4), dtype='int16')
    round_key[:, :] = w[40:44, :].T
    state = add_round_key(state, round_key)
    for iround in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = sub_bytes(state, inv_s_box)
        round_key[:, :] = w[4 * iround:4 + 4 * iround, :].T
        state = add_round_key(state, round_key)
        state = mix_columns(state, inv_poly_mat)
    state = inv_shift_rows(state)
    state = sub_bytes(state, inv_s_box)
    round_key[:, :] = w[0:4, :].T
    state = add_round_key(state, round_key)
    plaintext = np.reshape(state, (1, 16), 'F')
    return plaintext
