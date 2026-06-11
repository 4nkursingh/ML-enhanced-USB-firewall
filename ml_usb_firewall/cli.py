import argparse
from .demo import run_demo
from .evaluation import run_eval


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
    ap.add_argument(
        "--evaluate",
        action="store_true",
        help="Evaluate all engines: Accuracy, Precision, Recall, F1 on a held-out test set.",
    )
    args = ap.parse_args()

    if args.demo:
        run_demo()
    elif args.evaluate:
        run_eval()
    else:
        ap.print_help()
