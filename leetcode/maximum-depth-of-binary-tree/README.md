### Question

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Example 3:**

```
Input: root = []
Output: 0
```

**Example 4:**

```
Input: root = [0]
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `100 <= Node.val <= 100`

**Solution**

```tsx
function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;
    const left = maxDepth(root.left);
    const right = maxDepth(root.right);
    return Math.max(left, right) + 1;
};
```

**How does it work?**

1. Deep dive into the child, until the child is null, then return the child depth.
2. if child is null then return zero
3. the parent collects the depth of it childs and take the largest one as it child depth
4. After getting the child depth then plus 1 and return to it parent, until it reached the root node.

**Explanation**

It is kind of `Divide and Conquer` algorithm, in which each subtree calculate it own maximum depth and return the result to the higher level node, until reaching the root node.

**Analysis**

**Time Complexity:** O(n)

**Space Complexity:** O(n)