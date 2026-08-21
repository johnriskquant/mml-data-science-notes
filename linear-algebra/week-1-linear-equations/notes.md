# Week 1: Systems of Linear Equations & Singular Matrices

## 1. Systems of Linear Equations


## The Link Between Machine Learning and Systems of Equations

At its core, modeling a phenomenon in machine learning is about finding the optimal weights to satisfy a massive system of linear equations across an entire dataset.

### 1. The Foundational Model (1D Space)
We start with the basic algebraic equation of a line: $y = mx + b$. In machine learning terminology, the slope $m$ becomes our **weight** ($w$), and $b$ remains our **bias**. 
$$y = wx + b$$
*   **Geometric Visualization:** A straight line in a 2D space.
*   **Application:** Predicting a continuous variable based on a single input.

### 2. Scaling to Multiple Features (n-Dimensional Space)
Real-world datasets require multivariate models. The equation extends linearly to incorporate $n$ features:
$$y = w_1x_1 + w_2x_2 + \dots + w_nx_n + b$$
*   **Geometric Visualization:** With 2 features, the model becomes a 3D plane. Beyond 3 dimensions, it becomes an abstract $n$-dimensional hyperplane that is impossible to visualize but mathematically sound.
*   **Practical Context:** In credit decisioning, $x_1$ might represent revolving credit utilization, $x_2$ represents debt-to-income ratio, and $y$ represents the final predicted credit limit. 

### 3. The Full Dataset as a System of Equations

A dataset contains $m$ rows (observations). To train the model, we apply the equation across every single row $(i)$, creating a large system of linear equations:

$$
\begin{aligned}
y^{(1)} &= w_1x_1^{(1)} + w_2x_2^{(1)} + \dots + w_nx_n^{(1)} + b \\
y^{(2)} &= w_1x_1^{(2)} + w_2x_2^{(2)} + \dots + w_nx_n^{(2)} + b \\
&\vdots \\
y^{(m)} &= w_1x_1^{(m)} + w_2x_2^{(m)} + \dots + w_nx_n^{(m)} + b
\end{aligned}
$$


### 4. The Linear Algebra Solution
Instead of solving $m$ individual equations algebraically, we translate the entire dataset into a matrix format. Linear algebra provides the mathematical framework to process this massive system simultaneously, allowing the algorithm to compute the optimal vector of weights ($w_1 \dots w_n$) that minimizes the prediction error across all $m$ applicants.


## 5. The "System of Sentences" Framework

A highly intuitive way to conceptualize linear algebra is to view each equation in a system as a "sentence" of information. 

### Information Density, Rank, and Singularity
* **Non-Singular (Complete Information):** The number of independent sentences equals the number of variables. Every piece of information is unique, pinning down exactly one solution (a single point in space).
* **Singular - Redundant (Incomplete Information):** The system has fewer pieces of unique information than variables (e.g., one sentence is just a multiple of another). The system collapses into a line or plane of infinite solutions.
* **Singular - Contradictory (Inconsistent Information):** The sentences conflict with one another (e.g., $x + y = 1$ and $x + y = 2$). The system collapses into an impossibility, yielding zero solutions.

**Rank** is the mathematical measure of a system's true information density. It counts the exact number of strictly independent, non-contradictory sentences in your matrix.

---

## 6. Gaussian Elimination and Row Echelon Form (REF)

To distinguish between singular and non-singular systems, we use an information-filtering algorithm called **Gaussian Elimination**. 

By systematically subtracting multiples of equations from one another ("zeroing out"), we strip away redundancy without changing the underlying truth of the system. The goal is to reach **Row Echelon Form (REF)**, which forms a cascading staircase pattern:

$$
\begin{bmatrix}
\mathbf{1} & 2 & -1 \\
0 & \mathbf{3} & 4 \\
0 & 0 & \mathbf{5}
\end{bmatrix}
$$

Once in REF, the nature of the system is exposed:
1. **Non-Singular:** A perfect staircase. Every variable has a "pivot" (a leading non-zero coefficient).
2. **Singular (Redundant):** An entire row zeroes out, leaving $0 = 0$. This mathematically proves a sentence was redundant.
3. **Singular (Contradictory):** The variables zero out but leave a non-zero constant, resulting in a false mathematical statement like $0 = 7$.

---

## 7. Homogeneous Systems (Going Through the Origin)

When analyzing a system, it is often simpler to manage if all equations pass through the origin. This is known as a **Homogeneous System**, written as:

$$
A\mathbf{x} = \mathbf{0}
$$

By setting the constants (the outcome vector $\mathbf{b}$) to zero, we strip away the specific "translation" of the system in space. This allows us to study the pure geometric relationship between the variables. 
* If a homogeneous system is non-singular, its only solution is the origin: $\mathbf{x} = \mathbf{0}$. 
* If it is singular (redundant), it contains lines or planes of solutions passing through the origin (known in data science as the **null space**).


## 8. Linear Dependence, Determinants, and Matrix Shape

The concepts of redundancy and linear dependence apply to **all** matrices. However, the mathematical tools used to identify them depend on the shape of the matrix.

### The Square Matrix: Determinants & Singularity
The terms **Singular** and **Non-Singular**, as well as the **Determinant**, are strictly defined only for **square matrices** ($n \times n$). 

*   **Why?** Geometrically, a determinant measures how a matrix scales an object's area or volume when transforming space (e.g., mapping 3D space to 3D space). You cannot calculate a single "volume scaling factor" when mapping from 2D space into 5D space.
*   **The Rule:** For a square matrix $A$:
    *   If rows/columns are linearly dependent (redundant) $\rightarrow \det(A) = 0 \rightarrow$ Singular.
    *   If rows/columns are linearly independent $\rightarrow \det(A) \neq 0 \rightarrow$ Non-Singular.

### The Rectangular Matrix: Rank
Real-world datasets are almost never square. They are **rectangular matrices** ($m \times n$), where $m$ is the number of observations (rows) and $n$ is the number of features (columns). 

For rectangular matrices, we cannot compute a determinant. Instead, we measure linear dependence using **Rank**.
*   **The Rule:** A rectangular matrix cannot have a rank higher than its smallest dimension ($\min(m, n)$).
*   **The "Too Many Sentences" Rule:** If you have a $50000 \times 15$ matrix (50,000 loan applicants, 15 credit risk features), you have 50,000 "sentences" but only 15 variables. You are mathematically guaranteed to have massive linear dependence among the rows. 

### 9. The Data Science Bridge: Why Determinants Still Matter

Even though the raw dataset $X$ is a rectangular $m \times n$ matrix, determinants are still a massive part of machine learning. 

When training a linear algorithm (like Ordinary Least Squares), the algorithm doesn't invert the raw dataset. It multiplies the dataset by its own transpose to create a **Covariance Matrix**:

$$
X^T X
$$

No matter what shape $X$ is, the resulting matrix $X^T X$ is **always a perfect square** ($n \times n$). 
*   If your credit features (columns) are linearly independent, $X^T X$ is non-singular, its determinant is non-zero, and the model trains perfectly.
*   If two credit features are linearly dependent (e.g., calculating debt-to-income twice in slightly different ways), $X^T X$ becomes singular, its determinant becomes $0$, and the model crashes because the matrix cannot be inverted.
