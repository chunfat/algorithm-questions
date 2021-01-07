### Question

Given two strings *s* and *t* , write a function to determine if *t* is an anagram of *s*.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true

```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false

```

**Note:**You may assume the string contains only lowercase alphabets.

**Follow up:**What if the inputs contain unicode characters? How would you adapt your solution to such case?

- **Solution**

    ```tsx
    function isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) return false;
        let dict: number[] = Array.from(Array(26)).map(_ => 0);
        for (let i = 0; i < s.length; i++) {
            dict[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
            dict[t[i].charCodeAt(0) - 'a'.charCodeAt(0)]--;
        }
        for (let i = 0; i < dict.length; i++) {
            if (dict[i] != 0) return false;
        }
        return true;
    };
    ```

    **How does it work?**

    Used a hash map to store the character occurances of `s`, decrease the character occurances of `t`. The result of the final hash map should be all equal `0` if it is a valid anagram.

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(1), as only need store 26 (a-z) characters

**Lesson Learnt**

- Use a fixe 26 length array to store the occurances of a-z alphabets
- Transform character to array index by manipulating character's ASCII code