### Question

Given a string `s` consisting only of characters *a*, *b* and *c*.

Return the number of substrings containing **at least** one occurrence of all these characters *a*, *b* and *c*.

**Example 1:**

```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
```

**Example 2:**

```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
```

**Example 3:**

```
Input: s = "abc"
Output: 1
```

**Constraints:**

- `3 <= s.length <= 5 x 10^4`
- `s` only consists of *a*, *b* or *c* characters.

### Naive Solution (Timed out), O(n^n)

```tsx
function numberOfSubstrings(s: string): number {
    let count = 0;
    for (let i = 0; i < s.length - 2; i++) {
        for(let j = i + 2; j < s.length; j++) {
            if (containABC(s.substring(i, j+1))) count++
        }
    }
};

function containABC(s: string): boolean {
    return s.includes('a') && s.includes('b') && s.includes('c')
}
```

**Analysis**

1. `for (let i = 0; i < s.length - 2; i++) {` loop thru all characters, n
2. `for(let j = i + 2; j < s.length; j++) {` loop thru all characters, m
3. The complexity is at least O(m*n)
4. `containABC` function using `includes` the worst case is O(m*n), m is string length, n is search pattern length
5. So, the complexity is O(n^n)

### O(n) Solution

```tsx
function numberOfSubstrings(s: string): number {
    let count = 0;
    let lastIdx = { a: -1, b: -1, c:-1 };
    for(let i = 0; i < s.length; i++) {
        lastIdx[s[i]] = i;
        count += 1 + Math.min(...Object.values(lastIdx));
    }
    
    return count;
}
```

**How does it work?**

1. Loop each characters in string `s` from left to right,
2. Record the intermediate last index of each character `a`, `b`, `c` during the loop.
3. In each iteration, find the minimum value among the last index `a`, `b`, `c`.

e.g.

s: `abcabc`

initial index of a, b, c: `{ a: -1, b: -1, c: -1}`

i = 0; lastIdx = `{ a: 0, b: -1, c: -1}`; count = 0;

i = 1;  lastIdx = `{ a: 0, b: 1, c: -1}`; count = 0;

i = 2;  lastIdx = `{ a: 0, b: 1, c: 2}`; count = 1;

i = 3;  lastIdx = `{ a: 3, b: 1, c: 2}`; count = 3;

i = 4;  lastIdx = `{ a: 3, b: 4, c: 2}`; count = 6;

i = 5;  lastIdx = `{ a: 3, b: 4, c: 5}`; count = 10;

**Explanation**

The whole idea to find the last 3 `a` `b` `c` positions, once we found that any start position counting toward to last 3 `a` `b` `c` positions is count as a valid substring.

**e.g.**  

for string aaaabca, it is a sum of:

1. xxx`abc` ⇒ possible substring `abc`, x`abc`, xx`abc`, xxx`abc`

2. xxxa`bca` ⇒ possible substring `bca`, a`bca`, xa`bca`, xxa`bca`, xxx, `bca`

sum = 4 + 5 = 9

Complexity is **O(n)**, only one loop is needed.