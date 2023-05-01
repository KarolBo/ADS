from functools import cmp_to_key

def jarvis(points: list) -> list:
    points = [(x, y) for x, y in points]
    p0 = find_bottom_most(points)
    hull = []
    points_set = set(points)

    p = p0
    while True:
        hull.append(p)
        if p != p0:
            points_set.remove(p)
        for point in points_set:
            if hull[-1] == p or get_orientation(hull[-1], p, point) <= 0: # point is more clockwise than p or colinear
                p = point
        if p == p0:
            break

    return hull


###########################################################

def graham_scan(points: list) -> list:
    points = [(x, y) for x, y in points]
    p0 = find_bottom_most(points)
    points.remove(p0)
    hull = [p0]
    points.sort(key=cmp_to_key(lambda p, q: orientation_cmp(p0, p, q)))
    n = len(points)
    i = 0
    while i < n:
        if len(hull) < 2 or get_orientation(hull[-1], hull[-1], points[i]) >= 0:
            hull.append(points[i])
            i += 1
        else:
            hull.pop(-1)
    return hull


###########################################################

def find_bottom_most(points: list) -> list:
    bm = points[0]
    for p in points[1:]:
        if p[1] < bm[1]:
            bm = p
    return bm


# det < 0 -> clockwise
def get_orientation(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])


def orientation_cmp(p0, p, q):
    orientation = get_orientation(p0, p, q)
    if orientation < 0:
        return 1
    if orientation > 0:
        return -1
    if p[0]*p[0] + p[1]*p[1] < q[0]*q[0] + q[1]*q[1]:
        return -1
    return 1

###########################################################

test_input = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
test_output = [[3,5],[0,3],[2,1],[5,0],[3,0],[7,3],[6,1],[4,5],[1,4],[7,2],[4,0],[6,5],[1,2],[5,5],[2,5],[7,4]]

jarvis_output = jarvis(test_input)
print('Jarvis: ', jarvis_output.sort() == test_output.sort())

graham_output = graham_scan(test_input)
print('Graham: ', graham_output.sort() == test_output.sort())