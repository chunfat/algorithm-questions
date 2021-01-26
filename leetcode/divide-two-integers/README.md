### Question

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero, which means losing its fractional part. For example, `truncate(8.345) = 8` and `truncate(-2.7335) = -2`.

**Note:**

- Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, assume that your function **returns 2^31 − 1 when the division result overflows**.

**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

```

**Example 3:**

```
Input: dividend = 0, divisor = 1
Output: 0

```

**Example 4:**

```
Input: dividend = 1, divisor = 1
Output: 1

```

**Constraints:**

- `2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`

- **Bit Manipulation Solution**

    ```tsx
    function bitManipulation(dividend: number, divisor: number): number {
        if (dividend == (1 << 31) && divisor == -1) return ~(1 << 31);
        if (dividend <= (1 << 31) && divisor == 1) return 1 << 31;
        
        let absDividend = Math.abs(dividend);
        let absDivisor = Math.abs(divisor);
        let result = 0;
        
        for (let x = 31; x >= 0; x--) {
            if ((absDividend >>> x) - absDivisor >= 0) {
                result += (1 << x);
                absDividend -= (absDivisor << x);
            }
        }

        return (dividend > 0) == (divisor > 0) ? result : -result;

    }
    ```

    **How does it work?**

    Since JavaScript Numbers are always 64-bit Floating Point and the question bound the input range `2^31 <= dividend, divisor <= 2^31 - 1`, so we check the edge cases manually.

    - Case 1:
        - dividend: **-2147483648**, divisor: **-1** ⇒ return max value in 32-bit integer ⇒ ~(1 << 31)
    - Case 2:
        - dividend: **-2147483648**, divisor: **1** ⇒ return min value in 32-bit integer ⇒ 1 << 31

    After that, we can simply ignore the sign and take the absolute value of dividend and divisor. Then, we only do these 3 things repeatedly **util dividend is smaller than divisor**:

    1. Find how many **x** bits (31 to 0, inclusively) we need to right shift the dividend so that it would greater or equal to the divisor. ⇒ it also means dividend/(2^x) ≥ divisor.
    2. Add **2^x** to result, this is the multiple that divisor would need to multipy in order to make the dividend smaller.
    3. Minus the dividend by `(divisor * 2^x) ⇒ divisor << x`

    **Analysis**

    **Time Complexity:** O(32)

    **Space Complexity:** O(1)

**Lesson Learnt**

- Bit manipulation, [learn here](https://www.youtube.com/watch?v=NLKQEOgBAnw)
- Generate -2^31 in JS ⇒ 1 << 31, left shift 31 bits
- Generate 2^31 - 1 in JS ⇒ ~(1 << 31), left shift 31 bits then revert it
- Interest fact that when doing bit manipulation on number in JS, the range is [-2 ^ 31, 2^31 - 1], but you can still add one or minus one, it would not overflow.
- Do multiple/divide by 2, without using multiplcation, division and modulos