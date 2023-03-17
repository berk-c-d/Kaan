def euclidean_dist(items, first_point, second_point):
    x1, y1 = items[first_point][3:5]
    x2, y2 = items[second_point][3:5]

    x_diff_sq = (x1 - x2) ** 2
    y_diff_sq = (y1 - y2) ** 2

    distance = (x_diff_sq + y_diff_sq) ** 0.5

    return distance
