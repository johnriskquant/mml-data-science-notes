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
