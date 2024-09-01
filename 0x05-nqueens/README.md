# 0x05-nqueens


# N Queens Puzzle Solver

This Python script solves the N Queens puzzle, a classical problem in computer science and mathematics. The goal is to place N chess queens on an NxN chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
  - [Key Functions](#key-functions)
- [Usage](#usage)
- [Example Output](#example-output)
- [Requirements](#requirements)
- [Algorithm Explanation](#algorithm-explanation)
- [Limitations](#limitations)

## Overview

The N Queens problem is a well-known challenge of combinatorial optimization and backtracking. This script uses a backtracking algorithm to find one valid solution for the N Queens problem, given an input `N`.

## How it Works

### Key Functions

1. **`check_feasible(Psol, place, N)`**:
   - This function checks if placing a queen at a given position `place` is feasible within the current partial solution `Psol`.
   - It ensures that no two queens share the same column or diagonal.

2. **`Nqueen_Solving(Psol, N)`**:
   - This is the recursive backtracking function. It attempts to place queens on the board, and if it reaches an invalid configuration, it backtracks and tries a different placement.

3. **Main Execution**:
   - The script reads the value `N` from the command-line argument.
   - It attempts to find solutions for placing N queens on an NxN board by calling the `Nqueen_Solving` function.

## Usage

To use this script, ensure you have Python 3 installed. The script takes one argument, `N`, which specifies the size of the chessboard and the number of queens to place.

### Example Commands

python3 nqueens.py 8

This command will find one solution to the 8 Queens problem.

### Usage Notes

- `N` must be a number.
- The script will only work for values of `N` that are 4 or greater. For values of `N` less than 4, there are no valid solutions, and the script will return an error message.

## Example Output

For `N = 4`, the output would look something like:

[[0, 1], [1, 3], [2, 0], [3, 2]]

This output represents the positions of the queens on the board. Each sublist `[row, column]` indicates the position of a queen on the chessboard.

## Requirements

- Python 3.7+
- No external dependencies are required.

## Algorithm Explanation

This script uses a **backtracking algorithm** to find a solution to the N Queens problem. Here's a step-by-step breakdown:

1. The script starts by trying to place a queen in each column of the first row.
2. For each placement, the script checks if it is feasible by verifying that no two queens are in the same column or diagonal.
3. If the placement is valid, the algorithm recursively attempts to place queens in the next column.
4. If a full solution is found (i.e., all queens are placed without conflicts), the solution is returned.
5. If placing a queen leads to a conflict, the algorithm backtracks, removes the last placed queen, and tries the next possibility.

This backtracking process ensures that all possible placements are considered until a solution is found or all options are exhausted.

## Limitations

- **Single Solution**: The script currently finds only one solution to the N Queens problem. It does not find all possible solutions.
- **Performance**: The backtracking algorithm is effective but can be slow for large values of `N`, as it explores many possible placements.

## License

This project is open-source and available under the MIT License.

### Usage Example:

After saving the script to `nqueens.py`, running the following command for a 4x4 board will give the solution:

python3 nqueens.py 4

And you will get an output like:

[[0, 1], [1, 3], [2, 0], [3, 2]]

This `README.md` file provides an overview of the problem, how the script works, and how to run it, making it clear for users to understand and use your program.
