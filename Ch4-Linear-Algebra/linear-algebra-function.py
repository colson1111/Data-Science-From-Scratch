import math

def vector_add(v, w):
    """ adds corresponding elements """
    return [v_i + w_i for v_i, w_i in zip(v, w)]
    
def vector_subtract(v, w):
    """ subtracts corresponding elements """
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """ sums all corresponding elements """
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """ c is a number, v is a vector """
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """ compute the vector whose ith element is the mean of the 
    ith elements of the input vectors """
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))
   
def dot(v, w):
    """ the sum of the componentwise products of two vectors
    v_1 * w_1 + ... + v_n * w_n """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """ v_1 * v_1 + ... + v_n * v_n """
    return(dot(v, v))

def magnitude(v):
    """ calculate the length of a vector (sqrt of the sum of squares) """
    return math.sqrt(sum_of_squares(v))
    
def squared_distance(v, w):
    """ the distance between two vectors squared
    (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    """ the distance between two vectors """
    return magnitude(vector_subtract(v, w))
    
def shape(A):
    """ the number of rows and columns in a matrix """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols
    
def get_row(A, i):
    """ returns the specified row of the given matrix """
    return A[i]

def get_column(A, j):
    """ returns the specified column of the given matrix """
    return[A_i[j]
        for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """ returns a num_rows by num_cols matrix
    whose (i,j)th entry is entry_fn(i,j) """
    # Example:  identity_matrix = make_matrix(5, 5, is_diagonal)
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  # [entry_fn(i, 0), ...]
            for i in range(num_rows)]   # create one list for each i

def is_diagonal(i, j):
    """ 1's on the diagonal, 0's everywhere else """
    return 1 if i == j else 0
