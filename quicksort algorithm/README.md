# Quick Sort Algorithm

## Overview

This folder contains an implementation of the Quick Sort algorithm in Python. Quick sort is a fast, efficient, and widely used sorting algorithm based on the divide-and-conquer approach.

## What is Quick Sort?

Quick sort works by:

1. Selecting a pivot element
2. Partitioning the array into elements smaller than the pivot and larger than the pivot
3. Recursively sorting the sub-arrays on both sides of the pivot

## Algorithm Characteristics

| Property                   | Value                 |
| -------------------------- | --------------------- |
| Time Complexity            | O(n log n) on average |
| Worst-Case Time Complexity | O(n²)                 |
| Space Complexity           | O(log n) average      |
| Stability                  | No                    |
| In-place                   | Yes                   |
| Recursive                  | Yes                   |

## How It Works

### Step-by-Step Process:

1. Pick a pivot value from the array
2. Rearrange the array so that:
   - elements less than the pivot come before it
   - elements greater than the pivot come after it
3. Recursively apply the same process to the left and right partitions
4. Combine the results to get the sorted array

### Example:

```python
numbers = [10, 7, 8, 9, 1, 5]
```

Pivot: 10

Partition:

```python
[7, 8, 9, 1, 5] + [10] + []
```

Final sorted output:

```python
[1, 5, 7, 8, 9, 10]
```

## Implementation Details

### Function: `quick_sort(numbers)`

This function sorts a list of numbers using recursive quick sort.

**Parameters:**

- `numbers` (list): The list to be sorted

**Returns:**

- A new sorted list

### Key Components:

- **Pivot Selection**: The first element is chosen as the pivot
- **Partitioning**: Elements are split into smaller-than-pivot, equal-to-pivot, and greater-than-pivot groups
- **Recursion**: Each partition is sorted independently

## Usage

### Running the Script:

```bash
python quicksort_algorithm.py
```

### Example Usage:

```python
from quicksort_algorithm import quick_sort

numbers = [12, 4, 5, 6, 7, 3, 1, 15]
result = quick_sort(numbers)
print(result)
```

### Expected Output:

```python
[1, 3, 4, 5, 6, 7, 12, 15]
```

## Advantages

✅ Fast on average for large datasets  
✅ Uses less memory than merge sort in many cases  
✅ Efficient divide-and-conquer approach  
✅ Good general-purpose sorting algorithm

## Disadvantages

❌ Worst-case performance can be O(n²)  
❌ Not stable  
❌ Performance depends on pivot choice

## When to Use Quick Sort

- When sorting large datasets efficiently
- When in-place sorting is preferred
- When average-case performance matters more than worst-case guarantees

## Notes

- This implementation uses the first element as the pivot
- It creates new lists during partitioning
- The function returns a sorted list rather than modifying the original list in-place

## Further Reading

- [Quick Sort on Wikipedia](https://en.wikipedia.org/wiki/Quicksort)
- [Sorting Algorithm Visualizations](https://www.sorting-algorithms.com/quick-sort)

---

**Created**: 2026-09-01  
**Language**: Python 3.x  
**Type**: Educational Algorithm Implementation
