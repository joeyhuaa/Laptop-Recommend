# Laptop-Recommend

## Overview
This is a laptop recommendation system I built with two other teammates at HackDavis 2020. The program asks the user a series of
questions, and recommends up to 10 laptops that fit the user's answers. All of this happens via the Python console.

## Methodology
Because of the time constraints of a hackathon, we simplified this problem as much as possible.
We scraped data on roughly 1300 laptops from Newegg.com, split between gaming laptops (higher specs, pricier) and study laptops (lower specs, more affordable).
The recommendation algorithm subsets the complete dataset of laptops based on the user's budget, preferred use, storage
preferences, RAM preferences, and screen size preferences. 

## Conclusion
The program successfully accomplishes what it is supposed to accomplish: it recommends up to 10 laptops from our dataset, all of which
fit the user's responses to its questions.

The program is far from polished, as there is no front-end user interface, no links to the recommended laptops, and
the recommendation algorithm could be more precise. However, given our time and resource constraints, I am proud of this project.

Please give it a try by cloning the repository! Note that in the state the project is currently in, pandas must be installed
for it to run. Run the project from analysis.py.
