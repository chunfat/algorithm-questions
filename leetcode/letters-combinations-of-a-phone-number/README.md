### Question

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example 1:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

```

**Example 2:**

```
Input: digits = ""
Output: []

```

**Example 3:**

```
Input: digits = "2"
Output: ["a","b","c"]

```

**Constraints:**

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

- **Backtracking Solution**

    ```tsx
    function letterCombinations(digits: string): string[] { 
        // SC: O(1), only 26 letters, constant
        let map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        let ans = []
        
        // TC: O(3^n * 4^m)
        // n is the length of 3-letter digit key, (2,3,4,5,6,8)
        // m is the length of 4-letter digit key, (7, 9)
        // i.e digits = '2379', TC is O(3^2 * 4 ^2) => 3 * 3 * 7 * 7
        // Similarly, SC: O(3^n * 4^m)
        backtracking(ans, map, "", digits);
        
        return ans
    };

    function backtracking(ans: string[], map: {}, combination: string, next: string): void {
        if (next.length == 0) {
            // Goal, no more digits
            if (combination.length) ans.push(combination);
            return;
        }
        
        let letters = map[next.substring(0, 1)]    
        for (let i = 0; i < letters.length; i++) {
            // Choice, no constraint
            backtracking(ans, map, combination + letters[i], next.substring(1))
        }    
    }
    ```

    **How does it work?**

    Quite straightforward, generate all possible combinations.

    **Analysis**

    **Time Complexity:** O(3^n * 4^m)

    **Space Complexity:** O(3^n * 4^m)

- **Brute Force Solution**

    ```tsx
    function bruteForce(digits: string): string[] {
        // SC: O(1), only 26 letters, constant
        let map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        if (digits.length == 0) return [];
        if (digits.length == 1) return map[digits[0]];
        
        let ans = [];
        
        let n = 0;
        
        // TC: O(3^n * 4^m)
        // n is the length of 3-letter digit key, (2,3,4,5,6,8)
        // m is the length of 4-letter digit key, (7, 9)
        // i.e digits = '2379', TC is O(3^2 * 4 ^2) => 3 * 3 * 7 * 7
        
        while (n < digits.length) {
            const digit = map[digits[n]];
            
            if (ans.length) {
                let res = [];
                for (let d = 0; d < ans.length; d++) {
                    for (let i = 0; i < digit.length; i++) {
                        res.push(ans[d] + digit[i]);
                    }
                }
                ans = res;
            } else {
                ans = [...digit]
            }
            
            n++;
        }
        
        // SC: O(3^n * 4^m), same as TC
        return ans;
    }
    ```

    **How does it work?**

    Quite straightforward, generate all possible combinations.

    **Analysis**

    **Time Complexity:** O(3^n * 4^m)

    **Space Complexity:** O(3^n * 4^m)

**Lesson Learnt**

-