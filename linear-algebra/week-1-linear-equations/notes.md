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
