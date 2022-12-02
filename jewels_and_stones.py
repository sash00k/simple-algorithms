J = 'abcdefg'  # jewels
S = 'efkioph'  # stones

S = set(S)

counter = 0
for item in J:
    if item in S:
        counter += 1

print(counter)



