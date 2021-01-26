### Question

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

**Example 1:**

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Example 3:**

```
Input: height = [4,3,2,1,4]
Output: 16
```

**Example 4:**

```
Input: height = [1,2,1]
Output: 2
```

**Constraints:**

- `n = height.length`
- `2 <= n <= 3 * 104`
- `0 <= height[i] <= 3 * 104`
- **Solution**

    ```tsx
    function maxArea(height: number[]): number {
        let left = 0;
        let right = height.length - 1;
        let max = 0;
        
        // two pointers
        while (right > left) {
            let a = height[left];
            let b = height[right];
            max = Math.max(max, Math.min(a, b) * (right - left));
            
            if (a > b) {
                right--;
            } else {
                left++;
            }
        }
        
        return max;
    };
    ```

    **How does it work?**

    [container-with-most-water-explanation.mov](container-with-most-water-explanation.mov)

    Source: leetcode

    Why moving the smaller pillar would work?

    Suppose: h[i] ≤ h[j]

    Proof that:  h[i] ≤ h[j] contains the better answer.

    if [i + 1, j] does not contains the better answer, [i, i + 1] contains the better answer.

    However, len(i, j) > (i, i+1) and the answer is constrainted by the h[i]. If h[i] ≤ h[j] does not contain the better answer, it would have contradiction.

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(1)

**Lesson Learnt**

-