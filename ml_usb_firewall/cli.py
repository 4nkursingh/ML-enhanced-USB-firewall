import argparse
from .demo import run_demo


def main():
    ap = argparse.ArgumentParser(
        prog="ml-usb-firewall",
        description="ML-powered USB firewall — keystroke, exfil & hardware analysis.",
    )
    ap.add_argument(
        "--demo",
        action="store_true",
        help="Run automated simulation with benign and multi-modal attack profiles.",
    )
    args = ap.parse_args()

    if args.demo:
        run_demo()
    else:
        ap.print_help()
