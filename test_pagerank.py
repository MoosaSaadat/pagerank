import unittest
import pagerank as pr


class TestPageRank(unittest.TestCase):
    def test_transition_model(self):
        corpus = {
            "1.html": {"2.html", "3.html"},
            "2.html": {"3.html"},
            "3.html": {"2.html"},
        }
        page = "1.html"
        damping_factor = 0.85

        result = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}
        for page, rank in pr.transition_model(corpus, page, damping_factor).items():
            self.assertAlmostEqual(result[page], rank)


if __name__ == "__main__":
    unittest.main()
