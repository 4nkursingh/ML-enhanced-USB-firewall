# ml-usb-firewall

An open-source, ML-powered USB firewall that defends against HID script injection, mass-storage data exfiltration, and hardware descriptor spoofing — using three independent, self-calibrating machine learning engines.

---

## Architecture

```
ml_usb_firewall/
├── __init__.py          # Public API surface
├── cli.py               # argparse entry point
├── demo.py              # Simulation runner
├── inference.py         # Firewall orchestrator (majority-vote)
├── data/
│   ├── __init__.py
│   └── generators.py    # Synthetic data factories (all 3 engines)
└── engines/
    ├── __init__.py
    ├── keystroke.py     # RandomForestClassifier — HID vs human
    ├── exfil.py         # IsolationForest — mass-storage anomaly
    └── hardware.py      # DecisionTreeClassifier — spoof risk
```

---

## ML Engines

| Engine | Algorithm | Features | Threat |
|---|---|---|---|
| **Keystroke** | `RandomForestClassifier` | inter-key latency, variance | HID script injection |
| **Exfil** | `IsolationForest` | transfer speed, file entropy | Mass-storage exfiltration |
| **Hardware** | `DecisionTreeClassifier` | power draw (mA), endpoint count | Descriptor spoofing |

All models are trained on **self-generated synthetic data** at runtime — no external datasets required.

**Isolation Logic:** Device is isolated when **≥ 2 of 3** engines raise a flag (majority vote).

---

## Installation

```bash
pip install -r requirements.txt
pip install .
```

Or directly from PyPI (once published):

```bash
pip install ml-usb-firewall
```

---

## Usage

### CLI

```bash
ml-usb-firewall --demo
```

### Programmatic API

```python
from ml_usb_firewall import Firewall

fw = Firewall()
result = fw.eval(
    ks_lat=9,   ks_var=0.3,
    ex_spd=90,  ex_ent=0.92,
    hw_pwr=500, hw_ep=10,
)
print(result)
```

**Output:**
```python
{
    "keystroke_flag": 1,
    "exfil_flag": 1,
    "hardware_flag": 1,
    "isolated": 1,
}
```

### Individual Engines

```python
from ml_usb_firewall.engines.keystroke import KeystrokeEngine

ks = KeystrokeEngine()
print(ks.score(lat=9, var=0.4))   # 1 = bot
print(ks.prob(lat=9, var=0.4))    # 0.98 — confidence
```

---

## Demo Output (Sample)

```
----------------------------------------------------
  ML-USB-FIREWALL  |  Demo Simulation
----------------------------------------------------
  Initializing engines and calibrating models...
----------------------------------------------------
  Profile  : Benign Human Typist
  Keystroke: [    ]  Exfil: [    ]  Hardware: [    ]
  Decision : >>> ALLOWED  <<<
----------------------------------------------------
  Profile  : Multi-Modal Attack (HID + Exfil + Spoof)
  Keystroke: [FLAG]  Exfil: [FLAG]  Hardware: [FLAG]
  Decision : >>> ISOLATED <<<
----------------------------------------------------
```

---

## License

MIT
