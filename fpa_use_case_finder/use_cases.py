"""
Use Cases Database Module
=========================
Contains the comprehensive database of Claude Code use cases for FP&A.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from .categories import FPACategory, ComplexityLevel, ImplementationTime


@dataclass
class UseCase:
    """Represents a single Claude Code use case for FP&A."""
    id: str
    title: str
    description: str
    category: FPACategory
    subcategories: List[str]
    complexity: ComplexityLevel
    implementation_time: ImplementationTime
    benefits: List[str]
    example_prompts: List[str]
    tools_used: List[str]
    source: str
    source_url: Optional[str] = None
    productivity_gain: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    date_added: datetime = field(default_factory=datetime.now)


class UseCaseDatabase:
    """Database of all Claude Code use cases for FP&A."""

    def __init__(self):
        self.use_cases: List[UseCase] = self._load_use_cases()

    def _load_use_cases(self) -> List[UseCase]:
        """Load all predefined use cases."""
        return [
            # ============================================
            # BUDGETING & PLANNING USE CASES
            # ============================================
            UseCase(
                id="budget-001",
                title="Automated Budget Consolidation",
                description="Use Claude Code to automatically consolidate departmental budgets from multiple Excel files, reconcile submissions, identify inconsistencies, and generate a unified corporate budget.",
                category=FPACategory.BUDGETING,
                subcategories=["consolidation", "departmental budgets"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Reduce budget consolidation time by 80%",
                    "Automatic inconsistency detection",
                    "Standardized output format",
                    "Audit trail of all changes"
                ],
                example_prompts=[
                    "Consolidate all budget files in the /budgets folder, identify any departments with unrealistic assumptions, and create a summary report",
                    "Read the departmental budget submissions and flag any that exceed the 5% growth guideline",
                    "Create a Python script to merge quarterly budget files and highlight variances over $10,000"
                ],
                tools_used=["Python", "openpyxl", "pandas", "Excel"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                productivity_gain="80% reduction in consolidation time",
                tags=["automation", "consolidation", "excel", "multi-department"]
            ),
            UseCase(
                id="budget-002",
                title="Driver-Based Budget Model Creation",
                description="Build sophisticated driver-based budget models that automatically translate operational assumptions (customer growth, production volumes, market share) into comprehensive financial plans.",
                category=FPACategory.BUDGETING,
                subcategories=["driver-based planning", "operational modeling"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Dynamic budget adjustments based on drivers",
                    "Better alignment between operations and finance",
                    "Faster scenario analysis",
                    "Improved forecast accuracy"
                ],
                example_prompts=[
                    "Create a driver-based budget model where revenue is calculated from customer count × average order value × purchase frequency",
                    "Build an Excel model that links headcount growth to revenue targets with automatic COGS calculation",
                    "Design a budget template with linked drivers for SaaS metrics: ARR, churn, expansion revenue"
                ],
                tools_used=["Excel", "Python", "Financial modeling"],
                source="Cube Software",
                source_url="https://www.cubesoftware.com/blog/ai-for-fpa-financial-planning-analysis",
                productivity_gain="50% faster budget cycle",
                tags=["driver-based", "operational", "SaaS", "modeling"]
            ),
            UseCase(
                id="budget-003",
                title="Zero-Based Budget Analysis",
                description="Implement zero-based budgeting analysis by having Claude Code review every expense line item, question historical allocations, and suggest optimizations based on actual needs.",
                category=FPACategory.BUDGETING,
                subcategories=["zero-based budgeting", "cost optimization"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Identify unnecessary expenses",
                    "Data-driven cost reduction",
                    "Better resource allocation",
                    "Challenge status quo spending"
                ],
                example_prompts=[
                    "Analyze the marketing budget line by line and identify any items that haven't shown ROI in the past 2 years",
                    "Review all G&A expenses and flag items that have grown faster than revenue",
                    "Create a zero-based budget template for the IT department with justification requirements"
                ],
                tools_used=["Excel", "Python", "pandas"],
                source="FP&A Trends",
                source_url="https://fpa-trends.com/article/how-agentic-ai-powering-next-generation-fpa",
                tags=["ZBB", "cost-reduction", "analysis"]
            ),

            # ============================================
            # FORECASTING USE CASES
            # ============================================
            UseCase(
                id="forecast-001",
                title="Automated Rolling Forecast Updates",
                description="Create scripts that automatically update rolling forecasts with the latest actuals, recalculate projections, and highlight significant changes from previous forecasts.",
                category=FPACategory.FORECASTING,
                subcategories=["rolling forecast", "automation"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Always-current forecasts",
                    "Reduced manual data entry",
                    "Automatic variance flagging",
                    "Consistent methodology"
                ],
                example_prompts=[
                    "Update the rolling forecast model with Q3 actuals and extend the projection to Q4 next year",
                    "Create a Python script that pulls actuals from our data warehouse and updates the forecast Excel file weekly",
                    "Build an automated workflow that compares each forecast iteration and reports changes over 5%"
                ],
                tools_used=["Python", "Excel", "SQL", "pandas"],
                source="Cube Software",
                source_url="https://www.cubesoftware.com/blog/ai-tools-for-fpa",
                productivity_gain="Quarterly prep time reduced to hours",
                tags=["rolling", "automation", "actuals", "updates"]
            ),
            UseCase(
                id="forecast-002",
                title="Revenue Forecasting with ML",
                description="Build machine learning models for revenue forecasting that analyze historical patterns, seasonality, and external factors to generate more accurate predictions.",
                category=FPACategory.FORECASTING,
                subcategories=["machine learning", "revenue"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "15-30% improvement in forecast accuracy",
                    "Automatic pattern detection",
                    "Seasonality adjustment",
                    "Confidence intervals included"
                ],
                example_prompts=[
                    "Create a time series model to forecast next quarter's revenue using Prophet library",
                    "Analyze 3 years of sales data and build a model that accounts for seasonality and trend",
                    "Build a revenue forecasting model that incorporates macroeconomic indicators"
                ],
                tools_used=["Python", "Prophet", "scikit-learn", "pandas"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/claude-for-financial-services",
                productivity_gain="65% of teams rate AI forecasts as good/great vs 42% without",
                tags=["ML", "time-series", "revenue", "prediction"]
            ),
            UseCase(
                id="forecast-003",
                title="Cash Flow Forecasting Automation",
                description="Automate cash flow forecasting by analyzing AR/AP aging, payment patterns, and seasonal variations to predict future cash positions.",
                category=FPACategory.FORECASTING,
                subcategories=["cash flow", "treasury"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Better cash management",
                    "Early warning for cash shortfalls",
                    "Optimized working capital",
                    "Improved vendor payment timing"
                ],
                example_prompts=[
                    "Analyze AR aging report and predict collections for the next 90 days based on historical payment patterns",
                    "Create a 13-week cash flow forecast model that incorporates AP schedules and expected collections",
                    "Build a cash flow model that flags potential liquidity issues 30 days in advance"
                ],
                tools_used=["Excel", "Python", "SQL"],
                source="Oracle",
                source_url="https://www.oracle.com/erp/ai-driven-financial-planning-and-analysis/",
                tags=["cash-flow", "treasury", "working-capital", "liquidity"]
            ),
            UseCase(
                id="forecast-004",
                title="Expense Forecasting with Trend Analysis",
                description="Develop expense forecasting models that identify spending trends, detect anomalies, and project future costs based on historical patterns and known commitments.",
                category=FPACategory.FORECASTING,
                subcategories=["expense", "trend analysis"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Accurate expense projections",
                    "Anomaly detection",
                    "Better cost management",
                    "Early warning on cost overruns"
                ],
                example_prompts=[
                    "Analyze the past 24 months of operating expenses and project next year's costs by category",
                    "Identify expense categories with abnormal growth patterns in the current quarter",
                    "Create an expense forecast that accounts for known headcount additions and contract renewals"
                ],
                tools_used=["Python", "pandas", "Excel"],
                source="KPMG",
                source_url="https://kpmg.com/us/en/articles/2025/future-of-fpa-with-ai.html",
                tags=["expenses", "trends", "cost-management"]
            ),

            # ============================================
            # VARIANCE ANALYSIS USE CASES
            # ============================================
            UseCase(
                id="variance-001",
                title="Automated Variance Commentary Generation",
                description="Automatically generate variance explanations and commentary for budget vs actual reports, identifying root causes and suggesting corrective actions.",
                category=FPACategory.VARIANCE_ANALYSIS,
                subcategories=["commentary", "root cause"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Save hours on variance explanations",
                    "Consistent commentary quality",
                    "Faster month-end close",
                    "Better root cause identification"
                ],
                example_prompts=[
                    "Analyze the budget vs actual report and generate executive-level variance commentary for items over $50K",
                    "Review Q3 variances and identify the top 5 drivers of the revenue shortfall",
                    "Generate variance explanations for the board deck, focusing on EBITDA bridge items"
                ],
                tools_used=["Excel", "Python", "pandas"],
                source="Aleph",
                source_url="https://www.getaleph.com/answers/ai-fpa-software-variance-detection",
                productivity_gain="90% reduction in commentary writing time",
                tags=["commentary", "automation", "month-end", "reporting"]
            ),
            UseCase(
                id="variance-002",
                title="Real-Time Variance Monitoring",
                description="Build monitoring scripts that continuously compare actuals to budget/forecast and alert the team when material variances occur.",
                category=FPACategory.VARIANCE_ANALYSIS,
                subcategories=["monitoring", "alerts"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Proactive issue identification",
                    "Faster response to variances",
                    "Reduced surprise at month-end",
                    "Better cost control"
                ],
                example_prompts=[
                    "Create a Python script that checks daily sales against forecast and alerts if we're tracking more than 10% below",
                    "Build a monitoring dashboard that flags expense categories exceeding 90% of monthly budget",
                    "Set up automated alerts when any cost center exceeds 80% of quarterly budget mid-month"
                ],
                tools_used=["Python", "SQL", "APIs", "Slack/Email integration"],
                source="Surfside Capital Advisors",
                source_url="https://www.surfcapadvisors.com/2025/10/02/how-has-ai-changed-fpa/",
                tags=["monitoring", "alerts", "real-time", "proactive"]
            ),
            UseCase(
                id="variance-003",
                title="Multi-Dimensional Variance Decomposition",
                description="Perform sophisticated variance analysis that decomposes variances by multiple dimensions: price/volume, mix effects, currency impacts, and timing differences.",
                category=FPACategory.VARIANCE_ANALYSIS,
                subcategories=["decomposition", "multi-dimensional"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Deeper variance understanding",
                    "Separate controllable from uncontrollable factors",
                    "Better performance evaluation",
                    "More actionable insights"
                ],
                example_prompts=[
                    "Decompose the gross margin variance into price, volume, and mix effects for each product line",
                    "Analyze the revenue variance and separate the impact of currency fluctuations from operational performance",
                    "Create a variance waterfall showing contribution from each business unit and variance driver"
                ],
                tools_used=["Excel", "Python", "pandas"],
                source="Abacum",
                source_url="https://www.abacum.ai/blog/how-to-use-budget-vs-actuals-variance-analysis-to-improve-fp-a-outcomes",
                tags=["decomposition", "price-volume", "mix", "currency"]
            ),

            # ============================================
            # FINANCIAL MODELING USE CASES
            # ============================================
            UseCase(
                id="model-001",
                title="DCF Model Development",
                description="Build or enhance discounted cash flow (DCF) valuation models with automated sensitivity analysis and scenario comparisons.",
                category=FPACategory.FINANCIAL_MODELING,
                subcategories=["valuation", "DCF"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Consistent valuation methodology",
                    "Automated sensitivity tables",
                    "Quick scenario comparisons",
                    "Professional output format"
                ],
                example_prompts=[
                    "Build a DCF model for the acquisition target with a 5-year projection period and terminal value",
                    "Add sensitivity analysis to the DCF showing value impact of WACC and terminal growth rate changes",
                    "Create a DCF template with automated WACC calculation and scenario toggles"
                ],
                tools_used=["Excel", "Python", "VBA"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                productivity_gain="Claude passed 5 of 7 Financial Modeling World Cup levels",
                tags=["DCF", "valuation", "M&A", "investment-analysis"]
            ),
            UseCase(
                id="model-002",
                title="Three-Statement Model Construction",
                description="Create integrated three-statement financial models (Income Statement, Balance Sheet, Cash Flow) with proper linkages and circular reference handling.",
                category=FPACategory.FINANCIAL_MODELING,
                subcategories=["three-statement", "integration"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Proper statement integration",
                    "Automatic balancing",
                    "Scenario flexibility",
                    "Audit-ready structure"
                ],
                example_prompts=[
                    "Build a three-statement model with working capital schedules and debt amortization",
                    "Create an integrated financial model for a SaaS company with deferred revenue accounting",
                    "Debug my three-statement model - the balance sheet doesn't balance after adding the debt schedule"
                ],
                tools_used=["Excel", "VBA"],
                source="FundamentalLabs Excel Agent",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                productivity_gain="83% accuracy on complex Excel tasks",
                tags=["three-statement", "integration", "balance-sheet"]
            ),
            UseCase(
                id="model-003",
                title="LBO Model Development",
                description="Create leveraged buyout (LBO) models with debt schedules, returns analysis, and sensitivity to entry/exit multiples.",
                category=FPACategory.FINANCIAL_MODELING,
                subcategories=["LBO", "private equity"],
                complexity=ComplexityLevel.EXPERT,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Quick deal evaluation",
                    "Returns optimization",
                    "Debt capacity analysis",
                    "Sensitivity to key assumptions"
                ],
                example_prompts=[
                    "Build an LBO model with senior debt, mezzanine, and equity tranches",
                    "Create an LBO returns analysis with IRR sensitivity to entry multiple and exit timing",
                    "Add a debt schedule to my LBO model with cash sweep and mandatory amortization"
                ],
                tools_used=["Excel", "VBA"],
                source="F9 Finance",
                source_url="https://www.f9finance.com/claude-for-finance/",
                tags=["LBO", "PE", "returns", "debt-schedule"]
            ),
            UseCase(
                id="model-004",
                title="Formula Debugging and Optimization",
                description="Debug complex Excel formulas, identify circular references, and optimize model performance by improving formula efficiency.",
                category=FPACategory.FINANCIAL_MODELING,
                subcategories=["debugging", "optimization"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Fix broken formulas quickly",
                    "Improve model performance",
                    "Reduce file size",
                    "Better formula transparency"
                ],
                example_prompts=[
                    "Debug this SUMIFS formula that's returning #VALUE! error",
                    "Optimize my model - it takes 30 seconds to recalculate",
                    "Find and fix all circular references in my financial model",
                    "Convert these nested IF statements to a cleaner INDEX/MATCH approach"
                ],
                tools_used=["Excel", "VBA"],
                source="Claude in Excel",
                source_url="https://claude.com/claude-in-excel",
                tags=["debugging", "formulas", "optimization", "excel"]
            ),

            # ============================================
            # REPORTING USE CASES
            # ============================================
            UseCase(
                id="report-001",
                title="Automated Management Report Generation",
                description="Generate comprehensive management reports automatically from raw financial data, including variance analysis, KPI metrics, and executive commentary.",
                category=FPACategory.REPORTING,
                subcategories=["management reporting", "automation"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Consistent report formatting",
                    "Faster report production",
                    "Reduced manual errors",
                    "More time for analysis"
                ],
                example_prompts=[
                    "Create a monthly management report from the trial balance data with P&L, balance sheet, and KPIs",
                    "Generate an executive summary for the board highlighting the top 3 financial story points this quarter",
                    "Build a report template that automatically populates with data from our ERP export"
                ],
                tools_used=["Excel", "Python", "pandas", "reportlab"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/claude-for-financial-services",
                productivity_gain="NBIM achieved 20% productivity gains (213,000 hours)",
                tags=["management-reports", "automation", "executive-summary"]
            ),
            UseCase(
                id="report-002",
                title="KPI Dashboard Creation",
                description="Design and build KPI dashboards that track financial and operational metrics with automatic data refresh and trend visualization.",
                category=FPACategory.REPORTING,
                subcategories=["dashboards", "KPIs"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Real-time visibility",
                    "Self-service analytics",
                    "Consistent metric definitions",
                    "Mobile accessibility"
                ],
                example_prompts=[
                    "Create a Python dashboard showing revenue, gross margin, and operating income trends",
                    "Build an Excel dashboard with conditional formatting for KPI status indicators",
                    "Design a SaaS metrics dashboard tracking MRR, churn, CAC, and LTV"
                ],
                tools_used=["Python", "plotly", "Excel", "Power BI"],
                source="Data Studios",
                source_url="https://www.datastudios.org/post/claude-and-spreadsheets-advanced-data-analysis-with-ai-in-2025",
                tags=["dashboard", "KPI", "visualization", "metrics"]
            ),
            UseCase(
                id="report-003",
                title="Board Presentation Automation",
                description="Automate the creation of board presentations by pulling financial data, generating charts, and populating slides with key insights.",
                category=FPACategory.REPORTING,
                subcategories=["board reporting", "presentations"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Consistent branding",
                    "Faster deck preparation",
                    "Dynamic chart updates",
                    "Version control"
                ],
                example_prompts=[
                    "Create a PowerPoint slide deck with Q3 financial results and charts",
                    "Update the board presentation template with latest month-end numbers",
                    "Generate a financial summary slide with waterfall chart for EBITDA bridge"
                ],
                tools_used=["Python", "python-pptx", "Excel"],
                source="Claude Code Interpreter",
                source_url="https://simonwillison.net/2025/Sep/9/claude-code-interpreter/",
                tags=["board", "presentation", "powerpoint", "charts"]
            ),

            # ============================================
            # DATA INTEGRATION USE CASES
            # ============================================
            UseCase(
                id="data-001",
                title="ERP Data Extraction and Transformation",
                description="Build scripts to extract data from ERP systems, transform it into analysis-ready format, and load into Excel or data warehouses.",
                category=FPACategory.DATA_INTEGRATION,
                subcategories=["ERP", "ETL"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Automated data extraction",
                    "Consistent data formats",
                    "Reduced manual data entry",
                    "Audit trail"
                ],
                example_prompts=[
                    "Create a Python script to extract GL data from our SAP export and format for the budget model",
                    "Build an ETL pipeline that pulls sales data from NetSuite and loads it into our forecast template",
                    "Transform the Oracle export into a pivot-ready format with proper account hierarchy"
                ],
                tools_used=["Python", "pandas", "SQL", "APIs"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                tags=["ERP", "ETL", "SAP", "NetSuite", "Oracle"]
            ),
            UseCase(
                id="data-002",
                title="Data Warehouse Query Automation",
                description="Generate and execute SQL queries against Snowflake or Databricks to pull financial data for analysis and reporting.",
                category=FPACategory.DATA_INTEGRATION,
                subcategories=["data warehouse", "SQL"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Self-service data access",
                    "Complex query generation",
                    "Faster data retrieval",
                    "Reduced IT dependency"
                ],
                example_prompts=[
                    "Write a SQL query to pull monthly revenue by product category from Snowflake for the past 2 years",
                    "Create a query that calculates customer lifetime value from our data warehouse",
                    "Generate SQL to extract cost center expenses with department hierarchy from Databricks"
                ],
                tools_used=["SQL", "Python", "Snowflake", "Databricks"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/claude-for-financial-services",
                productivity_gain="NBIM can seamlessly query their Snowflake data warehouse",
                tags=["SQL", "Snowflake", "Databricks", "data-warehouse"]
            ),
            UseCase(
                id="data-003",
                title="API Integration for Market Data",
                description="Connect to financial data APIs (LSEG, S&P Capital IQ, Bloomberg) to pull real-time market data for analysis and models.",
                category=FPACategory.DATA_INTEGRATION,
                subcategories=["API", "market data"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Real-time data access",
                    "Automated data feeds",
                    "Multiple source integration",
                    "Reduced manual updates"
                ],
                example_prompts=[
                    "Build a Python script to pull daily stock prices from Yahoo Finance for our portfolio",
                    "Create an integration to fetch FX rates and update our currency exposure model",
                    "Connect to S&P Capital IQ API to pull peer company financials for benchmarking"
                ],
                tools_used=["Python", "APIs", "requests", "pandas"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                tags=["API", "market-data", "real-time", "integration"]
            ),

            # ============================================
            # SCENARIO PLANNING USE CASES
            # ============================================
            UseCase(
                id="scenario-001",
                title="What-If Scenario Modeling",
                description="Build flexible scenario models that allow quick toggling between base, upside, and downside cases with automatic recalculation.",
                category=FPACategory.SCENARIO_PLANNING,
                subcategories=["what-if", "scenarios"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Quick scenario comparison",
                    "Better risk understanding",
                    "Improved decision support",
                    "Dynamic assumptions"
                ],
                example_prompts=[
                    "Add scenario toggles to the budget model for base, optimistic, and pessimistic cases",
                    "Create a what-if analysis showing impact of 10%, 20%, 30% revenue decline on cash runway",
                    "Build scenario comparison tables for the three strategic options we're evaluating"
                ],
                tools_used=["Excel", "Python", "VBA"],
                source="Cube Software",
                source_url="https://www.cubesoftware.com/blog/ai-for-fpa-financial-planning-analysis",
                tags=["scenarios", "what-if", "risk", "decision-support"]
            ),
            UseCase(
                id="scenario-002",
                title="Monte Carlo Simulation",
                description="Implement Monte Carlo simulations to model uncertainty and generate probability distributions for key financial outcomes.",
                category=FPACategory.SCENARIO_PLANNING,
                subcategories=["Monte Carlo", "simulation"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Quantified uncertainty",
                    "Probability distributions",
                    "Risk-adjusted decisions",
                    "Confidence intervals"
                ],
                example_prompts=[
                    "Build a Monte Carlo simulation to model the range of possible NPV outcomes for this investment",
                    "Create a cash flow simulation with probability distributions for key revenue and expense drivers",
                    "Run 10,000 iterations to model the probability of achieving our revenue target"
                ],
                tools_used=["Python", "numpy", "@RISK", "Excel"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/claude-for-financial-services",
                tags=["Monte-Carlo", "simulation", "probability", "risk"]
            ),
            UseCase(
                id="scenario-003",
                title="Sensitivity Analysis Automation",
                description="Create automated sensitivity tables and tornado charts showing the impact of key assumption changes on financial outcomes.",
                category=FPACategory.SCENARIO_PLANNING,
                subcategories=["sensitivity", "tornado charts"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Identify key value drivers",
                    "Visual impact analysis",
                    "Better assumption focus",
                    "Quick recalculation"
                ],
                example_prompts=[
                    "Create a two-way sensitivity table showing IRR across different entry multiples and exit years",
                    "Build a tornado chart showing which assumptions have the largest impact on project NPV",
                    "Generate sensitivity analysis for the DCF model varying WACC and growth rates"
                ],
                tools_used=["Excel", "Python", "matplotlib"],
                source="F9 Finance",
                source_url="https://www.f9finance.com/claude-for-finance/",
                tags=["sensitivity", "tornado", "data-tables", "visualization"]
            ),

            # ============================================
            # COMPLIANCE USE CASES
            # ============================================
            UseCase(
                id="compliance-001",
                title="SOX Documentation Automation",
                description="Automate the creation and maintenance of SOX compliance documentation, control descriptions, and testing procedures.",
                category=FPACategory.COMPLIANCE,
                subcategories=["SOX", "documentation"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Consistent documentation",
                    "Faster audit preparation",
                    "Reduced compliance burden",
                    "Better control visibility"
                ],
                example_prompts=[
                    "Create SOX control documentation for the revenue recognition process",
                    "Generate testing procedures for our key financial controls",
                    "Update control descriptions to reflect changes in our close process"
                ],
                tools_used=["Word", "Excel", "documentation tools"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/claude-for-financial-services",
                tags=["SOX", "compliance", "audit", "controls"]
            ),
            UseCase(
                id="compliance-002",
                title="Audit Support Package Preparation",
                description="Automate the preparation of audit support packages with proper documentation, reconciliations, and supporting schedules.",
                category=FPACategory.COMPLIANCE,
                subcategories=["audit", "documentation"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Faster PBC preparation",
                    "Complete documentation",
                    "Reduced auditor questions",
                    "Consistent format"
                ],
                example_prompts=[
                    "Create an audit support package for the inventory balance with roll-forward and support",
                    "Generate reconciliations for all balance sheet accounts with proper sign-off sections",
                    "Prepare the revenue substantive testing package with sample selections"
                ],
                tools_used=["Excel", "Word", "Python"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                tags=["audit", "PBC", "documentation", "reconciliation"]
            ),

            # ============================================
            # AUTOMATION USE CASES
            # ============================================
            UseCase(
                id="automation-001",
                title="Month-End Close Automation",
                description="Automate repetitive month-end close tasks including journal entry preparation, reconciliation generation, and close checklist tracking.",
                category=FPACategory.AUTOMATION,
                subcategories=["month-end", "close"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Faster close cycle",
                    "Reduced errors",
                    "Consistent processes",
                    "Better tracking"
                ],
                example_prompts=[
                    "Create a script to generate standard month-end journal entries from our accrual template",
                    "Build an automated close checklist that tracks completion status and sends reminders",
                    "Automate the bank reconciliation process by matching transactions from the bank statement"
                ],
                tools_used=["Python", "Excel", "VBA"],
                source="Cube Software",
                source_url="https://www.cubesoftware.com/blog/ai-for-fpa-financial-planning-analysis",
                tags=["month-end", "close", "journals", "reconciliation"]
            ),
            UseCase(
                id="automation-002",
                title="Scheduled Report Distribution",
                description="Build automated workflows to generate and distribute financial reports on a scheduled basis to stakeholders.",
                category=FPACategory.AUTOMATION,
                subcategories=["scheduling", "distribution"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Consistent delivery",
                    "No manual distribution",
                    "Audit trail",
                    "Stakeholder self-service"
                ],
                example_prompts=[
                    "Create a Python script to generate the weekly sales report and email it to the leadership team",
                    "Build an automation to update the dashboard data and post to Slack every Monday morning",
                    "Set up scheduled generation of P&L reports for each department head"
                ],
                tools_used=["Python", "cron", "email APIs", "Slack API"],
                source="Claude Code Best Practices",
                source_url="https://www.anthropic.com/engineering/claude-code-best-practices",
                tags=["scheduling", "email", "distribution", "automation"]
            ),
            UseCase(
                id="automation-003",
                title="Data Validation and Quality Checks",
                description="Implement automated data validation rules to catch errors, inconsistencies, and anomalies in financial data before they impact reports.",
                category=FPACategory.AUTOMATION,
                subcategories=["data quality", "validation"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Early error detection",
                    "Improved data quality",
                    "Reduced rework",
                    "Audit confidence"
                ],
                example_prompts=[
                    "Create validation rules to check that debits equal credits for all journal entries",
                    "Build a data quality dashboard that flags anomalies in daily transaction data",
                    "Implement checks to ensure all required fields are populated before close"
                ],
                tools_used=["Python", "pandas", "Great Expectations"],
                source="Anthropic Financial Services",
                source_url="https://www.anthropic.com/news/advancing-claude-for-financial-services",
                tags=["validation", "data-quality", "errors", "checks"]
            ),

            # ============================================
            # EXCEL INTEGRATION USE CASES
            # ============================================
            UseCase(
                id="excel-001",
                title="Excel Template Standardization",
                description="Create and maintain standardized Excel templates for budgets, forecasts, and reports with consistent formatting and structure.",
                category=FPACategory.EXCEL_INTEGRATION,
                subcategories=["templates", "standardization"],
                complexity=ComplexityLevel.BEGINNER,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Consistent look and feel",
                    "Reduced formatting time",
                    "Easier consolidation",
                    "Better version control"
                ],
                example_prompts=[
                    "Create a standardized P&L template with proper formatting and conditional highlighting",
                    "Build a budget input template with data validation and protected formulas",
                    "Design a financial model template with consistent color coding and navigation"
                ],
                tools_used=["Excel", "VBA"],
                source="Claude in Excel",
                source_url="https://claude.com/claude-in-excel",
                tags=["templates", "Excel", "formatting", "standardization"]
            ),
            UseCase(
                id="excel-002",
                title="VBA Macro Development",
                description="Develop VBA macros to automate repetitive Excel tasks, create custom functions, and build interactive tools.",
                category=FPACategory.EXCEL_INTEGRATION,
                subcategories=["VBA", "macros"],
                complexity=ComplexityLevel.INTERMEDIATE,
                implementation_time=ImplementationTime.HOURS,
                benefits=[
                    "Task automation",
                    "Custom functionality",
                    "Time savings",
                    "Reduced errors"
                ],
                example_prompts=[
                    "Write a VBA macro to format all worksheets in the workbook consistently",
                    "Create a custom function to calculate weighted average cost of capital",
                    "Build a macro to export each worksheet as a separate PDF file"
                ],
                tools_used=["Excel", "VBA"],
                source="Claude in Excel",
                source_url="https://claude.com/claude-in-excel",
                tags=["VBA", "macros", "automation", "custom-functions"]
            ),
            UseCase(
                id="excel-003",
                title="Excel-Python Integration",
                description="Bridge Excel and Python to leverage advanced analytics while maintaining familiar Excel interface for end users.",
                category=FPACategory.EXCEL_INTEGRATION,
                subcategories=["Python", "xlwings"],
                complexity=ComplexityLevel.ADVANCED,
                implementation_time=ImplementationTime.DAYS,
                benefits=[
                    "Best of both worlds",
                    "Advanced analytics in Excel",
                    "Familiar user interface",
                    "Scalable processing"
                ],
                example_prompts=[
                    "Create a Python script that reads data from Excel, performs ML analysis, and writes results back",
                    "Build an xlwings integration to run Python forecasting models from Excel buttons",
                    "Set up a workflow where Excel triggers Python analysis and receives formatted results"
                ],
                tools_used=["Python", "xlwings", "openpyxl", "Excel"],
                source="Data Studios",
                source_url="https://www.datastudios.org/post/claude-and-spreadsheets-advanced-data-analysis-with-ai-in-2025",
                tags=["Python", "xlwings", "integration", "analytics"]
            ),
        ]

    def get_all_use_cases(self) -> List[UseCase]:
        """Get all use cases."""
        return self.use_cases

    def get_by_category(self, category: FPACategory) -> List[UseCase]:
        """Get use cases filtered by category."""
        return [uc for uc in self.use_cases if uc.category == category]

    def get_by_complexity(self, complexity: ComplexityLevel) -> List[UseCase]:
        """Get use cases filtered by complexity level."""
        return [uc for uc in self.use_cases if uc.complexity == complexity]

    def search(self, query: str) -> List[UseCase]:
        """Search use cases by keyword."""
        query_lower = query.lower()
        results = []

        for uc in self.use_cases:
            # Search in title, description, tags
            searchable = f"{uc.title} {uc.description} {' '.join(uc.tags)}".lower()
            if query_lower in searchable:
                results.append(uc)

        return results

    def get_by_id(self, use_case_id: str) -> Optional[UseCase]:
        """Get a specific use case by ID."""
        for uc in self.use_cases:
            if uc.id == use_case_id:
                return uc
        return None

    def get_statistics(self) -> Dict:
        """Get statistics about the use case database."""
        stats = {
            "total_use_cases": len(self.use_cases),
            "by_category": {},
            "by_complexity": {},
            "sources": set()
        }

        for uc in self.use_cases:
            # Count by category
            cat_name = uc.category.value
            stats["by_category"][cat_name] = stats["by_category"].get(cat_name, 0) + 1

            # Count by complexity
            comp_name = uc.complexity.value
            stats["by_complexity"][comp_name] = stats["by_complexity"].get(comp_name, 0) + 1

            # Collect sources
            stats["sources"].add(uc.source)

        stats["sources"] = list(stats["sources"])
        return stats
