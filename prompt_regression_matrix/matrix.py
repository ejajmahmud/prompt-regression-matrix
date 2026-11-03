"""Regression test matrix for evaluating and grading prompt iterations."""
from typing import List, Dict, Any, Callable


class PromptRegressionMatrix:
    def __init__(self):
        self._test_cases: List[Dict[str, Any]] = []

    def add_case(self, case_id: str, input_text: str, expected_substring: str) -> None:
        self._test_cases.append({
            "id": case_id,
            "input": input_text,
            "expected": expected_substring
        })

    def run_suite(self, prompt_runner: Callable[[str], str]) -> Dict[str, Any]:
        passed = 0
        failed = 0
        details = []

        for case in self._test_cases:
            output = prompt_runner(case["input"])
            ok = case["expected"] in output
            if ok:
                passed += 1
            else:
                failed += 1
            details.append({
                "id": case["id"],
                "passed": ok,
                "expected": case["expected"],
                "output_snippet": output[:40]
            })

        total = len(self._test_cases)
        return {
            "total_cases": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": round(passed / total, 4) if total > 0 else 1.0,
            "details": details
        }
