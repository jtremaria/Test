"""
Use Case Searcher Module
========================
Advanced search functionality for finding relevant use cases.
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from .use_cases import UseCase, UseCaseDatabase
from .categories import FPACategory, ComplexityLevel, FPACategories


@dataclass
class SearchResult:
    """Represents a search result with relevance score."""
    use_case: UseCase
    relevance_score: float
    matched_fields: List[str]


class UseCaseSearcher:
    """Advanced search engine for FP&A use cases."""

    def __init__(self, database: Optional[UseCaseDatabase] = None):
        self.database = database or UseCaseDatabase()
        self._build_index()

    def _build_index(self):
        """Build search index for faster lookups."""
        self.keyword_index: Dict[str, List[str]] = {}
        self.category_index: Dict[FPACategory, List[str]] = {}

        for uc in self.database.get_all_use_cases():
            # Index by keywords
            keywords = self._extract_keywords(uc)
            for keyword in keywords:
                if keyword not in self.keyword_index:
                    self.keyword_index[keyword] = []
                self.keyword_index[keyword].append(uc.id)

            # Index by category
            if uc.category not in self.category_index:
                self.category_index[uc.category] = []
            self.category_index[uc.category].append(uc.id)

    def _extract_keywords(self, use_case: UseCase) -> List[str]:
        """Extract searchable keywords from a use case."""
        text = f"{use_case.title} {use_case.description} {' '.join(use_case.tags)}"
        text = text.lower()

        # Simple tokenization
        words = text.replace(',', ' ').replace('.', ' ').split()
        # Filter short words and common stopwords
        stopwords = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to',
                     'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are',
                     'were', 'been', 'be', 'have', 'has', 'had', 'do', 'does',
                     'did', 'will', 'would', 'could', 'should', 'may', 'might',
                     'can', 'that', 'this', 'these', 'those'}
        keywords = [w for w in words if len(w) > 2 and w not in stopwords]

        return list(set(keywords))

    def search(
        self,
        query: str,
        categories: Optional[List[FPACategory]] = None,
        complexity: Optional[ComplexityLevel] = None,
        limit: int = 10
    ) -> List[SearchResult]:
        """
        Search for use cases matching the query.

        Args:
            query: Search query string
            categories: Optional list of categories to filter by
            complexity: Optional complexity level to filter by
            limit: Maximum number of results to return

        Returns:
            List of SearchResult objects sorted by relevance
        """
        query_lower = query.lower()
        query_keywords = set(query_lower.replace(',', ' ').replace('.', ' ').split())

        results: List[SearchResult] = []

        for uc in self.database.get_all_use_cases():
            # Apply filters
            if categories and uc.category not in categories:
                continue
            if complexity and uc.complexity != complexity:
                continue

            # Calculate relevance score
            score, matched = self._calculate_relevance(uc, query_lower, query_keywords)

            if score > 0:
                results.append(SearchResult(
                    use_case=uc,
                    relevance_score=score,
                    matched_fields=matched
                ))

        # Sort by relevance score descending
        results.sort(key=lambda x: x.relevance_score, reverse=True)

        return results[:limit]

    def _calculate_relevance(
        self,
        use_case: UseCase,
        query: str,
        query_keywords: set
    ) -> Tuple[float, List[str]]:
        """Calculate relevance score for a use case."""
        score = 0.0
        matched_fields = []

        # Title match (highest weight)
        if query in use_case.title.lower():
            score += 10.0
            matched_fields.append("title")
        else:
            title_keywords = set(use_case.title.lower().split())
            title_overlap = len(query_keywords & title_keywords)
            if title_overlap > 0:
                score += title_overlap * 3.0
                matched_fields.append("title")

        # Description match
        if query in use_case.description.lower():
            score += 5.0
            matched_fields.append("description")
        else:
            desc_keywords = set(use_case.description.lower().split())
            desc_overlap = len(query_keywords & desc_keywords)
            if desc_overlap > 0:
                score += desc_overlap * 1.5
                if "description" not in matched_fields:
                    matched_fields.append("description")

        # Tags match
        for tag in use_case.tags:
            if tag.lower() in query or query in tag.lower():
                score += 4.0
                if "tags" not in matched_fields:
                    matched_fields.append("tags")

        # Example prompts match
        for prompt in use_case.example_prompts:
            if query in prompt.lower():
                score += 3.0
                if "prompts" not in matched_fields:
                    matched_fields.append("prompts")
                break

        # Tools match
        for tool in use_case.tools_used:
            if tool.lower() in query or query in tool.lower():
                score += 2.0
                if "tools" not in matched_fields:
                    matched_fields.append("tools")

        # Benefits match
        for benefit in use_case.benefits:
            if query in benefit.lower():
                score += 1.5
                if "benefits" not in matched_fields:
                    matched_fields.append("benefits")
                break

        return score, matched_fields

    def get_similar_use_cases(self, use_case_id: str, limit: int = 5) -> List[UseCase]:
        """Find similar use cases based on category and tags."""
        source_uc = self.database.get_by_id(use_case_id)
        if not source_uc:
            return []

        scores: List[Tuple[UseCase, float]] = []

        for uc in self.database.get_all_use_cases():
            if uc.id == use_case_id:
                continue

            score = 0.0

            # Same category
            if uc.category == source_uc.category:
                score += 5.0

            # Overlapping tags
            tag_overlap = len(set(uc.tags) & set(source_uc.tags))
            score += tag_overlap * 2.0

            # Same complexity
            if uc.complexity == source_uc.complexity:
                score += 1.0

            # Same tools
            tool_overlap = len(set(uc.tools_used) & set(source_uc.tools_used))
            score += tool_overlap * 1.5

            if score > 0:
                scores.append((uc, score))

        # Sort by score
        scores.sort(key=lambda x: x[1], reverse=True)

        return [uc for uc, _ in scores[:limit]]

    def get_recommended_use_cases(
        self,
        user_context: Dict
    ) -> List[UseCase]:
        """
        Get recommended use cases based on user context.

        Args:
            user_context: Dictionary with keys like 'role', 'tools', 'challenges'

        Returns:
            List of recommended use cases
        """
        all_use_cases = self.database.get_all_use_cases()
        scores: List[Tuple[UseCase, float]] = []

        for uc in all_use_cases:
            score = 0.0

            # Match tools
            if 'tools' in user_context:
                for tool in user_context['tools']:
                    if any(tool.lower() in t.lower() for t in uc.tools_used):
                        score += 3.0

            # Match challenges to descriptions/benefits
            if 'challenges' in user_context:
                for challenge in user_context['challenges']:
                    challenge_lower = challenge.lower()
                    if challenge_lower in uc.description.lower():
                        score += 4.0
                    for benefit in uc.benefits:
                        if challenge_lower in benefit.lower():
                            score += 2.0

            # Match role to categories
            if 'role' in user_context:
                role_lower = user_context['role'].lower()
                role_category_map = {
                    'budget': [FPACategory.BUDGETING],
                    'forecast': [FPACategory.FORECASTING],
                    'analyst': [FPACategory.VARIANCE_ANALYSIS, FPACategory.FINANCIAL_MODELING],
                    'manager': [FPACategory.REPORTING, FPACategory.SCENARIO_PLANNING],
                    'controller': [FPACategory.COMPLIANCE, FPACategory.AUTOMATION],
                }
                for keyword, categories in role_category_map.items():
                    if keyword in role_lower and uc.category in categories:
                        score += 5.0

            # Prefer beginner/intermediate for new users
            if user_context.get('experience', 'intermediate') == 'beginner':
                if uc.complexity in [ComplexityLevel.BEGINNER, ComplexityLevel.INTERMEDIATE]:
                    score += 2.0

            if score > 0:
                scores.append((uc, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return [uc for uc, _ in scores[:10]]

    def search_by_prompt(self, task_description: str) -> List[SearchResult]:
        """
        Find use cases that match a natural language task description.

        Args:
            task_description: Natural language description of the task

        Returns:
            List of matching SearchResult objects
        """
        # Extract key phrases
        key_phrases = [
            'budget', 'forecast', 'variance', 'model', 'report', 'dashboard',
            'automate', 'excel', 'dcf', 'lbo', 'consolidate', 'scenario',
            'sensitivity', 'monte carlo', 'cash flow', 'revenue', 'expense',
            'audit', 'compliance', 'sox', 'erp', 'integration', 'api',
            'kpi', 'close', 'month-end', 'vba', 'python', 'sql'
        ]

        task_lower = task_description.lower()
        found_phrases = [p for p in key_phrases if p in task_lower]

        if not found_phrases:
            # Fall back to basic search
            return self.search(task_description)

        # Search with combined phrases
        combined_results: Dict[str, SearchResult] = {}

        for phrase in found_phrases:
            results = self.search(phrase, limit=5)
            for result in results:
                if result.use_case.id not in combined_results:
                    combined_results[result.use_case.id] = result
                else:
                    # Boost score for multiple matches
                    combined_results[result.use_case.id].relevance_score += result.relevance_score

        final_results = list(combined_results.values())
        final_results.sort(key=lambda x: x.relevance_score, reverse=True)

        return final_results[:10]
