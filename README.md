# **Simulated Annealing N-Queens Solver**

## **Introduction**

This Python script solves the N-Queens puzzle using the simulated annealing metaheuristic. Starting from a randomly generated board, the algorithm iteratively moves queens and “cools” the system until it finds a configuration with zero conflicts.

\!\[\](queens2.png)

## **Features**

* Cost Evaluation: Counts the number of conflicting queen pairs (each conflict adds \+2 to the cost).  
* Neighbor Generation: Selects one queen at random and moves it to a different row in its column.  
* Annealing Schedule: Configurable parameters including initial temperature, cooling rate (multiplicative decay), and stopping threshold.  
* Console Animation: Optional step-by-step board output to visualize convergence.  
* Unit Tests: Built-in pytest suite for validating `cost`, `moves`, `neighbor`, and `anneal` functions against main and held-out cases.

## **Installation**

Clone the repository  
git clone https://github.com/your-username/SimulatedAnnealingNQueens.git

1. cd SimulatedAnnealingNQueens  
2. Set up your environment  
   * Requires Python 3.6+ (no external dependencies).

(Optional) Create a virtual environment:  
python3 \-m venv venv

* source venv/bin/activate

## **Usage**

Run the solver with custom parameters:

python nqueens.py \--size N \--temp T \--decay D \--threshold X \[--verbose\]

* `--size N` : Board dimension (e.g. 8 for 8×8)  
* `--temp T` : Initial temperature (e.g. 100\)  
* `--decay D` : Decay rate per iteration (e.g. 0.99)  
* `--threshold X` : Temperature at which to stop (e.g. 0.01)  
* `--verbose` : Print board at each accepted move

### **Examples**

* Solve 8×8 with default settings:  
  python nqueens.py \--size 8 \--temp 100 \--decay 0.99 \--threshold 0.01  
* Visualize the process:  
  python nqueens.py \--size 10 \--temp 50 \--decay 0.95 \--threshold 0.001 \--verbose

## **Output**

Sample console output for an 8×8 board:

Initial cost: 16

Temperature: 100 \-\> 0.01 (decay=0.99)

Iteration 1: cost 14

...

Iteration 358: cost 0

Solved in 0.3 seconds

## **Testing**

Run all tests with pytest:

pytest

Tests cover:

* `test_nqueens.py`: core functionality  
* `test_nqueens_heldout.py`: additional scenarios

## **Project Structure**

SimulatedAnnealingNQueens/

├── nqueens.py                 \# Main implementation

├── test\_nqueens.py            \# Unit tests for core methods

├── test\_nqueens\_heldout.py    \# Held-out test cases

├── queens1.png                \# Example board snapshot

├── queens2.png                \# Additional visualization

└── README.md                  \# This document

## **Future Improvements**

* Experiment with alternative cooling schedules (e.g., exponential, logarithmic).  
* Add heuristic moves (e.g., swap two queens) to improve convergence speed.  
* Develop a GUI or web interface for real-time visualization.

