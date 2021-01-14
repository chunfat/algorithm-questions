### Question

Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

```

**Example 2:**

```
Input: l1 = [], l2 = []
Output: []

```

**Example 3:**

```
Input: l1 = [], l2 = [0]
Output: [0]

```

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `100 <= Node.val <= 100`
- Both `l1` and `l2` are sorted in **non-decreasing** order.
- **Recursive Solution**

    ```tsx
    /**
     * Definition for singly-linked list.
     * class ListNode {
     *     val: number
     *     next: ListNode | null
     *     constructor(val?: number, next?: ListNode | null) {
     *         this.val = (val===undefined ? 0 : val)
     *         this.next = (next===undefined ? null : next)
     *     }
     * }
     */

    function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
        return mergeTwoNodes(l1, l2);
    };

    function mergeTwoNodes(n1: ListNode | null, n2: ListNode | null): ListNode | null {
        if (n1 == null) return n2;
        if (n2 == null) return n1;
        if (n1.val < n2.val) {
            n1.next = mergeTwoNodes(n1.next, n2);
            return n1;
        } else {
            n2.next = mergeTwoNodes(n2.next, n1);
            return n2;
        }
    }
    ```

    **How does it work?**

    Simply loop thru the element in both list at the same time, return smaller element and find the next smaller node element by calling the mergeTwoNodes function recursively until either List 1 or List 2 element is null (base case).

    Base Case

    1. n1 is null → return n2
    2. n2 is null → return n1

    Recurrance Relation

    1. if n2 > n1 → mergeTwoNodes(n1.next, n2)
    2. if n1 > n2 → mergeTwoNodes(n2.next, n1)

    **Analysis**

    **Time Complexity:** O(n)

    **Space Complexity:** O(n), it is not tail recursion, for each function calls the system would allocate memory for the function (returning address, passed-in parameters and internal variables)


**Lesson Learnt**

- Visualization would definitely help in solving the problem.