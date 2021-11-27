import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "httpsuite",
    version = "1.0",
    author = "Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    license = "MIT",
    keywords = ["httpsuite", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/whoamisec75/httpsuite",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'bs4',
        'requests',
        'dnslib',
        'ipwhois',
    ],
    entry_points={
        'console_scripts': [
            'httpsuite = httpsuite.__main__:main'
        ]
    },
)
