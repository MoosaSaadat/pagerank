import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Total pages
    N = len(corpus)

    model = dict()
    for p in corpus:

        # Divide 1 - d among all pages
        pageRank = (1 - damping_factor) / N

        # If no connections, add eq probability
        if len(corpus[page]):
            if p in corpus[page]:
                pageRank += damping_factor / len(corpus[page])
        else:
            pageRank += damping_factor / len(corpus[page])
        model[p] = pageRank

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Total number of pages
    N = len(corpus)

    # Start with 1/N for all pages
    prevRanks = dict()
    for page in corpus:
        prevRanks[page] = 1 / N

    while True:
        currRanks = dict()

        # Calculate PageRank
        for currPage in corpus:
            currPageRank = (1 - damping_factor) / N
            for page, links in corpus.items():
                if page != currPage and currPage in links:
                    currPageRank += damping_factor * (
                        prevRanks[page] / len(corpus[page])
                    )
            currRanks[currPage] = currPageRank
            # print(f"currPage -> {currPage}, {currPageRank}")

        # Stop if Ranks converged
        if ranks_converged(currRanks, prevRanks):
            return currRanks

        prevRanks = currRanks.copy()


def ranks_converged(new_ranks, old_ranks):
    for page in new_ranks:

        # New probability not calculated
        if not new_ranks[page]:
            return False

        # Difference to the nearest 100th
        diff = new_ranks[page] - old_ranks[page]
        if round(diff, 3) > 0:
            # print("Not converged")
            return False
    return True


if __name__ == "__main__":
    main()
