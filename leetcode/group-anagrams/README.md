### Question

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]

```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]

```

**Constraints:**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lower-case English letters.
- **Sorting Solution**

    ```tsx
    function categorizeBySorting(strs: string[]): string[][] {
        let dict = {}
        
        for (let i = 0; i < strs.length; i++) {
            let sorted = strs[i].split('').sort().join('');
            if (!dict[sorted]) dict[sorted] = []
            dict[sorted].push(strs[i]);
        }

        let result = [];
        
        Object.values(dict).forEach(val => result.push(val));
        
        return result;
    }
    ```

    **How does it work?**

    For each words in `strs`, sort the characters and use it as a dictionary key. For each key, we maintain an array to store the words that has same key. For example, `eat` ⇒ `aet`, `tea` ⇒ `aet`,  `bat` ⇒ `abt`, `tan` ⇒ `ant`, `nat` ⇒ `ant` we would have a dictionary as below:

    `aet`: [eat, tea]

    `abt`: [bat]

    `ant`: [tan, nat]

    **Analysis**

    **Time Complexity:** O(n * k log k)

    **Space Complexity:** O(n * k), total content stored in the hash map.

- **Count Solution**

    ```tsx
    function categoriesByCount(strs: string[]): string[][] {
        let dict = {};
        let count = Array.from(Array(26));
        
        for (let i = 0; i < strs.length; i++) {
            count = count.fill(0);
            for (let j = 0; j < strs[i].length; j++) 
                count[strs[i][j].charCodeAt(0) - 'a'.charCodeAt(0)]++
            let key = count.join('#');
            if (!dict[key]) dict[key] = [];
            dict[key].push(strs[i]);
        }
        

        let result = [];
        
        Object.values(dict).forEach(val => result.push(val));
        
        return result;
    }
    ```

    **How does it work?**

    Simialar idea to the sorting approach, instead, it uses the alphabet count as key, i.e. `abc` ⇒ `1#1#1#0#0#0....`

    **Analysis**

    **Time Complexity:** O(n * k)

    **Space Complexity:** O(n * k), total content stored in the hash map.

**Lesson Learnt**

- A simple hashing technique by using the sorted alphabets key or alphabets count key.