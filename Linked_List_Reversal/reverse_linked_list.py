"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # store the previous node and the current one
        prev = None
        current = head

        while current:
            # save the next node
            next = current.next

            # reverse the pointer
            current.next = prev

            # bring up the prev
            prev = current

            # move up to next
            current = next

        return prev


"""
1. Pattern Recognition
Pattern: In-Place Linked List Reversal (Three Pointers / Iterative Pointer Manipulation)
Key Characteristics:
Need to reverse order of linked list nodes
Must work in-place (O(1) space, no new list)
Requires breaking and reconnecting .next pointers
"Reverse" in problem title for linked list
Similar Problems:
Reverse linked list II (reverse portion between positions)
Reverse nodes in k-group
Swap nodes in pairs
Palindrome linked list (requires reversal of second half)
Reorder list
2. High-Level Approach
Use three pointers to traverse the list while reversing direction of .next pointers. At each node, save the next node to avoid losing it, reverse the current node's pointer to point backward, then advance all pointers forward. Return the new head (which was the old tail).
3. Step-by-Step Logic
Initialize prev to None, current to head


Why: prev represents what should come after current in reversed list; old head becomes new tail pointing to None
While current exists, save current.next in a temp variable


Why: About to break the forward link, need to preserve access to rest of list
Reverse the pointer: set current.next = prev


Why: Make current node point backward instead of forward
Move prev forward to current


Why: For next iteration, current node becomes the "previous" node
Move current forward to saved next


Why: Advance to next node to continue reversal process
Return prev (not current)


Why: When loop ends, current is None, prev is the new head (old tail)
4. Key Insights & Edge Cases
What Makes It Work:
Three pointers maintain enough context to break and rebuild links
Reversing happens node by node in single pass
No recursion or extra space needed
Implementation Gotchas:
Order matters: Must save next BEFORE reversing pointer, or you lose the list
Return prev, not current: current becomes None at end; prev is the new head
Loop condition: while current not while next (handles single node correctly)
Don't initialize next outside loop - crashes on empty list
No need for special edge case checks - the loop handles empty/single node naturally
Edge Cases:
Empty list (head is None) → return None
Single node → return same node
Two nodes → correctly swaps them
5. Pseudocode
function reverseList(head):
    prev = None
    current = head
    
    while current exists:
        next = current.next       // Save next node
        current.next = prev       // Reverse pointer
        prev = current            // Move prev forward
        current = next            // Move current forward
    
    return prev  // New head

6. Complexity Analysis
Time Complexity: O(n)
Single pass through the linked list
Visit each node exactly once
Constant work per node
Space Complexity: O(1)
Only three pointer variables (prev, current, next)
No recursion stack or additional data structures
In-place modification of existing nodes

"""
