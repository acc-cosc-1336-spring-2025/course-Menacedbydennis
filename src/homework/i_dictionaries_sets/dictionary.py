def get_p_distance(list1, list2):
    
    if len(list1) != len(list2):
        raise ValueError("Both lists must be of the same length")
    
   
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    
    
    p_distance = differences / len(list1)
    
    return p_distance

def get_p_distance_matrix(list_of_lists):
    
    n = len(list_of_lists)
    
    
    p_distance_matrix = [[0] * n for _ in range(n)]
    
    
    for i in range(n):
        for j in range(i, n):
            p_dist = get_p_distance(list_of_lists[i], list_of_lists[j])
            p_distance_matrix[i][j] = p_dist
            p_distance_matrix[j][i] = p_dist  
    
    return p_distance_matrix