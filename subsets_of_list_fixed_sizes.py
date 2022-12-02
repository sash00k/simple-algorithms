import itertools


if __name__ == '__main__':
    K = 5
    N = 3
    sequence = [i for i in range(K)]

    for subseq in itertools.combinations(sequence, N):
        print(subseq)




