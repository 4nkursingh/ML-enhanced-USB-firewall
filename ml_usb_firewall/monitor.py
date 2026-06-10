"""
Stub USB device poller.

In production this module would call platform APIs (e.g. WMI on Windows,
udev on Linux) to enumerate connected USB devices and read real hardware
metrics. For now it logs a heartbeat so the service loop is exercisable
without hardware.

Replace `_read_device` with real sensor code to activate live enforcement.
"""
import logging
import random

_rng = random.Random(0)


def _read_device():
    return {
        "ks_lat": _rng.gauss(120, 30),
        "ks_var": _rng.gauss(25, 8),
        "ex_spd": _rng.gauss(5, 1.5),
        "ex_ent": _rng.uniform(0.1, 0.4),
        "hw_pwr": _rng.gauss(250, 30),
        "hw_ep": float(_rng.randint(1, 3)),
    }


def poll_devices(fw):
    metrics = _read_device()
    result = fw.eval(**metrics)
    if result["isolated"]:
        logging.warning("ISOLATED  flags=%s", result)
    else:
        logging.info("ALLOWED   flags=%s", result)
