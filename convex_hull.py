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
    points = [(x, y) for x, y in points]
    p0 = find_leftmost(points)
    points.remove(p0)
    hull = [p0]
    points.sort(key=cmp_to_key(lambda p, q: orientation_cmp(p0, p, q)))
    n = len(points)
    i = 0
    while i < n:
        if len(hull) < 2 or get_orientation(hull[-2], hull[-1], points[i]) >= 0:
            hull.append(points[i])
            i += 1
        else:
            hull.pop(-1)
    return [[x, y] for x, y in hull]


###########################################################

def find_leftmost(points: list) -> list:
    lm = points[0]
    for p in points[1:]:
        if p[1] < lm[1] or p[1] == lm[1] and p[0] < lm[0]:
            lm = p
    return lm


# det < 0 -> clockwise
def get_orientation(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])


def orientation_cmp(p0, p, q):
    orientation = get_orientation(p0, p, q)
    if orientation < 0:
        return 1
    if orientation > 0:
        return -1
    factor = 1 if p[0] <= p0[0] else -1 # on the right of p0 the nearest are first, on the left the othey way round
    if (p[0] - p0[0])**2 + (p[1] - p0[1])**2 > (q[0] - p0[0])**2 + (q[1] - p0[1])**2:
        return -factor
    return factor

###########################################################

test_input = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1]]
test_output = [[4,0],[1,3],[2,5],[6,5],[2,1],[5,0],[6,1],[1,4],[3,0],[1,2],[5,5],[7,2],[7,4],[7,3],[3,5],[4,5]]

jarvis_output = jarvis(test_input)
print('Jarvis: ', sorted(jarvis_output) == sorted(test_output))

graham_output = graham_scan(test_input)
print('Graham: ', sorted(graham_output) == sorted(test_output))