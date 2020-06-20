import unittest
import pagerank as pr


class TestPageRank(unittest.TestCase):
    def test_ranks_converged(self):
        old_rank = {"1.html": 0.501000, "2.html": 0.123470, "3.html": 0.354614}
        new_rank = {"1.html": 0.501352, "2.html": 0.123470, "3.html": 0.353614}
        self.assertTrue(pr.ranks_converged(new_rank, old_rank))

        old_rank = {"1.html": 0.501000, "2.html": 0.123470, "3.html": 0.354614}
        new_rank = {"1.html": 0.501552, "2.html": 0.123470, "3.html": 0.353614}
        self.assertFalse(pr.ranks_converged(new_rank, old_rank))

    def test_iterate_pagerank(self):

        # Test Corpus 0
        corpus = pr.crawl("corpus0")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)

        # Test Corpus 1
        corpus = pr.crawl("corpus1")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)

        # Test Corpus 2
        corpus = pr.crawl("corpus2")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)

    def test_transition_model(self):

        # Links exist
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

        # No links exist
        corpus = {
            "1.html": {},
            "2.html": {"3.html"},
            "3.html": {"2.html"},
        }
        page = "1.html"
        damping_factor = 0.85

        result = {"1.html": 0.333, "2.html": 0.333, "3.html": 0.333}
        for page, rank in pr.transition_model(corpus, page, damping_factor).items():
            self.assertAlmostEqual(result[page], rank, 3)

    def test_sample_pagerank(self):

        # Test Corpus 0
        corpus = pr.crawl("corpus0")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)

        # Test Corpus 1
        corpus = pr.crawl("corpus1")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)

        # Test Corpus 2
        corpus = pr.crawl("corpus2")
        ranks = pr.iterate_pagerank(corpus, pr.DAMPING)
        rankSum = 0
        for rank in ranks.values():
            rankSum += rank
        self.assertAlmostEqual(rankSum, 1, 1)


if __name__ == "__main__":
    unittest.main()
