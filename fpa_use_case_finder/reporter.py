"""
Report Generator Module
=======================
Generates formatted reports of use cases in various formats.
"""

from typing import List, Optional, Dict
from datetime import datetime
from .use_cases import UseCase, UseCaseDatabase
from .categories import FPACategory, FPACategories, ComplexityLevel
from .searcher import SearchResult


class ReportGenerator:
    """Generates formatted reports of FP&A use cases."""

    def __init__(self, database: Optional[UseCaseDatabase] = None):
        self.database = database or UseCaseDatabase()

    def generate_summary_report(self) -> str:
        """Generate a summary report of all use cases."""
        stats = self.database.get_statistics()
        category_names = FPACategories.get_category_names()

        lines = [
            "=" * 70,
            "CLAUDE CODE USE CASES FOR FP&A - SUMMARY REPORT",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "=" * 70,
            "",
            f"Total Use Cases: {stats['total_use_cases']}",
            "",
            "BY CATEGORY:",
            "-" * 40,
        ]

        for cat_value, count in sorted(stats['by_category'].items()):
            cat_name = category_names.get(cat_value, cat_value)
            lines.append(f"  {cat_name}: {count}")

        lines.extend([
            "",
            "BY COMPLEXITY:",
            "-" * 40,
        ])

        complexity_order = ['beginner', 'intermediate', 'advanced', 'expert']
        for comp in complexity_order:
            if comp in stats['by_complexity']:
                lines.append(f"  {comp.capitalize()}: {stats['by_complexity'][comp]}")

        lines.extend([
            "",
            "SOURCES:",
            "-" * 40,
        ])

        for source in sorted(stats['sources']):
            lines.append(f"  - {source}")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    def generate_category_report(self, category: FPACategory) -> str:
        """Generate a detailed report for a specific category."""
        use_cases = self.database.get_by_category(category)
        cat_info = FPACategories.get_category(category)

        lines = [
            "=" * 70,
            f"CATEGORY: {cat_info.name.upper()}",
            "=" * 70,
            "",
            f"Description: {cat_info.description}",
            f"Typical Tools: {', '.join(cat_info.typical_tools)}",
            f"Use Cases: {len(use_cases)}",
            "",
        ]

        for i, uc in enumerate(use_cases, 1):
            lines.extend(self._format_use_case_brief(uc, i))
            lines.append("")

        return "\n".join(lines)

    def generate_use_case_detail(self, use_case: UseCase) -> str:
        """Generate a detailed view of a single use case."""
        lines = [
            "=" * 70,
            f"USE CASE: {use_case.title}",
            "=" * 70,
            "",
            f"ID: {use_case.id}",
            f"Category: {FPACategories.get_category(use_case.category).name}",
            f"Complexity: {use_case.complexity.value.capitalize()}",
            f"Implementation Time: {use_case.implementation_time.value.capitalize()}",
            "",
            "DESCRIPTION:",
            "-" * 40,
            use_case.description,
            "",
            "BENEFITS:",
            "-" * 40,
        ]

        for benefit in use_case.benefits:
            lines.append(f"  * {benefit}")

        lines.extend([
            "",
            "EXAMPLE PROMPTS:",
            "-" * 40,
        ])

        for i, prompt in enumerate(use_case.example_prompts, 1):
            lines.append(f"  {i}. \"{prompt}\"")

        lines.extend([
            "",
            "TOOLS USED:",
            "-" * 40,
            f"  {', '.join(use_case.tools_used)}",
            "",
        ])

        if use_case.productivity_gain:
            lines.extend([
                "PRODUCTIVITY GAIN:",
                "-" * 40,
                f"  {use_case.productivity_gain}",
                "",
            ])

        lines.extend([
            "SOURCE:",
            "-" * 40,
            f"  {use_case.source}",
        ])

        if use_case.source_url:
            lines.append(f"  {use_case.source_url}")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)

    def generate_search_results_report(self, results: List[SearchResult]) -> str:
        """Generate a formatted report of search results."""
        if not results:
            return "No matching use cases found."

        lines = [
            "=" * 70,
            f"SEARCH RESULTS ({len(results)} matches)",
            "=" * 70,
            "",
        ]

        for i, result in enumerate(results, 1):
            uc = result.use_case
            lines.extend([
                f"{i}. {uc.title}",
                f"   Category: {FPACategories.get_category(uc.category).name}",
                f"   Complexity: {uc.complexity.value.capitalize()}",
                f"   Relevance: {result.relevance_score:.1f}",
                f"   Matched: {', '.join(result.matched_fields)}",
                "",
            ])

        return "\n".join(lines)

    def generate_quick_reference_guide(self) -> str:
        """Generate a quick reference guide organized by category."""
        lines = [
            "=" * 70,
            "CLAUDE CODE FOR FP&A - QUICK REFERENCE GUIDE",
            "=" * 70,
            "",
        ]

        for category in FPACategory:
            cat_info = FPACategories.get_category(category)
            use_cases = self.database.get_by_category(category)

            if not use_cases:
                continue

            lines.extend([
                f"## {cat_info.name.upper()}",
                f"   {cat_info.description}",
                "",
            ])

            for uc in use_cases:
                lines.append(f"   * {uc.title}")
                if uc.example_prompts:
                    lines.append(f"     Example: \"{uc.example_prompts[0][:60]}...\"")

            lines.append("")

        return "\n".join(lines)

    def generate_complexity_guide(self) -> str:
        """Generate a guide organized by complexity level."""
        lines = [
            "=" * 70,
            "USE CASES BY COMPLEXITY LEVEL",
            "=" * 70,
            "",
        ]

        complexity_descriptions = {
            ComplexityLevel.BEGINNER: "Simple tasks, minimal technical setup required",
            ComplexityLevel.INTERMEDIATE: "Moderate complexity, some technical knowledge helpful",
            ComplexityLevel.ADVANCED: "Complex implementations, requires programming skills",
            ComplexityLevel.EXPERT: "Sophisticated projects, deep technical expertise needed"
        }

        for complexity in ComplexityLevel:
            use_cases = self.database.get_by_complexity(complexity)

            if not use_cases:
                continue

            lines.extend([
                f"### {complexity.value.upper()}",
                f"    {complexity_descriptions[complexity]}",
                f"    ({len(use_cases)} use cases)",
                "",
            ])

            for uc in use_cases:
                cat_name = FPACategories.get_category(uc.category).name
                lines.append(f"    * [{cat_name}] {uc.title}")

            lines.append("")

        return "\n".join(lines)

    def generate_prompt_cookbook(self) -> str:
        """Generate a cookbook of example prompts organized by task type."""
        lines = [
            "=" * 70,
            "CLAUDE CODE PROMPT COOKBOOK FOR FP&A",
            "=" * 70,
            "",
            "Ready-to-use prompts for common FP&A tasks",
            "",
        ]

        for category in FPACategory:
            cat_info = FPACategories.get_category(category)
            use_cases = self.database.get_by_category(category)

            if not use_cases:
                continue

            lines.extend([
                f"### {cat_info.name.upper()}",
                "",
            ])

            for uc in use_cases:
                lines.append(f"**{uc.title}**")
                for prompt in uc.example_prompts:
                    lines.append(f"  > {prompt}")
                lines.append("")

        return "\n".join(lines)

    def _format_use_case_brief(self, uc: UseCase, number: int) -> List[str]:
        """Format a brief view of a use case."""
        return [
            f"{number}. {uc.title}",
            f"   Complexity: {uc.complexity.value.capitalize()} | "
            f"Time: {uc.implementation_time.value.capitalize()}",
            f"   {uc.description[:100]}...",
            f"   Tools: {', '.join(uc.tools_used)}",
        ]

    def export_to_markdown(self) -> str:
        """Export all use cases to a markdown document."""
        lines = [
            "# Claude Code Use Cases for FP&A",
            "",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*",
            "",
            "## Table of Contents",
            "",
        ]

        # TOC
        for category in FPACategory:
            cat_info = FPACategories.get_category(category)
            use_cases = self.database.get_by_category(category)
            if use_cases:
                anchor = cat_info.name.lower().replace(' ', '-').replace('&', 'and')
                lines.append(f"- [{cat_info.name}](#{anchor}) ({len(use_cases)} use cases)")

        lines.extend(["", "---", ""])

        # Content
        for category in FPACategory:
            cat_info = FPACategories.get_category(category)
            use_cases = self.database.get_by_category(category)

            if not use_cases:
                continue

            lines.extend([
                f"## {cat_info.name}",
                "",
                f"*{cat_info.description}*",
                "",
                f"**Typical Tools:** {', '.join(cat_info.typical_tools)}",
                "",
            ])

            for uc in use_cases:
                lines.extend([
                    f"### {uc.title}",
                    "",
                    f"**Complexity:** {uc.complexity.value.capitalize()} | "
                    f"**Time:** {uc.implementation_time.value.capitalize()}",
                    "",
                    uc.description,
                    "",
                    "**Benefits:**",
                ])

                for benefit in uc.benefits:
                    lines.append(f"- {benefit}")

                lines.extend([
                    "",
                    "**Example Prompts:**",
                ])

                for prompt in uc.example_prompts:
                    lines.append(f"- `{prompt}`")

                if uc.productivity_gain:
                    lines.extend([
                        "",
                        f"**Productivity Gain:** {uc.productivity_gain}",
                    ])

                lines.extend([
                    "",
                    f"*Source: [{uc.source}]({uc.source_url})*" if uc.source_url else f"*Source: {uc.source}*",
                    "",
                    "---",
                    "",
                ])

        return "\n".join(lines)
