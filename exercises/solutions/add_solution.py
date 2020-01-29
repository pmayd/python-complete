def add(*matrices):
    
    column_lengths = set([(len(m), len(col)) for m in matrices for col in m])
    if len(column_lengths) > 1:
        raise ValueError("Given matrices are not the same size.")
    
    matrix_sum = []
    for col_pair in zip(*matrices):
        col_elementwise_sum = []
        for pair in zip(*col_pair):
            col_elementwise_sum.append(sum(pair))
        
        matrix_sum.append(col_elementwise_sum)
     
    return matrix_sum