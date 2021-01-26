### Question

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Example 4:**

```
Input: s = "([)]"
Output: false

```

**Example 5:**

```
Input: s = "{[]}"
Output: true

```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.
- **Stack Solution**

    ```tsx
    function isValid(s: string): boolean {
        let map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        let stack = [];
        for (let i = 0; i < s.length; i++) {
           if (map[s[i]]){
               // close bracket
               let peek = stack[stack.length - 1];
               if (map[s[i]] != peek) return false;
               stack.pop();
           } else {
               // open bracket
               stack.push(s[i]);
           }
        }
        return stack.length === 0
    };
    ```

    **How does it work?**

    1. Push all `open` brackets to the stack.
    2. When `close` bracket encountered, check if the peek of stack is the expected `open` bracket, if yes pop the element. It it doesn not match return false as it is not a valid parentheses.
    3. The stack should be empty after the iteration.

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(n)

**Lesson Learnt**

- Usage of stack