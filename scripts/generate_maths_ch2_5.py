#!/usr/bin/env python3
"""Generate Maths problems for Chapters 2-5 - 12th Board 2026."""

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

# Chapters 2-5 data
chapters_data = {
    2: {
        "title": "Inverse Trigonometric Functions",
        "problems": [
            {"title": "Principal Values", "question": "Find the principal value of sin⁻¹(-1/2).", "background": "Inverse trigonometric functions are the inverse operations of trigonometric functions. The principal value is the value in the principal range: sin⁻¹: [-π/2, π/2], cos⁻¹: [0, π], tan⁻¹: (-π/2, π/2). These functions are one-to-one on their principal ranges.", "solution": "We need to find θ such that sin θ = -1/2 and -π/2 ≤ θ ≤ π/2. Since sin(-π/6) = -1/2 and -π/6 ∈ [-π/2, π/2], the principal value is -π/6.", "tips": ["<li>Use principal range for sin⁻¹: [-π/2, π/2]</li>", "<li>Find angle with given sine value</li>", "<li>Check if angle is in principal range</li>", "<li>Use reference angles</li>", "<li>Consider sign of the value</li>"], "formulas": "sin⁻¹: [-π/2, π/2], cos⁻¹: [0, π], tan⁻¹: (-π/2, π/2)"},
            {"title": "Domain and Range", "question": "Find domain and range of f(x) = cos⁻¹(2x - 1).", "background": "For cos⁻¹(f(x)), the domain requires -1 ≤ f(x) ≤ 1. The range of cos⁻¹ is [0, π]. To find domain, solve -1 ≤ 2x - 1 ≤ 1, which gives 0 ≤ 2x ≤ 2, so 0 ≤ x ≤ 1. The range remains [0, π].", "solution": "Domain: For cos⁻¹(2x - 1) to be defined, we need -1 ≤ 2x - 1 ≤ 1. This gives 0 ≤ 2x ≤ 2, so 0 ≤ x ≤ 1. Domain = [0, 1]. Range: Since cos⁻¹ has range [0, π], the range of f is [0, π].", "tips": ["<li>For cos⁻¹(f(x)): solve -1 ≤ f(x) ≤ 1</li>", "<li>Range of cos⁻¹ is [0, π]</li>", "<li>Solve compound inequality</li>", "<li>Express in interval notation</li>", "<li>Check endpoints</li>"], "formulas": "Domain of cos⁻¹(f(x)): -1 ≤ f(x) ≤ 1; Range of cos⁻¹: [0, π]"},
            {"title": "Properties", "question": "Prove that sin⁻¹(x) + cos⁻¹(x) = π/2 for -1 ≤ x ≤ 1.", "background": "Inverse trigonometric functions have important properties. The identity sin⁻¹(x) + cos⁻¹(x) = π/2 holds for all x ∈ [-1, 1]. This can be proved by showing that if θ = sin⁻¹(x), then cos⁻¹(x) = π/2 - θ. These properties are useful in solving equations and simplifying expressions.", "solution": "Let θ = sin⁻¹(x), so sin θ = x. Since sin²θ + cos²θ = 1, we have cos²θ = 1 - x², so cos θ = ±√(1 - x²). Since θ ∈ [-π/2, π/2], cos θ ≥ 0, so cos θ = √(1 - x²). Therefore, cos⁻¹(x) = π/2 - θ = π/2 - sin⁻¹(x). Hence sin⁻¹(x) + cos⁻¹(x) = π/2.", "tips": ["<li>Let θ = sin⁻¹(x)</li>", "<li>Use sin²θ + cos²θ = 1</li>", "<li>Consider the range of θ</li>", "<li>Use cos⁻¹(x) = π/2 - θ</li>", "<li>Verify the identity</li>"], "formulas": "sin⁻¹(x) + cos⁻¹(x) = π/2; sin²θ + cos²θ = 1"},
            {"title": "Composition", "question": "Simplify cos(sin⁻¹(x)).", "background": "Composition of trigonometric and inverse trigonometric functions can be simplified using right triangles or identities. For cos(sin⁻¹(x)), we can use the identity cos²θ = 1 - sin²θ. If θ = sin⁻¹(x), then sin θ = x, and we can find cos θ using the Pythagorean identity.", "solution": "Let θ = sin⁻¹(x), so sin θ = x. Using the identity cos²θ = 1 - sin²θ, we have cos²θ = 1 - x². Since θ ∈ [-π/2, π/2], cos θ ≥ 0, so cos θ = √(1 - x²). Therefore, cos(sin⁻¹(x)) = √(1 - x²).", "tips": ["<li>Let θ = sin⁻¹(x)</li>", "<li>Use cos²θ = 1 - sin²θ</li>", "<li>Consider the range of θ</li>", "<li>Take positive square root</li>", "<li>Verify with specific values</li>"], "formulas": "cos(sin⁻¹(x)) = √(1 - x²); cos²θ = 1 - sin²θ"},
            {"title": "Equations", "question": "Solve: 2sin⁻¹(x) = cos⁻¹(x).", "background": "Equations involving inverse trigonometric functions can be solved using properties and identities. For 2sin⁻¹(x) = cos⁻¹(x), we can use the identity sin⁻¹(x) + cos⁻¹(x) = π/2 to get 2sin⁻¹(x) = π/2 - sin⁻¹(x), so 3sin⁻¹(x) = π/2, giving sin⁻¹(x) = π/6.", "solution": "Using the identity sin⁻¹(x) + cos⁻¹(x) = π/2, we have cos⁻¹(x) = π/2 - sin⁻¹(x). Substituting: 2sin⁻¹(x) = π/2 - sin⁻¹(x), so 3sin⁻¹(x) = π/2. Therefore sin⁻¹(x) = π/6, so x = sin(π/6) = 1/2.", "tips": ["<li>Use sin⁻¹(x) + cos⁻¹(x) = π/2</li>", "<li>Substitute for cos⁻¹(x)</li>", "<li>Solve for sin⁻¹(x)</li>", "<li>Find x = sin(π/6)</li>", "<li>Check the solution</li>"], "formulas": "sin⁻¹(x) + cos⁻¹(x) = π/2; sin(π/6) = 1/2"},
            {"title": "Derivatives", "question": "Find the derivative of f(x) = tan⁻¹(x²).", "background": "The derivatives of inverse trigonometric functions are: d/dx[sin⁻¹(x)] = 1/√(1-x²), d/dx[cos⁻¹(x)] = -1/√(1-x²), d/dx[tan⁻¹(x)] = 1/(1+x²). For composite functions, use the chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x).", "solution": "Using the chain rule: f'(x) = d/dx[tan⁻¹(x²)] = (1/(1+(x²)²))·(2x) = 2x/(1+x⁴).", "tips": ["<li>Use d/dx[tan⁻¹(x)] = 1/(1+x²)</li>", "<li>Apply chain rule</li>", "<li>Differentiate x² to get 2x</li>", "<li>Substitute x² for x in formula</li>", "<li>Simplify the result</li>"], "formulas": "d/dx[tan⁻¹(x)] = 1/(1+x²); Chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x)"},
            {"title": "Integration", "question": "Evaluate ∫(1/√(1-x²)) dx.", "background": "The integral ∫(1/√(1-x²)) dx = sin⁻¹(x) + C. This is a standard integral that appears frequently. The domain of integration must be (-1, 1) for the integral to be real. This integral is related to the derivative of sin⁻¹(x).", "solution": "∫(1/√(1-x²)) dx = sin⁻¹(x) + C. This is a standard integral. The domain of integration is (-1, 1).", "tips": ["<li>Use standard integral formula</li>", "<li>Check domain of integration</li>", "<li>Add constant of integration</li>", "<li>Verify by differentiation</li>", "<li>Consider substitution if needed</li>"], "formulas": "∫(1/√(1-x²)) dx = sin⁻¹(x) + C"},
            {"title": "Graphs", "question": "Sketch the graph of y = tan⁻¹(x) and state its domain and range.", "background": "The graph of y = tan⁻¹(x) is the reflection of y = tan(x) across the line y = x, restricted to the principal range. It has horizontal asymptotes at y = ±π/2. The domain is (-∞, ∞) and the range is (-π/2, π/2). The function is increasing and has an inflection point at (0, 0).", "solution": "The graph of y = tan⁻¹(x) has domain (-∞, ∞) and range (-π/2, π/2). It passes through (0, 0) and has horizontal asymptotes at y = ±π/2. The function is increasing and has an inflection point at the origin.", "tips": ["<li>Domain: (-∞, ∞)</li>", "<li>Range: (-π/2, π/2)</li>", "<li>Horizontal asymptotes at y = ±π/2</li>", "<li>Passes through (0, 0)</li>", "<li>Increasing function</li>"], "formulas": "Domain: (-∞, ∞); Range: (-π/2, π/2); Asymptotes: y = ±π/2"},
            {"title": "Identities", "question": "Prove that tan⁻¹(x) + tan⁻¹(y) = tan⁻¹((x+y)/(1-xy)) for xy < 1.", "background": "The addition formula for tan⁻¹ is tan⁻¹(x) + tan⁻¹(y) = tan⁻¹((x+y)/(1-xy)) when xy < 1. This identity is useful for simplifying expressions involving multiple inverse tangent functions. The condition xy < 1 ensures the result is in the principal range.", "solution": "Let α = tan⁻¹(x) and β = tan⁻¹(y), so tan α = x and tan β = y. Using the addition formula for tangent: tan(α + β) = (tan α + tan β)/(1 - tan α tan β) = (x + y)/(1 - xy). Since xy < 1, we have α + β = tan⁻¹((x + y)/(1 - xy)). Therefore tan⁻¹(x) + tan⁻¹(y) = tan⁻¹((x + y)/(1 - xy)).", "tips": ["<li>Let α = tan⁻¹(x) and β = tan⁻¹(y)</li>", "<li>Use tan(α + β) = (tan α + tan β)/(1 - tan α tan β)</li>", "<li>Check condition xy < 1</li>", "<li>Apply tan⁻¹ to both sides</li>", "<li>Verify with specific values</li>"], "formulas": "tan⁻¹(x) + tan⁻¹(y) = tan⁻¹((x+y)/(1-xy)) for xy < 1"},
            {"title": "Applications", "question": "A ladder 10 m long leans against a wall. If the foot of the ladder is 6 m from the wall, find the angle the ladder makes with the ground.", "background": "Inverse trigonometric functions are used to find angles in right triangles. Given two sides, we can use inverse trigonometric functions to find the angle. For a right triangle with adjacent side a and hypotenuse h, the angle θ satisfies cos θ = a/h, so θ = cos⁻¹(a/h).", "solution": "In the right triangle formed by the ladder, wall, and ground, the adjacent side is 6 m and the hypotenuse is 10 m. The angle θ satisfies cos θ = 6/10 = 0.6. Therefore θ = cos⁻¹(0.6) ≈ 53.13°.", "tips": ["<li>Identify the right triangle</li>", "<li>Use cos θ = adjacent/hypotenuse</li>", "<li>Apply cos⁻¹ to find angle</li>", "<li>Check the answer makes sense</li>", "<li>Use calculator for numerical value</li>"], "formulas": "cos θ = adjacent/hypotenuse; θ = cos⁻¹(adjacent/hypotenuse)"}
        ]
    },
    3: {
        "title": "Matrices",
        "problems": [
            {"title": "Matrix Operations", "question": "If A = [[1,2],[3,4]] and B = [[5,6],[7,8]], find A + B and A - B.", "background": "Matrices are rectangular arrays of numbers. Matrix addition and subtraction are performed element-wise. For matrices A and B of the same size, (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ and (A - B)ᵢⱼ = Aᵢⱼ - Bᵢⱼ. Matrices must have the same dimensions for addition and subtraction.", "solution": "A + B = [[1+5, 2+6], [3+7, 4+8]] = [[6, 8], [10, 12]]. A - B = [[1-5, 2-6], [3-7, 4-8]] = [[-4, -4], [-4, -4]].", "tips": ["<li>Add/subtract corresponding elements</li>", "<li>Matrices must have same size</li>", "<li>Check each element carefully</li>", "<li>Verify dimensions of result</li>", "<li>Use systematic approach</li>"], "formulas": "(A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ; (A - B)ᵢⱼ = Aᵢⱼ - Bᵢⱼ"},
            {"title": "Matrix Multiplication", "question": "If A = [[1,2],[3,4]] and B = [[5,6],[7,8]], find AB.", "background": "Matrix multiplication is defined as (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ. The number of columns in A must equal the number of rows in B. The result has the same number of rows as A and the same number of columns as B. Matrix multiplication is not commutative: AB ≠ BA in general.", "solution": "AB = [[1×5+2×7, 1×6+2×8], [3×5+4×7, 3×6+4×8]] = [[5+14, 6+16], [15+28, 18+32]] = [[19, 22], [43, 50]].", "tips": ["<li>Use (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ</li>", "<li>Check dimensions: A is m×n, B is n×p</li>", "<li>Result is m×p</li>", "<li>Multiply row by column</li>", "<li>Verify each element</li>"], "formulas": "(AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ; Dimensions: (m×n)(n×p) = (m×p)"},
            {"title": "Transpose", "question": "Find the transpose of A = [[1,2,3],[4,5,6]].", "background": "The transpose of a matrix A, denoted Aᵀ, is obtained by interchanging rows and columns. If A is m×n, then Aᵀ is n×m. The element at position (i,j) in A becomes the element at position (j,i) in Aᵀ. Properties: (Aᵀ)ᵀ = A, (A + B)ᵀ = Aᵀ + Bᵀ, (AB)ᵀ = BᵀAᵀ.", "solution": "Aᵀ = [[1,4],[2,5],[3,6]]. The first row [1,2,3] becomes the first column, and the second row [4,5,6] becomes the second column.", "tips": ["<li>Interchange rows and columns</li>", "<li>First row becomes first column</li>", "<li>Check dimensions: m×n becomes n×m</li>", "<li>Verify each element position</li>", "<li>Use systematic approach</li>"], "formulas": "Aᵀᵢⱼ = Aⱼᵢ; (Aᵀ)ᵀ = A"},
            {"title": "Determinant", "question": "Find the determinant of A = [[2,3],[4,5]].", "background": "The determinant of a 2×2 matrix [[a,b],[c,d]] is ad - bc. The determinant is a scalar value that can be computed for square matrices. It has important properties: det(AB) = det(A)det(B), det(Aᵀ) = det(A), det(kA) = kⁿdet(A) for n×n matrix A.", "solution": "det(A) = (2)(5) - (3)(4) = 10 - 12 = -2.", "tips": ["<li>Use formula: det([[a,b],[c,d]]) = ad - bc</li>", "<li>Multiply diagonal elements</li>", "<li>Subtract product of off-diagonal elements</li>", "<li>Check the sign</li>", "<li>Verify with properties</li>"], "formulas": "det([[a,b],[c,d]]) = ad - bc"},
            {"title": "Inverse Matrix", "question": "Find the inverse of A = [[2,1],[3,2]].", "background": "The inverse of a 2×2 matrix A = [[a,b],[c,d]] is A⁻¹ = (1/det(A))[[d,-b],[-c,a]]. A matrix has an inverse if and only if its determinant is non-zero. Properties: AA⁻¹ = A⁻¹A = I, (AB)⁻¹ = B⁻¹A⁻¹, (Aᵀ)⁻¹ = (A⁻¹)ᵀ.", "solution": "First, det(A) = (2)(2) - (1)(3) = 4 - 3 = 1. Since det(A) ≠ 0, A has an inverse. A⁻¹ = (1/1)[[2,-1],[-3,2]] = [[2,-1],[-3,2]].", "tips": ["<li>Check if det(A) ≠ 0</li>", "<li>Use formula: A⁻¹ = (1/det(A))[[d,-b],[-c,a]]</li>", "<li>Swap diagonal elements</li>", "<li>Change sign of off-diagonal elements</li>", "<li>Verify AA⁻¹ = I</li>"], "formulas": "A⁻¹ = (1/det(A))[[d,-b],[-c,a]]; AA⁻¹ = A⁻¹A = I"},
            {"title": "System of Equations", "question": "Solve using matrices: 2x + y = 5, 3x + 2y = 8.", "background": "A system of linear equations can be written as AX = B, where A is the coefficient matrix, X is the variable matrix, and B is the constant matrix. If A is invertible, then X = A⁻¹B. This method is useful for systems with the same number of equations and variables.", "solution": "The system can be written as [[2,1],[3,2]][[x],[y]] = [[5],[8]]. From the previous problem, A⁻¹ = [[2,-1],[-3,2]]. So [[x],[y]] = [[2,-1],[-3,2]][[5],[8]] = [[10-8],[-15+16]] = [[2],[1]]. Therefore x = 2, y = 1.", "tips": ["<li>Write system as AX = B</li>", "<li>Find A⁻¹</li>", "<li>Use X = A⁻¹B</li>", "<li>Check the solution</li>", "<li>Verify with original equations</li>"], "formulas": "AX = B; X = A⁻¹B"},
            {"title": "Elementary Operations", "question": "Use elementary row operations to find the inverse of A = [[1,2],[3,4]].", "background": "Elementary row operations are: (1) Interchange two rows, (2) Multiply a row by a non-zero constant, (3) Add a multiple of one row to another. To find A⁻¹, form the augmented matrix [A|I] and use elementary row operations to transform it to [I|A⁻¹].", "solution": "Form [A|I] = [[1,2|1,0],[3,4|0,1]]. R₂ → R₂ - 3R₁: [[1,2|1,0],[0,-2|-3,1]]. R₂ → (-1/2)R₂: [[1,2|1,0],[0,1|3/2,-1/2]]. R₁ → R₁ - 2R₂: [[1,0|-2,1],[0,1|3/2,-1/2]]. Therefore A⁻¹ = [[-2,1],[3/2,-1/2]].", "tips": ["<li>Form augmented matrix [A|I]</li>", "<li>Use elementary row operations</li>", "<li>Transform to [I|A⁻¹]</li>", "<li>Check each step</li>", "<li>Verify AA⁻¹ = I</li>"], "formulas": "Use [A|I] → [I|A⁻¹] using elementary row operations"},
            {"title": "Rank", "question": "Find the rank of A = [[1,2,3],[2,4,6],[1,1,1]].", "background": "The rank of a matrix is the maximum number of linearly independent rows (or columns). It can be found by reducing the matrix to row-echelon form and counting the non-zero rows. The rank is important in determining the number of solutions to a system of linear equations.", "solution": "Using elementary row operations: R₂ → R₂ - 2R₁: [[1,2,3],[0,0,0],[1,1,1]]. R₃ → R₃ - R₁: [[1,2,3],[0,0,0],[0,-1,-2]]. R₂ ↔ R₃: [[1,2,3],[0,-1,-2],[0,0,0]]. R₂ → -R₂: [[1,2,3],[0,1,2],[0,0,0]]. The matrix has 2 non-zero rows, so rank(A) = 2.", "tips": ["<li>Reduce to row-echelon form</li>", "<li>Count non-zero rows</li>", "<li>Use elementary row operations</li>", "<li>Check linear independence</li>", "<li>Verify the result</li>"], "formulas": "Rank = number of linearly independent rows"},
            {"title": "Eigenvalues", "question": "Find the eigenvalues of A = [[3,1],[1,3]].", "background": "An eigenvalue λ of matrix A satisfies det(A - λI) = 0. For a 2×2 matrix [[a,b],[c,d]], the characteristic equation is λ² - (a+d)λ + (ad-bc) = 0. Eigenvalues are important in many applications including stability analysis and principal component analysis.", "solution": "The characteristic equation is det(A - λI) = det([[3-λ,1],[1,3-λ]]) = (3-λ)² - 1 = λ² - 6λ + 8 = 0. Solving: λ = (6 ± √(36-32))/2 = (6 ± 2)/2 = 4 or 2. Therefore the eigenvalues are λ₁ = 4 and λ₂ = 2.", "tips": ["<li>Form A - λI</li>", "<li>Find det(A - λI) = 0</li>", "<li>Solve the characteristic equation</li>", "<li>Check both eigenvalues</li>", "<li>Verify by substitution</li>"], "formulas": "det(A - λI) = 0; For 2×2: λ² - (a+d)λ + (ad-bc) = 0"},
            {"title": "Applications", "question": "A company produces two products. The profit matrix is P = [[10,15],[20,25]] where Pᵢⱼ is profit from product i in market j. Find total profit if 100 units of product 1 and 150 units of product 2 are sold.", "background": "Matrices are used in business applications to model production, costs, and profits. The total profit can be calculated using matrix multiplication. If Q is the quantity matrix and P is the profit matrix, then total profit = QᵀP, where Qᵀ is the transpose of Q.", "solution": "The quantity matrix is Q = [[100],[150]]. The total profit is QᵀP = [100, 150][[10,15],[20,25]] = [100×10+150×20, 100×15+150×25] = [1000+3000, 1500+3750] = [4000, 5250]. Therefore total profit is 4000 + 5250 = 9250.", "tips": ["<li>Form quantity matrix Q</li>", "<li>Use QᵀP for total profit</li>", "<li>Multiply matrices carefully</li>", "<li>Sum the results</li>", "<li>Check units and interpretation</li>"], "formulas": "Total profit = QᵀP; Qᵀ = transpose of quantity matrix"}
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
    """Generate maths problems for chapters 2-3."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
