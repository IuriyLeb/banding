import sys

chromosome_length = {}
chromosome_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', 'X', 'Y']
window = int(sys.argv[1])
step = int(window / 10)
start = 1
end = 0
with open('./all_chroms.fa.fai') as file:
    for line in file:
        line = line.strip().split('\t')
        chromosome_length[line[0]] = {}
        chromosome_length[line[0]]['start'] = start
        end = start + int(line[1]) - 1
        chromosome_length[line[0]]['end'] = end

for chromosome in chromosome_names:
    up = chromosome_length['chr{}'.format(chromosome)]['start']
    down = chromosome_length['chr{}'.format(chromosome)]['end']
    result = 0
    while (result + window) < down :
        result = up + window
        print(f"chr{chromosome}\t{up}\t{result}")
        up += step
