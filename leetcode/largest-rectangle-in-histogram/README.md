### Question

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![https://assets.leetcode.com/uploads/2018/10/12/histogram.png](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)

Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

![https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)

The largest rectangle is shown in the shaded area, which has area = `10` unit.

**Example:**

```
Input: [2,1,5,6,2,3]
Output: 10

```

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
Input: heights = [2,4]
Output: 4

```

**Constraints:**

- `1 <= heights.length <= 105`
- `0 <= heights[i] <= 104`

- **Using Stack Solution**

    ```tsx
    function largestRectangleArea(heights: number[]): number {
        let ans = 0; // min height is 0 therefore the smallest possible area is 0
        let hstack = []; // height stack
        let pstack = []; // position stack
        // add a zero at the end to ease the computation
        // for case: 1,2,3,4,5,6,7,8, it would end with a 8-length stack
        heights.push(0)
        for (let i = 0; i < heights.length; i++) {
            let height = heights[i]; // current height
            
            // for case [2, 1, 1]
            // should reuse the left-most greater height position
            // so we can get the max area: 3 * 1 = 3
            let lastPosition = Number.MAX_SAFE_INTEGER;
            
            // if current height < peek height in stack, pop til not true
            while (hstack.length && hstack[hstack.length - 1] > height) {
                // cache the left-most greater than current position
                lastPosition = pstack.pop();
                // calculate the area of the popped  height;
                ans = Math.max(ans, (i - lastPosition) * hstack.pop());
            }
            
            // if current height > peek height in stack, add to stack
            if (!hstack.length || height > hstack[hstack.length - 1]) {
                hstack.push(height);
                // use the minimum between current position and last greater than current height position
                pstack.push(Math.min(i, lastPosition));
            }
            
            // for case peek of hstack equals to current height
            // should do nothing
        }
        
        return ans;
    };
    ```

    **How does it work?**

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(n)

**Lesson Learnt**

- I was so close to getting the correct O(n) solution. The idea I had was exactly same as the stack solution. My original solution is calculating the max area on the fly, which make it too complicated and too chaotic in logic. This is also the reason that why I couldn't solve it.
- Do not only analyze the solution in the brain, should draw it out and do more observations.
- Do not be bothered doing the brute force solution, try to do the brute force first, then try to analyze which part is waste of computation time and not necessary.