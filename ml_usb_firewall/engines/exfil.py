import numpy as np
from sklearn.ensemble import IsolationForest
from ..data.generators import gen_exfil


class ExfilEngine:
    def __init__(self):
        self._clf = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        self._train()

    def _train(self):
        X, _ = gen_exfil(normal_only=True)
        self._clf.fit(X)

    def score(self, spd, ent):
        feat = np.array([[spd, ent]])
        raw = self._clf.predict(feat)[0]
        return 1 if raw == -1 else 0

    def anomaly_score(self, spd, ent):
        feat = np.array([[spd, ent]])
        return float(-self._clf.decision_function(feat)[0])
