### Question

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

**Example 1:**

```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

```

**Example 2:**

```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

**Note:**

1. The input string length won't exceed 1000.

- **Dynamic Programming Solution**

    ```tsx
    function dynamicProgramming(s: string): number {
        let dp = [];
        let ans = s.length;
        
        for (let i = 0; i < s.length; i++) {
            dp[i] = [];
            // r == l
            dp[i][i] = true;
        }
        
        for (let i = s.length - 1; i >= 0; i--) {
            for (let j = i + 1; j < s.length; j++) {
                // r = l + 1, s[r] == s[l]
                if (s[i] == s[j]) {
                    // r - l == 1, e.g. 'aa'
                    // inner substring is palindromic, l + 1, r - 1
                    if (j - i == 1 || dp[i + 1][j - 1]) {
                        dp[i][j] = true;
                        ans++;
                    }
                }
            }
        }
        
        
        return ans;
    }
    ```

    **How does it work?**

    Similar idea as solving [Longest Palindromic Substring](../longest-palindromic-substring/README.md) 

    **Analysis**

    **Time Complexity:** O(n^2)

    **Space Complexity:** O(n ^ 2)

- **Expand Around Centers Solution**

    ```tsx
    function expandAroundCenters(s: string): number {
        let ans = 0;
        
        for (let i = 0; i < s.length; i++) {
            // char itself is palindromic
            ans++;

            // treat current char as palindrome center;
            let char = s[i];
            
            // expand the palindrome center;
            let left = i;
            let right = i;

            while (left > 0 && right < s.length - 1 && 
                   s[left - 1] === s[right + 1]) {
                ans++;
                left--;
                right++;
            }
            
            // if s[i] === s[i+1], expand it as palindrome center
            if (i < s.length - 1 && s[i] == s[i + 1]) {
                ans++;
                left = i;
                right = i + 1;
                while (left > 0 && right < s.length - 1 && 
                   s[left - 1] === s[right + 1]) {
                    ans++;
                    left--;
                    right++;
                }
            }
            
        }
        
        return ans;
    }
    ```

    **How does it work?**

    Similar idea as solving [Longest Palindromic Substring](../longest-palindromic-substring/README.md) 

    **Analysis**

    **Time Complexity:** O(n)^2

    **Space Complexity:** O(1)

**Lesson Learnt**

-