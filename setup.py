from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = systeminfo.snapshot:main",
        ],
    },
    version="0.1",
    author="Dzmitry Kramich",
    author_email="Dzmitry_Kramich@epam.com",
    description="Information about usage CPU, memory, virtual memory"
)
