

print(ord('a'))

#EXERcice 2
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def is_voyelle(l):
    end_letter = ['a', 'e', 'i', 'o', 'u', 'y']
    return l in end_letter


def mot_magique(word):
    if 5 <= len(word) <= 7:
        if is_voyelle(word[-1]):
            if ord(word[0]) + 1 == ord(word[1]):
                return True
    return False


nb_word = 0
words_seen = []
for word in lines[1:]:
    if mot_magique(word) and word not in words_seen:
        nb_word += 1
        words_seen.append(word)
print(nb_word)

# exercice 3

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])
target = N / 2
x = 0
vals = [int(i) for i in lines[1].split()]
for i in range(len(vals[:-1])):
    val = vals[i]
    val_n = vals[i + 1]
    if val == target and val_n == target:
        x = "INF"
        break
    if val == target or (val < target and val_n > target) or (val > target and val_n < target):
        x += 1
if val_n == target and (x != "INF"):
    x += 1
print(x)