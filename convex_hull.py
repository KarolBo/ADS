from functools import cmp_to_key

def jarvis(points: list) -> list:
    points = [(x, y) for x, y in points]
    p0 = find_leftmost(points)
    hull = []
    points_set = set(points)

    p = p0
    while True:
        hull.append(p)
        if p != p0:
            points_set.remove(p)
        for point in points_set:
            if point == hull[-1]:
                continue
            orientation = get_orientation(hull[-1], p, point)
            d_point = (point[0] - hull[-1][0])**2 + (point[1] - hull[-1][1])**2
            d_p = (p[0] - hull[-1][0])**2 + (p[1] - hull[-1][1])**2

            if hull[-1] == p or orientation < 0 or (orientation == 0 and d_point < d_p): # point is more clockwise than p OR colinear and closer
                p = point

        if p == p0:
            break

    return [[x, y] for x, y in hull]


###########################################################

def graham_scan(points: list) -> list:
    p0 = find_leftmost(points)
    hull = []
    points.sort(key=cmp_to_key(lambda p, q: orientation_cmp(p0, p, q)))

    # handle colinear points at the beggining
    i = 0
    n = len(points)
    while i < (n - 1) and get_orientation(p0, points[i], points[i+1]) == 0:
        i += 1
    points[:i+1] = sorted(points[:i+1], key=lambda p: get_distance(p0, p))

    # main loop
    for p in points:
        while len(hull) > 1 and get_orientation(hull[-2], hull[-1], p) < 0:
            hull.pop(-1)
        hull.append(p)

    return hull

###########################################################

def monotone_chain(points: list[list[int]]) -> list[list[int]]:
    points.sort(key=lambda t: tuple(t))
    upper = []
    lower = []

    for p in points:
      # upper
      while len(upper) > 1 and get_orientation(upper[-2], upper[-1], p) > 0:
        upper.pop(-1)
      upper.append(tuple(p))

      # lower
      while len(lower) > 1 and get_orientation(lower[-2], lower[-1], p) < 0:
        lower.pop(-1)
      lower.append(tuple(p))

    hull = list(set(upper+lower))
    return [[x, y] for x, y in hull]

###########################################################

def find_leftmost(points: list) -> list:
    lm = points[0]
    for p in points[1:]:
        if p[0] < lm[0] or p[0] == lm[0] and p[1] < lm[1]:
            lm = p
    return lm


# det < 0 -> clockwise
def get_orientation(p, q, r):
    px = q[0] - p[0]
    py = q[1] - p[1]
    qx = r[0] - q[0]
    qy = r[1] - q[1]
    return (px * qy) - (py * qx)


def orientation_cmp(p0, p, q):
    orientation = get_orientation(p0, p, q)
    if orientation < 0:
        return 1
    elif orientation > 0:
        return -1

    return get_distance(p0, q) - get_distance(p0, p)
    

def get_distance(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

###########################################################

test_input = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
test_output = [[3,5],[0,3],[2,1],[5,0],[3,0],[7,3],[6,1],[4,5],[1,4],[7,2],[4,0],[6,5],[1,2],[5,5],[2,5],[7,4]]

jarvis_output = jarvis(list(test_input))
print('Jarvis: ', sorted(jarvis_output) == sorted(test_output))

graham_output = graham_scan(list(test_input))
print('Graham: ', sorted(graham_output) == sorted(test_output))

andrews_output = monotone_chain(list(test_input))
print('Andrew: ', sorted(andrews_output) == sorted(test_output))
