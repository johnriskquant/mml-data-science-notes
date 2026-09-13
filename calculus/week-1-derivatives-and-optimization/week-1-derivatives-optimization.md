*   **Instantaneous Rate of Change:** In 2D, this is the limit of $\frac{\Delta y}{\Delta x}$ as $\Delta x \to 0$, giving $\frac{dy}{dx}$. In higher dimensions, this expands into the **Gradient** (a vector of partial derivatives pointing to the steepest ascent) or the **Jacobian** matrix.
*   **Notation:** **Leibniz** ($\frac{dy}{dx}$) explicitly names the variables, which is highly useful for tracking units and applying the chain rule. **Lagrange** ($f'(x)$) is much faster to write and highlights the function itself.
*   **Non-Differentiable Points:** A derivative requires a smooth, continuous curve. It fails at **Corners/Cusps** (e.g., $f(x) = |x|$ at $x=0$, where left and right slopes clash), **Jump Discontinuities** (a literal break in the graph), and **Vertical Tangents** (where the slope becomes infinite, like $f(x) = \sqrt[3]{x}$ at $x=0$).

## 2. Core Rules & Common Derivatives
*   **Standard Derivatives:** The derivative of a constant is $0$. A linear function $f(x)=cx$ becomes $f'(x)=c$. The Power Rule states that $f(x)=x^n$ becomes $f'(x)=nx^{n-1}$.
*   **Sum and Product Rules:** The Sum Rule is straightforward: $(f+g)' = f' + g'$. The Product Rule requires alternating terms: $(fg)' = f'g + fg'$ (e.g., $(x^2 \cdot x^3)' = 2x(x^3) + x^2(3x^2) = 5x^4$).
*   **The Chain Rule:** For nested functions, $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$. This mechanically unpacks functions layer by layer and is the exact mathematical engine behind neural network backpropagation.

## 3. Euler's Number & Inverse Functions
*   **Euler's Number ($e$):** Defined by the limit $\lim_{n \to \infty} (1 + \frac{1}{n})^n \approx 2.718$. It is the uniquely perfect function where its rate of change is exactly itself: $\frac{d}{dx}e^x = e^x$.
*   **Inverse Functions:** The natural log ($\ln(x)$) undoes $e^x$. If $f(a) = b$, its inverse $g(b) = a$. Their derivatives are intimately connected via $g'(b) = \frac{1}{f'(a)}$, leading to the fact that $\frac{d}{dx}\ln(x) = \frac{1}{x}$.

## 4. Optimization & Cost Functions
*   **Local vs. Global Extrema:** Setting $f'(x) = 0$ reveals flat spots (critical points). A **Local Min/Max** is the peak or valley in a specific neighborhood, while the **Global** is the absolute highest or lowest point across the entire function.
*   **Squared Loss:** We define the error function, calculate its derivative, and set it to $0$ to analytically find the exact parameters that minimize the squared error.
*   **Log Loss & The Casino:** To maximize a winning probability function like $G(p) = p^7(1-p)^3$, we wrap it in a logarithm: $\ln(G(p)) = 7\ln(p) + 3\ln(1-p)$. Setting the derivative to zero ($\frac{7}{p} - \frac{3}{1-p} = 0$) elegantly solves to $p = 0.7$.
*   **Why Negative Log?** Probabilities $p \in [0, 1]$ shrink rapidly when multiplied, causing computer underflow. Their logarithms are also negative. We use $-\ln(p)$ to turn multiplication into simple addition and force the final loss to be a positive number we can cleanly minimize.
