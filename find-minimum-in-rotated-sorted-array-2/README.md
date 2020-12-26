### Question

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:**

```
Input: [1,3,5]
Output: 1
```

**Example 2:**

```
Input: [2,2,2,0,1]
Output: 0
```

**Note:**

- This is a follow up problem to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/).
- Would allow duplicates affect the run-time complexity? How and why?
- **Solution**

    ```tsx
    function findMin(nums: number[]): number {
        const n = nums.length;
        if (n == 1) return nums[0];

        // if the array is in order return the first elements    
        if (nums[n - 1] > nums[0]) return nums[0];
        
        let left = 0;
        let right = n - 1;
        
        while (right > left) {
            let mid = Math.floor((right - left)/2) + left;
            if (nums[right] > nums[mid]) {
                right = mid;
            } else if (nums[right] < nums[mid]) {
                left = mid + 1;
            } else {
                right -= 1;
            }
        }
        return nums[left];
    };
    ```

    **How does it work?**

    This is another application of modified binary search. 

    By observation, we know that if the array is not sorted:

    1. At any index, either LHS or RHS would be a sorted array.
    2. If nums[**right**] > nums[**mid]**, means RHS is sorted,
    3. If RHS is sorted, means the minimum value is **not** in RHS, except the current nums**[mid]**, since the most right element always > than the elements on the left handside, nums**[mid]** is the smallest on RHS, would also be the global minimum number. With that in mind, we would **look into the LHS including the nums[mid]** by setting the **right = mid.**
    4. If LHS is sorted, means the current nums**[mid]** is the largest number in LHS, also it is not the minimum value. 
    5. If nums**[mid]** > nums**[right],** the minimum would be in the RHS, go to RHS by setting **left = mid + 1**.
    6. If nums**[mid]** == nums**[right],  duplication found,** we just move the right pointer forward. **right -= 1**
    7. After all, we return the minimum value **nums[left]**

    **Analysis**

    **Time Complexity:** O(log n)

    **Space Complexity:** O(1)

**Lesson learnt**

- Practise more on binary search