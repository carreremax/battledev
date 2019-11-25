# Exercice 1

import sys


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

ages = [int(j) for j in lines[1].split() if 5 <= int(j) <= 9]
print(len(ages))

# Exercice 2
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

nb_traj = 0
for l in lines[1:]:
    nb_traj += (int(l) - 1) // 10 + 1 # pour éviter que 10 donne 2, on fait -1, ça donne 9, puis rajoute 1 au résultat

print(nb_traj)

# Exercice 3
