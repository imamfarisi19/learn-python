import numpy as np
from scipy import sparse

eye = np.eye(4) 
print("NumPy array:\n{}".format(eye)) 

# Convert the NumPy array to a SciPy sparse matrix is CSR format 
# Only the nonzero entries are stored 
sparse_matrix = sparse.csr_matrix(eye) 
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix)) 

