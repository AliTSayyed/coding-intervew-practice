"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_area

        # brute force
        # max_area = 0

        # for i in range(len(height) - 1):
        #     j = i + 1
        #     while j < len(height):
        #         length = min(height[i], height[j])

        #         width = j - i

        #         area = length * width

        #         max_area = max(max_area, area)

        #         j += 1

        # return max_area


"""
# LeetCode 11: Container With Most Water

## 1. Pattern Recognition

**Pattern:** Two Pointers (Opposite Ends) with Greedy Choice

**Key Characteristics:**
- Need to find optimal pair with some constraint (maximizing area)
- Area depends on two factors: distance (width) and limiting factor (min height)
- Can eliminate suboptimal solutions without checking all pairs
- Width starts at maximum and can only decrease
- Looking for trade-off between width and height

**Similar Problems:**
- LeetCode 42: Trapping Rain Water
- LeetCode 167: Two Sum II (sorted array)
- LeetCode 15: 3Sum
- LeetCode 16: 3Sum Closest
- Any optimization problem with two endpoints

## 2. High-Level Approach

Start with pointers at both ends to maximize width. Calculate the area using the shorter of the two heights (the limiting factor). Move the pointer at the shorter height inward, because moving the taller height cannot improve the area (width decreases and height remains limited by the shorter line). Continue until pointers meet, tracking the maximum area.

## 3. Step-by-Step Logic

1. **Initialize left pointer at start (0) and right pointer at end (len-1)**
   - Why: Start with maximum possible width to establish baseline

2. **Calculate current area = min(height[left], height[right]) × (right - left)**
   - Why: Area is limited by the shorter height (water would overflow)
   - Width is the distance between the two lines

3. **Update max_area if current area is larger**
   - Why: Track the best solution found so far

4. **Move the pointer at the shorter height inward**
   - Why: Moving the taller pointer guarantees the area gets worse (width decreases, height stays capped by shorter line)
   - Moving the shorter pointer gives us a chance to find a taller line that could compensate for the lost width
   - This greedy choice eliminates all worse solutions involving the current shorter line

5. **If heights are equal, move both pointers (optional optimization)**
   - Why: Either choice is valid; moving both speeds up convergence slightly

6. **Repeat until left < right**
   - Why: When pointers meet, we've evaluated all potentially optimal pairs

## 4. Key Insights & Edge Cases

**Key Insights:**
- **Area is always limited by the shorter height** - this is the fundamental constraint
- **Width can only decrease** as pointers move inward, so we start with max width
- **Greedy choice is optimal:** Moving the shorter pointer is the only way to possibly improve
- **We never miss the optimal solution** because:
  - If optimal pair uses indices (i, j), we'll either evaluate it directly OR
  - We'll find a better solution with greater width that uses one of those indices
- **Elimination principle:** Each move eliminates all solutions involving that shorter height that can't be better

**Implementation Details:**
- Use `min(height[left], height[right])` to get limiting height
- Track `max_area` throughout, don't try to find it at the end
- When heights are equal, moving either pointer works (your choice to move both is fine)
- Condition is `while left < right`, not `<=` (can't form container with same line)

**Edge Cases:**
- Array with 2 elements: Works, forms one container
- All heights equal: Still works, maximum area is at furthest apart
- One very tall line: Algorithm still finds optimal pairing
- Decreasing or increasing heights: Algorithm handles monotonic sequences correctly

## 5. Pseudocode

```
function maxArea(height):
    left = 0
    right = length - 1
    max_area = 0
    
    while left < right:
        // Calculate current area
        current_height = min(height[left], height[right])
        current_width = right - left
        current_area = current_height * current_width
        
        // Update maximum
        max_area = max(max_area, current_area)
        
        // Move pointer at shorter height
        if height[left] < height[right]:
            left++
        else if height[right] < height[left]:
            right--
        else:
            // Equal heights - can move either or both
            left++
            right--
    
    return max_area
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Each pointer moves at most n times
- Pointers move toward each other, visiting each element once
- Single pass through the array
- Each iteration does O(1) work (min, multiplication, comparison)

**Space Complexity:** O(1)
- Only using a few variables: left, right, max_area, current calculations
- No extra data structures that scale with input size
- Constant space regardless of array size
"""
