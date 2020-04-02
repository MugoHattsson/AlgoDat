import sys

N = int(sys.stdin.readline())
lines = ' '.join([line.rstrip() for line in sys.stdin]).split(' ')
matrix = []
print(len(lines))

while len(lines) != 0:
    print(len(lines))
    matrix.append(lines[:N+1])
    lines = lines[N+1:]

#print(lines)
print()
#print(matrix)
