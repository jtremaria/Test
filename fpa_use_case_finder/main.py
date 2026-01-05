#!/usr/bin/env python3
"""
FP&A Use Case Finder - Main CLI Application
============================================
A comprehensive tool to discover Claude Code use cases for Financial Planning & Analysis.

Usage:
    python -m fpa_use_case_finder [command] [options]

Commands:
    search      Search for use cases by keyword
    list        List all use cases or filter by category
    show        Show details of a specific use case
    report      Generate various reports
    recommend   Get personalized recommendations
    stats       Show database statistics
"""

import argparse
import sys
from typing import Optional

from .use_cases import UseCaseDatabase
from .searcher import UseCaseSearcher
from .reporter import ReportGenerator
from .categories import FPACategory, ComplexityLevel, FPACategories


class FPAUseCaseFinderCLI:
    """Command-line interface for the FP&A Use Case Finder."""

    def __init__(self):
        self.database = UseCaseDatabase()
        self.searcher = UseCaseSearcher(self.database)
        self.reporter = ReportGenerator(self.database)

    def run(self, args: Optional[list] = None):
        """Run the CLI application."""
        parser = self._create_parser()
        parsed_args = parser.parse_args(args)

        if hasattr(parsed_args, 'func'):
            parsed_args.func(parsed_args)
        else:
            self._interactive_mode()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser."""
        parser = argparse.ArgumentParser(
            prog='fpa_use_case_finder',
            description='Find Claude Code use cases for FP&A',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  fpa_use_case_finder search "budget consolidation"
  fpa_use_case_finder list --category budgeting
  fpa_use_case_finder show budget-001
  fpa_use_case_finder report --type summary
  fpa_use_case_finder recommend --role analyst --tools excel python
            """
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # Search command
        search_parser = subparsers.add_parser('search', help='Search for use cases')
        search_parser.add_argument('query', type=str, help='Search query')
        search_parser.add_argument('--category', '-c', type=str, help='Filter by category')
        search_parser.add_argument('--complexity', '-x', type=str,
                                   choices=['beginner', 'intermediate', 'advanced', 'expert'],
                                   help='Filter by complexity')
        search_parser.add_argument('--limit', '-n', type=int, default=10, help='Max results')
        search_parser.set_defaults(func=self._cmd_search)

        # List command
        list_parser = subparsers.add_parser('list', help='List use cases')
        list_parser.add_argument('--category', '-c', type=str, help='Filter by category')
        list_parser.add_argument('--complexity', '-x', type=str,
                                 choices=['beginner', 'intermediate', 'advanced', 'expert'],
                                 help='Filter by complexity')
        list_parser.set_defaults(func=self._cmd_list)

        # Show command
        show_parser = subparsers.add_parser('show', help='Show use case details')
        show_parser.add_argument('use_case_id', type=str, help='Use case ID')
        show_parser.add_argument('--similar', '-s', action='store_true',
                                help='Show similar use cases')
        show_parser.set_defaults(func=self._cmd_show)

        # Report command
        report_parser = subparsers.add_parser('report', help='Generate reports')
        report_parser.add_argument('--type', '-t', type=str,
                                   choices=['summary', 'category', 'complexity',
                                           'reference', 'cookbook', 'markdown'],
                                   default='summary',
                                   help='Report type')
        report_parser.add_argument('--category', '-c', type=str,
                                   help='Category for category report')
        report_parser.add_argument('--output', '-o', type=str, help='Output file')
        report_parser.set_defaults(func=self._cmd_report)

        # Recommend command
        recommend_parser = subparsers.add_parser('recommend', help='Get recommendations')
        recommend_parser.add_argument('--role', '-r', type=str, help='Your role')
        recommend_parser.add_argument('--tools', '-t', nargs='+', help='Tools you use')
        recommend_parser.add_argument('--challenges', '-ch', nargs='+',
                                     help='Your challenges')
        recommend_parser.set_defaults(func=self._cmd_recommend)

        # Stats command
        stats_parser = subparsers.add_parser('stats', help='Show statistics')
        stats_parser.set_defaults(func=self._cmd_stats)

        # Categories command
        categories_parser = subparsers.add_parser('categories', help='List all categories')
        categories_parser.set_defaults(func=self._cmd_categories)

        return parser

    def _cmd_search(self, args):
        """Execute search command."""
        category = None
        if args.category:
            try:
                category = [FPACategory(args.category.lower())]
            except ValueError:
                print(f"Unknown category: {args.category}")
                print("Use 'categories' command to see available categories")
                return

        complexity = None
        if args.complexity:
            complexity = ComplexityLevel(args.complexity.lower())

        results = self.searcher.search(
            args.query,
            categories=category,
            complexity=complexity,
            limit=args.limit
        )

        if not results:
            print(f"No use cases found for: '{args.query}'")
            print("\nTry these search tips:")
            print("  - Use simpler keywords (e.g., 'budget' instead of 'budget consolidation')")
            print("  - Search by category: search --category forecasting")
            print("  - Search by tool: search 'excel' or search 'python'")
            return

        print(self.reporter.generate_search_results_report(results))

    def _cmd_list(self, args):
        """Execute list command."""
        use_cases = self.database.get_all_use_cases()

        if args.category:
            try:
                category = FPACategory(args.category.lower())
                use_cases = [uc for uc in use_cases if uc.category == category]
            except ValueError:
                print(f"Unknown category: {args.category}")
                return

        if args.complexity:
            complexity = ComplexityLevel(args.complexity.lower())
            use_cases = [uc for uc in use_cases if uc.complexity == complexity]

        if not use_cases:
            print("No use cases match the specified filters.")
            return

        print(f"\nFound {len(use_cases)} use cases:\n")
        print("-" * 60)

        for uc in use_cases:
            cat_name = FPACategories.get_category(uc.category).name
            print(f"[{uc.id}] {uc.title}")
            print(f"    Category: {cat_name} | Complexity: {uc.complexity.value}")
            print()

    def _cmd_show(self, args):
        """Execute show command."""
        use_case = self.database.get_by_id(args.use_case_id)

        if not use_case:
            print(f"Use case not found: {args.use_case_id}")
            print("\nAvailable IDs:")
            for uc in self.database.get_all_use_cases()[:10]:
                print(f"  - {uc.id}: {uc.title}")
            print("  ...")
            return

        print(self.reporter.generate_use_case_detail(use_case))

        if args.similar:
            similar = self.searcher.get_similar_use_cases(args.use_case_id)
            if similar:
                print("\nSIMILAR USE CASES:")
                print("-" * 40)
                for uc in similar:
                    print(f"  - [{uc.id}] {uc.title}")

    def _cmd_report(self, args):
        """Execute report command."""
        report_content = ""

        if args.type == 'summary':
            report_content = self.reporter.generate_summary_report()
        elif args.type == 'category':
            if not args.category:
                print("Category required for category report. Use --category")
                return
            try:
                category = FPACategory(args.category.lower())
                report_content = self.reporter.generate_category_report(category)
            except ValueError:
                print(f"Unknown category: {args.category}")
                return
        elif args.type == 'complexity':
            report_content = self.reporter.generate_complexity_guide()
        elif args.type == 'reference':
            report_content = self.reporter.generate_quick_reference_guide()
        elif args.type == 'cookbook':
            report_content = self.reporter.generate_prompt_cookbook()
        elif args.type == 'markdown':
            report_content = self.reporter.export_to_markdown()

        if args.output:
            with open(args.output, 'w') as f:
                f.write(report_content)
            print(f"Report saved to: {args.output}")
        else:
            print(report_content)

    def _cmd_recommend(self, args):
        """Execute recommend command."""
        context = {}

        if args.role:
            context['role'] = args.role
        if args.tools:
            context['tools'] = args.tools
        if args.challenges:
            context['challenges'] = args.challenges

        if not context:
            print("Please provide at least one of: --role, --tools, --challenges")
            print("\nExample:")
            print("  recommend --role 'FP&A analyst' --tools excel python")
            return

        recommendations = self.searcher.get_recommended_use_cases(context)

        if not recommendations:
            print("No recommendations found for your profile.")
            return

        print("\n" + "=" * 60)
        print("RECOMMENDED USE CASES FOR YOUR PROFILE")
        print("=" * 60 + "\n")

        for i, uc in enumerate(recommendations, 1):
            cat_name = FPACategories.get_category(uc.category).name
            print(f"{i}. {uc.title}")
            print(f"   Category: {cat_name}")
            print(f"   Complexity: {uc.complexity.value.capitalize()}")
            print(f"   {uc.description[:80]}...")
            print()

    def _cmd_stats(self, args):
        """Execute stats command."""
        print(self.reporter.generate_summary_report())

    def _cmd_categories(self, args):
        """List all available categories."""
        print("\nAVAILABLE CATEGORIES:")
        print("-" * 60 + "\n")

        for cat_info in FPACategories.get_all_categories():
            use_cases = self.database.get_by_category(cat_info.category)
            print(f"{cat_info.category.value}")
            print(f"  Name: {cat_info.name}")
            print(f"  Description: {cat_info.description}")
            print(f"  Use Cases: {len(use_cases)}")
            print(f"  Keywords: {', '.join(cat_info.keywords[:5])}")
            print()

    def _interactive_mode(self):
        """Run in interactive mode."""
        print("\n" + "=" * 60)
        print("FP&A USE CASE FINDER FOR CLAUDE CODE")
        print("=" * 60)
        print("\nWelcome! This tool helps you discover Claude Code use cases")
        print("specifically designed for Financial Planning & Analysis.")
        print()
        print("Quick Commands:")
        print("  search <query>     - Search for use cases")
        print("  list               - List all use cases")
        print("  categories         - Show all categories")
        print("  stats              - Show statistics")
        print("  help               - Show all commands")
        print("  quit               - Exit")
        print()

        while True:
            try:
                user_input = input("fpa> ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break

                if user_input.lower() == 'help':
                    self._show_interactive_help()
                    continue

                # Parse and execute command
                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()

                if command == 'search' and len(parts) > 1:
                    results = self.searcher.search(parts[1], limit=5)
                    print(self.reporter.generate_search_results_report(results))

                elif command == 'list':
                    use_cases = self.database.get_all_use_cases()[:10]
                    for uc in use_cases:
                        print(f"  [{uc.id}] {uc.title}")
                    print(f"\n  ... and {len(self.database.get_all_use_cases()) - 10} more")

                elif command == 'categories':
                    for cat in FPACategory:
                        info = FPACategories.get_category(cat)
                        count = len(self.database.get_by_category(cat))
                        print(f"  {cat.value}: {info.name} ({count})")

                elif command == 'stats':
                    print(self.reporter.generate_summary_report())

                elif command == 'show' and len(parts) > 1:
                    uc = self.database.get_by_id(parts[1])
                    if uc:
                        print(self.reporter.generate_use_case_detail(uc))
                    else:
                        print(f"Use case not found: {parts[1]}")

                else:
                    # Try as natural language search
                    results = self.searcher.search_by_prompt(user_input)
                    if results:
                        print(f"\nFound {len(results)} relevant use cases:\n")
                        for r in results[:5]:
                            print(f"  - {r.use_case.title}")
                    else:
                        print("No matches found. Try 'help' for commands.")

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    def _show_interactive_help(self):
        """Show help for interactive mode."""
        print("""
Available Commands:
  search <query>     Search for use cases by keyword
  list               List all use cases
  show <id>          Show details of a specific use case
  categories         Show all categories
  stats              Show database statistics
  help               Show this help
  quit               Exit the application

Natural Language:
  You can also type natural language queries like:
  - "how to automate budget consolidation"
  - "excel forecasting"
  - "variance analysis automation"
""")


def main():
    """Entry point for the CLI."""
    cli = FPAUseCaseFinderCLI()
    cli.run()


if __name__ == '__main__':
    main()
