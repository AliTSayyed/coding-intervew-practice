"""
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        mySet = set()
        max_count = float("-inf")

        left = 0
        right = 0

        # sliding window
        while right < len(s):
            # keep moving left until all duplicates are removed
            # effectively resets the subtring to contain only unique values
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1

            # not a duplicate so add it to the set
            mySet.add(s[right])

            # keep track of the max substring
            max_count = max(max_count, right - left + 1)

            # keep checking for new unique chars
            right += 1

        return max_count


"""
# Longest Substring Without Repeating Characters

## 1. Pattern Recognition
**Pattern:** Sliding Window + Hash Set

**Key Characteristics:**
- Finding longest/shortest contiguous sequence with constraints
- Need to track unique elements in current window
- Window expands and contracts dynamically

**Similar Problems:**
- Longest Substring with K Distinct Characters
- Minimum Window Substring
- Longest Repeating Character Replacement
- Fruit Into Baskets

## 2. High-Level Approach
Use two pointers to maintain a sliding window of unique characters. Expand the window by moving right pointer, and shrink from left when duplicates appear. Track the maximum window size seen.

## 3. Step-by-Step Logic

1. **Initialize window:** Start with `left=0`, `right=0`, empty set, `max_count=0`
   - *Why:* Window begins at start of string

2. **Expand window:** Move `right` pointer through string
   - *Why:* Explore all possible substrings

3. **Check for duplicates:** If `s[right]` already in set
   - Remove `s[left]` from set and increment `left`
   - Repeat until duplicate removed
   - *Why:* Maintains uniqueness constraint by shrinking window from left

4. **Add character:** Add `s[right]` to set
   - *Why:* Character is now guaranteed unique in window

5. **Update maximum:** Calculate current window size `(right - left + 1)`
   - *Why:* Track longest valid substring found

6. **Continue:** Move `right` forward
   - *Why:* Explore next potential substring

## 4. Key Insights & Edge Cases

**What makes it work:**
- Set provides O(1) lookup for duplicates
- Left pointer only moves forward, never backward (each character removed at most once)
- Window always contains unique characters

**Implementation details:**
- Inner while loop removes characters until duplicate gone
- Update max_count **after** adding character but **before** incrementing right
- Each character added and removed from set exactly once

**Edge cases:**
- Empty string → return 0
- Single character → return 1
- All unique characters → return length of string
- All same characters → return 1

## 5. Pseudocode

```
initialize left = 0, right = 0, max_count = 0, empty set

while right < length of string:
    while s[right] exists in set:
        remove s[left] from set
        increment left
    
    add s[right] to set
    update max_count with (right - left + 1)
    increment right

return max_count
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Each character visited at most twice (once by right, once by left)
- Set operations are O(1)
- Total: O(2n) = O(n)

**Space Complexity:** O(min(n, m))
- n = string length, m = character set size
- Set stores at most all unique characters in string
- For ASCII: O(128), for Unicode: O(n) worst case
"""
