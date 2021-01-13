### Question

Given an integer `n`, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```

**Constraints:**

- `0 <= n <= 8`
- **Recursive Solution**

    ```tsx
    /**
     * Definition for a binary tree node.
     * class TreeNode {
     *     val: number
     *     left: TreeNode | null
     *     right: TreeNode | null
     *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
     *         this.val = (val===undefined ? 0 : val)
     *         this.left = (left===undefined ? null : left)
     *         this.right = (right===undefined ? null : right)
     *     }
     * }
     */

    function generateTrees(n: number): Array<TreeNode | null> {
        if (n === 0) return [];
        return generateSubTrees(1, n);
    };

    function generateSubTrees(start: number, end: number): Array<TreeNode | null> {
        // Base cases
        if (start === end) return [new TreeNode(start)];
        if (start > end) return [null];

        let result = [];
        
        // for all possible roots
        for (let i = start; i <= end; i++) {
            // generate all possible left subtrees
            let leftTrees = generateSubTrees(start, i - 1);
            // generate all possible right subtrees
            let rightTrees = generateSubTrees(i + 1, end);
            for(let l = 0; l < leftTrees.length; l++) {
                for (let r = 0; r < rightTrees.length; r++) {
                    // all possible subtrees
                    result.push(new TreeNode(i, leftTrees[l], rightTrees[r]));
                }
            }
        }
        return result;
    }
    ```

    **How does it work?**

    In order to **generate all possible unique subtrees**, we have to generate possible roots from 1 to n, i.e. n is 2, we would need to generate all unique subtrees that the root is 1 and also all unique subtrees that the root is 2. To accomplish that at least one loop is needed. 

    Then, for each possible root node, we also want to **generate all the possible left and right unique subtrees**.  For example: n is 4, and we want to generate all possible subtrees of root node 2. We know that anything less than 2 would be in the LHS of the root node, and if it is greater then root node, it would be in the RHS. So for root node 2, the LHS would has node 1, and the RHS would has node 3 and 4. The LHS has only 1 node, so nothing interesting. For the RHS, there are 2 nodes, it needs to generate all possbile unique subtrees. To do so, we would recursively call the same function with the start is 3 and the end is 4. 

    After getting all the possible subtrees, we would **combine all the possible subtrees and push it to the result.**

    Base Cases

    1. **start === end,** **return [new TreeNode(start)**
    2. **start > end, return [null]**

    Recurrance Relation

    For each root,

    1. Generate all possible left subtrees ⇒ **generateSubTrees(start, i - 1)**
    2. Generate all possible right subtrees ⇒ **generateSubTrees(i + 1, end)**
    3. Combine all possible all left and right to generate all possible root subtrees.

    Note: **i** is the current node value

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(n), non-tail recursion.

**Lesson Learnt**

-