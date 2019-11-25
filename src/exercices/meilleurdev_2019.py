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
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

prim_nb = [2,3,5,7,11]
res = set()
for i in lines[1:]:
    val = int(i)
    for col in prim_nb:
        if val%col ==0:
            res.add(col)
res = list(res)
res.sort()
ret = ""
for val in res:
    ret = ret+str(val)+" "
print(ret)

# exercice 4
import sys


def DEBUG(to_print):
    sys.stderr.write(str(to_print) + '\n')


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

bug = [l for l in lines[1].split()]
DEBUG(bug)
re = [l for l in lines[2].split()]
DEBUG(re)
res = ""
for l in lines[3]:
    if l.lower() in bug:
        if l.isupper():
            res = res + re[bug.index(l.lower())].upper()
        else:
            res = res + re[bug.index(l.lower())]
    else:
        res = res + l

print(res)

# exercice 5