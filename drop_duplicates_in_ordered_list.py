arr = [0.1, 0.2, 0.4, 0.4, 0.4, 0.5, 0.5, 0.6, 1.0, 3.1]

result_arr = [arr[0]]
for elem in arr[1:]:
    if elem != result_arr[-1]:
        result_arr.append(elem)

print(result_arr)
