## 1. Vector Fundamentals
Vectors are quantitative objects represented as tuples of numbers. A vector's coordinates correspond directly to the dimensions of the space it inhabits (e.g., a vector $(4,3)$ exists in 2D space). They can be written as either row or column vectors and are defined by two key properties:

*   **Magnitude (Norm):** The "size" or length of the vector in space. 
    *   **$L_1$ Norm (Taxicab distance):** $|x| + |y|$ for a vector $(x, y)$.
    *   **$L_2$ Norm (Helicopter/Euclidean distance):** $\sqrt{x^2 + y^2}$.
*   **Direction:** Defined by the angle $\theta$ between the vector and the axis. Calculated using rise over run: $\theta = \arctan(y/x)$.

## 2. Vector Operations & Geometric Intuition
Vector arithmetic has direct geometric translations:
*   **Addition:** Forms the diagonal of the parallelogram created by the two vectors.
*   **Subtraction:** Represents the vector connecting the tips of the two vectors (forming a side of the parallelogram).

## 3. The Dot Product and Projections
The dot product is the algebraic sum of multiplied element pairs between two vectors ($\sum u_i \cdot v_i$). 

**Relationship to Magnitude:** 
The magnitude of a vector is directly derived from its dot product with itself: $\|u\|_2 = \sqrt{\langle u, u \rangle}$.

**Geometric Meaning ($u \cdot v = \|u\| \|v\| \cos\theta$):**
The cosine of the angle ($\theta$) entirely determines the sign of the dot product, which tells us how the vectors project onto one another:
*   **$\langle u,v \rangle > 0$:** Positive projection (vectors point in a generally similar direction, $\theta < 90^\circ$).
*   **$\langle u,v \rangle < 0$:** Negative projection (vectors point away from each other, $\theta > 90^\circ$).
*   **$\langle u,v \rangle = 0$:** Orthogonal (vectors are completely independent/perpendicular, $\theta = 90^\circ$, since $\cos(90^\circ) = 0$).

## 4. Matrices as Linear Transformations
A linear system can be expressed as a matrix multiplied by a vector ($Ax = b$). For this to work, the number of columns in the matrix must perfectly match the length of the vector. 

Beyond representing systems of equations, matrices act as **linear transformations**. Matrix multiplication is the act of applying a transformation (like stretching, rotating, or squashing) to a vector's space.

*   **Identity Matrix ($I$):** The neutral transformation. Multiplying a matrix by $I$ produces the exact same matrix, leaving the space completely unchanged.
*   **Inverse Matrix ($A^{-1}$):** Algebraically, it is a matrix that produces the Identity matrix when multiplied by $A$ ($A \cdot A^{-1} = I$). Geometrically, it represents the exact "undoing" or reversal of a linear transformation.
*   **Singularity & Invertibility:** Singular matrices are *not* invertible. Geometrically, they compress space (e.g., squashing a 2D plane into a 1D line). You cannot inverse or "un-squash" this transformation because information was destroyed, resulting in a 1-to-many mapping or no mapping at all.


## 5. Python / NumPy Implementations

In data science, we rely on the `numpy` library to compute these vector and matrix operations efficiently without writing manual loops.

```python
import numpy as np

# Define vectors as numpy arrays
u = np.array([4, 3])
v = np.array([1, 2])

# 1. Magnitudes (Norms)
# L1 Norm (Taxicab)
l1_norm = np.linalg.norm(u, ord=1) # Returns 7.0

# L2 Norm (Euclidean / Helicopter)
# By default, np.linalg.norm computes the L2 norm
l2_norm = np.linalg.norm(u) # Returns 5.0

# 2. Vector Operations
# Vector addition (parallelogram diagonal)
addition = u + v 

# Dot Product
# Can be computed using np.dot() or the @ operator
dot_product = np.dot(u, v)
# OR: dot_product = u @ v

# 3. Matrix Transformations
A = np.array([[1, 2], 
              [3, 4]])

# Apply a linear transformation to vector u
transformed_u = A @ u

# Compute the inverse of a matrix (only works if non-singular!)
A_inverse = np.linalg.inv(A)
