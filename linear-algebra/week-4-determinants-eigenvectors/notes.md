## 1. The Geometry of Transformations: Determinants & Invertibility
When we apply a linear transformation (via a matrix), the space itself morphs. The **determinant** measures the scaling factor of that transformation—specifically, how much the area (2D) or volume (3D) of the basis is stretched or squished.

*   **Non-Singular (Invertible):** $\det(A) \neq 0$. The transformed space still spans the same number of dimensions (e.g., a 2D square transforms into a 2D parallelogram). Because no dimensions are lost, you can perfectly map back to the original space (invertible).
*   **Singular (Non-Invertible):** $\det(A) = 0$. The transformation completely collapses space into a lower dimension (e.g., a 2D square is squished into a 1D line or a 0D point). The original information is destroyed, so it cannot be inverted.
*   **Sign of the Determinant:** A positive determinant preserves the orientation of the space. A negative determinant means the space was flipped inside-out during the transformation (the basis vectors crossed over each other).
*   **Multiplicative Property:** The determinant of sequential transformations is the product of their individual determinants: $\det(AB) = \det(A) \det(B)$.

---

## 2. Basis and Span (The Skeleton of Space)
A **basis** is the coordinate system that defines a vector space. For a set of vectors to qualify as a basis, they must strictly meet two conditions:
1.  **Span the space:** You must be able to reach every single point in the space using a linear combination of these vectors ($c_1v_1 + c_2v_2$).
2.  **Be linearly independent:** There can be no redundant vectors (no vector can be built using the others).

The most common is the **Standard Basis**. In $\mathbb{R}^2$, this is $\hat{i} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\hat{j} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$. Any vector in the space is just a combination of these (e.g., $v = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$ is exactly $4\hat{i} + 3\hat{j}$).

---

## 3. Eigenvectors, Eigenvalues, and Eigenbases
When a matrix transforms space, most vectors are knocked completely off their original trajectories. 
*   **Eigenvectors:** The stubborn vectors that refuse to change direction. They remain perfectly on their original line of span.
*   **Eigenvalues ($\lambda$):** The scalar factor by which the eigenvector is stretched, squashed, or flipped along its line.
*   **Eigenbasis:** A basis coordinate system made entirely out of eigenvectors. 

**How to Calculate Them:**
We start from the core definition: $Av = \lambda v$.
By inserting the Identity matrix, we move everything to one side: $(A - \lambda I)v = 0$.
For a non-zero vector $v$ to equal zero after multiplication, the matrix $(A - \lambda I)$ must be singular (collapsing space). Therefore, its determinant must be zero.

1.  **Find the Eigenvalue:** Solve the characteristic polynomial $\det(A - \lambda I) = 0$ for $\lambda$.
2.  **Find the Eigenvector:** Take the $\lambda$ you just found, plug it back into $(A - \lambda I)v = 0$, and use Gaussian elimination (row reduction) to solve the linear system for the exact coordinates of $v$.

---

## 4. Principal Component Analysis (PCA) & Dimensionality Reduction
Eigenvectors are the mechanical foundation of PCA. We reduce dimensions to make massive datasets easier to manage, visualize, and compute, while strictly minimizing the loss of useful information.

**A. Centering and the Covariance Matrix**
Before doing anything, we must subtract the mean from our data $(X - \mu)$. This centers the entire dataset at the origin $(0,0)$. We then calculate the Covariance Matrix $(X-\mu)^T(X-\mu)$, which perfectly captures the shape, spread, and directional relationships of the variables.

Because the data is centered at the origin, we can intuitively view covariance by quadrant:
*   **Quadrant I (+x, +y) & Quadrant III (-x, -y):** Data points here contribute positively to the covariance (if one variable increases, the other increases).
*   **Quadrant II (-x, +y) & Quadrant IV (+x, -y):** Data points here contribute negatively to the covariance (inversely correlated).

**B. Projection (Capturing the Spread)**
Projection is the act of dropping a "shadow" of our data onto a specific line. We project the centered dataset onto a unit vector $v$ using the dot product formula: $X \cdot \frac{v}{\|v\|}$. To avoid losing information, we want to choose a vector $v$ that results in the longest possible shadows (maximizing the variance).

**C. Why use the Eigenvectors of the Covariance Matrix?**
The Covariance Matrix is a square matrix that holds the mathematical "shape" of the data cloud. When we calculate its eigenvectors, they are mathematically guaranteed to point precisely in the directions of maximum data spread (the Principal Components). 
*   The eigenvector with the **largest eigenvalue** is the primary axis of variance. 
*   By projecting our data onto this specific eigenvector, we successfully flatten the data into a lower dimension while preserving the maximum amount of original information.
