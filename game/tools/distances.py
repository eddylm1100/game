import math

__version__="0.0.1"


def euclidian_distance(p1:tuple, p2: tuple) -> float:
    return math.dist(p1, p2)

def manhattan_distance(p1,p2) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
    
print("Achtung! Das hier wird auch ausgegeben!")