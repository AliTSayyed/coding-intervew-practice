"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
"""

import math


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # Binary search on the speed range
        left = 1  # Minimum possible speed (1 banana/hour)
        right = max(piles)  # Maximum needed speed (eat largest pile in 1 hour)

        while left < right:
            mid = (left + right) // 2  # Try this eating speed

            # Check if Koko can finish all bananas at this speed
            possible = self.can_finish(piles, mid, h)

            if possible:
                # Speed works, but try a slower speed to find minimum
                right = mid
            else:
                # Speed too slow, need to eat faster
                left = mid + 1

        # left has converged to the minimum speed that works
        return left

    def can_finish(self, piles, speed, hours):
        # Calculate total hours needed at this speed
        hours_needed = 0

        # For each pile, calculate how many hours needed
        for pile in piles:
            # Ceiling division: pile/speed rounded up
            # (Koko spends full hour on each pile even if not full)
            hours_needed += math.ceil(pile / speed)

        # Return True if we can finish within the time limit
        return hours_needed <= hours


"""
1. Pattern Recognition
Pattern: Binary Search on Answer Space (Not on Array)
Key Characteristics:
Need to find minimum/maximum value that satisfies a condition
Can verify if a value works in reasonable time
If value k works, all values > k also work (or vice versa) - creates a sorted decision space
Problem asks for "minimum X such that Y" or "maximum X such that Y"
O(log n) time complexity required or optimal
Similar Problems:
LC 1011: Capacity To Ship Packages Within D Days
LC 410: Split Array Largest Sum
LC 1482: Minimum Number of Days to Make m Bouquets
LC 2187: Minimum Time to Complete Trips (mentioned in video)
Any "minimum/maximum value satisfying condition" problem
2. High-Level Approach
Binary search on the range of possible eating speeds (1 to max pile size) rather than on the piles array itself. For each candidate speed, check if Koko can finish all bananas within h hours by calculating hours needed for each pile (ceiling division). If the speed works, try slower; if not, try faster. Converge to the minimum working speed.
3. Step-by-Step Logic
Define search space: left = 1, right = max(piles)


Why: Minimum speed is 1 banana/hour. Maximum useful speed is max(piles) since eating faster doesn't help (can only eat one pile per hour).
Binary search on speed: Calculate mid speed


Why: We're searching for the minimum speed in a range where slower speeds fail and faster speeds work.
Check if current speed works: Use helper function can_finish(speed)


For each pile, calculate hours needed: ⌈pile / speed⌉
Sum all hours and check if ≤ h
Why: Must check each pile individually due to "one pile per hour" constraint. Can't just do total_bananas / speed.
If speed works: right = mid (try slower speeds)


Why: If speed k works, it might not be the minimum. Need to check if slower speeds also work. Keep mid as candidate since it might be the answer.
If speed doesn't work: left = mid + 1 (need faster speed)


Why: All speeds ≤ mid are too slow. Eliminate left half including mid.
Return left when converged


Why: Left points to the minimum speed that satisfies the condition.
4. Key Insights & Edge Cases
What Makes This Work:
The key insight: if speed k works, all speeds > k also work (monotonic property)
This creates a "sorted" decision space: [fail, fail, fail, | work, work, work]
We're finding the boundary between failure and success
Binary search isn't on the array - it's on the answer space (possible speeds)
Implementation Details:
Use ceiling division for hours per pile: math.ceil(pile / speed) or (pile + speed - 1) // speed
Must check EACH pile individually (can't use sum(piles) / speed)
Use right = mid (not mid - 1) when speed works because mid could be the minimum
The "one pile per hour" constraint is critical - even if pile has fewer bananas than speed, the hour is consumed
Edge Cases:
h equals number of piles - answer is max(piles) (one pile per hour at max speed)
h is very large - answer is 1 (can eat slowly)
Single pile - answer is ⌈pile / h⌉
All piles same size - still need binary search
5. Pseudocode
function minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) / 2
        
        if can_finish(piles, mid, h):
            # Speed works, try slower to find minimum
            right = mid
        else:
            # Speed too slow, need faster
            left = mid + 1
    
    return left


function can_finish(piles, speed, h):
    hours_needed = 0
    
    for each pile in piles:
        # Ceiling division for this pile
        hours_needed += ⌈pile / speed⌉
    
    return hours_needed <= h

6. Complexity Analysis
Time Complexity: O(n × log(max(piles)))
Binary search runs log(max(piles)) iterations (searching speed range from 1 to max)
Each iteration calls can_finish which is O(n) to check all piles
Overall: O(n × log(max(piles)))
Space Complexity: O(1)
Only using constant extra variables (left, right, mid, hours_needed)
No additional data structures or recursion stack
The helper function doesn't use extra space proportional to input

"""
