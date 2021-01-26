### Question

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, $10^4$]`.
- $`-2^{31}$ <= Node.val <= $2^{31}$ - 1`
- **Solution**

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

    function isValidBST(root: TreeNode | null): boolean {
        return divideAndConquer(root);
    };

    function divideAndConquer(root?: TreeNode, minNode?: TreeNode, maxNode?: TreeNode): boolean {
        if (!root) return true;
        if (minNode?.val >= root.val) return false;
        if (maxNode?.val <= root.val) return false;
        return divideAndConquer(root.left, minNode, root) && divideAndConquer(root.right, root, maxNode);
    }
    ```

    **How does it work?**

    A typical divide and conquer solution. We divide the tree into two subtrees, and keep dividing it util the leaf node. At the root node, it would pass down itself as the max node to the left subtree and similarly pass down itself as min node to the right subtree. At each node, we would validate the node value by comparing the node value to the min/max node. For the left subtree, it must be smaller than it parent node. And for the right subtree, it must greater than it parent node. 

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(1)

**Lesson Learnt**

-