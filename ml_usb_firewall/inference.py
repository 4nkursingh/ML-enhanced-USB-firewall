from .engines.keystroke import KeystrokeEngine
from .engines.exfil import ExfilEngine
from .engines.hardware import HardwareEngine

_THRESH = 0.5


class Firewall:
    def __init__(self):
        self.ks = KeystrokeEngine()
        self.ex = ExfilEngine()
        self.hw = HardwareEngine()

    def eval(self, ks_lat, ks_var, ex_spd, ex_ent, hw_pwr, hw_ep):
        f_ks = self.ks.score(ks_lat, ks_var)
        f_ex = self.ex.score(ex_spd, ex_ent)
        f_hw = self.hw.score(hw_pwr, hw_ep)
        triggered = int((f_ks + f_ex + f_hw) >= 2)
        return {
            "keystroke_flag": f_ks,
            "exfil_flag": f_ex,
            "hardware_flag": f_hw,
            "isolated": triggered,
        }
