"""Unit tests for PromptRegressionMatrix."""
import unittest
from prompt_regression_matrix.matrix import PromptRegressionMatrix

class TestRegressionMatrix(unittest.TestCase):
    def test_evaluation_grading(self):
        m = PromptRegressionMatrix()
        m.add_case("t1", "hi", "hello")
        m.add_case("t2", "bye", "goodbye")

        res = m.run_suite(lambda inp: "hello" if inp == "hi" else "farewell")
        self.assertEqual(res["passed"], 1)
        self.assertEqual(res["failed"], 1)
        self.assertEqual(res["pass_rate"], 0.5)

if __name__ == "__main__":
    unittest.main()
