### Question

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example:**

```
Input:  [1,2,3,4]Output: [24,12,8,6]
```

**Constraint:** It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

**Note:** Please solve it **without division** and in O(*n*).

**Follow up:** Could you solve it with constant space complexity? (The output array **does not** count as extra space for the purpose of space complexity analysis.)

- **Brute Force Solution**

    ```tsx
    function bruteForce(nums: number[]): number[] {
        let result: number[] = [];
        for(let i = 0; i < nums.length; i++) {
            let temp = 1;
            for(let j = 0; j < nums.length; j++) {
                if (i == j) continue;
                temp *= nums[j];
            }
            result.push(temp);
        }
        return result;
    }
    ```

    **How does it work?**

    1. The outer loop iterate each i, 0 → nums.length
    2. The inter loop iterate each nums and multipy `temp`, except `i`, then store the result.

    **Explanation**

    Simple brute force, multipy each elements except current one.

    **Analysis**

    **Time Complexity:** O(**n^2**)

    **Space Complexity:** O(**n**)

- **Two Loops with Stack Solution**

    ```tsx
    function twoLoopsWithStack(nums: number[]): number[] {
        let result: number[] = [1];
        let stack: number[] = [nums[0]];
        let m: number = 1;
        
        for(let i = 1; i < nums.length; i++) {
            result[i] = result[i - 1] * stack[stack.length - 1];
            stack.push(nums[i]);
        }
        
        for(let i = 2; i <= nums.length; i++) {
            let idx = nums.length - i;
            m *= stack.pop();
            result[idx] *= m;
        }
        
        return result;
    }
    ```

    **How does it work?**

    The first loop goes thru each elements of nums starting from 1 → n.length - 1:

    1. Push the current number to stack.
    2. Store temporary result of `the peek number of stack times previous temporary result`.

    After the first loop, we would have a reverse num stack and a temporary result.

    Then, the second loop, start from 2 → n.length:

    1. calculate the inverse index ⇒ nums.length - i
    2. for each iteration, pop an element of stack and multiply and store it to `m` ⇒ `m = m * stack.pop()`
    3. update the result element with inverse index ⇒ `m * result[idx]`

    **Explanation**

    Loop thru each element in `nums`, store the result of `previous result * nums[i-1]`:

    1. Given array `nums` [1,2,3,4], after first loop, `result` ⇒ [1,1,2,6]

        result[0]=1;

        result[1]= result[0] * nums[0] = 1 * 1 = 1;

        result[2]= result[1] * nums[1] = 1 * 2 = 2;

        result[3]= result[2] * nums[2] = 2 * 3 = 6;

    2. Second start `from 2 to nums.length`, calcualte inverse index and pop each stack items [4, 3, 2, 1]:

        i = 2; idx = 4 - 2 = 2; m = 1 * 4 = 4; result[2] = result[2] * m = 2 * 4 = 8;

        i = 3; idx = 4 - 3 = 1; m = 4 * 3 = 12; result[1] = result[1] * m = 1 * 12 = 12;

        i = 4; idx = 4 - 4 = 0; m = 12 * 2 = 24; reuslt[0] = result[0] * m = 1 * 24 = 24;

    3. Final result = [24, 12, 8, 6]

    **Analysis**

    For time, it loops twice.

    For space, it uses two n-length arrays.

    **Time Complexity:** O(**2n**) ⇒ O(**n**)

    **Space Complexity:** O(**2n**) ⇒ O(**n**)

- **Left and Right Product**

    ```tsx
    function leftRightProduct(nums: number[]): number[] {
        let result: number[] = [];
        let left: number[] = [];
        let right: number[] = [];
        
        left[0] = 1;
        right[nums.length - 1] = 1;
        
        for(let i = 1; i < nums.length; i++) {
            left[i] = nums[i - 1] * left[i - 1];
        }
        
        for(let i = nums.length - 2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }
        
        for(let i = 0; i < nums.length; i++) {
            result[i] = left[i] * right[i]
        }
        
        return result;
        
    }
    ```

    **How does it work?**

    1. Loop thru each element from left to right, store the left`[i]` = left`[n-1]` * nums`[n-1]`.
    2. Loop thru each element from right to left, store the right`[i]` = right`[n+1]` * nums`[n+1]`.
    3. Multiple product of all elements to the left and to the right

    **Explanation**

    Given [1, 2, 3, 4]

    1. Loop left to right, left ⇒ [1, 1, 2, 6]
    2. Loop right to left, right ⇒ [24, 12, 4, 1]
    3. Multiple each same position element of left and right, result ⇒ [24, 12, 8, 6]

    **Analysis**

    **Time Complexity:** O(**3n**) ⇒ O(**n**)

    **Space Complexity:** O(**3n**) ⇒ O(**n**)

- **Left and Right Product 2**

    ```tsx
    function leftRightProduct2(nums: number[]): number[] {
        let result: number[] = [];
        let left: number[] = [];
        let right: number[] = [];
        
        left[0] = 1;
        right[nums.length - 1] = 1;
        
        for(let i = 1; i < nums.length; i++) {
            left[i] = nums[i - 1] * left[i - 1];
            right[nums.length - i - 1] = nums[nums.length - i] * right[nums.length - i];
        }
        
        for(let i = 0; i < nums.length; i++) {
            result[i] = left[i] * right[i]
        }
        
        return result;
        
    }
    ```

    **How does it work?**

    Same as the previous one, but do left and right in one go.

    **Explanation**

    **Analysis**

    **Time Complexity:** O(**2n**) ⇒ O(**n**)

    **Space Complexity:** O(**3n**) ⇒ O(**n**)

    - **Constant Space**

    ```tsx
    function constantSpace(nums: number[]): number[] {
        let result: number[] = [];
        let r = 1;
        
        result[0] = 1;
        
        for(let i = 1; i < nums.length; i++) {
            result[i] = nums[i - 1] * result[i - 1];
        }
        
        for(let i = nums.length - 1; i >= 0; i--) {
            result[i] *= r;
            r *= nums[i];
        }
        
        return result;
        
    }
    ```

    **How does it work?**

    1. Loop thru `nums` array from left to right,  store the result`[i]` = nums`[n-1]` * result`[n-1]`.
    2. Loop thru nums array from right to left, this time we use an extra variable `r` to store the product of num from right, and calculate the final result[i] *= r.

    **Explanation**

    Given [1, 2, 3, 4]

    1. Loop left to right, result ⇒ [1, 1, 2, 6]

        initial; result[0] = 1; r = 1

        i=1; result[i] = nums[i - 1] * result[i - 1] = 1 * 1 = 1; result = [1, 1]

        result = [1, nums[0] * result[0]] = [1, `1 * 1`]

        i=2; result[i] = nums[i - 1] * result[i - 1] = 2 * 1 = 2; result = [1, 1, 2]

        result = [1, nums[0] * result[0]] = [1, 1 * 1, `1 * 1 * 2`]

        i=3; result[i] = nums[i - 1] * result[i - 1] = 3 * 2 = 6; result = [1, 1, 2, 6]
        
        result = [1, nums[0] * result[0]] = [1, 1 * 1, 1 * 1 * 2, `1 * 1 * 2 * 3`]

    2. Loop right to left, use `r` to store the product of num from right, final result ⇒ [24, 12, 8, 6]

        i=3; result[i] *= r = 6 * 1 = 6; result ⇒ [1, 1, 2, **6**], r *= nums[i] = 1 * 4 = 4
        
        result = [1, 1 * 1, 1 * 1 * 2, `1 * 1 * 2 * 3 * 1`] =  [1, 1 * 1, 1 * 1 * 2, `6`]

        i=2; result[i] *= r =  2 * 4 = 8; result ⇒ [1, 1, **8**, 6], r *= nums[i] = 4 * 3 = 12

        result = [1, 1 * 1, `1 * 1 * 2 * 4`, 6] = [1, 1 * 1, `8`, 6]

        i=1; result[i] *= r = 1 * 12 = 12; result ⇒ [1, **12**, 8, 6], r *= nums[i] = 12 * 2 = 24

        result = [1, `1 * 1 * 12`, 8, 6] = [1, `12`, 8, 6]
        i=0; result[i] *= r = 1 * 12 = 24; result ⇒ [**24**, 12, 8, 6], r *= nums[i] = 24 * 1 = 24

        result = [`1 * 24`, 12, 8, 6] = [`24`, 12, 8, 6]

        In a nutshell:
        e.g. 
        
        [ `a`, b, c, d, e] ⇒ a = product of left * product of right = b * c * d * e = a

        [ a, `b`, c, d, e] ⇒ b = product of left * product of right = a * c * d * e = b

        [ a, b, `c`, d, e] ⇒ c = product of left * product of right = a * b * e * d = c

        [ a, b, c, `d`, e] ⇒ d = product of left * product of right = a * b * c * e = d
        
        [ a, b, c, d, `e`] ⇒ e = product of left * product of right = a * b * c * d = e

    1. the first loop calculate the product of left and store to result[], where we get [1, a, ab, abc,  abcd ]

    2. the second loop calculate the product of right and calculate the final result, where we get:

        r is initized to 1, to ease the calculation,

        r =   ,       result = [1,            a,       ab,      abc,   abcd]

        r = e,       result = [1,           a,       ab,      abce, abcd]

        r = de,     result = [1,          a,       abde, abce, abcd]

        r = cde,   result = [1,         acde, abde, abce, abcd]
        
        r = bcde, result = [bcde, acde, abde, abce, abcd]

    **Analysis**

    **Time Complexity:** O(**2n**) ⇒ O(**n**)

    **Space Complexity:** O(**n**) ⇒ O(**n**), Ignore the result array, it is O(**1**)