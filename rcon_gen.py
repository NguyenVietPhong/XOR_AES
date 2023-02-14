def rcon_gen(x):
    import numpy as np
    from poly_mult import poly_mult
    rcon = np.zeros((10, 4), dtype='int16')
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    mod_pol = int('100011011', 2)
    rcon[0, 0] = 1
    for i in range(1, 10):
        rcon[i, 0] = poly_mult(rcon[i-1, 0], 2, mod_pol)
    return rcon