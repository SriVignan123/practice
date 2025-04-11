"""
sorts.py
---------
Contains:
- Insertion Sort
- Merge Sort
- Quick Sort (with safe pivot)
- Hybrid Quick-Insertion Sort
"""

def insertion_sort(an_array):
    """
    Performs insertion sort.
    
    Parameters:
        an_array (list): The list to sort.
        
    Returns:
        list: Sorted list.
    """
    for i in range(1, len(an_array)):
        key = an_array[i]
        j = i - 1
        while j >= 0 and an_array[j] > key:
            an_array[j + 1] = an_array[j]
            j -= 1
        an_array[j + 1] = key
    return an_array

def merge_sort(an_array):
    """
    Performs merge sort.
    
    Parameters:
        an_array (list): The list to sort.
        
    Returns:
        list: Sorted list.
    """
    if len(an_array) < 2:
        return an_array
    mid = len(an_array) // 2
    left = merge_sort(an_array[:mid])
    right = merge_sort(an_array[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into one.
    
    Parameters:
        left (list): Left half.
        right (list): Right half.
        
    Returns:
        list: Merged and sorted result.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result



def quick_sort(an_array):
    import random
    """
    Performs quick sort using a random pivot to avoid stack overflow on sorted arrays.
    
    Parameters:
        an_array (list): The list to sort.
        
    Returns:
        list: Sorted list.
    """
    if len(an_array) < 2:
        return an_array

    pivot = random.choice(an_array)  # ✅ Random pivot is more robust
    less = [x for x in an_array if x < pivot]
    equal = [x for x in an_array if x == pivot]
    greater = [x for x in an_array if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


def quick_insertion_sort(an_array):
    """
    Hybrid quick + insertion sort.
    Uses insertion sort for small subarrays to improve performance.
    
    Parameters:
        an_array (list): The list to sort.
        
    Returns:
        list: Sorted list.
    """
    if len(an_array) < 2:
        return an_array

    # Use insertion sort for small arrays
    if len(an_array) < 20:
        return insertion_sort(an_array)

    pivot = an_array[len(an_array) // 2]
    less = [x for x in an_array if x < pivot]
    equal = [x for x in an_array if x == pivot]
    greater = [x for x in an_array if x > pivot]

    return quick_insertion_sort(less) + equal + quick_insertion_sort(greater)
