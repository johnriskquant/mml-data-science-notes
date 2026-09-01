import numpy as np

# ==========================================
# 1. HELPER FUNCTIONS
# ==========================================

def swap_rows(M, row_index_1, row_index_2):
    """Swaps two rows in the matrix."""
    M = M.copy()
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M

def augmented_matrix(A, B):
    """Combines coefficient matrix A and constant matrix B."""
    return np.hstack((A, B))

def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """Finds the first non-zero value down a specific column to use as a pivot."""
    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        if not np.isclose(val, 0, atol=1e-5):
            return i + starting_row
    return -1

def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    """Finds the first non-zero value across a specific row."""
    M_copy = M.copy()
    if augmented:
        M_copy = M_copy[:, :-1]
        
    row_array = M_copy[row]
    for i, val in enumerate(row_array):
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1


# ==========================================
# 2. ROW ECHELON FORM (REF)
# ==========================================

def row_echelon_form(A, B):
    """Transforms the system into Row Echelon Form with unitary pivots."""
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0):
        return 'Singular system'

    A = A.astype('float64')
    B = B.astype('float64')
    M = augmented_matrix(A, B)
    num_rows = len(A) 

    for row in range(num_rows):
        pivot_candidate = M[row, row]

        # Scout for a new pivot if the diagonal is 0
        if np.isclose(pivot_candidate, 0): 
            first_non_zero = get_index_first_non_zero_value_from_column(M, row, row + 1) 
            M = swap_rows(M, row, first_non_zero) 
            pivot = M[row, row] 
        else:
            pivot = pivot_candidate 
        
        # Normalize pivot to 1
        M[row] = (1 / pivot) * M[row]

        # Zero out the rows below the pivot
        for j in range(row + 1, num_rows): 
            value_below_pivot = M[j, row]
            M[j] = M[j] - (value_below_pivot * M[row])
            
    return M


# ==========================================
# 3. BACK SUBSTITUTION
# ==========================================

def back_substitution(M):
    """Sweeps from bottom-right to top-left to isolate variables."""
    M = M.copy()
    num_rows = M.shape[0]

    for row in reversed(range(num_rows)): 
        substitution_row = M[row]
        index = get_index_first_non_zero_value_from_row(M, row, augmented=True)

        for j in range(row): 
            row_to_reduce = M[j]
            value = row_to_reduce[index]
            
            # Zero out the values above the pivot
            row_to_reduce = row_to_reduce - (value * substitution_row)
            M[j] = row_to_reduce

    # Extract and return the final constants column
    return M[:, -1]


# ==========================================
# 4. MASTER WRAPPER
# ==========================================

def gaussian_elimination(A, B):
    """Executes the full solving algorithm."""
    M = row_echelon_form(A, B)
    
    # Check for singularity before doing back-substitution
    if isinstance(M, str):
        return M 
        
    solution = back_substitution(M)
    return solution
