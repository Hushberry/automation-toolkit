from setuptools import setup

setup(
    name="automation-toolkit",
    version="1.0.0",
    py_modules=["toolkit"],
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "toolkit=toolkit:main",
        ],
    },
)
