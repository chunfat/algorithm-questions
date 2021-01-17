### Question

Write an efficient algorithm that searches for a `target` value in an `m x n` integer `matrix`. The `matrix` has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `109 <= matix[i][j] <= 109`
- All the integers in each row are **sorted** in ascending order.
- All the integers in each column are **sorted** in ascending order.
- `109 <= target <= 109`

- **Binary Serach Solution**

    ```tsx
    function searchMatrix(matrix: number[][], target: number): boolean {
        let m = matrix.length;
        for (let i = 0; i < m; i++) 
            if (binarySearch(matrix[i], target)) return true;
        
        return false;
    }
        
    function binarySearch(row: number[], target: number): boolean {
        let start = 0;
        let end = row.length;
        while (end >= start) {
            let mid = Math.floor((start + end) / 2);
            if (row[mid] === target) return true;
            if (row[mid] < target) start = mid + 1;
            else end = mid - 1;
        }
        return false;
    }
    ```

    **How does it work?**

    Simply perform binary search at each row.

    **Analysis**

    **Time Complexity:** O(m log n)

    **Space Complexity:** O(1)

- **Divide And Conquer Solution**

    ```tsx
    function divideAndConquer(matrix: number[][], target: number, row: number, col: number, m: number, n: number): boolean {
        const midRow = Math.floor(m / 2) + row;
        const midCol = Math.floor(n / 2) + col;
        // base case
        if (matrix[midRow][midCol] === target) return true;
        if (midRow === row && midCol === col) return false;
        
        // recurrance relation
        if (matrix[midRow][midCol] < target) {
            return (
                // region 1
                divideAndConquer(matrix, target, row, midCol, Math.ceil(m / 2), Math.ceil(n / 2)) ||
                // region 2
                divideAndConquer(matrix, target, midRow, col, Math.ceil(m / 2), Math.ceil(n / 2)) ||
                // region 3
                divideAndConquer(matrix, target, midRow, midCol, Math.ceil(m / 2), Math.ceil(n / 2))
            );
        } else { 
            return (
                // region 0
                divideAndConquer(matrix, target, row, col, Math.ceil(m / 2), Math.ceil(n / 2)) ||
                // region 1
                divideAndConquer(matrix, target, row, midCol, Math.ceil(m / 2), Math.ceil(n / 2)) ||
                // region 2
                divideAndConquer(matrix, target, midRow, col, Math.ceil(m / 2), Math.ceil(n / 2))
            );
        }
    };
    ```

    **How does it work?**

    1. Starting from the middle cell, divide the matrix into 4 matrics.
    2. Based on the middle cell value, if target greater than cell value, recursively search in regions 1, 2, 3, no need to search region 0, since the values in region 0 must less than the target. If target less than middle cell value, recursively search in regions 0, 1, 2, similarly no need to search region 3, coz all values in region 3 are greater than the target.
    3. In each submatrics, it will do 2. recursively until no more submatrics.
    4. If target found stop all recursively call and return true.

    **Analysis**

    **Time Complexity:** O(n), at each recusive call, it would generate 3 more funcion calls, it would no more than n.

    **Space Complexity:** O(n), it is not tail recursion.

    [https://2ality.com/2015/06/tail-call-optimization.html](https://2ality.com/2015/06/tail-call-optimization.html)

- **Linear Solution**

    ```tsx
    function searchMatrix(matrix: number[][], target: number): boolean {
        // starting from bottom left corner or top right corner
        let m = matrix.length;
        let n = matrix[0].length;
        let row = m - 1;
        let col = 0;
        
        while (row >= 0 && col < n) {
            if (matrix[row][col] === target) return true;
            if (matrix[row][col] > target) row--;
            else col++;
        }
        
        return false;
    }
    ```

    **How does it work?**

    We can choose either start from top right corner or bottom left corner, because only at these two cells, the adjacent values are smaller or greater than it values. Based on that, say we start from bottom left corner cell, if the value is less than target we go to the greater value cell and is greater than go to smaller value cell, repeat the process util reach the top right corner or the current cell value equals to target.

    **Analysis**

    **Time Complexity:** O(m+n)

    **Space Complexity:** O(1)

**Lesson Learnt**

- Design a divide and conquer algorithm