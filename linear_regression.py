def get_y(m, b, x):
    y = m*x + b
    return y
# print(get_y(1, 0, 7) == 7)
# print(get_y(5, 10, 3) == 25)

def calculate_error(m, b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y - y_point)
    return distance
# print(calculate_error(1, 0, (3, 3)))
# print(calculate_error(1, 0, (3, 4)))
# print(calculate_error(1, -1, (3, 3)))
# print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
def calculate_all_error(m, b, points):
    error = 0
    for point in points:
        error = calculate_error(m, b, point)
    return error
# print(calculate_all_error(1, 0, datapoints))
# print(calculate_all_error(1, 1, datapoints))
# print(calculate_all_error(1, -1, datapoints))
# print(calculate_all_error(-1, 1, datapoints))

