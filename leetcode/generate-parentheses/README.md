### Question

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

**Example 2:**

```
Input: n = 1
Output: ["()"]

```

**Constraints:**

- `1 <= n <= 8`

- **Backtracking Solution**

    ```tsx
    function generateParenthesis(n: number): string[] {
        let result: string[] = []
        helper('(', n, 1, 0, result);
        return result;
    };

    function helper(s: string, n: number, open: number, close: number, result: string[]) {
        // all n bracket pairs found
        if (close == n) {
            result.push(s);
            return;
        }

        // Our Constraints
        if (open > close) {
            // Choice 1: add close bracket
            helper(s + ')', n, open, close + 1, result);
        }

        // Our Constraints
        if (open < n) {
    				// Choice 2: add open bracket
            helper(s + '(', n, open + 1, close, result);
        }
    }
    ```

    **How does it work?**

    When doing backtracking, we needs 3 things:

    - Our Goal - all n bracket pairs found.
    - Our Constraints
        1. Can only add close bracket, when the number of open bracket is greater than the number of close bracket.
        2. Can only add open bracket, when the number of open bracket is less than n.
    - Our Choices
        1. Place either open or close bracket.

    **Analysis**

    **Time Complexity:** O(2^n), exponential

    **Space Complexity:** O(2^n), exponential

**Lesson Learnt**

- Another practise to generate all possible patterns with constraints.