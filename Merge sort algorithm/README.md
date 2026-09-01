# Merge Sort Algorithm

## Overview

This repository contains an implementation of the **Merge Sort** algorithm in Python. Merge sort is a highly efficient, stable, and divide-and-conquer sorting algorithm that guarantees consistent performance.

## What is Merge Sort?

Merge sort is a sorting algorithm that works by:

1. **Dividing** the array into two halves
2. **Recursively** sorting each half
3. **Merging** the sorted halves back together in sorted order

## Algorithm Characteristics

| Property             | Value                                        |
| -------------------- | -------------------------------------------- |
| **Time Complexity**  | O(n log n) - Best, Average, and Worst case   |
| **Space Complexity** | O(n) - Requires additional space for merging |
| **Stability**        | Yes - Equal elements maintain relative order |
| **In-place**         | No - Requires extra memory                   |
| **Recursive**        | Yes                                          |

## How It Works

### Step-by-Step Process:

1. **Base Case**: If the array has 1 or fewer elements, it's already sorted
2. **Divide**: Split the array at the middle point
3. **Conquer**: Recursively sort the left and right halves
4. **Merge**: Combine the two sorted halves into a single sorted array

### Example:

```
Input:  [4, 10, 6, 14, 2, 1, 8, 5]

Divide:
        [4, 10, 6, 14] | [2, 1, 8, 5]
        [4, 10] [6, 14] | [2, 1] [8, 5]
        [4] [10] [6] [14] | [2] [1] [8] [5]

Merge:
        [4, 10] [6, 14] | [1, 2] [5, 8]
        [4, 6, 10, 14] | [1, 2, 5, 8]

Output: [1, 2, 4, 5, 6, 8, 10, 14]
```

## Implementation Details

### Function: `merge_sort(array)`

Sorts an array in-place using the merge sort algorithm.

**Parameters:**

- `array` (list): The list to be sorted

**Returns:**

- None (modifies the array in-place)

### Key Components:

- **Divide Phase**: Splits array into two halves using the middle point
- **Merge Phase**: Combines two sorted subarrays while maintaining order
- Three merge loops handle remaining elements from left and right subarrays

## Usage

### Running the Script:

```bash
python merge_sort_algorithm.py
```

### Expected Output:

```
Unsorted array:
[4, 10, 6, 14, 2, 1, 8, 5]
```

### Using in Your Code:

```python
from merge_sort_algorithm import merge_sort

# Create an array
numbers = [4, 10, 6, 14, 2, 1, 8, 5]

# Sort the array (in-place)
merge_sort(numbers)

# Print the sorted result
print(numbers)  # Output: [1, 2, 4, 5, 6, 8, 10, 14]
```

## Advantages

✅ **O(n log n)** guaranteed performance in all cases  
✅ **Stable** - preserves relative order of equal elements  
✅ **Predictable** - no worst-case scenarios  
✅ **Parallelizable** - can be optimized for parallel processing

## Disadvantages

❌ **Space Complexity** - requires O(n) extra space  
❌ **Not in-place** - additional memory overhead  
❌ **Slower on small datasets** - compared to insertion sort or quicksort

## Comparison with Other Sorting Algorithms

| Algorithm      | Best       | Average    | Worst      | Space    | Stable |
| -------------- | ---------- | ---------- | ---------- | -------- | ------ |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |

## When to Use Merge Sort

- When **consistent O(n log n)** performance is critical
- When **stability** is required
- When you have **sufficient extra memory** available
- For **external sorting** (sorting data that doesn't fit in memory)
- In **multi-threaded** environments with parallelization

## Notes

- The current implementation modifies the input array in-place
- This implementation is optimal for educational purposes
- For production use, consider Python's built-in `sorted()` which uses Timsort
- The algorithm uses standard Python list slicing and indexing

## Further Reading

- [Merge Sort on Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
- [Merge Sort Visualization](https://www.visualgo.net/en/sorting)

---

**Created**: 2026-09-01  
**Language**: Python 3.x  
**Type**: Educational Algorithm Implementation
