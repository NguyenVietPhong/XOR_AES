def cipher (plaintext, w, s_box, poly_mat, x):
    import numpy as np
    from add_round_key import add_round_key
    from shift_rows import shift_rows
    from mix_columns import mix_columns
    from sub_bytes import sub_bytes
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    [row, col] = plaintext.shape
    [row2, col2] = w.shape
    state = np.reshape(plaintext, (4, 4), 'F')
    round_key = np.zeros((4, 4), dtype='int16')
    round_key[:, :] = w[0:4, :].T
    state = add_round_key(state, round_key)
    for iround in range(1, 10):
        state = sub_bytes(state, s_box)
        state = shift_rows(state)
        state = mix_columns(state, poly_mat)
        round_key[:, :] = w[4*iround:4+4*iround, :].T
        state = add_round_key(state, round_key)
    state = sub_bytes(state, s_box)
    state = shift_rows(state)
    round_key[:, :] = w[40:44, :].T
    state = add_round_key(state, round_key)
    ciphertext = np.reshape(state, (1, 16), 'F')
    return ciphertext
