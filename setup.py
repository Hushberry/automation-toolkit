from setuptools import setup

setup(
    name="automation-toolkit",
    version="1.0.0",
    description="A Python CLI tool for system automation tasks",
    author="Hushberry",
    py_modules=["toolkit"],
    install_requires=[
        "psutil"
    ],
    entry_points={
        "console_scripts": [
            "toolkit=toolkit:main"
        ]
    }
)
