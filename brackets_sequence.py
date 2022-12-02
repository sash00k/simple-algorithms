def generate_sequences(counter, index, sequence):
    if index == K:
        print(''.join(sequence))
    if counter + 1 < K - index:
        sequence[index] = '('
        generate_sequences(counter+1, index+1, sequence)
    if counter > 0:
        sequence[index] = ')'
        generate_sequences(counter-1, index+1, sequence)


if __name__ == '__main__':
    K = 6
    init_sequence = [0] * K
    init_counter = 0
    init_index = 0

    generate_sequences(counter=init_counter,
                       index=init_index,
                       sequence=init_sequence)
