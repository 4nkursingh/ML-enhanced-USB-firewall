import numpy as np


_TEST_RNG = np.random.default_rng(99)


def gen_ks_test(n=200):
    h_lat = _TEST_RNG.normal(120, 30, (n // 2, 1))
    h_var = _TEST_RNG.normal(25, 8, (n // 2, 1))
    h_X = np.hstack([h_lat, h_var])

    b_lat = _TEST_RNG.normal(10, 2, (n // 2, 1))
    b_var = _TEST_RNG.normal(0.5, 0.2, (n // 2, 1))
    b_X = np.hstack([b_lat, b_var])

    X = np.vstack([h_X, b_X])
    y = np.concatenate([np.zeros(n // 2), np.ones(n // 2)])
    idx = _TEST_RNG.permutation(len(y))
    return X[idx], y[idx]


def gen_exfil_test(n=200):
    n_spd = _TEST_RNG.normal(5, 1.5, (n // 2, 1))
    n_ent = _TEST_RNG.uniform(0.1, 0.4, (n // 2, 1))
    n_X = np.hstack([n_spd, n_ent])

    a_spd = _TEST_RNG.normal(80, 15, (n // 2, 1))
    a_ent = _TEST_RNG.uniform(0.7, 1.0, (n // 2, 1))
    a_X = np.hstack([a_spd, a_ent])

    X = np.vstack([n_X, a_X])
    y = np.concatenate([np.zeros(n // 2), np.ones(n // 2)])
    idx = _TEST_RNG.permutation(len(y))
    return X[idx], y[idx]


def gen_hw_test(n=200):
    l_pwr = _TEST_RNG.normal(250, 30, (n // 2, 1))
    l_ep = _TEST_RNG.integers(1, 4, (n // 2, 1)).astype(float)
    l_X = np.hstack([l_pwr, l_ep])

    s_pwr = _TEST_RNG.normal(480, 50, (n // 2, 1))
    s_ep = _TEST_RNG.integers(5, 12, (n // 2, 1)).astype(float)
    s_X = np.hstack([s_pwr, s_ep])

    X = np.vstack([l_X, s_X])
    y = np.concatenate([np.zeros(n // 2), np.ones(n // 2)])
    idx = _TEST_RNG.permutation(len(y))
    return X[idx], y[idx]
