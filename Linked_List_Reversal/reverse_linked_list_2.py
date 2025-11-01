"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # draw this out but its 3 phases and need to keep track of 4 nodes
        # the before left node, the left position node, the right position node,
        # and the after right node.
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 <- 3 <- 4 -> 5 reverse step
        # 1 -> 4 -> 3 -> 2 -> 5 reconnect step

        # Phase 1 find the before reversal point
        # use dummy to handle edge cases
        dummy = ListNode(0, head)
        before_left = dummy
        # 1 indexed positons
        for i in range(1, left):
            before_left = before_left.next

        # Phase 2 reverse
        tail = before_left.next
        prev = None
        current = before_left.next
        for i in range(right - left + 1):
            next = current.next
            current.next = prev
            prev = current
            current = next

        # Phase 3 find the after reversal point and reconnect
        # using what we stored to reconnect
        tail.next = current
        before_left.next = prev
        return dummy.next


"""
1. Pattern Recognition
Pattern: In-Place Linked List Reversal (Partial/Bounded Reversal with Reconnection)
Key Characteristics:
Reverse only a portion of linked list (between two positions)
Must preserve connections before and after reversed section
In-place modification with O(1) space
Problem mentions reversing "from position X to Y"
Similar Problems:
Reverse entire linked list
Reverse nodes in k-group
Swap nodes in pairs
Rotate list
Reorder list
2. High-Level Approach
Use a dummy node to handle edge cases, then find the node before the reversal point. Reverse the sublist between left and right positions using standard three-pointer technique, while tracking the tail of the reversed section. Finally, reconnect the reversed portion to the rest of the list by pointing the before node to the new head and the tail to the node after the reversed section.
3. Step-by-Step Logic
Create dummy node pointing to head


Why: Handles edge case where left=1 (reversing from head); provides stable anchor for reconnection
Traverse to node before position left


Why: Need reference to node before reversal to reconnect later; dummy allows this to work even when left=1
Save the tail before starting reversal


Why: The node at position left becomes the tail of reversed section; need reference to reconnect its next pointer later
Reverse nodes from position left to right using three pointers


Why: Standard reversal technique applied to subset; iterate exactly (right-left+1) times to reverse correct range
After reversal, reconnect before_left to new head of reversed section


Why: Links the part before reversal to the now-reversed portion
Reconnect tail to the node after the reversed section


Why: Links the end of reversed portion to the rest of the list; current pointer is already at this position after loop
Return dummy.next as new head


Why: Actual head may have changed if left=1; dummy.next always points to correct head
4. Key Insights & Edge Cases
What Makes It Work:
Dummy node eliminates special case handling for reversing from head
Saving tail reference before reversal allows proper reconnection afterward
After reversal loop, current naturally points to node after reversed section
Standard three-pointer reversal works on any sublist
Implementation Gotchas:
Positions are 1-indexed not 0-indexed
Save tail before reversal: tail = before_left.next before starting loop
Loop count: Iterate exactly right - left + 1 times (inclusive range)
Reconnection order: tail.next = current not current.next = tail (forward, not backward)
Return dummy.next not head (head may change if left=1)
Range for finding before_left: Use range(1, left) or range(left-1)
Edge Cases:
left = 1 (reverse from head)
left = right (single node, no reversal needed but still works)
Reverse entire list (left=1, right=length)
Two-node list with left=1, right=2
5. Pseudocode
function reverseBetween(head, left, right):
    // Phase 1: Find node before reversal point
    dummy = new Node(0, head)
    before_left = dummy
    
    for i from 1 to left-1:
        before_left = before_left.next
    
    // Phase 2: Reverse sublist
    tail = before_left.next  // Save future tail
    prev = None
    current = before_left.next
    
    for i from 0 to (right - left):
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    // Phase 3: Reconnect
    before_left.next = prev     // Connect to new head of reversed
    tail.next = current         // Connect tail to rest of list
    
    return dummy.next

6. Complexity Analysis
Time Complexity: O(n)
Traverse to position left: O(left)
Reverse (right - left + 1) nodes: O(right - left)
Total single pass through relevant portion: O(n) worst case
Space Complexity: O(1)
Only pointer variables (dummy, before_left, tail, prev, current, next)
In-place modification, no additional data structures
No recursion stack

"""
