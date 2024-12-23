
"""
Assignment Title: Counting the Number of Islands

Background:
In computer science, the "Number of Islands" problem is a classic graph traversal problem 
that involves identifying distinct clusters in a grid. The task simulates real-world applications 
like image processing, social network analysis, and geographic mapping.

Problem Statement:
You are given a 2D grid of '1's (land) and '0's (water). An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or vertically. You need to determine the number of islands 
in the given grid.

Task:
Write a Python function `count_islands(grid: List[List[str]]) -> int` that takes a 2D grid as input 
and returns the total number of distinct islands.

Input:
- A 2D grid represented as a list of lists of strings, where:
  - '1' represents land.
  - '0' represents water.
- The grid dimensions are at most 300 x 300.

Output:
- An integer representing the number of islands.

Example:

Input:
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]

Output:
3

Explanation:
- Island 1: Formed by the top-left cluster of '1's.
- Island 2: Formed by the middle '1'.
- Island 3: Formed by the bottom-right cluster of '1's.

Constraints:
1. The grid can contain only the characters '1' and '0'.
2. You may assume all four edges of the grid are surrounded by water.
3. The grid may contain no land ('1'), in which case the output should be 0.

Guidelines:
1. Implement the solution using either Depth-First Search (DFS).
2. Avoid visiting the same cell more than once. Use a mechanism (e.g., marking visited cells) 
   to keep track of visited land cells.
3. Test your solution with edge cases, such as an empty grid, a grid with no islands, or a grid with a single island.

Bonus Challenges:
1. Optimize the solution for memory usage in large grids.
2. Modify the function to allow diagonal connections (i.e., islands connected diagonally are considered part of the same island).
3. Visualize the grid and the islands using a plotting library like Matplotlib.

Submission:
- Save your solution in a Python file named `number_of_islands.py`.
- Include comments explaining your approach and any assumptions.
- Test your code with at least five unique test cases and include them in a separate file named `test_number_of_islands.py`.
"""

from typing import List

def count_islands(grid: List[List[str]]) -> int:
    """
    Counts the number of distinct islands in the given 2D grid.
    
    Args:
        grid (List[List[str]]): A 2D grid of '1's (land) and '0's (water).
    
    Returns:
        int: The total number of islands.
    """
    counter = 0
    for i,row in enumerate(grid):
      for j,cell in enumerate (row):
         if cell == '1':
            stack_islands = [(i,j)]
            k = 0
            counter +=1
            while stack_islands:
              
               temp_cell = stack_islands.pop()
               grid[temp_cell[0]][temp_cell[1]] = '2'
               neighbors = get_island_neighbors (grid,temp_cell)
               stack_islands.extend(neighbors) 
    return counter



def get_island_neighbors(grid,cell: tuple)-> list[tuple]:
  row,coll = cell
  neighbors = [
                (row-1,coll-1),(row-1,coll),(row-1,coll+1),
                (row,coll-1),                  (row,coll+1),
                (row+1,coll-1),(row+1,coll),(row+1,coll+1)]
  n_r=len(grid)
  n_c = len(grid[row])
  resalt_island_neighbors = [(_row,_coll)  
                      for _row ,_coll in neighbors 
                      if 0<=_row <n_r and 0<=_coll<n_c
                       and grid[_row][_coll]=='1' ]

  return resalt_island_neighbors

  