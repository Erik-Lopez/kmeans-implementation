import random

from useful_stuff import average

def generate_points(amount_of_points):
    points = []

    for _ in range(amount_of_points):
        point = [random.uniform(0, 10), random.uniform(0, 10)]
        points.append(point)

    return points

def generate_clusters(points, k):
    assert len(points) >= k, "Too many clusters, idiot."

    clusters = [random.choice(points) for _ in range(k)]

    return clusters

def average_point_position(points):
    x_average = average([point[0] for point in points])
    y_average = average([point[1] for point in points])

    return [x_average, y_average]
