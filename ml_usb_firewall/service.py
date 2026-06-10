"""
Windows service wrapper that runs the USB firewall monitor as a background process.
Designed to be registered with the Windows Task Scheduler or run at startup.
"""
import time
import logging
import sys
from pathlib import Path

from ml_usb_firewall.inference import Firewall
from ml_usb_firewall.monitor import poll_devices

LOG_PATH = Path.home() / "ml_usb_firewall.log"

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
)


def run():
    logging.info("ml-usb-firewall service starting...")
    fw = Firewall()
    logging.info("All engines calibrated. Monitoring USB bus...")

    while True:
        try:
            poll_devices(fw)
        except KeyboardInterrupt:
            logging.info("Shutdown requested.")
            sys.exit(0)
        except Exception as exc:
            logging.error("Poll error: %s", exc)
        time.sleep(2)


if __name__ == "__main__":
    run()
