"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""


class Solution:
    def calPoints(self, operations) -> int:
        if not operations:
            return 0

        ret = []

        # loop through opearations and follow instructions per operator
        # if not an operator convert string number to int
        for item in operations:
            if item == "C":
                ret.pop()
            elif item == "D":
                ret.append(ret[-1] * 2)
            elif item == "+":
                ret.append(ret[-1] + ret[-2])
            else:
                ret.append(int(item))

        return sum(ret)


"""
1. Pattern Recognition
Pattern: Stack Simulation
Key Characteristics:
Need to process operations sequentially in order
Operations depend on most recent elements (last 1-2 items)
Need to remove/modify previous results
"Undo" or "look back" operations present (like "C")
Similar Problems:
Valid Parentheses (LC 20)
Min Stack (LC 155)
Evaluate Reverse Polish Notation (LC 150)
Backspace String Compare (LC 844)
Build an Array With Stack Operations (LC 1441)
2. High-Level Approach
Use a stack to maintain valid scores as you process each operation. For special operations (C, D, +), manipulate the stack accordingly; for numeric strings, convert and push to stack. Finally, sum all remaining values in the stack to get the total score.
3. Step-by-Step Logic
Initialize empty stack (list) for scores


WHY: Stack allows O(1) access to most recent scores and easy addition/removal
Iterate through each operation


WHY: Must process operations in order as each depends on previous state
Handle "C" operation: remove last score


WHY: Invalidates previous round, stack.pop() removes most recent entry
Handle "D" operation: double last score and add


WHY: New score is 2× the last valid score, append to maintain history
Handle "+" operation: sum last two scores and add


WHY: New score combines two most recent scores (stack[-1] + stack[-2])
Handle numeric strings: convert to int and add


WHY: Default case - just record the score for this round
Return sum of all scores in stack


WHY: Stack contains all valid, non-cancelled scores after processing
4. Key Insights & Edge Cases
What Makes This Work:
Stack naturally maintains order and provides O(1) access to recent elements
Each operation only needs to look back at most 2 positions
Pop operation handles "undo" elegantly
Final stack contains exactly the valid scores to sum
Important Details:
Must convert numeric strings to integers: int(item)
Use negative indexing for clean access: stack[-1] (last), stack[-2] (second-to-last)
No need to check stack size for "+" or "D" - problem guarantees valid operations
Operations modify stack in-place, maintaining running state
Edge Cases:
Empty operations list: return 0
All scores cancelled out with "C": stack becomes empty, sum = 0
Negative numbers: handled automatically by int() conversion
Single operation: works fine (e.g., just "5" returns 5)
5. Pseudocode
function calPoints(operations):
    if operations is empty:
        return 0
    
    stack = []
    
    for each operation in operations:
        if operation == "C":
            remove last element from stack
        
        else if operation == "D":
            double_score = last element × 2
            add double_score to stack
        
        else if operation == "+":
            sum_score = last element + second-to-last element
            add sum_score to stack
        
        else:  // it's a number string
            convert operation to integer
            add integer to stack
    
    return sum(all elements in stack)

6. Complexity Analysis
Time Complexity: O(n)
n = number of operations
Single pass through operations list: O(n)
Each operation (pop, append, arithmetic) is O(1)
Final sum of stack: O(n) worst case (all scores remain valid)
Total: O(n) + O(n) = O(n)
Space Complexity: O(n)
Stack stores up to n scores in worst case (all numeric operations, no "C")
No additional data structures needed
In best case (many "C" operations), could be O(1), but worst case is O(n)
Why Not Other Patterns:
Don't need two pointers (no searching/comparison)
Don't need hash map (no frequency counting or lookups)
Don't need recursion (linear sequential processing)
Stack is perfect: LIFO matches "most recent score" requirements

"""
