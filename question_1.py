from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def poly(poly_coords, point):
    point = Point(point[0], point[1])
    polygon = Polygon(poly_coords)
    if polygon.contains(point):
        return True
    return False


if __name__ == '__main__':
    # poly_coords = [[1, 0], [8, 3], [8, 8], [1, 5]]
    poly_coords = [
        [-3, 2], [-2, -0.8], [0, 1.2], [2.2, 0], [2, 4.5]
    ]
    point = [0, 0]
    print(poly(poly_coords, point))
