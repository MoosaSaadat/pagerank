# PageRank
### Harvard CS50's Introduction to Artificial Intelligence with Python (Project 2)

Rank web pages by importance using PageRank algorithm

## Description
In **PageRank’s** algorithm, a website is more important if it is linked to by other important websites. The importance of a link is determined by assigning it a **weight**. Links from more important websites have their links weighted more and links from less important websites have their links weighted less. This definition seems a bit circular, but there are multiple strategies for calculating these rankings. In this project, two different models are used to rank pages:
1. **Markov Chain:** Each page represents a *state*, and each page has a *transition model* that chooses among its *links* at random. At each time step, the state switches to one of the pages linked to by the current state. By *sampling* states randomly from the Markov Chain, we can get an estimate for each page’s PageRank. We can start by choosing a page at random, then keep following links at random, keeping track of how many times we’ve visited each page. After we’ve gathered all of our samples (based on a number we choose in advance), the proportion of the time we were on each page might be an estimate for that page’s rank.
2. **Iterative Algorithm:** We can also define a page’s PageRank using a recursive mathematical expression. A page's rank *PR* can be calculated using the following formula:
![Formula](assets/formula.png)
In this formula, *d* is the damping factor, *N* is the total number of pages in the corpus, *i* ranges over all pages that link to page *p*, and *NumLinks(i)* is the number of links present on page *i*.

## Example
Pass a directory containing webpages and this program will calculate page's rank using both models. Both of these models produce very similar results.
```
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```