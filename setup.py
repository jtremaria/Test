#!/usr/bin/env python3
"""
Setup script for FP&A Use Case Finder
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fpa_use_case_finder",
    version="1.0.0",
    author="Claude Code Assistant",
    description="Find Claude Code use cases for Financial Planning & Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tristanmoreno/Test",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
        "rich": [
            "rich>=13.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fpa-finder=fpa_use_case_finder.main:main",
        ],
    },
)
