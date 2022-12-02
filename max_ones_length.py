from random import randint

seq = []
for _ in range(10):
    seq.append(randint(0, 1))

max_len = 0
counter = 0
for item in seq:
    if item == 1:
        counter += 1
    elif item == 0:
        counter = 0
    if counter > max_len:
        max_len = counter

seq = ''.join(map(str, seq))
print(max_len)
print(seq.find(max_len * '1'), seq.count(max_len * '1'))
