# Selection Sort Algorithm

## Overview

This folder contains an implementation of the Selection Sort algorithm in Python. Selection sort is a simple comparison-based sorting algorithm that repeatedly selects the smallest element from the unsorted portion of the list and places it in its correct position.

## What is Selection Sort?

Selection sort works by:

1. Finding the minimum value in the unsorted part of the array
2. Swapping it with the first unsorted element
3. Repeating the process until the entire array is sorted

## Algorithm Characteristics

| Property         | Value |
| ---------------- | ----- |
| Time Complexity  | O(n²) |
| Space Complexity | O(1)  |
| Stability        | No    |
| In-place         | Yes   |
| Recursive        | No    |

## How It Works

### Step-by-Step Process:

1. Assume the first element is the minimum
2. Compare it with the remaining elements
3. If a smaller element is found, update the minimum index
4. Swap the minimum element into its correct position
5. Repeat until the array is sorted

### Example:

```python
items = [29, 10, 14, 37, 13]
```

Pass 1:

- Minimum is 10
- Swap with 29

Result:

```python
[10, 29, 14, 37, 13]
```

Pass 2:

- Minimum is 13
- Swap with 29

Result:

```python
[10, 13, 14, 37, 29]
```

Pass 3:

- Minimum is 14
- Already in place

Final result:

```python
[10, 13, 14, 29, 37]
```

## Implementation Details

### Function: `selection_sort(items)`

This function sorts a list in ascending order using selection sort.

**Parameters:**

- `items` (list): The list to be sorted

**Returns:**

- The sorted list

### Key Components:

- **min_index**: Tracks the index of the smallest element in the unsorted section
- **Nested loop**: Searches the unsorted portion for the minimum value
- **Swap**: Places the minimum value into the correct position

## Usage

### Example Usage:

```python
from selction_sort import selection_sort

numbers = [64, 25, 12, 22, 11]
result = selection_sort(numbers)
print(result)
```

### Expected Output:

```python
[11, 12, 22, 25, 64]
```

## Advantages

✅ Simple and easy to understand  
✅ Performs well for very small datasets  
✅ Uses constant extra space  
✅ Easy to implement in-place

## Disadvantages

❌ Slow for large datasets with O(n²) time complexity  
❌ Not efficient for large lists  
❌ Unstable sorting algorithm

## When to Use Selection Sort

- When the list is very small
- For teaching basic sorting concepts
- When memory usage must be minimal

## Notes

- This implementation sorts in ascending order
- It modifies the list in place and returns the sorted result
- It is not suitable for large datasets when performance matters

## Further Reading

- [Selection Sort on Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)
- [Selection Sort Visualization](https://www.geeksforgeeks.org/selection-sort/)

---

**Created**: 2026-09-01  
**Language**: Python 3.x  
**Type**: Educational Algorithm Implementation
