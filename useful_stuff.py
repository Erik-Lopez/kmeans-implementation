def cartesian_distance_between(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return (dx**2 + dy**2)**0.5

def index_of_smallest_value(array):
    smallest_element = [0, float("inf")]

    for idx,element in enumerate(array):
        if element < smallest_element[1]:
            smallest_element[0] = idx
            smallest_element[1] = element
    
    return smallest_element[0] 

def average(X):
    return sum(X) / len(X)
