import sys
seq = ''


def find_pattern(number_of_chromosome, sequence, pattern='T', lendth=13):
    position = 0
    while position < len(sequence):
        if sequence[position:position+lendth] == pattern*lendth:
            print(number_of_chromosome, '\t', position+1, end='\t')
            while sequence[position:position+lendth] == pattern*lendth and \
                    (sequence[position+lendth+1] == pattern and position+lendth+2 < len(sequence)):
                lendth += 1
            print(position+lendth+1)
            lendth = 13
            position = position + lendth
        else:
            position += 1


with open('./chr{}.fa'.format(sys.argv[1])) as file:
    for line in file:
        if line[0] == ">":
            number_of_chromosome = line[1:5]
            continue
        else:
            seq += line.strip()
    find_pattern(number_of_chromosome='chr{}'.format(sys.argv[1]), sequence=seq)
