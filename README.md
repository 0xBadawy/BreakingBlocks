
 
  
   
=======
<div align="center">

<img height="120" src="https://registry.npmmirror.com/@lobehub/assets-logo/1.0.0/files/assets/logo-3d.webp">
<img height="120" src="https://gw.alipayobjects.com/zos/kitchen/qJ3l3EPsdW/split.svg">
<img height="120" src="https://registry.npmmirror.com/@lobehub/assets-emoji-anim/1.0.0/files/assets/robot.webp">

<h1>AI Puzzle Solver</h1>

</div>



This GitHub repository contains Python implementations of various puzzle-solving algorithms for a 10x10 grid puzzle. The puzzle involves filling a grid with colored blocks and finding the optimal sequence of moves to clear the last row. The implemented algorithms include
## Introduction

The AI Puzzle Solver is a Python application that uses Pygame for graphical representation and implements various search algorithms to solve puzzles. The main focus is on searching algorithms such as Depth-First Search, Breadth-First Search, A*, Uniform Cost Search, and others.

## Algorithms

The following search algorithms are implemented:
 
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Depth-Limited Search (DLS)**
- **Iterative deepening depth-first search (IDLS)**
- **Uniform Cost Search (UCS)**
- **Greedy Best-First Search**
- ***A* Search**

## screenshot from game

[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/fbaf9eec6c8483f05f178d9e3b04d627e00e2b27/Image/repo/image%20num%20(2).png)]()
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/fbaf9eec6c8483f05f178d9e3b04d627e00e2b27/Image/repo/image%20num%20(4).png)]()
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/fbaf9eec6c8483f05f178d9e3b04d627e00e2b27/Image/repo/image%20num%20(3).png)]()
[![AI Puzzle Solver](https://github.com/Mohamed-badawy-sayed/BreakingBlocks/blob/fbaf9eec6c8483f05f178d9e3b04d627e00e2b27/Image/repo/image%20num%20(1).png)]()




  
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


## Agent Specification ( PEAS )


| Aspect              | Description                                                                               |
|---------------------|-------------------------------------------------------------------------------------------|
| **Performance Measure** | - The number of squares cleared in a given time.                                           |
|                      | - The time taken to complete the level and space.                                          |
| **Environment**         | - A grid of colored squares linked in a top, right, left, and bottom manner.               |
|                      | - The state of the environment changes as the agent makes moves to destroy interconnected squares.|
| **Actuators**           | - Select and destroy squares in the grid.                                                  |
| **Sensors**             | - The colors of the squares and their connectivity.                                        |
|                      | - Look at the last row to see if it is complete or not.                                    |

 

## contributors 
<a href="https://github.com/Mohamed-badawy-sayed/BreakingBlocks/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Mohamed-badawy-sayed/BreakingBlocks" />
</a>

## Tools
- Python 3.x
- Pygame

Install dependencies using:

```bash
pip install pygame
