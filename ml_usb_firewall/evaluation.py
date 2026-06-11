import numpy as np

from .engines.keystroke import KeystrokeEngine
from .engines.exfil import ExfilEngine
from .engines.hardware import HardwareEngine
from .data.test_generators import gen_ks_test, gen_exfil_test, gen_hw_test


def _compute(y_true, y_pred):
    tp = int(np.sum((y_pred == 1) & (y_true == 1)))
    tn = int(np.sum((y_pred == 0) & (y_true == 0)))
    fp = int(np.sum((y_pred == 1) & (y_true == 0)))
    fn = int(np.sum((y_pred == 0) & (y_true == 1)))

    acc = (tp + tn) / (tp + tn + fp + fn)
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0

    return {
        "TP": tp, "TN": tn, "FP": fp, "FN": fn,
        "accuracy":  round(acc,  4),
        "precision": round(prec, 4),
        "recall":    round(rec,  4),
        "f1":        round(f1,   4),
    }


def _eval_ks(engine):
    X, y = gen_ks_test()
    preds = np.array([engine.score(r[0], r[1]) for r in X])
    return _compute(y, preds)


def _eval_exfil(engine):
    X, y = gen_exfil_test()
    preds = np.array([engine.score(r[0], r[1]) for r in X])
    return _compute(y, preds)


def _eval_hw(engine):
    X, y = gen_hw_test()
    preds = np.array([engine.score(r[0], r[1]) for r in X])
    return _compute(y, preds)


def run_eval():
    W = 56
    BAR = "=" * W
    DIV = "-" * W

    def hdr(title):
        pad = (W - len(title) - 2) // 2
        print(f"\n{'=' * pad} {title} {'=' * (W - pad - len(title) - 2)}")

    def row(label, val, suffix=""):
        print(f"  {label:<14} {val}{suffix}")

    def conf(m):
        print(f"  {'Confusion Matrix':}")
        print(f"               Predicted 0   Predicted 1")
        print(f"  Actual 0       {m['TN']:>6}        {m['FP']:>6}")
        print(f"  Actual 1       {m['FN']:>6}        {m['TP']:>6}")

    print(f"\n{BAR}")
    print(f"  ML-USB-FIREWALL  |  Engine Evaluation Report")
    print(f"  Test set: 200 samples per engine  (seed=99, held-out)")
    print(BAR)

    ks = KeystrokeEngine()
    ex = ExfilEngine()
    hw = HardwareEngine()

    engines = [
        ("KEYSTROKE ENGINE", "RandomForestClassifier (100 trees)",
         "Latency (ms), Variance (ms)", _eval_ks(ks)),
        ("EXFIL ENGINE",     "IsolationForest (contamination=0.05)",
         "Transfer Speed (MB/s), File Entropy", _eval_exfil(ex)),
        ("HARDWARE ENGINE",  "DecisionTreeClassifier (max_depth=6)",
         "Power Draw (mA), Endpoint Count", _eval_hw(hw)),
    ]

    for name, algo, feats, m in engines:
        hdr(name)
        print(f"  Algorithm : {algo}")
        print(f"  Features  : {feats}")
        print(DIV)
        row("Accuracy",  f"{m['accuracy']  * 100:.2f}%")
        row("Precision", f"{m['precision'] * 100:.2f}%")
        row("Recall",    f"{m['recall']    * 100:.2f}%")
        row("F1 Score",  f"{m['f1']        * 100:.2f}%")
        print(DIV)
        conf(m)

    print(f"\n{BAR}")
    print(f"  Metric Definitions")
    print(DIV)
    print(f"  Accuracy   = (TP+TN) / All          Fraction of correct predictions")
    print(f"  Precision  = TP / (TP+FP)            Of flagged: how many are real threats")
    print(f"  Recall     = TP / (TP+FN)            Of real threats: how many were caught")
    print(f"  F1 Score   = 2*(P*R)/(P+R)           Harmonic mean — balances P and R")
    print(f"  TP=True Positive  TN=True Negative   FP=False Positive  FN=False Negative")
    print(f"{BAR}\n")
