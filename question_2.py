def is_same_line(p1, p2, check):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m * p1[0]
    y = m * check[0] + c
    check.append(y)
    return is_colinear(p1, p2, check)


def is_colinear(p1, p2, check):
    area = (p1[0] * (p2[1] - check[1])) + (p2[0] * (check[1] - p1[1])) + (check[0] * (p1[1] - p2[1]))
    if area == 0:
        return True
    return False


def main_logic(buildings, source):
    p2 = buildings[1][-1]
    check = [4]
    if is_same_line(source, p2, check):
        l1 = abs(abs(buildings[1][2][0]) - abs(buildings[1][0][0]))
        l2 = abs(abs(buildings[1][1][1]) - abs(buildings[1][0][1]))
        l3 = abs(abs(check[1]) - abs(buildings[0][0][1]))
        l4 = abs(abs(check[0]) - abs(buildings[0][2][0]))
        return l1 + l2 + l3 + l4


if __name__ == '__main__':
    buildings = [
        [[4, 0], [4, -5], [7, -5], [7, 0]],
        [[0.4, -2], [0.4, -5], [2.5, -5], [2.5, -2]]
    ]
    source = [-3.5, 1]
    length = main_logic(buildings, source)
    print(length)
