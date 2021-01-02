### Question

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1:**

![https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Constraints:**

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit or `'.'`.

- **3 Pass Solution**

    ```tsx
    function threePassSolution(board: string[][]) {
        
        for (let row = 0; row < 9; row++) {
            // check row
            let set = new Set();
            for (let i = 0; i < 9; i++) {
                if (board[row][i] == '.') continue;
                if (set.has(board[row][i])) return false
                set.add(board[row][i]);
            }
        }
             
        for (let col = 0; col < 9; col++) {
            // check column   
            let set = new Set();
            for (let i = 0; i < 9; i++) {
                if (board[i][col] == '.') continue;
                if (set.has(board[i][col])) return false
                set.add(board[i][col]);
            } 
        }
            
        for (let row = 0; row < 9; row+=3) {
            for (let col = 0; col < 9; col+=3) {
                // check boxes
                let set = new Set();
                for(let i = 0; i < 3; i++) {
                    for (let j = 0; j < 3; j++) {
                        if (board[row + i][col + j] == '.') continue;
                        if (set.has(board[row + i][col + j])) return false;
                        set.add(board[row + i][col + j]);
                    }    
                }
            }
        }
        
        return true;
    }
    ```

    **How does it work?**

    1. Check each rows
    2. Check each columns
    3. Check each boxes

    **Analysis**

    Clean code, do one thing in a function

    > If the time complexity is the same, there is no reason to make any premature optimizations. Always choose the simplest, most maintainable solution.

    **Time Complexity:** O(81) + O(81) + O(9 * 9 * 3 * 3) => O(1)

    **Space Complexity:** O(9 + 9 + 9) => O(1), used 3 9-length hash set

- **One Iteration Solution**

    ```tsx
    function oneIteration(board: string[][]) {
        let rowSets: Set<string>[] = [];
        let colSets: Set<string>[] = [];
        let boxSets: Set<string>[] = [];
        
        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                const num = board[r][c];
                const b = Math.floor(r / 3) * 3 + Math.floor(c / 3)
                if (num === ".") continue;
                if (!rowSets[r]) rowSets[r] = new Set();
                if (!colSets[c]) colSets[c] = new Set();
                if (!boxSets[b]) boxSets[b] = new Set();
                if (rowSets[r].has(num)) return false;
                if (colSets[c].has(num)) return false;
                if (boxSets[b].has(num)) return false;
                rowSets[r].add(num);
                colSets[c].add(num);
                boxSets[b].add(num);
            }
        }
        return true;
    }
    ```

    **How does it work?**

    Similar to 3 pass approach, but merged into one loop.

    **Analysis**

    Arguablely, not clean code coz it is smart coding (do 3 things in 1 functions)

    **Time Complexity:** O(81) as go thru 81 cells => O(1)

    **Space Complexity:** O(9 + 9 + 9), used 3 9-length hash set => O(1)

**Lesson Learnt**

- Always choose the simplest, most maintainable solution.
-