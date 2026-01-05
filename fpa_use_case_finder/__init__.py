"""
FP&A Use Case Finder for Claude Code
=====================================
A comprehensive tool to discover and catalog Claude Code use cases
specifically for Financial Planning & Analysis (FP&A) teams.

Author: Claude Code Assistant
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Claude Code Assistant"

from .use_cases import UseCaseDatabase
from .searcher import UseCaseSearcher
from .categories import FPACategories
from .reporter import ReportGenerator

__all__ = [
    "UseCaseDatabase",
    "UseCaseSearcher",
    "FPACategories",
    "ReportGenerator"
]
