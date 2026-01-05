"""
FP&A Categories Module
======================
Defines the core categories and subcategories for FP&A use cases.
"""

from dataclasses import dataclass
from typing import List, Dict
from enum import Enum


class FPACategory(Enum):
    """Main FP&A functional categories."""
    BUDGETING = "budgeting"
    FORECASTING = "forecasting"
    VARIANCE_ANALYSIS = "variance_analysis"
    FINANCIAL_MODELING = "financial_modeling"
    REPORTING = "reporting"
    DATA_INTEGRATION = "data_integration"
    SCENARIO_PLANNING = "scenario_planning"
    COMPLIANCE = "compliance"
    AUTOMATION = "automation"
    EXCEL_INTEGRATION = "excel_integration"


class ComplexityLevel(Enum):
    """Complexity levels for implementation."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class ImplementationTime(Enum):
    """Estimated implementation effort."""
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"


@dataclass
class CategoryInfo:
    """Information about an FP&A category."""
    category: FPACategory
    name: str
    description: str
    keywords: List[str]
    typical_tools: List[str]


class FPACategories:
    """Manager for FP&A categories and their metadata."""

    CATEGORIES: Dict[FPACategory, CategoryInfo] = {
        FPACategory.BUDGETING: CategoryInfo(
            category=FPACategory.BUDGETING,
            name="Budgeting & Planning",
            description="Annual budgets, rolling budgets, departmental budget consolidation",
            keywords=["budget", "planning", "allocation", "cost center", "departmental"],
            typical_tools=["Excel", "Python", "SQL", "Power Query"]
        ),
        FPACategory.FORECASTING: CategoryInfo(
            category=FPACategory.FORECASTING,
            name="Financial Forecasting",
            description="Revenue forecasting, expense projections, cash flow predictions",
            keywords=["forecast", "projection", "prediction", "trend", "time series"],
            typical_tools=["Python", "R", "Excel", "Statistical models"]
        ),
        FPACategory.VARIANCE_ANALYSIS: CategoryInfo(
            category=FPACategory.VARIANCE_ANALYSIS,
            name="Variance Analysis",
            description="Budget vs actuals, trend analysis, root cause identification",
            keywords=["variance", "deviation", "comparison", "actuals", "budget vs actual"],
            typical_tools=["Excel", "Python", "BI tools", "SQL"]
        ),
        FPACategory.FINANCIAL_MODELING: CategoryInfo(
            category=FPACategory.FINANCIAL_MODELING,
            name="Financial Modeling",
            description="DCF models, three-statement models, valuation, M&A analysis",
            keywords=["model", "DCF", "valuation", "three-statement", "LBO", "M&A"],
            typical_tools=["Excel", "Python", "VBA"]
        ),
        FPACategory.REPORTING: CategoryInfo(
            category=FPACategory.REPORTING,
            name="Financial Reporting",
            description="Management reports, board presentations, KPI dashboards",
            keywords=["report", "dashboard", "KPI", "presentation", "visualization"],
            typical_tools=["Excel", "PowerPoint", "Power BI", "Tableau"]
        ),
        FPACategory.DATA_INTEGRATION: CategoryInfo(
            category=FPACategory.DATA_INTEGRATION,
            name="Data Integration",
            description="ERP integration, data warehouse queries, API connections",
            keywords=["integration", "ERP", "API", "database", "ETL", "data warehouse"],
            typical_tools=["Python", "SQL", "APIs", "Snowflake", "Databricks"]
        ),
        FPACategory.SCENARIO_PLANNING: CategoryInfo(
            category=FPACategory.SCENARIO_PLANNING,
            name="Scenario Planning",
            description="What-if analysis, sensitivity analysis, Monte Carlo simulations",
            keywords=["scenario", "sensitivity", "what-if", "Monte Carlo", "simulation"],
            typical_tools=["Excel", "Python", "@RISK", "Crystal Ball"]
        ),
        FPACategory.COMPLIANCE: CategoryInfo(
            category=FPACategory.COMPLIANCE,
            name="Compliance & Controls",
            description="SOX compliance, audit support, internal controls documentation",
            keywords=["compliance", "SOX", "audit", "controls", "documentation"],
            typical_tools=["Excel", "Documentation tools", "Workflow systems"]
        ),
        FPACategory.AUTOMATION: CategoryInfo(
            category=FPACategory.AUTOMATION,
            name="Process Automation",
            description="Automated workflows, scheduled reports, data pipelines",
            keywords=["automation", "workflow", "pipeline", "scheduled", "batch"],
            typical_tools=["Python", "VBA", "Power Automate", "Airflow"]
        ),
        FPACategory.EXCEL_INTEGRATION: CategoryInfo(
            category=FPACategory.EXCEL_INTEGRATION,
            name="Excel Integration",
            description="Excel automation, formula debugging, template creation",
            keywords=["Excel", "spreadsheet", "formula", "VBA", "macro", "template"],
            typical_tools=["Excel", "VBA", "Python openpyxl", "xlwings"]
        )
    }

    @classmethod
    def get_all_categories(cls) -> List[CategoryInfo]:
        """Get all category information."""
        return list(cls.CATEGORIES.values())

    @classmethod
    def get_category(cls, category: FPACategory) -> CategoryInfo:
        """Get information for a specific category."""
        return cls.CATEGORIES.get(category)

    @classmethod
    def find_category_by_keywords(cls, text: str) -> List[FPACategory]:
        """Find matching categories based on keywords in text."""
        text_lower = text.lower()
        matches = []

        for category, info in cls.CATEGORIES.items():
            for keyword in info.keywords:
                if keyword.lower() in text_lower:
                    if category not in matches:
                        matches.append(category)
                    break

        return matches

    @classmethod
    def get_category_names(cls) -> Dict[str, str]:
        """Get mapping of category values to display names."""
        return {
            cat.value: info.name
            for cat, info in cls.CATEGORIES.items()
        }
