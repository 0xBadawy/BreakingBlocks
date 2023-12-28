### AI Puzzle Solver

This GitHub repository contains Python implementations of various puzzle-solving algorithms for a 10x10 grid puzzle. The puzzle involves filling a grid with colored blocks and finding the optimal sequence of moves to clear the last row. The implemented algorithms include
## Introduction

The AI Puzzle Solver is a Python application that uses Pygame for graphical representation and implements various search algorithms to solve puzzles. The main focus is on artificial intelligence algorithms such as Depth-First Search, Breadth-First Search, A*, Uniform Cost Search, and others.

## Algorithms

The following search algorithms are implemented:

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Depth-Limited Search (DLS)**
- **Uniform Cost Search (UCS)**
- **Greedy Best-First Search**
- ***A* Search**
  
## Algorithm analysis and comparison
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/2121745e78d4a0974f6b221df179458fdfd0afbe/Image/repo/Picture7.png)]()

## Algorithm analysis and comparison
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/9e84c77e837cda3b7a935978626602ce2e8ff738/Image/repo/Picture3.png)]()



## Algorithm analysis and comparison
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/9e84c77e837cda3b7a935978626602ce2e8ff738/Image/repo/Picture4.png)]()


## Algorithm analysis and comparison
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/9e84c77e837cda3b7a935978626602ce2e8ff738/Image/repo/Picture5.png)]()


## Algorithm analysis and comparison
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/2121745e78d4a0974f6b221df179458fdfd0afbe/Image/repo/Picture8.png)]()



## 

| Name       | Greedy | A*    | BFS    | DFS    | DLS    | IDLS   | UCS    |
|------------|--------|-------|--------|--------|--------|--------|-------|
| Total State| 51     | 18635 | 136975 | 217    | 648443 | 501328 | 107538|
| Path       | 5      | 5     | 5      | 17     | 6      | 5      | 5     |
| Space (KB) | 19     | 7279  | 53498  | 84     | 253298 | 195831 | 42030 |
| Time (ms)  | 2      | 1943  | 15604  | 12     | 25444  | 19817  | 12855 |
| Complete   | YES    | YES   | YES    | YES    | NO     | YES    | YES   |
| Optimal    | YES    | YES   | YES    | NO     | NO     | YES    | YES   |


This GitHub repository contains Python implementations of various puzzle-solving algorithms for a 10x10 grid puzzle. The puzzle involves filling a grid with colored blocks and finding the optimal sequence of moves to clear the last row. The implemented algorithms include

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the main Python script (`PyGameWind.py`).

## Agent Specification ( PEAS )

Certainly! Let's convert the provided information into a table format:

| Aspect              | Description                                                                               |
|---------------------|-------------------------------------------------------------------------------------------|
| **Performance Measure** | - The number of squares cleared in a given time.                                           |
|                      | - The time taken to complete the level and space.                                          |
| **Environment**         | - A grid of colored squares linked in a top, right, left, and bottom manner.               |
|                      | - The state of the environment changes as the agent makes moves to destroy interconnected squares.|
| **Actuators**           | - Select and destroy squares in the grid.                                                  |
| **Sensors**             | - The colors of the squares and their connectivity.                                        |
|                      | - Look at the last row to see if it is complete or not.                                    |


You can copy and paste this Markdown code into your GitHub README or any other Markdown-supported platform. Feel free to adjust the formatting or wording as needed.


The project uses the following dependencies:

- Python 3.x
- Pygame

Install dependencies using:

```bash
pip install pygame
