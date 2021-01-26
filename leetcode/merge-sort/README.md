- **Top down In-place Solution**

    ```tsx
    function merge(arr: number[], left: number, right: number): void {
        // get middle
        const mid = Math.floor((left + right) / 2);
        const leftArr: number[] = [];
        const rightArr: number[] = [];

        // initialize left right arrays
        for (let i = left; i <= mid; i++) leftArr.push(arr[i]);
        for (let i = mid + 1; i <= right; i++) rightArr.push(arr[i]);

        // add max int to both arrays, ease computation
        leftArr.push(Number.MAX_SAFE_INTEGER);
        rightArr.push(Number.MAX_SAFE_INTEGER);

        let idxLeft = 0;
        let idxRight = 0;

        for (let i = left; i <= right; i++) {
            if (leftArr[idxLeft] <= rightArr[idxRight]) {
                arr[i] = leftArr[idxLeft];
                idxLeft++;
            } else {
                arr[i] = rightArr[idxRight];
                idxRight++;
            }
        }

    }

    function mergeSort(arr: number[], left: number, right: number): void {
        if (right > left) {
            const mid = Math.floor((left + right) / 2);
            mergeSort(arr, left, mid); // sort LHS
            mergeSort(arr, mid + 1, right); // sort RHS
            merge(arr, left, right); // merge 2 halves
        }
    }

    let arr = [4, 1, 3, 9, 7];
    mergeSort(arr, 0, arr.length - 1);
    console.log(arr)

    let arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
    mergeSort(arr2, 0, arr2.length - 1);
    console.log(arr2)
    ```

    **Time Complexity:** O(n log n)

    **Space Complexity:** O(n)

- **Bottom Up Solution**

    ```tsx
    // bottom up merge sort
    function bottomUp(nums: number[]): number[] {
        // split
        let arr = nums.map(n => [n]);

        while(arr.length !== 1) {
            let result = [];
            for (let i = 0; i < arr.length; i+=2) {
                if (i == arr.length - 1) result.push(arr[i])
                else result.push(merge(arr[i], arr[i + 1]))
            }
            arr = result;
        }

        return arr[0];
    }

    function merge(leftArr: number[], rightArr: number[]): number[] {
        if (!leftArr.length) return rightArr;
        if (!rightArr.length) return leftArr;
        
        let result = [];
        let len = leftArr.length + rightArr.length
        leftArr.push(Number.MAX_SAFE_INTEGER);
        rightArr.push(Number.MAX_SAFE_INTEGER);
        let leftIdx = 0;
        let rightIdx = 0;
        for (let i = 0; i < len; i++) {
            if (leftArr[leftIdx] < rightArr[rightIdx]) {
                result.push(leftArr[leftIdx])
                leftIdx++;
            } else {
                result.push(rightArr[rightIdx])
                rightIdx++;
            }
        }
        
        return result;
    }
    ```

    **Time Complexity:** O(n log n)

    **Space Complexity:** O(n)