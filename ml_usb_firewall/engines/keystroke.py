import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ..data.generators import gen_keystroke


class KeystrokeEngine:
    def __init__(self):
        self._clf = RandomForestClassifier(n_estimators=100, random_state=42)
        self._train()

    def _train(self):
        X, y = gen_keystroke()
        self._clf.fit(X, y)

    def score(self, lat, var):
        feat = np.array([[lat, var]])
        return int(self._clf.predict(feat)[0])

    def prob(self, lat, var):
        feat = np.array([[lat, var]])
        return float(self._clf.predict_proba(feat)[0][1])
