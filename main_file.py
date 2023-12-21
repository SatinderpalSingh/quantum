import numpy as np
import time
from scipy.linalg import eig
MATRIX_SIZE = 1000
random_matrix = np.random.randint(1000, 10000, size=(MATRIX_SIZE, MATRIX_SIZE))

def calculate_eigenvalues(random_matrix):
    eigenvalues, _ = eig(random_matrix)
    return eigenvalues

if __name__ == "__main__":
    input_matrix = random_matrix

    start_time = time.time()
    result = calculate_eigenvalues(input_matrix)
    end_time = time.time()

    print("Input Matrix:")
    print(input_matrix)
    print("\nEigenvalues:")
    print(result)
    print("\nResult generated in:")
    print(end_time - start_time)

