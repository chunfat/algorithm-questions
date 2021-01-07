### Question

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```

**Constraints:**

- `s` consists only of printable ASCII characters.
- **Solution**

    ```tsx
    function isPalindrome(s: string): boolean {
        // two pointers approach
        s = s.replace(/[^0-9a-z]/gi, "").toLowerCase();
        let left = 0;
        let right = s.length - 1;
        while (right > left) {
            if (s[left++] != s[right--]) return false;
        }
        
        return true;
    };
    ```

    **How does it work?**

    First, we make sure that the string contains only alphanumeric characters. Then, we use two pointers, to compare the left and right characters, if it is not the same then return false. It can be further simplified by using just one pointer as below:

    ```tsx
    function isPalindrome(s: string): boolean {
        // two pointers approach
        s = s.replace(/[^0-9a-z]/gi, "").toLowerCase();

        for (let i = 0; i < s.length; i++) {
            if (s[i] != s[s.length - 1 - i]) return false;
        }
        return true;
    }
    ```

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(1)

**Lesson Learnt**

-