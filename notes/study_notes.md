# LeetCode Study Notes

This document contains important concepts, algorithms, and data structures for LeetCode problems.

## 📚 Data Structures

### Arrays
- **Time Complexity**: Access O(1), Search O(n), Insert/Delete O(n)
- **Space Complexity**: O(n)
- **Key Concepts**:
  - Index-based access
  - Contiguous memory
  - Fixed size (in some languages)

### Hash Tables (Hash Maps)
- **Time Complexity**: Average O(1) for all operations
- **Space Complexity**: O(n)
- **Key Concepts**:
  - Key-value pairs
  - Hash function
  - Collision resolution
  - Load factor

### Linked Lists
- **Time Complexity**: Access O(n), Search O(n), Insert/Delete O(1) at head/tail
- **Space Complexity**: O(n)
- **Key Concepts**:
  - Node structure (value + pointer)
  - Head and tail pointers
  - Fast insertions/deletions
  - No random access

### Stacks
- **Time Complexity**: Push/Pop O(1), Search O(n)
- **Space Complexity**: O(n)
- **Key Concepts**:
  - LIFO (Last In, First Out)
  - Top pointer
  - Common operations: push, pop, peek, isEmpty

### Queues
- **Time Complexity**: Enqueue/Dequeue O(1), Search O(n)
- **Space Complexity**: O(n)
- **Key Concepts**:
  - FIFO (First In, First Out)
  - Front and rear pointers
  - Common operations: enqueue, dequeue, peek, isEmpty

### Trees
- **Time Complexity**: Search/Insert/Delete O(log n) for balanced trees
- **Space Complexity**: O(n)
- **Key Concepts**:
  - Root, parent, child, leaf nodes
  - Height and depth
  - Traversal methods (inorder, preorder, postorder, level-order)

### Graphs
- **Time Complexity**: Varies by algorithm
- **Space Complexity**: O(V + E)
- **Key Concepts**:
  - Vertices and edges
  - Directed vs undirected
  - Weighted vs unweighted
  - Adjacency list vs adjacency matrix

### Heaps (Priority Queues)
- **Time Complexity**: Insert/Delete O(log n), Get min/max O(1)
- **Space Complexity**: O(n)
- **Key Concepts**:
  - Complete binary tree
  - Min-heap vs max-heap
  - Heapify operations

## 🔧 Algorithms

### Two Pointers
- **Use Cases**: Array problems, palindrome checks, sorted array operations
- **Pattern**: Use two indices to traverse array from different positions
- **Examples**: Two Sum II, Valid Palindrome, Container With Most Water

### Sliding Window
- **Use Cases**: Subarray/substring problems with fixed or variable size
- **Pattern**: Maintain a window and slide it through the array
- **Examples**: Longest Substring Without Repeating Characters, Minimum Window Substring

### Binary Search
- **Use Cases**: Sorted arrays, finding specific values or conditions
- **Pattern**: Divide search space in half each iteration
- **Time Complexity**: O(log n)
- **Examples**: Binary Search, Search in Rotated Sorted Array

### Depth-First Search (DFS)
- **Use Cases**: Tree/graph traversal, backtracking, path finding
- **Pattern**: Explore as far as possible along each branch
- **Implementation**: Recursive or iterative with stack
- **Examples**: Number of Islands, Word Search

### Breadth-First Search (BFS)
- **Use Cases**: Level-order traversal, shortest path, graph exploration
- **Pattern**: Explore all neighbors at current depth before moving deeper
- **Implementation**: Queue-based
- **Examples**: Binary Tree Level Order Traversal, Word Ladder

### Dynamic Programming
- **Use Cases**: Optimization problems, overlapping subproblems
- **Pattern**: Break down into smaller subproblems and store results
- **Types**: 1D DP, 2D DP, memoization vs tabulation
- **Examples**: Climbing Stairs, House Robber, Longest Common Subsequence

### Backtracking
- **Use Cases**: Permutations, combinations, constraint satisfaction
- **Pattern**: Try choices, backtrack when constraints violated
- **Implementation**: Recursive with state management
- **Examples**: Subsets, Permutations, N-Queens

### Greedy
- **Use Cases**: Optimization problems with local optimal choices
- **Pattern**: Make locally optimal choice at each step
- **Examples**: Jump Game, Gas Station, Lemonade Change

## 🎯 Common Patterns

### Array Manipulation
1. **Prefix Sum**: Precompute cumulative sums for range queries
2. **Kadane's Algorithm**: Maximum subarray sum
3. **Dutch National Flag**: Three-way partitioning
4. **Cyclic Sort**: Sort array with elements in range [1, n]

### String Manipulation
1. **Anagram Detection**: Sort or count characters
2. **Palindrome**: Two pointers from ends
3. **Substring Search**: Sliding window or KMP algorithm
4. **String Matching**: Regular expressions or custom logic

### Tree Traversal
1. **Inorder**: Left → Root → Right (gives sorted order for BST)
2. **Preorder**: Root → Left → Right (useful for serialization)
3. **Postorder**: Left → Right → Root (useful for deletion)
4. **Level-order**: BFS with queue

### Graph Algorithms
1. **Topological Sort**: DFS with cycle detection
2. **Shortest Path**: Dijkstra's, Bellman-Ford, Floyd-Warshall
3. **Minimum Spanning Tree**: Kruskal's, Prim's
4. **Strongly Connected Components**: Tarjan's algorithm

## 📝 Problem-Solving Framework

### 1. Understand the Problem
- Read carefully and identify inputs/outputs
- Clarify edge cases and constraints
- Ask clarifying questions if needed

### 2. Plan the Solution
- Identify the appropriate data structure
- Choose the right algorithm/pattern
- Consider time and space complexity
- Plan for edge cases

### 3. Implement
- Write clean, readable code
- Use meaningful variable names
- Add comments for complex logic
- Test with examples

### 4. Test and Optimize
- Test with edge cases
- Analyze time/space complexity
- Look for optimization opportunities
- Consider alternative approaches

## 🔍 Common Mistakes to Avoid

1. **Not reading the problem carefully** - Miss important constraints
2. **Jumping to code too quickly** - Plan first, code second
3. **Ignoring edge cases** - Empty arrays, single elements, etc.
4. **Not considering space complexity** - Memory constraints matter
5. **Over-engineering** - Start simple, optimize if needed
6. **Not testing thoroughly** - Test with multiple examples

## 📚 Resources for Learning

### Websites
- [LeetCode](https://leetcode.com/) - Practice problems
- [NeetCode](https://neetcode.io/) - Video explanations
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Algorithm tutorials
- [HackerRank](https://www.hackerrank.com/) - Additional practice

### Books
- "Cracking the Coding Interview" by Gayle McDowell
- "Introduction to Algorithms" by CLRS
- "Algorithm Design Manual" by Steven Skiena

### YouTube Channels
- NeetCode
- Back To Back SWE
- Abdul Bari
- mycodeschool

---

*Last updated: [Current Date]*
