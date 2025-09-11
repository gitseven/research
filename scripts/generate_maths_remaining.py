#!/usr/bin/env python3
"""Generate remaining Maths chapters 4-13 - 12th Board 2026."""

from pathlib import Path

def create_problem_html(chapter, problem_num, title, question, background, solution, tips, formulas):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Ch {chapter} Problem {problem_num} — {title}</title>
  <style>
    body {{ margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; background:#ffffff; color:#111827; line-height:1.55; }}
    .container {{ max-width: 960px; margin:0 auto; padding:24px; }}
    h1 {{ margin:0 0 8px; font-size:26px; color:#38bdf8; }}
    h2 {{ margin:18px 0 8px; font-size:20px; color:#a78bfa; }}
    .panel {{ background:#ffffff; border:1px solid #e5e7eb; border-radius:10px; padding:16px; margin:16px 0; }}
    .q {{ border-left:3px solid #f59e0b; padding-left:10px; }}
    .solution {{ border-left:3px solid #10b981; padding-left:10px; background:#f0fdf4; }}
    .concept-section {{ background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px; margin:12px 0; }}
    .math-diagram {{ max-width:100%; height:auto; display:block; margin:12px auto; border:1px solid #e5e7eb; border-radius:8px; background:#fafafa; }}
    .muted {{ color:#374151; }}
    ul {{ margin:8px 0 8px 20px; }}
    li {{ margin:4px 0; }}
    .formula {{ background:#fef3c7; border:1px solid #f59e0b; border-radius:6px; padding:8px; margin:8px 0; text-align:center; font-family: 'Courier New', monospace; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Chapter {chapter} · Problem {problem_num}</h1>
    <div class="panel q">
      <h2>Question</h2>
      <p>{question}</p>
    </div>

    <div class="concept-section">
      <h2>Background Concept — {title}</h2>
      {background}
    </div>

    <div class="panel solution">
      <h2>Solution</h2>
      <p>{solution}</p>
    </div>

    <div class="panel">
      <h2>Tips to Solve</h2>
      <ul>
        {tips}
      </ul>
    </div>

    <div class="panel">
      <h2>Key Formulas</h2>
      <div class="formula">
        {formulas}
      </div>
    </div>

    <div class="panel">
      <h2>Source</h2>
      <p class="muted">Expected 12th Board 2026 - Chapter {chapter}</p>
    </div>
  </div>
</body>
</html>"""

# Remaining chapters data (4-13)
chapters_data = {
    4: {
        "title": "Determinants",
        "problems": [
            {"title": "Determinant Properties", "question": "Evaluate the determinant of A = [[2,3,1],[1,2,3],[3,1,2]].", "background": "The determinant of a 3×3 matrix [[a,b,c],[d,e,f],[g,h,i]] is a(ei-fh) - b(di-fg) + c(dh-eg). Determinants have important properties: det(AB) = det(A)det(B), det(Aᵀ) = det(A), det(kA) = kⁿdet(A) for n×n matrix A, and det(A⁻¹) = 1/det(A).", "solution": "Using the formula: det(A) = 2(2×2-3×1) - 3(1×2-3×3) + 1(1×1-2×3) = 2(4-3) - 3(2-9) + 1(1-6) = 2(1) - 3(-7) + 1(-5) = 2 + 21 - 5 = 18.", "tips": ["<li>Use the 3×3 determinant formula</li>", "<li>Calculate each minor carefully</li>", "<li>Alternate signs: +, -, +</li>", "<li>Check arithmetic</li>", "<li>Verify with properties</li>"], "formulas": "det([[a,b,c],[d,e,f],[g,h,i]]) = a(ei-fh) - b(di-fg) + c(dh-eg)"},
            {"title": "Cramer's Rule", "question": "Solve using Cramer's rule: 2x + 3y = 7, 4x + 5y = 13.", "background": "Cramer's rule provides a method to solve systems of linear equations using determinants. For the system ax + by = e, cx + dy = f, the solutions are x = det([[e,b],[f,d]])/det([[a,b],[c,d]]) and y = det([[a,e],[c,f]])/det([[a,b],[c,d]]). This method works when the coefficient matrix is invertible.", "solution": "The coefficient matrix is A = [[2,3],[4,5]] with det(A) = 2×5 - 3×4 = 10 - 12 = -2. For x: replace first column with constants: A₁ = [[7,3],[13,5]], det(A₁) = 7×5 - 3×13 = 35 - 39 = -4, so x = -4/(-2) = 2. For y: replace second column with constants: A₂ = [[2,7],[4,13]], det(A₂) = 2×13 - 7×4 = 26 - 28 = -2, so y = -2/(-2) = 1.", "tips": ["<li>Find det(A) of coefficient matrix</li>", "<li>Replace columns with constants</li>", "<li>Calculate determinants of modified matrices</li>", "<li>Use x = det(A₁)/det(A), y = det(A₂)/det(A)</li>", "<li>Check the solution</li>"], "formulas": "x = det(A₁)/det(A), y = det(A₂)/det(A) where A₁, A₂ are matrices with replaced columns"},
            {"title": "Area of Triangle", "question": "Find the area of triangle with vertices (1,2), (3,4), and (5,1).", "background": "The area of a triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃) is (1/2)|det([[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]])|. This formula uses the determinant of a 3×3 matrix. The absolute value ensures the area is positive. This method is useful in coordinate geometry.", "solution": "Using the formula: Area = (1/2)|det([[1,2,1],[3,4,1],[5,1,1]])| = (1/2)|1(4×1-1×1) - 2(3×1-1×5) + 1(3×1-4×5)| = (1/2)|1(4-1) - 2(3-5) + 1(3-20)| = (1/2)|3 - 2(-2) + 1(-17)| = (1/2)|3 + 4 - 17| = (1/2)|-10| = 5.", "tips": ["<li>Use the determinant formula for area</li>", "<li>Include 1 in the third column</li>", "<li>Take absolute value</li>", "<li>Multiply by 1/2</li>", "<li>Check with other methods</li>"], "formulas": "Area = (1/2)|det([[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]])|"},
            {"title": "Adjoint Matrix", "question": "Find the adjoint of A = [[1,2],[3,4]].", "background": "The adjoint (or adjugate) of a matrix A is the transpose of the cofactor matrix. For a 2×2 matrix [[a,b],[c,d]], the adjoint is [[d,-b],[-c,a]]. The adjoint is related to the inverse: A⁻¹ = (1/det(A))adj(A). The adjoint is useful in finding inverses and solving systems.", "solution": "For A = [[1,2],[3,4]], the cofactor matrix is [[4,-3],[-2,1]]. Taking the transpose: adj(A) = [[4,-2],[-3,1]].", "tips": ["<li>Find the cofactor matrix</li>", "<li>Take the transpose</li>", "<li>For 2×2: adj([[a,b],[c,d]]) = [[d,-b],[-c,a]]</li>", "<li>Check with A·adj(A) = det(A)I</li>", "<li>Use for finding inverse</li>"], "formulas": "adj(A) = transpose of cofactor matrix; A⁻¹ = (1/det(A))adj(A)"},
            {"title": "System Consistency", "question": "Determine if the system x + 2y = 3, 2x + 4y = 6 has a unique solution.", "background": "A system of linear equations has a unique solution if and only if the determinant of the coefficient matrix is non-zero. If det(A) = 0, the system may have no solution or infinitely many solutions. The rank of the coefficient matrix and augmented matrix determine the nature of solutions.", "solution": "The coefficient matrix is A = [[1,2],[2,4]] with det(A) = 1×4 - 2×2 = 4 - 4 = 0. Since det(A) = 0, the system does not have a unique solution. The second equation is 2 times the first equation, so the system has infinitely many solutions.", "tips": ["<li>Find det(A) of coefficient matrix</li>", "<li>If det(A) ≠ 0: unique solution</li>", "<li>If det(A) = 0: check consistency</li>", "<li>Compare equations for dependence</li>", "<li>Use rank to determine solution type</li>"], "formulas": "Unique solution ⟺ det(A) ≠ 0; No solution or infinitely many ⟺ det(A) = 0"},
            {"title": "Minors and Cofactors", "question": "Find the minor and cofactor of element a₂₃ in A = [[1,2,3],[4,5,6],[7,8,9]].", "background": "The minor Mᵢⱼ of element aᵢⱼ is the determinant of the submatrix obtained by deleting the i-th row and j-th column. The cofactor Cᵢⱼ = (-1)ᵢ⁺ʲMᵢⱼ. Minors and cofactors are used in finding determinants, adjoints, and inverses of matrices.", "solution": "For a₂₃ = 6, delete row 2 and column 3: M₂₃ = det([[1,2],[7,8]]) = 1×8 - 2×7 = 8 - 14 = -6. The cofactor C₂₃ = (-1)²⁺³M₂₃ = (-1)⁵(-6) = -1(-6) = 6.", "tips": ["<li>Delete the i-th row and j-th column</li>", "<li>Find determinant of remaining matrix</li>", "<li>Use Cᵢⱼ = (-1)ᵢ⁺ʲMᵢⱼ</li>", "<li>Check the sign carefully</li>", "<li>Verify with expansion formula</li>"], "formulas": "Mᵢⱼ = det(submatrix); Cᵢⱼ = (-1)ᵢ⁺ʲMᵢⱼ"},
            {"title": "Determinant Expansion", "question": "Expand the determinant of A = [[2,1,0],[1,3,2],[0,1,1]] along the first row.", "background": "The determinant can be expanded along any row or column using the formula det(A) = Σⱼ aᵢⱼCᵢⱼ where Cᵢⱼ is the cofactor. Expanding along the first row: det(A) = a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃. This method is useful for larger matrices.", "solution": "Expanding along first row: det(A) = 2C₁₁ + 1C₁₂ + 0C₁₃ = 2det([[3,2],[1,1]]) - 1det([[1,2],[0,1]]) + 0 = 2(3×1-2×1) - 1(1×1-2×0) = 2(3-2) - 1(1-0) = 2(1) - 1(1) = 2 - 1 = 1.", "tips": ["<li>Use det(A) = Σⱼ aᵢⱼCᵢⱼ</li>", "<li>Calculate each cofactor</li>", "<li>Alternate signs: +, -, +</li>", "<li>Check arithmetic</li>", "<li>Verify with other methods</li>"], "formulas": "det(A) = Σⱼ aᵢⱼCᵢⱼ; Cᵢⱼ = (-1)ᵢ⁺ʲMᵢⱼ"},
            {"title": "Volume of Parallelepiped", "question": "Find the volume of parallelepiped formed by vectors a = (1,2,3), b = (2,1,1), c = (3,2,1).", "background": "The volume of a parallelepiped formed by vectors a, b, c is |det([a;b;c])| where [a;b;c] is the matrix with a, b, c as rows. This formula uses the scalar triple product. The volume is zero if the vectors are coplanar (linearly dependent).", "solution": "The volume is |det([[1,2,3],[2,1,1],[3,2,1]])| = |1(1×1-1×2) - 2(2×1-1×3) + 3(2×2-1×3)| = |1(1-2) - 2(2-3) + 3(4-3)| = |1(-1) - 2(-1) + 3(1)| = |-1 + 2 + 3| = |4| = 4.", "tips": ["<li>Form matrix with vectors as rows</li>", "<li>Find determinant</li>", "<li>Take absolute value</li>", "<li>Check if vectors are coplanar</li>", "<li>Verify with scalar triple product</li>"], "formulas": "Volume = |det([a;b;c])|; Scalar triple product = a·(b×c)"},
            {"title": "Inverse using Adjoint", "question": "Find the inverse of A = [[2,1],[3,2]] using the adjoint method.", "background": "The inverse of a matrix A can be found using A⁻¹ = (1/det(A))adj(A). This method works for any invertible matrix. First find the determinant, then the adjoint, and finally divide by the determinant. This is an alternative to the elementary row operations method.", "solution": "First, det(A) = 2×2 - 1×3 = 4 - 3 = 1. The adjoint is adj(A) = [[2,-1],[-3,2]]. Therefore A⁻¹ = (1/1)[[2,-1],[-3,2]] = [[2,-1],[-3,2]].", "tips": ["<li>Find det(A)</li>", "<li>Calculate adj(A)</li>", "<li>Use A⁻¹ = (1/det(A))adj(A)</li>", "<li>Check AA⁻¹ = I</li>", "<li>Verify with other methods</li>"], "formulas": "A⁻¹ = (1/det(A))adj(A); adj(A) = transpose of cofactor matrix"},
            {"title": "Applications", "question": "A triangle has vertices A(0,0), B(3,0), C(1,2). Find its area and check if the points are collinear.", "background": "Determinants are used in coordinate geometry to find areas and check collinearity. Three points are collinear if and only if the area of the triangle formed by them is zero. The area formula using determinants is more efficient than using the distance formula and Heron's formula.", "solution": "Using the area formula: Area = (1/2)|det([[0,0,1],[3,0,1],[1,2,1]])| = (1/2)|0(0×1-1×2) - 0(3×1-1×1) + 1(3×2-0×1)| = (1/2)|0 - 0 + 1(6-0)| = (1/2)|6| = 3. Since the area is non-zero, the points are not collinear.", "tips": ["<li>Use determinant formula for area</li>", "<li>Check if area = 0 for collinearity</li>", "<li>Include 1 in third column</li>", "<li>Take absolute value</li>", "<li>Verify with other methods</li>"], "formulas": "Area = (1/2)|det([[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]])|; Collinear ⟺ Area = 0"}
        ]
    },
    5: {
        "title": "Continuity and Differentiability",
        "problems": [
            {"title": "Continuity", "question": "Check if f(x) = {x² if x < 1, 2x-1 if x ≥ 1} is continuous at x = 1.", "background": "A function f is continuous at x = a if lim(x→a) f(x) = f(a). This requires: (1) f(a) exists, (2) lim(x→a) f(x) exists, (3) lim(x→a) f(x) = f(a). For piecewise functions, check left and right limits separately. Continuity is essential for differentiability.", "solution": "At x = 1: f(1) = 2(1) - 1 = 1. Left limit: lim(x→1⁻) f(x) = lim(x→1⁻) x² = 1. Right limit: lim(x→1⁺) f(x) = lim(x→1⁺) (2x-1) = 1. Since lim(x→1) f(x) = f(1) = 1, f is continuous at x = 1.", "tips": ["<li>Check f(a) exists</li>", "<li>Find left and right limits</li>", "<li>Check if limits are equal</li>", "<li>Verify lim(x→a) f(x) = f(a)</li>", "<li>Use appropriate formulas for each piece</li>"], "formulas": "f continuous at x = a ⟺ lim(x→a) f(x) = f(a)"},
            {"title": "Differentiability", "question": "Check if f(x) = |x| is differentiable at x = 0.", "background": "A function f is differentiable at x = a if f'(a) exists. This requires the left and right derivatives to exist and be equal. For f(x) = |x|, the derivative is f'(x) = 1 for x > 0 and f'(x) = -1 for x < 0. At x = 0, the left and right derivatives are different, so f is not differentiable at x = 0.", "solution": "For x > 0: f(x) = x, so f'(x) = 1. For x < 0: f(x) = -x, so f'(x) = -1. At x = 0: Left derivative = lim(h→0⁻) (f(0+h)-f(0))/h = lim(h→0⁻) (|h|-0)/h = lim(h→0⁻) (-h)/h = -1. Right derivative = lim(h→0⁺) (f(0+h)-f(0))/h = lim(h→0⁺) (|h|-0)/h = lim(h→0⁺) h/h = 1. Since left derivative ≠ right derivative, f is not differentiable at x = 0.", "tips": ["<li>Find left and right derivatives</li>", "<li>Use definition of derivative</li>", "<li>Check if they are equal</li>", "<li>Consider the function definition</li>", "<li>Verify with graph</li>"], "formulas": "f'(a) = lim(h→0) (f(a+h)-f(a))/h; Differentiable ⟺ left derivative = right derivative"},
            {"title": "Chain Rule", "question": "Find the derivative of f(x) = sin(x² + 1).", "background": "The chain rule states that if f(x) = g(h(x)), then f'(x) = g'(h(x))·h'(x). This is used for composite functions. The chain rule can be extended to multiple compositions. It's one of the most important rules in calculus and is used extensively in finding derivatives.", "solution": "Let g(u) = sin(u) and h(x) = x² + 1, so f(x) = g(h(x)). Then g'(u) = cos(u) and h'(x) = 2x. By the chain rule: f'(x) = g'(h(x))·h'(x) = cos(x² + 1)·2x = 2x cos(x² + 1).", "tips": ["<li>Identify inner and outer functions</li>", "<li>Find derivatives of both</li>", "<li>Use f'(x) = g'(h(x))·h'(x)</li>", "<li>Substitute back</li>", "<li>Simplify the result</li>"], "formulas": "Chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x)"},
            {"title": "Product Rule", "question": "Find the derivative of f(x) = x² sin(x).", "background": "The product rule states that if f(x) = u(x)v(x), then f'(x) = u'(x)v(x) + u(x)v'(x). This is used for functions that are products of two other functions. The product rule can be extended to products of more than two functions. It's essential for finding derivatives of polynomial and trigonometric functions.", "solution": "Let u(x) = x² and v(x) = sin(x). Then u'(x) = 2x and v'(x) = cos(x). By the product rule: f'(x) = u'(x)v(x) + u(x)v'(x) = 2x sin(x) + x² cos(x).", "tips": ["<li>Identify u(x) and v(x)</li>", "<li>Find u'(x) and v'(x)</li>", "<li>Use f'(x) = u'(x)v(x) + u(x)v'(x)</li>", "<li>Substitute and simplify</li>", "<li>Check with other methods</li>"], "formulas": "Product rule: d/dx[u(x)v(x)] = u'(x)v(x) + u(x)v'(x)"},
            {"title": "Quotient Rule", "question": "Find the derivative of f(x) = (x² + 1)/(x + 1).", "background": "The quotient rule states that if f(x) = u(x)/v(x), then f'(x) = (u'(x)v(x) - u(x)v'(x))/v(x)². This is used for functions that are quotients of two other functions. The quotient rule is derived from the product rule. It's important to remember the order: numerator derivative times denominator minus numerator times denominator derivative.", "solution": "Let u(x) = x² + 1 and v(x) = x + 1. Then u'(x) = 2x and v'(x) = 1. By the quotient rule: f'(x) = (u'(x)v(x) - u(x)v'(x))/v(x)² = (2x(x + 1) - (x² + 1)(1))/(x + 1)² = (2x² + 2x - x² - 1)/(x + 1)² = (x² + 2x - 1)/(x + 1)².", "tips": ["<li>Identify u(x) and v(x)</li>", "<li>Find u'(x) and v'(x)</li>", "<li>Use f'(x) = (u'(x)v(x) - u(x)v'(x))/v(x)²</li>", "<li>Expand and simplify</li>", "<li>Check with polynomial division</li>"], "formulas": "Quotient rule: d/dx[u(x)/v(x)] = (u'(x)v(x) - u(x)v'(x))/v(x)²"},
            {"title": "Implicit Differentiation", "question": "Find dy/dx if x² + y² = 25.", "background": "Implicit differentiation is used when y is not explicitly expressed as a function of x. We differentiate both sides with respect to x, treating y as a function of x. This requires using the chain rule for terms involving y. The result gives dy/dx in terms of x and y.", "solution": "Differentiating both sides with respect to x: d/dx[x² + y²] = d/dx[25]. This gives 2x + 2y(dy/dx) = 0. Solving for dy/dx: 2y(dy/dx) = -2x, so dy/dx = -2x/(2y) = -x/y.", "tips": ["<li>Differentiate both sides with respect to x</li>", "<li>Use chain rule for y terms</li>", "<li>Solve for dy/dx</li>", "<li>Simplify the result</li>", "<li>Check with explicit form if possible</li>"], "formulas": "For F(x,y) = 0: dF/dx + (dF/dy)(dy/dx) = 0"},
            {"title": "Higher Order Derivatives", "question": "Find the second derivative of f(x) = x³ - 3x² + 2x.", "background": "The second derivative f''(x) is the derivative of the first derivative f'(x). It represents the rate of change of the slope. Higher order derivatives are found by repeatedly differentiating. The second derivative is used to determine concavity and inflection points.", "solution": "First derivative: f'(x) = 3x² - 6x + 2. Second derivative: f''(x) = d/dx[3x² - 6x + 2] = 6x - 6.", "tips": ["<li>Find first derivative</li>", "<li>Differentiate again</li>", "<li>Simplify the result</li>", "<li>Check with power rule</li>", "<li>Use for concavity analysis</li>"], "formulas": "f''(x) = d/dx[f'(x)]; Power rule: d/dx[xⁿ] = nxⁿ⁻¹"},
            {"title": "Logarithmic Differentiation", "question": "Find the derivative of f(x) = xˣ.", "background": "Logarithmic differentiation is used for functions of the form f(x) = g(x)ʰ⁽ˣ⁾. We take the natural logarithm of both sides and then differentiate. This method is useful when both the base and exponent are functions of x. The key steps are: take ln, differentiate, solve for f'(x).", "solution": "Taking natural logarithm: ln(f(x)) = ln(xˣ) = x ln(x). Differentiating both sides: (1/f(x))f'(x) = d/dx[x ln(x)] = 1·ln(x) + x·(1/x) = ln(x) + 1. Therefore f'(x) = f(x)(ln(x) + 1) = xˣ(ln(x) + 1).", "tips": ["<li>Take natural logarithm of both sides</li>", "<li>Use properties of logarithms</li>", "<li>Differentiate both sides</li>", "<li>Solve for f'(x)</li>", "<li>Substitute back for f(x)</li>"], "formulas": "For f(x) = g(x)ʰ⁽ˣ⁾: ln(f(x)) = h(x)ln(g(x)), then differentiate"},
            {"title": "Parametric Differentiation", "question": "Find dy/dx if x = t², y = t³.", "background": "Parametric differentiation is used when x and y are both functions of a parameter t. The derivative dy/dx is found using dy/dx = (dy/dt)/(dx/dt). This method is useful for curves defined parametrically. The parameter t often represents time in physical applications.", "solution": "Given x = t² and y = t³. Then dx/dt = 2t and dy/dt = 3t². Therefore dy/dx = (dy/dt)/(dx/dt) = (3t²)/(2t) = 3t/2.", "tips": ["<li>Find dx/dt and dy/dt</li>", "<li>Use dy/dx = (dy/dt)/(dx/dt)</li>", "<li>Simplify the result</li>", "<li>Check with elimination method</li>", "<li>Consider domain restrictions</li>"], "formulas": "For x = f(t), y = g(t): dy/dx = (dy/dt)/(dx/dt)"},
            {"title": "Applications", "question": "A particle moves along the curve y = x². When x = 2, the particle is moving at 3 units/sec in the x-direction. Find the rate of change of y.", "background": "Related rates problems involve finding the rate of change of one quantity with respect to time when the rate of change of another related quantity is known. We use the chain rule: dy/dt = (dy/dx)(dx/dt). This connects the rates of change of related variables.", "solution": "Given y = x², so dy/dx = 2x. When x = 2: dy/dx = 2(2) = 4. Also given dx/dt = 3. Using the chain rule: dy/dt = (dy/dx)(dx/dt) = 4(3) = 12. Therefore y is changing at 12 units/sec when x = 2.", "tips": ["<li>Find dy/dx</li>", "<li>Evaluate at given point</li>", "<li>Use dy/dt = (dy/dx)(dx/dt)</li>", "<li>Substitute known values</li>", "<li>Check units and interpretation</li>"], "formulas": "Chain rule: dy/dt = (dy/dx)(dx/dt); Related rates: dy/dt = (dy/dx)(dx/dt)"}
        ]
    }
}

def generate_chapter(chapter_num, chapter_data):
    """Generate all problems for a chapter."""
    chapter_dir = Path(f"Maths/ch{chapter_num}")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    for i, problem in enumerate(chapter_data["problems"], 1):
        html_content = create_problem_html(
            chapter_num, i, problem["title"], problem["question"],
            problem["background"], problem["solution"], 
            "\n".join(problem["tips"]), problem["formulas"]
        )
        
        output_file = chapter_dir / f"problem-{chapter_num}-{i:02d}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {output_file}")

def main():
    """Generate maths problems for chapters 4-5."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
