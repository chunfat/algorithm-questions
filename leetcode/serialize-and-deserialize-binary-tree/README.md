### Question

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Example 4:**

```
Input: root = [1,2]
Output: [1,2]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `1000 <= Node.val <= 1000`

---

- **Solution**

    ```tsx
    /*
     * Encodes a tree to a single string.
     */
    function serialize(root: TreeNode | null): string {
        if (!root) return '';
        let result = '';
        let q = [root];
        while(q.length) {
            let n = q.shift();
            result += (n ? n.val : '') + ',';
            if (!n) continue;
            q.push(n.left);
            q.push(n.right);
        }
        return result;
    };

    /*
     * Decodes your encoded data to tree.
     */
    function deserialize(data: string): TreeNode | null {
        const nodes = data.split(',');
        if (!nodes || !nodes.length || !nodes[0]) return null;
        const root = new TreeNode(parseInt(nodes.shift()));
        const q = [root]; // dequeue the first node (root node)
        
        while (q.length) {
            const currNode = q.shift();
            if (currNode) {
                // dequeue next 2 nodes in nodes
                const left = nodes.shift();
                const right = nodes.shift();
                if (left) currNode.left = new TreeNode(parseInt(left));
                if (right) currNode.right = new TreeNode(parseInt(right));
                q.push(currNode.left);
                q.push(currNode.right);
            }
        }
        
        return root;
        
    };

    /**
     * Your functions will be called as such:
     * deserialize(serialize(root));
     */
    ```

    **How does it work?**

    Using `Breath First Search BFS` technique for serialization.

    1. First, Push **Root** node to **Queue**
    2. Dequeue the a node from the **Queue**
    3. Concatenate current node value to a the result string variable
    4. Skip to next node if current node is `null`
    5. Push childs from **Left** to **Right** to the **Queue**
    6. Repeat 2 - 5, until the **Queue** is empty.

    For deserialization, it is using the same technique.

    1. First, Push **Root** node to **Queue,** Remove **root(1st) node(element)** from the tokens
    2. Dequeue the a node from the **Queue,** save it as current node
    3. Skip to next node if the current node is null
    4. Dequeue first 2 items from the tokens, and add it as left and right of the current node
    5. Add the current left node and right node to the **Queue**
    6. Repeat 2 - 5, until the **Queue** is empty.

    **Explanation**

    Serialization:

    Go thru the breath first when travse the child of a node.

    For each node, it pushes child nodes to the queue first, so it make sure the breath go first.

    Then, it dequeues a node from the queue, and repeat the same process to 

    Deserializtion:

    It is basically the reverse of what we done in the serialization.
    From root node, keep filling the nodes in the breath of the current node.

    **Analysis**

    - Serialization

        **Time Complexity:** O(n)

        **Space Complexity:** O(n)

    - Deserialization

        **Time Complexity:** O(n)

        **Space Complexity:** O(n)