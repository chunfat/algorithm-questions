### Question

Implement [pow(*x*, *n*)](http://www.cplusplus.com/reference/valarray/pow/), which calculates *x* raised to the power *n* (i.e. xn).

**Example 1:**

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**

```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Constraints:**

- `100.0 < x < 100.0`
- `231 <= n <= 2311`
- `104 <= xn <= 104`
- **Solution**

    ```tsx
    function myPow(x: number, n: number): number {
        if (n === 0) return 1;
        // x ^ -n = 1/x ^ n
        if (n < 0) return myPow(1/x, n * -1);
        // n is even, x ^ n = (x * x) ^ (n / 2)
        // e.g. 2 ^ 4 = 2 * 2 * 2 * 2 = 4 * 4 = 4 ^ 2
        if (n % 2 === 0) return myPow(x * x, n / 2);
        // n is odd, x ^ n = ((x * x) ^ ((n - 1) / 2)) * x
        // e.g. 2 ^ 5 = 2 * 2 * 2 * 2 * 2 = 4 * 4 * 2 = (4 ^ 2) * 2
        return myPow(x * x, (n - 1) / 2) * x;
    };
    ```

    **How does it work?**

    $x^n = x * x * ... * x$

    $x^{-n} =$  $1 \over x^n$

    if $n$ is even, $x^n = (x * x)^{n\over2}$, 
    e.g. $2^4 =$ $2 * 2 * 2 * 2$ $= 4 * 4 = 4^{2}$

    if n is odd, $x^n = (x * x)^{n-1\over2} * x$, 
    e.g. $2^5 = 2 * 2 * 2 *2 *2$  $= 4 * 4 * 2 = 4^2 * 2^1$

    **Analysis**

    **Time Complexity:** O(log n)

    **Space Complexity:** O(log n)

**Lesson Learnt**

- A smarter divide and conquer algorithm makes a huge different in time complexity.