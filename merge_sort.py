from random import randint
from time import time


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    y = merge_sort(arr[:mid])
    z = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


if __name__ == '__main__':
    MAX_NUM = 10**2
    numbers = [randint(0, MAX_NUM) for _ in range(MAX_NUM)]

    t0 = time()
    print(merge_sort(numbers))
    time1 = time() - t0
    print(time1)

    t0 = time()
    print(sorted(numbers))
    time2 = time() - t0
    print(time() - t0)

    print(time1/time2)
