import sys
import math

N = int(sys.stdin.readline().split(' ')[0])

def main():
    P = readPoints()
    px = sorted(P, key = lambda p: p[0])
    py = sorted(P, key = lambda p: p[1])

    print("%.6f" % closest(px, py, N))
    
def closest(px, py, n):
    if n <= 3:
        shortest = float('inf')
        for p1 in px:
            for p2 in py:
                if p1 != p2:
                    dist = distance(p1,p2)
                    if dist < shortest:
                        shortest = dist
        return shortest            
    else:
        lx, rx = splitList(px)
        limit = lx[-1][0]

        ly, ry = splitBy(limit, py)
        
        #print("Kör algoritmen")
        delta = min(closest(lx, ly, len(lx)), closest(rx, ry, len(rx)))
        sy = list(filter(lambda p: abs(p[0] - limit) < delta, py))
    
        #size = len(sy)
        for i in range(len(sy)):
            #for j in range(i+1, i+2):
                j = i+1
                if j < len(sy):
                    dist = distance(sy[i], sy[j])
                    if dist < delta:
                        delta = dist
        
        return delta

def splitBy(limit, py):
    ly = []
    ry = []
    for p in py:
        if p[0] < limit:
            ly.append(p)
        else:
            ry.append(p)
    return ly, ry

def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx**2 + dy**2)

def readPoints():
    result = []
    for _ in range(N):
        result.append(readPoint())
    return result

def readPoint():
    makeTuple = lambda xs: (int(xs[0]), int(xs[1]))
    return makeTuple(sys.stdin.readline().rstrip().split(' ')) 
    
def splitList(xs):
    half = len(xs)//2
    return xs[:half], xs[half:]  

if __name__ == '__main__':
    main()