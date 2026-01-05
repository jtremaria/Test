# FP&A Use Case Finder for Claude Code

A comprehensive tool to discover and explore Claude Code use cases specifically designed for Financial Planning & Analysis (FP&A) teams.

## Overview

This application aggregates the best use cases for leveraging Claude Code in FP&A workflows, sourced from:
- [Anthropic Financial Services](https://www.anthropic.com/news/advancing-claude-for-financial-services)
- [Claude in Excel](https://claude.com/claude-in-excel)
- [FP&A Trends Research](https://fpa-trends.com)
- Industry best practices and real-world implementations

## Features

- **30+ Curated Use Cases** across 10 FP&A categories
- **Smart Search** with relevance scoring and keyword matching
- **Personalized Recommendations** based on your role and tools
- **Ready-to-Use Prompts** for immediate implementation
- **Multiple Report Formats** including markdown export

## Installation

```bash
# Clone the repository
git clone https://github.com/Tristanmoreno/Test.git
cd Test

# Run directly (no dependencies required)
python -m fpa_use_case_finder

# Or install as a package
pip install -e .
fpa-finder
```

## Quick Start

### Interactive Mode
```bash
python -m fpa_use_case_finder
```

### Search for Use Cases
```bash
python -m fpa_use_case_finder search "budget consolidation"
python -m fpa_use_case_finder search "forecasting" --category forecasting
python -m fpa_use_case_finder search "excel" --complexity beginner
```

### List Use Cases
```bash
python -m fpa_use_case_finder list
python -m fpa_use_case_finder list --category budgeting
python -m fpa_use_case_finder list --complexity advanced
```

### View Use Case Details
```bash
python -m fpa_use_case_finder show budget-001
python -m fpa_use_case_finder show forecast-002 --similar
```

### Generate Reports
```bash
python -m fpa_use_case_finder report --type summary
python -m fpa_use_case_finder report --type cookbook
python -m fpa_use_case_finder report --type markdown --output use_cases.md
```

### Get Recommendations
```bash
python -m fpa_use_case_finder recommend --role "FP&A analyst" --tools excel python
python -m fpa_use_case_finder recommend --challenges "manual consolidation" "slow close"
```

## Categories

| Category | Description | Use Cases |
|----------|-------------|-----------|
| **Budgeting & Planning** | Annual budgets, rolling budgets, departmental consolidation | 3 |
| **Financial Forecasting** | Revenue forecasting, expense projections, cash flow predictions | 4 |
| **Variance Analysis** | Budget vs actuals, trend analysis, root cause identification | 3 |
| **Financial Modeling** | DCF models, three-statement models, LBO analysis | 4 |
| **Financial Reporting** | Management reports, KPI dashboards, board presentations | 3 |
| **Data Integration** | ERP integration, data warehouse queries, API connections | 3 |
| **Scenario Planning** | What-if analysis, Monte Carlo simulations, sensitivity analysis | 3 |
| **Compliance & Controls** | SOX documentation, audit support | 2 |
| **Process Automation** | Month-end close, scheduled reports, data validation | 3 |
| **Excel Integration** | Template standardization, VBA macros, Python-Excel bridge | 3 |

## Example Use Cases

### Budget Consolidation
```
Consolidate all budget files in the /budgets folder, identify any
departments with unrealistic assumptions, and create a summary report
```
**Productivity Gain:** 80% reduction in consolidation time

### Variance Commentary Generation
```
Analyze the budget vs actual report and generate executive-level
variance commentary for items over $50K
```
**Productivity Gain:** 90% reduction in commentary writing time

### Rolling Forecast Automation
```
Update the rolling forecast model with Q3 actuals and extend the
projection to Q4 next year
```
**Productivity Gain:** Quarterly prep time reduced to hours

### DCF Model Development
```
Build a DCF model for the acquisition target with a 5-year projection
period and terminal value
```
**Note:** Claude passed 5 of 7 Financial Modeling World Cup levels

## Real-World Results

- **NBIM (Norwegian Sovereign Wealth Fund):** 20% productivity gains, equivalent to 213,000 hours
- **Financial Modeling:** 83% accuracy on complex Excel tasks
- **Forecasting:** 65% of teams rate AI forecasts as "good/great" vs 42% without AI

## Project Structure

```
fpa_use_case_finder/
├── __init__.py          # Package initialization
├── __main__.py          # Module entry point
├── main.py              # CLI application
├── categories.py        # FP&A category definitions
├── use_cases.py         # Use case database (30+ cases)
├── searcher.py          # Search engine with scoring
└── reporter.py          # Report generation
```

## Python Usage

```python
from fpa_use_case_finder import UseCaseDatabase, UseCaseSearcher, ReportGenerator

# Initialize
db = UseCaseDatabase()
searcher = UseCaseSearcher(db)
reporter = ReportGenerator(db)

# Search for use cases
results = searcher.search("budget automation")
for result in results:
    print(f"{result.use_case.title} (score: {result.relevance_score})")

# Get recommendations
recommendations = searcher.get_recommended_use_cases({
    'role': 'FP&A Manager',
    'tools': ['Excel', 'Python'],
    'challenges': ['slow month-end close']
})

# Generate reports
print(reporter.generate_summary_report())
markdown = reporter.export_to_markdown()
```

## Sources

- [Anthropic Financial Services](https://www.anthropic.com/news/advancing-claude-for-financial-services)
- [Claude for Financial Services - Thoughtworks](https://www.thoughtworks.com/en-us/insights/blog/generative-ai/claude-financial-services-what-need-know)
- [Claude in Excel](https://claude.com/claude-in-excel)
- [FP&A Trends - Agentic AI](https://fpa-trends.com/article/how-agentic-ai-powering-next-generation-fpa)
- [Cube Software - AI for FP&A](https://www.cubesoftware.com/blog/ai-for-fpa-financial-planning-analysis)
- [F9 Finance - Claude for Finance](https://www.f9finance.com/claude-for-finance/)
- [KPMG - Future of FP&A with AI](https://kpmg.com/us/en/articles/2025/future-of-fpa-with-ai.html)
- [Data Studios - Claude and Spreadsheets](https://www.datastudios.org/post/claude-and-spreadsheets-advanced-data-analysis-with-ai-in-2025)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests with additional use cases or improvements.
