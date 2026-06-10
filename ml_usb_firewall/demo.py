from .inference import Firewall

_SEP = "-" * 52

_PROFILES = [
    {
        "label": "Benign Human Typist",
        "params": dict(ks_lat=115, ks_var=22, ex_spd=4.8, ex_ent=0.2, hw_pwr=240, hw_ep=2),
    },
    {
        "label": "HID Script Injection Only",
        "params": dict(ks_lat=9, ks_var=0.4, ex_spd=4.5, ex_ent=0.2, hw_pwr=245, hw_ep=2),
    },
    {
        "label": "Mass Storage Exfiltration Only",
        "params": dict(ks_lat=118, ks_var=24, ex_spd=92, ex_ent=0.88, hw_pwr=248, hw_ep=2),
    },
    {
        "label": "Spoofed Hardware Only",
        "params": dict(ks_lat=112, ks_var=20, ex_spd=5.1, ex_ent=0.22, hw_pwr=490, hw_ep=9),
    },
    {
        "label": "Multi-Modal Attack (HID + Exfil + Spoof)",
        "params": dict(ks_lat=8, ks_var=0.3, ex_spd=95, ex_ent=0.95, hw_pwr=510, hw_ep=11),
    },
    {
        "label": "HID + Hardware Spoof (no exfil)",
        "params": dict(ks_lat=7, ks_var=0.2, ex_spd=4.9, ex_ent=0.18, hw_pwr=495, hw_ep=10),
    },
]


def _fmt(label, res):
    iso = "ISOLATED" if res["isolated"] else "ALLOWED "
    ks = "FLAG" if res["keystroke_flag"] else "    "
    ex = "FLAG" if res["exfil_flag"] else "    "
    hw = "FLAG" if res["hardware_flag"] else "    "
    return (
        f"  Profile  : {label}\n"
        f"  Keystroke: [{ks}]  Exfil: [{ex}]  Hardware: [{hw}]\n"
        f"  Decision : >>> {iso} <<<\n"
    )


def run_demo():
    fw = Firewall()
    print(_SEP)
    print("  ML-USB-FIREWALL  |  Demo Simulation")
    print(_SEP)
    print("  Initializing engines and calibrating models...")
    print(_SEP)

    for p in _PROFILES:
        res = fw.eval(**p["params"])
        print(_fmt(p["label"], res))
        print(_SEP)
