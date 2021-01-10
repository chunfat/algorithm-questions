### Question

Given an integer `rowIndex`, return the `rowIndexth` row of the Pascal's triangle.

Notice that the row index starts from **0**.

![https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Follow up:**

Could you optimize your algorithm to use only *O*(*k*) extra space?

**Example 1:**

```
Input: rowIndex = 3
Output: [1,3,3,1]
```

**Example 2:**

```
Input: rowIndex = 0
Output: [1]
```

**Example 3:**

```
Input: rowIndex = 1
Output: [1,1]
```

**Constraints:**

- `0 <= rowIndex <= 33`

- **Recursive Solution**

    ```tsx
    function recursion(rowIndex: number): number[] {
        let result = [];
        let memo: number[][] = [];
        for (let col = 0; col < rowIndex + 1; col++) {
            result.push(getRowCol(rowIndex, col, memo));
        }
        return result;
    }

    function getRowCol(row: number, col: number, memo: number[][]): number {
        if (col == 0 || row == col) return 1;
        if (!memo[row]) memo[row] = [];
        if (memo[row][col]) return memo[row][col];
        memo[row][col] = getRowCol(row - 1, col, memo) + getRowCol(row - 1, col - 1, memo);
        return memo[row][col];
    }
    ```

    **How does it work?**

    The first element and the last element in the row must be `1` . And the value in between is [i - 1][j] + [i - 1][j - 1], where `i` is row and `j` is column. Based on that, we can easily come up with a recursive function and we use memorization to reduce time complexity.

    **Base Case**: **j = 0** or **i = j** ⇒ return **1**

    **Recurrence Relation**: row**[j]** = row**[i - 1][j]** + row**[i - 1][j - 1]**

    **Memoization**: ****memo**[j]** = row**[j]**

    **Analysis**

    **Time Complexity:** O((n(n+1))/2) ⇒ O(n^2) 
    [https://stackoverflow.com/questions/28966072/complexity-time-on-or-onn1-2](https://stackoverflow.com/questions/28966072/complexity-time-on-or-onn1-2)

    **Space Complexity:** O(n^2)

- **Iterative Solution**

    ```tsx
    function iterative(rowIndex: number): number[] {
        let row = [1];
        for (let i = 1; i <= rowIndex; i++) {
            for (let j = i - 1; j > 0; j--) {
                row[j] = row[j - 1] + row[j];
            }
            row.push(1)
        }
        return row;
    }
    ```

    **How does it work?**

    The idea is the same as recursive version, but we can only use a `n`-length array to memorize the calculated result. Here, it keeps modifying the cached array until it reach the target row.

    E.g. n = 5;
    Initial ⇒ [1]
    At i = 1 ⇒ [1, 1]
    At i = 2 ⇒ [**1, 1**] ⇒ [1, 2] ⇒ [1, 2, **1**]
    At i = 3 ⇒ [1, **2, 1**] ⇒ [**1, 2**, 3] ⇒ [1, 3, 3] ⇒ [1, 3, 3, **1**]
    At i = 4 ⇒ [1, 3, **3, 1**] ⇒ [1, **3, 3**, 4] ⇒ [**1, 3**, 6, 4] ⇒ [1, 4, 6, 4, **1**]
    At i = 5 
    ⇒ [1, 4, 6, **4, 1**] ⇒ [1, 4, **6, 4**, 5] ⇒ [1, **4, 6**, 10, 5] ⇒ [**1, 4**, 10, 10, 5] ⇒ [1, 5, 10, 10, 5, **1]**

    **Analysis**

    **Time Complexity:** O(n ^ 2)

    **Space Complexity:** O(n)

**Lesson Learnt**

-