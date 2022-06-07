from point import generate_points, generate_clusters, average_point_position
from useful_stuff import cartesian_distance_between, index_of_smallest_value, plot

def calibrate_positions_of_clusters(points, clusters, assignation_table):
    # Recolocar cada cluster
    for index_of_cluster in range(len(clusters)):
        # assignation_table:
        # índice de assignation_table = índice de points
        # [ 1, 1, 0, 1, 1, 2, 2, 2, ... ]
        point_indices_for_corresponding_cluster = [point_index for point_index,value in enumerate(assignation_table) if value == index_of_cluster]
        points_for_corresponding_cluster: list = [points[point_index] for point_index in point_indices_for_corresponding_cluster]

        average_of_points_for_corresponding_cluster = average_point_position(points_for_corresponding_cluster)

        clusters[index_of_cluster] = average_of_points_for_corresponding_cluster

def assign_cluster_to_each_point(points, clusters, distance_between):
    assignation_table = []

    # Comprobar la distancia de cada punto a cada cluster
    for index_of_point,point in enumerate(points):
        distances = []

        for index_of_cluster,cluster in enumerate(clusters):
            distance = distance_between(point, cluster) 
            distances.append(distance)

            # calcular distancias

        cluster_index = index_of_smallest_value(distances)
        assignation_table.append(cluster_index)

    return assignation_table

def get_clusters_by_kmeans(points: list, clusters: list, distance_function, k=2, iterations=10):
    if iterations == 0:
        return clusters

    # Input the index of a point, get the index of the cluster assigned
    # assignation_table[index_of_point] -> index_of_corresponding_cluster
    assignation_table = assign_cluster_to_each_point(points, clusters, distance_function)

    calibrate_positions_of_clusters(points, clusters, assignation_table)

    plot(points, clusters, should_show_images=True, should_save_images=True)

    # Re-ejecutar la función con nuevos clusters
    return get_clusters_by_kmeans(points, clusters, distance_function, iterations=iterations-1)
    

def main(amount_of_points, k, distance_function):
    points = generate_points(amount_of_points)
    clusters = generate_clusters(points, k)

    clusters = get_clusters_by_kmeans(points, clusters, distance_function, k)

    plot(points, clusters, should_show_images=True, should_save_images=False)

if __name__ == "__main__": 
    amount_of_points = 10
    k = 2
    distance_function = cartesian_distance_between

    main(amount_of_points, k, distance_function)
