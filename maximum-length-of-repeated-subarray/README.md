### Question

Given two integer arrays `A` and `B`, return the maximum length of an subarray that appears in both arrays.

**Example 1:**

```
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

```

**Note:**

1. 1 <= len(A), len(B) <= 1000
2. 0 <= A[i], B[i] < 100
- **Brute Force Solution**

    ```tsx
    function bruteForce(A: number[], B: number[]): number {
        let ans = 0;
        for (let i = 0; i < A.length; i++) {
            for (let j = 0; j < B.length; j++) {
                let k = 0;
                while (A[i + k] === B[j + k]) k++;
                ans = Math.max(ans, k);
            }
        }
        return ans;
    }
    ```

    **How does it work?**

    Simple naive solution using nested loops. It is simply comparing each element A[i] and B[j], when they are same, compare A[i + 1] and B[j + 1], repeate and count the same element til A[i + 1] ≠ B[i + 1] or no more element in either A or B, then store the max count to ans.

    **Analysis**

    A simple brute force. We can a bit optimization of this approach by skipping the compared element. i.e. A: 1, 2, `3, 2, 1` and B: `3, 2, 1`, 4, 7, we know that when A[2 - 4] and B[0 - 2] are repeated by comparing A[3 - 4] and B[1 - 2]. When checking A[3] and B[1], it would go comparing A[4] and B[2] again. We can avoid this by just simple using a seen array to store the compared pairs. However, it would not improve the time complexity.

    **Time Complexity:** O(n * m * min(n, m))

    **Space Complexity:** O(1)

- **Recursion Solution**

    ```tsx
    function recursion(A: number[], B: number[]): number {
        let ans = 0;
        
        for (let i = 0; i < A.length; i++) {
            for (let j = 0; j < B.length; j++) {
                ans = Math.max(ans, countSame(A, B, i, j));
            }
        }
        
        return ans;
    }

    function countSame(A: number[], B: number[], i: number, j: number): number {
        if (i == A.length || j == B.length) return 0;
        if (A[i] != B[j]) return 0;
        return 1 + countSame(A, B, i + 1, j + 1);
    }
    ```

    **How does it work?**

    The idea is same as brute force, but we are doing the checking recursively here.

    1. if A[i] ≠ B[j] or i/j out of boundary, we return 0
    2. if A[i] == B[j], we check the next pair A[i + 1] and B[j + 1]
    3. Each pair that A[i] == B[j], we add 1 to the count.

    **Analysis**

    Here, we break it down into a smaller problem by just comparing the current A[i] B[j] pair at a time. When applying recursion, we defined a base case `A[i] ≠ B[j] or i/j out of boundary` and the next comparing case.

    **Time Complexity:** O(n * m * min(n, m))

    **Space Complexity:** O(1)

- **Dynamic Programming Solution**

    ```tsx
    function dynamicProgramming(A: number[], B: number[]): number {
        let ans = 0;
        let dp: number[][] = [];
        dp[A.length] = [];
        for (let i = A.length - 1; i >= 0; i--) {
            if (!dp[i]) dp[i] = []; // initialize the array
            for (let j = B.length - 1; j >= 0; j--) {
                if (A[i] != B[j]) continue;
                dp[i][j] = (dp[i + 1][j + 1] || 0) + 1
                ans = Math.max(ans, dp[i][j]);
            }
        }
        return ans;
    }
    ```

    **How does it work?**

    This solution is derived from the recursive approach. By looking at the recursion approach, we find that for each comparing pair A[i], B[j], is the result of the next pair A[i + 1] B[j + 1], count + 1 if it is same. Also, we know that we may compare the same pair again for another A[i] B[j], so we can memorize the result of pair A[i + 1] B[j + 1] by adopting `dynamic programming` approach. For each `dp[i][j]` (A[i], B[j]), the result is `dp[i + 1][j + 1] + 1`. We can then come up with an algorithm that is bottom-up to pre-calculate the result of dp[i + 1][j + 1] for dp[i][j].

    **Analysis**

    **Time Complexity:** O(n * m)

    **Space Complexity:** O(n * m)

**Lesson Learnt**

- Always start with the naive brute force solution, and then try to implement recursion version of it.
- Try to find the pattern and find the painpoint.
- If there is any duplication process, it might then be solved by `Dynamic Programing`