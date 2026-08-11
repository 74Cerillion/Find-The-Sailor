# Find-The-Sailor
Employ Baye's rule for statistical likelihood analysis to find a missing sailor lost at sea in 'Cape Python'

Bayesian Search and Rescue Simulator

Results of Monte Carlo Simulation:
Sample Size: 10,000 simulations
Concentrated-Search-Only: 2.758avg searches to find the sailor
Split-Search Only: 2.291avg searches to find the sailor

A Python search-and-rescue simulation that uses Bayes' theorem, probability of detection, stochastic search effectiveness, and Monte Carlo simulation to model the search for a missing sailor.
Overview
The program divides a geographic search region into three search areas and assigns an initial probability that the missing sailor is located in each area.
After each unsuccessful search, Bayesian probability updates are used to revise the probability that the sailor is located in each region.
Search effectiveness is modeled using planned and actual Search Effectiveness Probabilities (SEP), with actual conditions generated stochastically around forecast conditions.
Features
    • Bayesian probability updates after unsuccessful searches
    • Three geographic search regions
    • Tracking of previously searched coordinates
    • Planned vs. actual Search Effectiveness Probability (SEP)
    • Probability of Detection (PoD)
    • Triangular probability distributions for modeled search conditions
    • Multiple search strategies
    • Monte Carlo comparison across 10,000 simulated rescue operations
    • Handling of exhausted search regions and rare simulation edge cases
Monte Carlo Experiment
Two search strategies were compared across 10,000 simulated rescue operations:
    1. Concentrated Search — search the area with the highest Bayesian target probability twice.
    2. Split Search — search the pair of areas with the highest combined target probability.
Results with the Concentrated Search yielded an average rescue effort of 2.758 searches while the Split Search came in 16.9% faster on average at 2.291 searches.
The simulation also tracks failed trials where the split-search strategy exhausts enough search regions that no valid two-area combination remains.
Technologies
    • Python
    • NumPy
    • OpenCV
    • Bayesian probability
    • Monte Carlo simulation
    • Stochastic modeling
Background
This project began as the Bayesian Search and Rescue project from Real-World Python and was extended through the chapter's challenge projects.
Additional implementations include coordinate-search memory, Monte Carlo strategy testing, planned versus actual search effectiveness, Probability of Detection calculations, and additional edge-case handling.
