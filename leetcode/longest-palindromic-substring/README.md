### Question

Given a string `s`, return *the longest palindromic substring* in `s`.

**Example 1:**

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

```

**Example 2:**

```
Input: s = "cbbd"
Output: "bb"

```

**Example 3:**

```
Input: s = "a"
Output: "a"

```

**Example 4:**

```
Input: s = "ac"
Output: "a"

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters (lower-case and/or upper-case),

- **Brute Force Solution**

    ```tsx
    function bruteForce(s: string): string {
        let longest = '';
        for (let i = 0; i < s.length; i++) {
            for (let j = i; j < s.length; j++) {
                if (isPalindrome(s, i, j)) {
                    if (j - i + 1 > longest.length) longest = s.substring(i, j + 1);
                }
            }
        }
        return longest;
    }

    function isPalindrome(s: string, left: number, right: number): boolean {
        while (right > left)
            if (s[left++] !== s[right--]) return false;
        return true;
    }
    ```

    **How does it work?**

    Brute force approach, compare every possible palindromes and pick the longest one.

    From this approach, we can find a lot of duplicated process, we can apply dynamic programming approach.

    **Analysis**

    **Time Complexity:** O(n^3), nest loop + checking palindrome loop

    **Space Complexity:** O(1)

- **Dynamic Programming Solution**

    ```tsx
    function dynamicProgramming(s: string): string {
        let dp: boolean[][] = [];
        
        for (let i = 0; i < s.length; i++) {
            dp[i] = [];
            dp[i][i] = true;
        }
        let start = 0;
        let end = 0;
        for (let i = s.length - 1; i >= 0; i--) {
            for (let j = i + 1; j < s.length; j++) {
                if (s[i] === s[j]) {
                    if (j - i == 1 || dp[i + 1][j - 1]) {
                        dp[i][j] = true;
                        if (j - i > end - start) {
                            start = i;
                            end = j;
                        }
                    }
                }
            }
        }
        
        return s.substring(start, end + 1);
    }
    ```

    **How does it work?**

    Oberservations:

    1. if length is 1, start == end, s[start] == s[end], it is palindromic. e.g. "a"
    2. if length is 2, end = start + 1, s[start] == s[end], it is palindromic. e.g. "aa"
    3. if length is 3, end = start + 2, s[start] == s[end] and s[start + 1] == s[end - 1], it is palindromic. e.g. "aba"

    Upon the observation, we can assure that a palindromic string, say "abbba", the inner string must also be palindromic. ⇒ "bbb". With that in mind, we can simply derive a recurrence relation, check if the inner string is palindromic and the base case is **1.** and **2.** Indeed, we can find the solution recursively, and reduce the time complexity using memoization technique.

    In order to avoid stack overflow (if the given `s` is super large), we can apply dynamic programming technique to do it iteratively. We use [start, end] as key to store the result of wheher the the given range [start, end] is palindromic to avoid duplicated palindrome check. 

    **Analysis**

    **Time Complexity:** O(n ^ 2)

    **Space Complexity:** O(n ^ 2)

- **Expand Around Centers Solution**

    ```tsx
    function expandAroundCenters(s: string): string {
        let start = 0;
        let end = 0;
        
        for (let i = 0; i < s.length; i++) {
            // consider s[i] is the center
            // try to expand left and right
            let left = i;
            let right = i;
            
            // Skip duplicate characters in the middle
            while (right < s.length && s[right + 1] == s[right]) right++; 
            while (right < s.length && left > 0 && s[right + 1] == s[left - 1]) {
                right++; 
                left--;
            }
            
            // update palindrome
            if (right - left > end - start) {
                start = left;
                end = right;
            }
        }
        
        return s.substring(start, end + 1);
    }
    ```

    **How does it work?**

    Simply loop thru all characters in string. For each character, we treat it as the center of a palindrome and try to expand around the center to get the largest possible palindrome. 

    There is a special case if there is a consecutive duplicate characters, it would break the above algorithm, thats we need to skip duplicate characters.

    **Analysis**

    **Time Complexity:** O(n ^ 2), this would be faster becoz it skip a lot unnecessary steps.

    **Space Complexity:** O(1)

**Lesson Learnt**

- Use [start, end] as key to store the computed result.
- Consider using other information such as [start, end] as key to solve the problem.
- Do not bother implement the brute force approach.
- Implement the brute force, then find the optimizable parts, quite often it can be optimized using memoization technique.
- Do the observations first, clearly understand the problem.