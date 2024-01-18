import argparse
import math

def isprime(p):
    for i in range(2, round(math.sqrt(p)) + 1):
        if p%i == 0:
            return False
    else:
        return True

def generateseq(seqtype ,l):
    if l <= 0:
        raise ValueError
    if seqtype == 'fibonacci':
        if l == 1:
            seq = [0]
        else:
            seq = [0,1]
            for i in range(2,l):
                next = seq[i-1] + seq[i-2]
                seq.append(next)
    if seqtype == 'prime':
        seq = []
        p = 2
        while len(seq) < l:
            if isprime(p):
                seq.append(p)
            p += 1
    if seqtype == 'square':
        seq = []
        for i in range(1,l+1):
            seq.append(i**2)
    if seqtype == 'triangular':
        seq = [1]
        triang = 1
        for i in range(2,l+1):
            triang += i
            seq.append(triang)
    if seqtype == 'factorial':
        seq = [1]
        fac = 1
        for i in range(2,l+1):
            fac = i*fac
            seq.append(fac)
    return seq

def main(args):
    return(generateseq(args.sequence, args.length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add sequences.')
    parser.add_argument('--sequence', choices = ['fibonacci', 'prime', 'square', 'triangular', 'factorial'], help = 'type of sequence')
    parser.add_argument('--length', type=int, help = 'length of sequence', default = 1)
    args = parser.parse_args()
    print(main(args))