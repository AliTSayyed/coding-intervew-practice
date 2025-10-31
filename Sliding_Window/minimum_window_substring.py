"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # initlize empty freqeuncy tracking
        t_freq, window_freq = {}, {}

        # t_freq will not change can create it
        for letter in t:
            t_freq[letter] = t_freq.get(letter, 0) + 1

        # keep track of what letters are needed to statisfy t
        have, need = 0, len(t_freq)

        res, resLen = "", float("inf")

        left = 0

        for right in range(len(s)):
            letter = s[right]

            window_freq[letter] = window_freq.get(letter, 0) + 1

            if letter in t_freq and window_freq[letter] == t_freq[letter]:
                have += 1

            while have == need:
                # update our min possible sub array if smaller
                if (right - left + 1) < resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1

                # shrink window from the left
                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    have -= 1
                left += 1

        return res


"""
# Minimum Window Substring

## 1. Pattern Recognition

**Pattern:** Variable-Size Sliding Window + Hash Map

**Key Characteristics:**
- Finding optimal contiguous substring/subarray
- Need to track character frequencies or counts
- Window size is not fixed - must find the minimum/maximum that satisfies constraints
- Can maintain state incrementally as window expands/contracts

**Similar Problems:**
- Longest substring without repeating characters
- Longest substring with at most K distinct characters
- Find all anagrams in a string
- Permutation in string
- Smallest subarray with sum greater than K

## 2. High-Level Approach

Use two pointers to maintain a sliding window. Expand the right pointer to include characters until the window contains all required characters from `t`. Once valid, contract from the left to find the smallest valid window, then continue expanding right to find other potential windows. Track the minimum window throughout.

## 3. Step-by-Step Logic

1. **Build target frequency map:** Count all characters in `t` with their frequencies
   - *Why:* Need to know what we're looking for and how many of each character

2. **Initialize tracking variables:** Window frequency map, left pointer, min window tracker, and "satisfied" counter
   - *Why:* Need to track current window state and best result found

3. **Expand right pointer:** Add each character to window, update its frequency
   - *Why:* Grow window until it becomes valid

4. **Track satisfaction:** When a character's count in window matches its required count in `t`, increment satisfied counter
   - *Why:* Efficiently check if window is valid without looping through all characters

5. **Contract when valid:** While `satisfied == need`, try shrinking from left
   - Save current window if smaller than previous minimum
   - Remove left character, update frequencies and satisfied counter
   - *Why:* Find the smallest valid window starting from this position

6. **Continue until end:** Right pointer sweeps through entire string, left pointer contracts when possible
   - *Why:* Must check all possible windows to find the global minimum

## 4. Key Insights & Edge Cases

**What Makes It Work:**
- Both pointers only move forward (never reset), making it O(n)
- Frequency maps updated incrementally - never recalculate from scratch
- "Satisfied" counter optimization avoids checking all characters repeatedly

**Implementation Gotchas:**
- Update `window_freq` when adding/removing characters (easy to forget)
- Check `letter in t_freq` before incrementing/decrementing satisfied counter
- Use `==` not `>=` when checking if requirement just satisfied (only increment once)
- Remember `s[left:right+1]` to include character at right index
- Return statement goes AFTER the loop, not inside it

**Edge Cases:**
- `t` is empty → return empty string
- `s` shorter than `t` → return empty string
- No valid window exists → return empty string (check if `resLen` still infinity)
- All of `s` is the minimum window

## 5. Pseudocode

```
Build t_freq map from t
Initialize window_freq = {}, left = 0
Initialize have = 0, need = len(t_freq)
Initialize min_result = "", min_length = infinity

for right from 0 to len(s):
    char = s[right]
    Add char to window_freq
    
    if char in t_freq and window_freq[char] == t_freq[char]:
        have += 1
    
    while have == need:  // window is valid
        if (right - left + 1) < min_length:
            Save current window as result
            Update min_length
        
        Remove s[left] from window_freq
        if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
            have -= 1
        left += 1

return result if found, else ""
```

## 6. Complexity Analysis

**Time Complexity:** O(n + m)
- n = length of `s`, m = length of `t`
- Building `t_freq`: O(m)
- Each character in `s` visited at most twice (once by right, once by left): O(n)
- Total: O(n + m)

**Space Complexity:** O(m + k)
- `t_freq`: O(m) where m is length of `t`
- `window_freq`: O(k) where k is number of unique characters in the window (at most 26 for lowercase, 52 for mixed case, etc.)
- In practice: O(1) if character set is fixed/limited
"""
