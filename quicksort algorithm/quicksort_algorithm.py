def quick_sort(numbers):
    # Base case
    if len(numbers) <= 1:
        return numbers

    # Choose the first element as the pivot
    pivot = numbers[0]

    # Partition the list
    less_than_pivot = [num for num in numbers if num < pivot]
    equal_to_pivot = [num for num in numbers if num == pivot]
    greater_than_pivot = [num for num in numbers if num > pivot]

    # Recursively sort and combine
    return (
        quick_sort(less_than_pivot)
        + equal_to_pivot
        + quick_sort(greater_than_pivot)
    )