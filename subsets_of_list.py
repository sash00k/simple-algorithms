import itertools


def add_bin_one(back_index: int) -> None:
    if abs(back_index) == K+1:
        return
    if mask[back_index] == 0:
        mask[back_index] = 1
    else:
        mask[back_index] = 0
        add_bin_one(back_index=back_index-1)


if __name__ == '__main__':
    K = 5
    sequence = [i for i in range(K)]

    itertools_sol_set = set()
    # itertools solution
    for i in range(1, K+1):
        for subseq in itertools.combinations(sequence, i):
            itertools_sol_set.add(tuple(subseq))

    manual_sol_set = set()
    # manual solution
    mask = [0] * K
    for _ in range(2 ** K - 1):
        add_bin_one(back_index=-1)
        subseq = tuple([elem for elem, cond in zip(sequence, mask) if cond == 1])
        manual_sol_set.add(subseq)

    print(itertools_sol_set == manual_sol_set)




