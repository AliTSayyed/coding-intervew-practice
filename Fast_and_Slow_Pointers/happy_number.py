"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        # while the fast value is not 1 check for a cycle
        while fast != 1:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

            if fast == slow and fast != 1:
                return False

        return True

    def getNext(self, n: int) -> int:
        total = 0
        while n > 0:
            # extract the last digit
            digit = n % 10

            # add its square to the total
            total += digit * digit

            # remove the last digit
            n = n // 10

        return total


"""
Problem:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Solution:
Happy Number
1. Pattern Recognition
Pattern: Fast and Slow Pointers (Floyd's Cycle Detection) + Math
Key Characteristics:
Problem mentions "loops endlessly in a cycle"
Following a sequence where each number leads to the next (implicit linked list)
Need to detect if sequence reaches target (1) or enters infinite cycle
Can apply cycle detection without physical linked list structure
Similar Problems:
Linked list cycle detection
Find the duplicate number (array as implicit linked list)
Detect cycle in any sequence/transformation problem
Any problem with "eventually repeats" or "loops forever"
2. High-Level Approach
Treat the number sequence as an implicit linked list where each number "points to" the next via sum of squared digits. Use fast/slow pointers: slow advances one step, fast advances two steps. If they meet and aren't at 1, there's a cycle without reaching 1 (not happy). If either reaches 1, it's happy.
3. Step-by-Step Logic
Create helper to get next number: Extract all digits using modulo/division, square each, sum them


Why: This defines the "next" transformation in our sequence (like .next in linked list)
Initialize both pointers at starting number n


Why: Start from same position to establish relative speed difference
Move slow one step, fast two steps per iteration


Why: Creates speed differential to detect cycles, same as linked list cycle detection
Check if they meet before reaching 1


Why: Meeting indicates cycle; if not at 1, it's an endless non-happy cycle
Continue until fast reaches 1 or pointers meet


Why: Either we reach happiness (1) or detect we're stuck in cycle
Return whether we ended at 1


Why: Being at 1 means happy; being stuck in cycle means not happy
4. Key Insights & Edge Cases
What Makes It Work:
Every number sequence either reaches 1 or enters a cycle (proven mathematically)
No sequence grows infinitely - sum of squared digits decreases for large numbers
Fast/slow guarantees cycle detection without extra space
Implementation Gotchas:
Use digit ** 2 or digit * digit, not Math.pow in Python
Must call getNext(slow) and getNext(fast), not getNext(n) repeatedly
While condition can be fast != 1 or slow != 1 (either works)
Check slow == 1 at end, not fast != 1 in the loop condition
Extract ALL digits with modulo loop, not just one
Edge Cases:
n = 1 (already happy)
Single digit numbers
Numbers that quickly reach 1
Numbers that enter common cycles (like 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4)
5. Pseudocode
function isHappy(n):
    slow = n
    fast = n
    
    while fast != 1:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
        
        if slow == fast:
            break
    
    return slow == 1

function getNext(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10
    
    return total

6. Complexity Analysis
Time Complexity: O(log n)
Each transformation reduces number of digits (sum of squared digits is smaller for large numbers)
Cycle detection takes at most O(k) where k is cycle length
Upper bound on cycle length is based on number of possible sums for digits
Overall logarithmic in the input value
Space Complexity: O(1)
Only using two pointer variables (slow, fast)
No hash set or additional data structures
Alternative hash set approach would be O(k) where k is numbers seen before cycle
"""
