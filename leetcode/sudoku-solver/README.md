### Question

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1:**

![https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
```

![https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

**Constraints:**

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`.
- It is **guaranteed** that the input board has only one solution.
- **Solution**

    ```tsx
    function solveSudoku(board: string[][]): void {
        // Initialize 3 used hashset - 0 : row, 1: col, 2: box
        let usedSet: Set<string>[][] = [[], [], []];
        initialize(board, usedSet);
        solver(board, 0, 0, usedSet);
    };

    function initialize(board: string[][], usedSet: Set<string>[][]) {
        for (let r = 0; r < 9; r++) {
            usedSet[0][r] = new Set();
            for (let c = 0; c < 9; c++) {
                const num = board[r][c];
                const b = Math.floor(r / 3) * 3 + Math.floor(c / 3)
                if (!usedSet[1][c]) usedSet[1][c] = new Set();
                if (!usedSet[2][b]) usedSet[2][b] = new Set();
                if (num === ".") continue;
                usedSet[0][r].add(num);
                usedSet[1][c].add(num);
                usedSet[2][b].add(num);
            }
        }
    }

    function solver(board: string[][], row: number, col: number, usedSet: Set<string>[][]) {
        // Our Goal, solve the puzzle
        if (row >= 9) return true;
        if (col >= 9) return solver(board, row + 1, 0, usedSet);
        
        // Cell is not free
        if (board[row][col] !== ".") return solver(board, row, col + 1, usedSet);
        
        const box = Math.floor(row / 3) * 3 + Math.floor(col / 3)
        
        for (let i = 1; i < 10; i++) {
            // Our Constraint, is digit valid to place
            if (isDigitValid(row, col, box, `${i}`, usedSet)) { 
                
                // Our Choice, Place a digit
                placeDigit(row, col, box, `${i}`, board, usedSet);
                
                // Solve the board
                const solved = solver(board, row, col + 1, usedSet);
                if (solved) return true;
                
                // Undo our choice
                undoDigit(row, col, box, `${i}`, board, usedSet);
            }
        }
        
    }

    function isDigitValid(row: number, col: number, box: number, digit: string, usedSet: Set<string>[][]) {
        return !usedSet[0][row].has(digit) && !usedSet[1][col].has(digit) && !usedSet[2][box].has(digit)
    }

    function placeDigit(row: number, col: number, box: number, digit: string, board: string[][], usedSet: Set<string>[][]) {
        board[row][col] = digit;
        usedSet[0][row].add(digit);
        usedSet[1][col].add(digit);
        usedSet[2][box].add(digit);
    }

    function undoDigit(row: number, col: number, box: number, digit: string, board: string[][], usedSet: Set<string>[][]) {
        board[row][col] = ".";
        usedSet[0][row].delete(digit);
        usedSet[1][col].delete(digit);
        usedSet[2][box].delete(digit);
    }
    ```

    **How does it work?**

    By applying Backtracking algorithm, we follow the 3 Keys:

    1. Our Goal - Solve the puzzle by fill in all empty cells
    2. Our Constraint - The digit in each cell must be unique (in terms of row, col, and box)
    3. Our Choice - Place a digit in empty cell

    In order to `solve the puzzle`, we **attempt to fill 1 - 9 digit** in empty cell. After placing a digit, it would `validate by the constraint`. If the placement is valid, then it would move to next cell and repeat the same process. At each cell, it would **try all 9 possiblities**, if none of it pass the constraint, it would reset the current cell to empty and backtrack to the previous cell. The previous cell would then try next possible digit. The process keeps *repeating unitil it reach the last cell*.

    To validate the the placement, we would applys the checking logic same as [Valid Sudoku](../valid-sudoku/README.md), but an optimized version to reduce the time complexity. At here, it does not validate the entire board again and again, instead by simply checking the hashsets.

    **Analysis**

    **Time Complexity:** O(n^n)

    **Space Complexity:** O(1)

**Lesson Learnt**

- Identify the complexity, the key performance factor then optimize it