## 1. Elementary Row Operations (Preserving Singularity)

When solving linear systems, we can manipulate equations without changing the underlying geometry or the system's true rank. These three valid moves are the mechanical foundation for translating any matrix into Row Echelon Form:
*   **Row Swapping:** Exchanging the position of two sentences (rows).
*   **Scalar Multiplication:** Multiplying a row by a non-zero constant.
*   **Row Addition/Subtraction:** Adding or subtracting a multiple of one row from another.

---

## 2. System Outcomes & Degrees of Freedom

*   **Singular Redundant (Infinite Solutions):** Occurs when equations carry overlapping information. The solution space expands into a continuous geometric shape. 
    *   *Example:* $a + b = 10$. If we set $a = x$, then $b = 10 - x$. This system has **1 degree of freedom** because exactly one variable ($x$) is completely free to vary.
*   **Singular Contradictory (No Solution):** Equations contain mutually exclusive constraints, collapsing into mathematical impossibilities.

---

## 3. Matrix Row Reduction: REF vs. RREF

We apply Elementary Row Operations systematically to filter out redundancy.
*   **Pivot (Definition):** The first non-zero number from the left in a non-zero row. In optimized algorithms, we often force pivots to equal 1.
*   **Row Echelon Form (REF):** Forms a staircase pattern where all entries strictly *below* the pivots are zeroes.
*   **Reduced Row Echelon Form (RREF):** A stricter state where all entries both *above* and *below* the pivots are zeroes, fully isolating each variable.

---

## 4. Rank and The Solution Space

Rank measures the absolute information density of the system. In REF or RREF, the rank is simply the **total count of pivots**.

**The Solution Space Formula:**
To understand how rank dictates the solution space, we look at the total number of variables (columns) versus the true information (rank).

$$
\text{Total Variables} - \text{Rank} = \text{Degrees of Freedom}
$$

*Why is it related?* Every piece of unique information (rank) locks down one dimension of space. If a system has 3 variables but a rank of 2, it is missing one piece of defining information. That missing information translates directly into 1 degree of freedom (a 1D line of infinite solutions).
