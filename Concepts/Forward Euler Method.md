---
title: Forward Euler Method
material_type: concept note
course: Part IA Differential Equations
source_file: Ch.4 First-order Linear Differential Equations.pdf
drive_file_id: 1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3
source_url: https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view
source_pages: [4, 5]
---

# Forward Euler Method

For the [[First-Order Linear Differential Equations|initial-value problem]]
$$5y'-3y=0,\qquad y(0)=y_0,$$
take $x_n=nh$, with $h>0$. Approximate the derivative by the forward difference:
$$y'(x_n)\approx\frac{y_{n+1}-y_n}{h}.$$
Here the computed $y_n$ approximates $y(x_n)$.

The discrete equation is
$$5\frac{y_{n+1}-y_n}{h}-3y_n=0,$$
giving the **forward Euler recurrence**
$$y_{n+1}=\left(1+\frac{3h}{5}\right)y_n.$$
Repeated substitution yields
$$y_n=\left(1+\frac{3h}{5}\right)^ny_0.$$

The exact ODE solution is $y(x)=y_0e^{3x/5}$; the recurrence is a numerical approximation.

See [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]], pages 4–5.
