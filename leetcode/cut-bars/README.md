### Question

Imagine that there is a **n cm** length bar and we want to cut it in to **n** **1cm** length bar. However a bar can only cut by 1 person. 

I.e. if there are 3 bars and 3 persons, each person can cut one bar.

When there are **m** persons, what is the minimum times to cut a **n** bar into **n** 1cm bars?

For example, a 8cm bar and 3 persons, the minimum times is 4.

![cut-bars-q.png](cut-bars-q.png)

- **Solution**

    ```tsx
    // Recursion approach
    function cutBarRecursively(n: number, m: number, current: number): number {
        if (current >= n) return 0; // has been cut into n 1cm cutBar

        // when m > current, double cut all bar into 2 bars
        if (m > current) {
            return 1 + cutBarRecursively(n, m, current * 2);
        } else {
            // when current >= m, can only cut m bars into 2 bars
            return 1 + cutBarRecursively(n, m, current + m);
        }
    }

    // iterative approach
    function cutBarIteratively(n: number, m: number): number {
        let current = 1;
        let times = 0;
        
        while (current < n) {
            current += m > current ? current : m;
            times++;
        }

        return times;
    }
    ```

    **How does it work?**

    ![cut-bars-sol.png](cut-bars-sol.png)

    **Analysis**

    **Time Complexity:** O(n), if m == 1, then it would run n times

    **Space Complexity:** O(1)

**Lesson Learnt**

-