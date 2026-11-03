"""Command-line interface for Prompt Regression Matrix."""
import argparse
from .matrix import PromptRegressionMatrix

def main():
    parser = argparse.ArgumentParser(description="Prompt Regression Matrix CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate prompt evaluation matrix")
    args = parser.parse_args()

    matrix = PromptRegressionMatrix()
    matrix.add_case("c1", "format as json", "```json")
    matrix.add_case("c2", "calculate 2+2", "4")

    # Mock runner
    runner = lambda inp: "Result: 4 with ```json code```"
    results = matrix.run_suite(runner)
    print("Matrix Evaluation Results:")
    print(f"Pass Rate: {results['pass_rate'] * 100}% ({results['passed']}/{results['total_cases']})")

if __name__ == "__main__":
    main()
