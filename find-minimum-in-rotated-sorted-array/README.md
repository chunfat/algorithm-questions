### Question

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums`, return *the minimum element of this array*.

**Example 1:**

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

```

**Example 3:**

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5000`
- `5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

- **Solution**

    ```tsx
    function findMin(nums: number[]): number {
        const n = nums.length;
        if (n == 1) return nums[0];
        // array is rotated, binary search
        let left = 0;
        let right = n - 1;
        
        while(right > left) {
            let mid = left + Math.floor((right - left) / 2);
            
            // array sorted, return left value
            if (nums[right] > nums[left]) return nums[left];
            
            if (nums[mid] >= nums[left]) {
                // LHS is sorted
                // 1 2 3 is not a case
                // 2 3 4 5 1, 3 4 5 1 2
    						// 3 1 <-- handled by >=
                // the minimum must be on the RHS
                left = mid + 1;
            } else {
                // RHS is sorted
                // 5 6 1 2 3 4
                // the minimum would be on the LHS, including mid
                right = mid;
            }
            
        }
        
        return nums[left];
        
    };
    ```

    **How does it work?**

    Similar to [Find Minimum in Rotated Sorted Array II](https://www.notion.so/Find-Minimum-in-Rotated-Sorted-Array-II-0f8ae4b3ea45445c9e40c47c8c13edfc), except that all numbers are unique here.

    By observation, we know that:

    1. if it is sorted, the left most value must be the minimum.
    2. if not sorted,

        2.1 At any index, either LHS or RHS is sorted

        2.2 if LHS is sorted, the minimum must be in RHS, since

        2.2.1 the RHS is not sorted

        2.2.2 if both LHS and RHS is sorted, should be handled by 1.

        2.3 If RHS is sorted, the minimum must be in LHS (including nums[mid], since

        2.3.1 nums**[mid]** is the minimum of RHS, could also be the global minimum

    3. After all, the nums[left] would be the minimum value.

    **Analysis**

    **Time Complexity:** O(log n)

    **Space Complexity:** O(1)

**Lesson learnt**

- Use Binary Search for searching an array, gurantee O(log n)
- Practise Binary search and basic sorting algorithms