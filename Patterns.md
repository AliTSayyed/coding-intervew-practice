# Coding Pattern Reference Guide

## 1. Prefix Sum

**When to Use:**

- Range/Subarray Sum Queries
- Counting Subarrays with a Property
- Multiple Queries on the Same Array
- Balancing/Equilibrium Problems

---

## 2. Two Pointer

**When to Use:**

- Sorted Array or String
- Pairs/Triplets with Conditions
- Palindrome Checking
- Partitioning/Rearranging
- Merging Sorted Sequences

---

## 3. Sliding Window

**When to Use:**

- **Contiguous subarray/substring** (must be consecutive elements)
- **Optimization keywords:** "longest", "shortest", "maximum", "minimum"
- **Constraint on window:** sum, product, character count, distinct elements
- Looking for ALL valid subarrays or ONE optimal subarray

---

## 4. Fast & Slow Pointers

**When to Use:**

- Cycle Detection
- Find Middle Element
- Linked List Positioning
- Palindrome Checking
- Happy Number / Cycle in Sequences

---

## 5. Linked List In-Place Reversal

**When to Use:**

- "Reverse" in the problem
- Reorder/rearrange nodes
- Space constraint O(1)
- Sub-list manipulation

---

## 6. Monotonic Stack

**When to Use:**

- Next Greater/Smaller Element
- Range queries with min/max
- Maintaining order while processing
- Temperature/stock price patterns

---

## 7. Top K Elements

**When to Use:**

- Literally asks for "top k" or "k largest/smallest"
- Partial sorting needed
- Streaming/continuous data
- **Optimization:** O(n log k) better than O(n log n)

---

## 8. Overlapping Intervals

**When to Use:**

- Merge intervals
- Find overlapping intervals
- Minimum meeting rooms
- Insert interval
- Remove overlapping
- **Anything with start/end times, ranges, or segments**

---

## 9. Modified Binary Search

**When to Use:**

- Sorted or rotated sorted array
- Find first/last occurrence
- Minimizing/maximizing with condition
- Kth smallest/largest in sorted structure
- Answer space is searchable
- Search rotated array
- Find boundaries
- Search answer space
- 2D matrix search

---

## 10. Binary Tree Traversal

**When to Use:**

- Binary tree problems
- Tree traversal (preorder, inorder, postorder, level-order)
- Root to leaf paths
- Level by level processing
- Ancestor/descendant relationships
- Path in tree
- Visit all nodes in specific order
- Find paths, sums, depths
- Build/modify tree structure
- Check tree properties

---

## 11. DFS (Depth-First Search)

**When to Use:**

- Graph/Tree exploration problems
- Exhaustive search needed
- Path/route problems
- Grid problems
- Recursive structure
- Need to explore deep before going wide

---

## 12. BFS (Breadth-First Search)

**When to Use:**

- **Keywords:** "shortest path/distance", "minimum steps/moves", "level by level", "nearest/closest", "layer/distance from source"
- Need shortest unweighted path
- Process nodes at same distance together
- Multi-source problems (start from multiple points)
- State-space exploration with minimal steps

---

## 13. Matrix Traversal

**When to Use:**

- **Keywords:** "matrix", "grid", "2D array", "connected cells", "islands/regions", "shortest path in grid", "spiral order", "diagonal traversal"
- Visit all cells with conditions
- Find paths between cells
- Count regions/components
- Transform based on neighbors

---

## 14. Backtracking

**When to Use:**

- **Keywords:** "all combinations/permutations", "generate all", "find all solutions", "subset/partition"
- Constraint satisfaction (Sudoku, N-Queens)
- Explore all possibilities
- **Pattern:** Make choice → explore → undo choice
- Build solution incrementally
- Prune invalid paths early

---

## 15. Dynamic Programming

**When to Use:**

- **Keywords:** "maximum/minimum", "count ways/number of ways", "longest/shortest", "is it possible"
- **Overlapping subproblems** (same calculation repeated)
- **Optimal substructure** (optimal solution uses optimal subsolutions)
- Choices at each step affecting future states
- Can be solved recursively but too slow
