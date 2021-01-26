### Question

Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a* + *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Notice** that the solution set must not contain duplicate quadruplets.

**Example 1:**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```

**Example 2:**

```
Input: nums = [], target = 0
Output: []

```

**Constraints:**

- `0 <= nums.length <= 200`
- `109 <= nums[i] <= 109`
- `109 <= target <= 109`

- **Wraps 3 sum Solution**

    ```tsx
    function fourSum(nums: number[], target: number): number[][] {
        return wrapThreeSum(nums, target);
    };

    function wrapThreeSum(nums: number[], target: number): number[][] {
        let ans = [];
        
        nums.sort((a, b) => a - b);
        
        for (let i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                let subAns = threeSum(nums, target - nums[i], i + 1);
                for (let j = 0; j < subAns.length; j++) {
                    ans.push([nums[i], ...subAns[j]]);
                }
            }
        }
            
        return ans;
    }

    function threeSum(nums: number[], target: number, start: number): number[][] {
        let ans = [];
        
        for (let i = start; i < nums.length; i++) {
            if (i == start || nums[i] != nums[i - 1]) {
                let l = i + 1;
                let r = nums.length - 1;

                while (r > l) {
                    let sum = nums[i] + nums[l] + nums[r];

    								// skip seen numbers
                    if (sum < target || (l > i + 1 && nums[l] == nums[l - 1])) {
                        l++;
                    } else if (sum > target || (r < nums.length - 1 && nums[r] == nums[r + 1])) {
                        r--;
                    } else {
                        ans.push([nums[i], nums[l++], nums[r--]]);
                    }

                }
            }
        }
     
        return ans;
    }
    ```

    **How does it work?**

    Same approach as solving [3 Sum](https://www.notion.so/3-Sum-758f8406dbc84afd8a8f6d72f278a9df):

    1. Sort an array, O(n log n)
    2. Go thru each element in array
    3. For each element, try to find all possible the 3 Sum of other elements in the array where is the target is `target - current element`
    4. Add the found 3 Sum together with the current element to result.

    **Analysis**

    **Time Complexity:** O(n^3)

    **Space Complexity:** O(n)

- **K Sum** **Solution**

    ```tsx
    function fourSum(nums: number[], target: number): number[][] {
        nums.sort((a, b) => a - b);
        return kSum(nums, target, 0, 4);
    };

    function kSum(nums: number[], target: number, start: number, k: number): number[][] {
        let result: number[][] = [];
        
        if (start == nums.length || k * nums[start] > target || k * nums[nums.length - 1] < target)
            return result;
        
        if (k == 2) return twoSum(nums, target, start);
        
        for (let i = start; i < nums.length; i++) {
            // skip if the current is equal to the previous one
            if (i == start || nums[i] != nums[i - 1]) {
                let subKSumResult = kSum(nums, target - nums[i], i + 1, k - 1);
                for (let j = 0; j < subKSumResult.length; j++) {
                    result.push([nums[i], ...subKSumResult[j]])
                }
            }
        }
        
        return result;
    }

    function twoSum(nums: number[], target: number, start: number): number[][] {
        let result: number[][] = [];
        let left = start;
        let right = nums.length - 1;
        
        while (right > left) {
            let sum = nums[left] + nums[right];
            
            if (sum < target || (left > start && nums[left] == nums[left - 1])) {
                left++;
            } else if (sum > target || (right < nums.length - 1 && nums[right] == nums[right + 1])) {
                right--;
            } else {
                result.push([nums[left++], nums[right--]]);
            }
        }
        
        return result;
    }
    ```

    **How does it work?**

    The is a generic algorithm for k-Sum, the approach is nothing changed.

    **Analysis**

    **Time Complexity:** O(n ^ k - 1)

    **Space Complexity:** O(n)

**Lesson Learnt**

- Sorting would make the problem easier to solve.
- Be careful of the duplicates.