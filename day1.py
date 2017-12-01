

def sum_pairs(seq, shift):
    sum = 0
    seq_shift = seq[shift:] + seq[:shift]
    for pair in zip(seq, seq_shift):
        if pair[0] == pair[1]:
            sum += int(pair[0])
    return sum

def sum_pairs_inc_one(seq):
    return sum_pairs(seq, 1)

def sum_pairs_inc_half(seq):
    half = len(seq) / 2
    return sum_pairs(seq, half)
