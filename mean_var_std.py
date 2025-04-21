import numpy as np

def calculate(list):
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
    array = np.array(list)
    matrix = array.reshape(3, 3)
    mean_val = [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(array).tolist()]
    var_val = [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(array).tolist()]
    std_val = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(array).tolist()]
    max_val = [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(array).tolist()]
    min_val = [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(array).tolist()]
    sum_val = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(array).tolist()]
    calculations = {'mean': mean_val, 'variance': var_val, 'standard deviation': std_val, 'max': max_val, 'min': min_val, 'sum': sum_val}
    return calculations