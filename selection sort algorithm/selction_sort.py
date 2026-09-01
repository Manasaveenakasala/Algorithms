def selection_sort(items):
    for i in range(len(items)):
        min_index = i

        # Find the smallest item in the unsorted portion
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        # Swap only if the smallest item is not already in position
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]

    return items