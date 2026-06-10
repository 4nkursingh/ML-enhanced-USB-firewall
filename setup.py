from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as fh:
    long_desc = fh.read()

setup(
    name="ml-usb-firewall",
    version="1.0.0",
    author="ML-USB-Firewall Contributors",
    description="ML-powered USB firewall: keystroke, exfil and hardware analysis.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/ml-usb-firewall",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "scikit-learn",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "ml-usb-firewall=ml_usb_firewall.cli:main",
            "ml-usb-firewall-service=ml_usb_firewall.service:run",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
