def euclidian_dist(items, first_point, second_point):
    x_1 = items[first_point][3]
    x_2 = items[second_point][3]
    y_1 = items[first_point][4]
    y_2 = items[second_point][4]

    x_diff_sqr = (x_1 - x_2) ** 2
    y_diff_sqr = (y_1 - y_2) ** 2

    distance = (x_diff_sqr + y_diff_sqr) ** (1 / 2)

    return distance
