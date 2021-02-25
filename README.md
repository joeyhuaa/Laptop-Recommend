# Laptop-Recommend

## Overview
This is a laptop recommendation system I built with two other teammates at HackDavis 2020. The program asks the user a series of
questions, and recommends up to 10 laptops that fit the user's answers. All of this happens via the Python console.

## Methodology
Because of the time constraints of a hackathon, we simplified this problem as much as possible.
We scraped data on roughly 1300 laptops from Newegg.com, split between gaming laptops (higher specs, pricier) and study laptops (lower specs, more affordable).
The recommendation algorithm subsets the complete dataset of laptops based on the user's budget, preferred use, storage
preferences, RAM preferences, and screen size preferences. 
