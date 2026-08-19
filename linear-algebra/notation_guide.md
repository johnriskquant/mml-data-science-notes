# Linear Algebra: Notation Guide

This reference guide outlines the standard mathematical notation used throughout these notes and the accompanying Python implementations. 

## Fundamental Entities

| Notation | Description |
| :--- | :--- |
| $A, B, C$ | Capital letters represent matrices. |
| $u, v, w$ | Lowercase letters represent vectors. |
| $A \in \mathbb{R}^{m \times n}$ | Matrix $A$ has $m$ rows and $n$ columns. |
| $\mathbb{R}$ | The set of real numbers (e.g., $0, -0.642, 2, 3.456$). |
| $\mathbb{R}^n$ | The set of $n$-dimensional real vectors. |
| $\mathbb{R}^2$ | The set of 2-dimensional vectors. |
| $v \in \mathbb{R}^2$ | Vector $v$ is an element of $\mathbb{R}^2$ (e.g., $v = \begin{bmatrix} 1 \\ 3 \end{bmatrix}$). |

## Matrix & Vector Operations

| Notation | Description |
| :--- | :--- |
| $A^T$ | The transpose of matrix $A$. |
| $v^T$ | The transpose of vector $v$. |
| $A^{-1}$ | The inverse of square matrix $A$. |
| $\det(A)$ | The determinant of matrix $A$. |
| $AB$ | Matrix multiplication of matrices $A$ and $B$. |
| $u \cdot v$ or $\langle u, v \rangle$ | The dot product of vectors $u$ and $v$. |

## Norms & Transformations

| Notation | Description |
| :--- | :--- |
| $\|v\|_1$ | L1-norm of a vector (Manhattan distance / sum of absolute values). |
| $\|v\|_2$ , $\|v\|$, or $|v|$ | L2-norm of a vector (Euclidean distance / standard magnitude). |
| $T: \mathbb{R}^2 \rightarrow \mathbb{R}^3$ | A transformation $T$ mapping a vector in 2D space to 3D space. |
| $T(v) = w$ | The transformation $T$ applied to vector $v$ results in vector $w$. |

---
*Note: In production FinTech data science (e.g., using Python's NumPy or Polars), vectors are typically represented as 1-dimensional arrays, and matrices as 2-dimensional arrays or DataFrames. Transposing ($A^T$) and dot products ($u \cdot v$) are foundational for calculating weighted risk scores and executing gradient descent optimizations.*
