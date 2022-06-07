def cartesian_distance_between(p1, p2):
    return ((p1 - p2)**2)**0.5

def index_of_smallest_value(array):
    smallest_element = [0, float("inf")]

    for idx,element in enumerate(array):
        if element < smallest_element[1]:
            smallest_element[0] = idx
            smallest_element[1] = element
    
    return smallest_element[0] 
