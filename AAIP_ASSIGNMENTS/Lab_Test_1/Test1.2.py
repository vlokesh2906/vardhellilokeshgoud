from typing import Iterable, List, Dict, Sequence
import math
import statistics
import unittest


def _compute_stats_impl(data: Sequence[float]) -> Dict[str, float]:
    """Core implementation used by all public wrappers."""
    nums = list(data)
    if not nums:
        raise ValueError("data must be non-empty")
    count = len(nums)
    mean = statistics.mean(nums)
    median = statistics.median(nums)
    minimum = min(nums)
    maximum = max(nums)
    # population std dev to keep deterministic for small samples
    variance = sum((x - mean) ** 2 for x in nums) / count
    std = math.sqrt(variance)
    return {
        "count": float(count),
        "mean": float(mean),
        "median": float(median),
        "min": float(minimum),
        "max": float(maximum),
        "std": float(std),
    }


# Poorly commented / original form (no docstring)
def poorly_commented_compute(data):
    # expects an iterable of numbers, returns some stats in a dict
    nums = list(data)
    if not nums:
        raise ValueError("data must be non-empty")
    return _compute_stats_impl(nums)


# Manual comments: inline explanation but no structured docstring
def manual_commented_compute(data):
    # Convert input to list to allow multiple passes.
    # Check for empty input and raise a ValueError.
    # Use statistics.mean/median and simple min/max calculations.
    nums = list(data)
    if not nums:
        raise ValueError("data must be non-empty")
    return _compute_stats_impl(nums)


# AI-generated refactor: type hints, one-line summary, parameter/return sections, raises and example
def ai_documented_compute(data: Sequence[float]) -> Dict[str, float]:
    """Compute basic descriptive statistics for a non-empty numeric sequence.

    Args:
        data: A non-empty sequence of numeric values (ints or floats).

    Returns:
        A dict with keys:
            - 'count': number of items (as float for uniformity)
            - 'mean': arithmetic mean
            - 'median': median value
            - 'min': smallest value
            - 'max': largest value
            - 'std': population standard deviation

    Raises:
        ValueError: if `data` is empty.

    Example:
        >>> ai_documented_compute([1, 2, 3])
        {'count': 3.0, 'mean': 2.0, 'median': 2.0, 'min': 1.0, 'max': 3.0, 'std': 0.816496580927726}
    """
    return _compute_stats_impl(data)


# Small evaluator that compares explicitness of AI docstring vs manual comments
def evaluate_documentation(ai_doc: str, manual_text: str) -> dict:
    """Return simple clarity/completeness signals for two documentation texts."""
    def signals(text: str) -> dict:
        lower = (text or "").lower()
        return {
            "has_summary": bool(lower.strip().splitlines()[0]) if text else False,
            "mentions_args": "args" in lower or "parameters" in lower or "param" in lower,
            "mentions_returns": "return" in lower,
            "mentions_raises": "raise" in lower,
            "mentions_example": "example" in lower or ">>>" in lower,
            "length": len(text or ""),
        }
    return {"ai": signals(ai_doc), "manual": signals(manual_text)}


# Unit tests to verify refactor preserved behavior and to exercise evaluator
class TestComputeStats(unittest.TestCase):
    def setUp(self):
        self.sample = [1.0, 2.0, 3.0, 4.0, 5.0]

    def test_behavior_equivalence(self):
        expected = _compute_stats_impl(self.sample)
        self.assertEqual(poorly_commented_compute(self.sample), expected)
        self.assertEqual(manual_commented_compute(self.sample), expected)
        self.assertEqual(ai_documented_compute(self.sample), expected)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            ai_documented_compute([])

    def test_evaluator_flags(self):
        ai_doc = ai_documented_compute.__doc__
        manual_doc = (
            "# Convert input to list to allow multiple passes.\n"
            "# Check for empty input and raise a ValueError.\n"
            "# Use statistics.mean/median and simple min/max calculations."
        )
        eval_result = evaluate_documentation(ai_doc, manual_doc)
        # AI docstring should mention Args/Returns/Raises/Example
        self.assertTrue(eval_result["ai"]["mentions_args"])
        self.assertTrue(eval_result["ai"]["mentions_returns"])
        self.assertTrue(eval_result["ai"]["mentions_raises"])
        self.assertTrue(eval_result["ai"]["mentions_example"])
        # Manual comments typically shorter and may lack structured sections
        self.assertFalse(eval_result["manual"]["mentions_args"])
        self.assertFalse(eval_result["manual"]["mentions_example"])


if __name__ == "__main__":
    # Run tests on Windows:
    # python "c:\Users\vardh\OneDrive\Documents\AIPP LAB TEST\Lab_Test_1\Test1.2.py"
    import unittest
    unittest.main(verbosity=2)
