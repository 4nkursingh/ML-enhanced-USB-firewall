import numpy as np

_RNG = np.random.default_rng(42)

def gen_keystroke(n=600):
    human_lat = _RNG.normal(120, 30, (n // 2, 1))
    human_var = _RNG.normal(25, 8, (n // 2, 1))
    human_X = np.hstack([human_lat, human_var])
    human_y = np.zeros(n // 2)

    bot_lat = _RNG.normal(10, 2, (n // 2, 1))
    bot_var = _RNG.normal(0.5, 0.2, (n // 2, 1))
    bot_X = np.hstack([bot_lat, bot_var])
    bot_y = np.ones(n // 2)

    X = np.vstack([human_X, bot_X])
    y = np.concatenate([human_y, bot_y])
    idx = _RNG.permutation(len(y))
    return X[idx], y[idx]


def gen_exfil(n=600, normal_only=False):
    normal_spd = _RNG.normal(5, 1.5, (n // 2, 1))
    normal_ent = _RNG.uniform(0.1, 0.4, (n // 2, 1))
    normal_X = np.hstack([normal_spd, normal_ent])

    if normal_only:
        return normal_X, np.ones(n // 2)

    attack_spd = _RNG.normal(80, 15, (n // 2, 1))
    attack_ent = _RNG.uniform(0.7, 1.0, (n // 2, 1))
    attack_X = np.hstack([attack_spd, attack_ent])

    X = np.vstack([normal_X, attack_X])
    y = np.concatenate([np.ones(n // 2), -np.ones(n // 2)])
    idx = _RNG.permutation(len(y))
    return X[idx], y[idx]


def gen_hardware(n=600):
    legit_pwr = _RNG.normal(250, 30, (n // 2, 1))
    legit_ep = _RNG.integers(1, 4, (n // 2, 1)).astype(float)
    legit_X = np.hstack([legit_pwr, legit_ep])
    legit_y = np.zeros(n // 2)

    spoof_pwr = _RNG.normal(480, 50, (n // 2, 1))
    spoof_ep = _RNG.integers(5, 12, (n // 2, 1)).astype(float)
    spoof_X = np.hstack([spoof_pwr, spoof_ep])
    spoof_y = np.ones(n // 2)

    X = np.vstack([legit_X, spoof_X])
    y = np.concatenate([legit_y, spoof_y])
    idx = _RNG.permutation(len(y))
    return X[idx], y[idx]
