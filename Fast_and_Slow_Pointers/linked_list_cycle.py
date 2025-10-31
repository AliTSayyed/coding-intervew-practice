"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # check while there is a current node and the next node exists as well
        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

            if fast == slow:
                return True

        return False

        # O(n) time but O(n) space
        # seen = set()

        # current = head

        # while current is not None:
        #     if current in seen:
        #         return True
        #     seen.add(current)
        #     current = current.next
        # return False


"""
# Linked List Cycle Detection

## 1. Pattern Recognition

**Pattern:** Fast and Slow Pointers (Floyd's Cycle Detection Algorithm)

**Key Characteristics:**
- Detecting cycles in linked list
- Need O(1) space solution
- Two pointers moving at different speeds through same data structure
- Problem involves "catching up" or "meeting point" concept

**Similar Problems:**
- Find cycle start position
- Find middle of linked list
- Happy number problem
- Detect duplicate in array (with constraints)

## 2. High-Level Approach

Use two pointers starting at head: slow moves one step, fast moves two steps. If a cycle exists, fast will eventually catch up to slow (they'll meet). If no cycle, fast reaches the end (None).

## 3. Step-by-Step Logic

1. **Initialize both pointers at head**
   - *Why:* Start from same position to establish relative speed difference

2. **Move slow one step, fast two steps per iteration**
   - *Why:* Creates speed differential where fast gains one position per iteration

3. **Check if pointers meet**
   - *Why:* In a cycle, fast catches slow since it moves faster. Gap closes by 1 each iteration, guaranteeing meeting

4. **If fast reaches None, no cycle exists**
   - *Why:* In non-cyclic list, fast reaches end before catching slow

## 4. Key Insights & Edge Cases

**What Makes It Work:**
- Fast pointer gains exactly one position on slow per iteration
- In a cycle of any size, this guarantees they'll meet
- Fast laps slow at most once before meeting

**Implementation Gotchas:**
- Check `fast and fast.next` not `fast.next.next` (prevents null pointer access)
- Must check both conditions: `fast` could be None, or `fast.next` could be None
- Compare node objects (`slow == fast`), not values

**Edge Cases:**
- Empty list (head is None)
- Single node with no cycle
- Single node pointing to itself
- Two nodes forming cycle
- Cycle at end vs cycle at beginning

## 5. Pseudocode

```
Initialize slow = head, fast = head

while fast exists AND fast.next exists:
    Move slow one step forward
    Move fast two steps forward
    
    if slow == fast:
        return True (cycle detected)

return False (reached end, no cycle)
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Non-cyclic: fast reaches end in n/2 steps
- Cyclic: fast catches slow within one lap of cycle, which is at most n steps
- Linear traversal in both cases

**Space Complexity:** O(1)
- Only two pointer variables used
- No additional data structures (vs O(n) for hash set approach)
"""
