"""
sort_times.py
Compares sorting algorithm performance by timing them on random and sorted arrays.
"""

import time
import random
from sorts import insertion_sort, merge_sort, quick_sort, quick_insertion_sort

# Sizes of arrays to test for performance
SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def sort_function_timer(sort_function, an_array):
    """
    Times how long a given sorting function takes to run on a specific array.

    Parameters:
        sort_function (function): The sorting algorithm to test.
        an_array (list): The input list to be sorted.

    Returns:
        float: Time taken in seconds.
    """
    start = time.time()  # Start timer
    sort_function(an_array)  # Execute the sort
    end = time.time()  # End timer
    return end - start  # Calculate elapsed time

def print_sort_time_using_random_arrays(sort_function):
    """
    Prints the time taken to sort random arrays of increasing size using the given sort function.

    Parameters:
        sort_function (function): The sorting function to evaluate.
    """
    print(f"\nTiming {sort_function.__name__} on random arrays:")
    for size in SIZES:
        # Generate a random array of given size with values 1-10000
        arr = [random.randint(1, 10000) for _ in range(size)]
        elapsed = sort_function_timer(sort_function, arr)
        print(f"Size {size}: {elapsed:.6f} seconds")

def print_sort_time_using_sorted_arrays(sort_function):
    """
    Prints the time taken to sort pre-sorted (ascending) arrays of increasing size.

    Parameters:
        sort_function (function): The sorting function to evaluate.
    """
    print(f"\nTiming {sort_function.__name__} on sorted arrays:")
    for size in SIZES:
        arr = list(range(size))  # Pre-sorted array
        elapsed = sort_function_timer(sort_function, arr)
        print(f"Size {size}: {elapsed:.6f} seconds")

def main():
    """
    Runs timing tests for each sorting algorithm using both random and sorted arrays.
    """
    # Test on randomly generated arrays
    print_sort_time_using_random_arrays(insertion_sort)
    print_sort_time_using_random_arrays(merge_sort)
    print_sort_time_using_random_arrays(quick_sort)
    print_sort_time_using_random_arrays(quick_insertion_sort)

    # Test on pre-sorted arrays
    print_sort_time_using_sorted_arrays(insertion_sort)
    print_sort_time_using_sorted_arrays(merge_sort)
    print_sort_time_using_sorted_arrays(quick_sort)
    print_sort_time_using_sorted_arrays(quick_insertion_sort)

# Entry point check
if __name__ == "__main__":
    main()
