from random import randint
from time import time


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    pivot_idx = randint(0, len(arr)-1)
    pivot = arr[pivot_idx]
    less_or_equal = [elem for i, elem in enumerate(arr) if i != pivot_idx and elem <= pivot]
    greater = [elem for i, elem in enumerate(arr) if i != pivot_idx and elem > pivot]
    return quick_sort(less_or_equal) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    MAX_NUM = 10**5
    # numbers = [randint(0, MAX_NUM) for _ in range(randint(0, MAX_NUM))]
    numbers = [randint(0, MAX_NUM) for _ in range(MAX_NUM)]

    t0 = time()
    quick_sort(numbers)
    time1 = time() - t0
    print(time1)

    t0 = time()
    sorted(numbers)
    time2 = time() - t0
    print(time() - t0)

    print(time1/time2)

