from point import generate_points

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

def get_clusters_by_kmeans(points: list, clusters: list, k=2, iterations=100):
    if iterations == 0:
        return clusters

    # Input the index of a point, get the index of the cluster assigned
    # assignation_table[index_of_point] -> index_of_corresponding_cluster
    assignation_table = assign_cluster_to_each_point(points, clusters)

    calibrate_positions_of_clusters(points, clusters, assignation_table)

    # Re-ejecutar la función con nuevos clusters
    get_clusters_by_kmeans(points, clusters, iterations=iterations-1)
    

def main(amount_of_points):
    points = generate_points(amount_of_points)
    clusters = generate_clusters(points)

    clusters = get_clusters_by_kmeans(points, clusters)

if __name__ == "__main__": 
    amount_of_points = 10

    main(amount_of_points)
