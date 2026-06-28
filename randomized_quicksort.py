import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", randomized_quicksort(data))