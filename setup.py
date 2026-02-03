from setuptools import setup, find_packages

setup(
    name="topsis-dhruv-590",
    version="0.1",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    author="Dhruv Sethi",
    description="TOPSIS implementation using Python",
)
