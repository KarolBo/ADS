def jarvis(points: list) -> list:
    points = [(x, y) for x, y in points]
    p0 = find_bottom_most(points)
    hull = []
    points_set = set(points)
    n = len(points)

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

def find_bottom_most(points: list) -> list:
    bm = points[0]
    for p in points[1:]:
        if p[1] < bm[1]:
            bm = p
    return bm


# det < 0 -> clockwise
def get_orientation(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])


###########################################################

test_input = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
test_output = [[1,1],[2,0],[4,2],[3,3],[2,4]]
output = jarvis(test_input)
print(output.sort() == test_output.sort())