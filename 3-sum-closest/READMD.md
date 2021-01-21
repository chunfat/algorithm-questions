### Question

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

```

**Constraints:**

- `3 <= nums.length <= 10^3`
- `10^3 <= nums[i] <= 10^3`
- `10^4 <= target <= 10^4`

- **Brute Force Solution**

    ```tsx
    function bruteforce(nums: number[], target: number): number {
        let ans: number;
        
        for (let i = 0; i < nums.length - 2; i++) {
            for (let j = i + 1; j < nums.length - 1; j++) {
                for (let k = j + 1; k < nums.length; k++) {
                    let sum = nums[i] + nums[j] + nums[k]
                    if (ans == null || Math.abs(target - ans) > Math.abs(target - sum)) {
                        ans = sum;
                    }
                }
            }
        }
        
        return ans;
    }
    ```

    **How does it work?**

    Generate all possible combinations and select the closest sum.

    **Analysis**

    **Time Complexity:** O(n^3)

    **Space Complexity:** O(1)

- **Two Pointers Solution**

    ```tsx
    function twoPointers(nums: number[], target: number): number {
        let ans: number;
        // Depends on the sorting algorithm used
        // Say Merge Sort, TC: O(n log n), SC: O(n)
        nums.sort((a, b) => a - b);
        
        // TC: O(n^2), SC: O(1)
        for (let i = 0; i < nums.length - 2; i++) {
            if (nums[i] == nums[i - 1]) continue;
            let j = i + 1;
            let k = nums.length - 1;
            
            while (j < k) {
                let sum = nums[i] + nums[j] + nums[k];
                
                if (ans == null || Math.abs(target - ans) > Math.abs(target - sum)) ans = sum;
                if (sum == target) return sum;
                if (sum > target) k--; 
                else j++;
            }
        }
        
        return ans;
        
    }
    ```

    **How does it work?**

    The approach is similar to [3 Sum](https://www.notion.so/3-Sum-758f8406dbc84afd8a8f6d72f278a9df), but we are finding the closest sum instead.

    **Analysis**

    **Time Complexity:** O(n^2)

    **Space Complexity:** O(n)

**Lesson Learnt**

-