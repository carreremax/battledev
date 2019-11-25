# Exercice 1

import sys


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

ages = [int(j) for j in lines[1].split() if 5 <= int(j) <= 9]
print(len(ages))