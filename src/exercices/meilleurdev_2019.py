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
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def DEBUG(to_print):
    sys.stderr.write(str(to_print) + '\n')


n_part = int(lines[0])
begin = []
end = []
for l in lines[1:]:
    begin.append(int(l.split()[0]))
    end.append(int(l.split()[1]))

begin.sort()
end.sort()

b = 0
e = 0
nb_part = 0
max_part = 0
for i in range(len(begin) + len(end)):
    if b == len(begin):
        break
    if e == len(end):
        for j in range(b, len(begin)):
            nb_part += 1
        if nb_part > max_part:
            max_part = nb_part
        break
    if begin[b] < end[e]:
        nb_part += 1
        b += 1
    else:
        nb_part -= 1
        e += 1
    if nb_part > max_part:
        max_part = nb_part
print(max_part)

# exo 6
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def DEBUG(to_print):
    sys.stderr.write(str(to_print) + '\n')


lin = int(lines[0].split()[0])
stat = int(lines[0].split()[1])

b = int(lines[1].split()[0])
e = int(lines[1].split()[1])

slines = []
for l in lines[3:]:
    slines.append([int(i) for i in l.split()])

graph = [set() for i in range(stat)]
for i in range(len(graph)):
    for slin in slines:
        if i + 1 in slin:
            graph[i] = graph[i].union(set(slin))


def visit_neighbour(i):
    n_s = graph[i - 1]
    for n in n_s:
        if n not in visited and n not in to_visit:
            to_visit2.add(n)


visited = set()
to_visit = [b]
target = e
nb_array = 0
while (len(to_visit) > 0):
    if target in to_visit:
        print(nb_array)
        break
    to_visit2 = set()
    for node in to_visit:
        visit_neighbour(node)
    nb_array += 1
    visited = visited.union(set(to_visit))
    to_visit = list(to_visit2)
    
if len(to_visit) == 0:
    print(-1)
