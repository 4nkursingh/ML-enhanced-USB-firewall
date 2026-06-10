import numpy as np
from sklearn.tree import DecisionTreeClassifier
from ..data.generators import gen_hardware


class HardwareEngine:
    def __init__(self):
        self._clf = DecisionTreeClassifier(max_depth=6, random_state=42)
        self._train()

    def _train(self):
        X, y = gen_hardware()
        self._clf.fit(X, y)

    def score(self, pwr, ep):
        feat = np.array([[pwr, ep]])
        return int(self._clf.predict(feat)[0])

    def risk(self, pwr, ep):
        feat = np.array([[pwr, ep]])
        return float(self._clf.predict_proba(feat)[0][1])
