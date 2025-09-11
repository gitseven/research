#!/usr/bin/env python3
"""Generate comprehensive Maths problems for 12th Board 2026 - All Chapters."""

from pathlib import Path

def create_problem_html(chapter, problem_num, title, question, background, solution, tips, formulas, visualization_svg):
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
    h3 {{ margin:16px 0 6px; font-size:18px; color:#7c3aed; }}
    .panel {{ background:#ffffff; border:1px solid #e5e7eb; border-radius:10px; padding:16px; margin:16px 0; }}
    .q {{ border-left:3px solid #f59e0b; padding-left:10px; }}
    .solution {{ border-left:3px solid #10b981; padding-left:10px; background:#f0fdf4; }}
    .concept-section {{ background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:12px; margin:12px 0; }}
    .math-diagram {{ max-width:100%; height:auto; display:block; margin:12px auto; border:1px solid #e5e7eb; border-radius:8px; background:#fafafa; }}
    code {{ background:#f8fafc; border:1px solid #e5e7eb; padding:2px 6px; border-radius:6px; font-family: 'Courier New', monospace; }}
    .muted {{ color:#374151; }}
    ul {{ margin:8px 0 8px 20px; }}
    li {{ margin:4px 0; }}
    .formula {{ background:#fef3c7; border:1px solid #f59e0b; border-radius:6px; padding:8px; margin:8px 0; text-align:center; font-family: 'Courier New', monospace; }}
    .highlight {{ background:#fef3c7; padding:2px 4px; border-radius:4px; }}
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

    <div class="panel">
      <h2>Visualization</h2>
      {visualization_svg}
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

# Comprehensive Maths problems for all chapters
chapters_data = {
    1: {
        "title": "Relations and Functions",
        "problems": [
            {
                "title": "Types of Relations",
                "question": "Let A = {1, 2, 3, 4} and R = {(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)}. Check if R is reflexive, symmetric, and transitive.",
                "background": "A relation R on set A is: <strong>Reflexive</strong> if (a,a) ∈ R for all a ∈ A; <strong>Symmetric</strong> if (a,b) ∈ R implies (b,a) ∈ R; <strong>Transitive</strong> if (a,b) ∈ R and (b,c) ∈ R implies (a,c) ∈ R. An equivalence relation satisfies all three properties. Relations are fundamental in mathematics and computer science.",
                "solution": "Reflexive: Yes, as (1,1), (2,2), (3,3), (4,4) ∈ R. Symmetric: Yes, as (1,2) ∈ R and (2,1) ∈ R. Transitive: Yes, checking all combinations: (1,1) and (1,2) → (1,2) ∈ R ✓. Since R satisfies all three properties, it is an equivalence relation.",
                "tips": ["<li>Check reflexivity: (a,a) must be in R for all a</li>", "<li>Check symmetry: if (a,b) ∈ R, then (b,a) ∈ R</li>", "<li>Check transitivity: if (a,b) and (b,c) ∈ R, then (a,c) ∈ R</li>", "<li>Use systematic approach for each property</li>", "<li>Equivalence relation = reflexive + symmetric + transitive</li>"],
                "formulas": "Reflexive: (a,a) ∈ R ∀a ∈ A; Symmetric: (a,b) ∈ R ⟹ (b,a) ∈ R; Transitive: (a,b), (b,c) ∈ R ⟹ (a,c) ∈ R",
                "svg": '<svg viewBox="0 0 400 200" class="math-diagram"><circle cx="100" cy="100" r="60" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="105" text-anchor="middle" font-size="12" fill="#374151">A = {1,2,3,4}</text><text x="100" y="180" text-anchor="middle" font-size="10" fill="#6b7280">Reflexive, Symmetric, Transitive</text></svg>'
            },
            {
                "title": "One-to-One and Onto Functions",
                "question": "Let f: R → R be defined by f(x) = 2x + 3. Show that f is one-to-one and onto.",
                "background": "A function f: A → B is <strong>one-to-one (injective)</strong> if f(x₁) = f(x₂) implies x₁ = x₂. It is <strong>onto (surjective)</strong> if for every y ∈ B, there exists x ∈ A such that f(x) = y. A function that is both one-to-one and onto is called <strong>bijective</strong>. Linear functions f(x) = ax + b with a ≠ 0 are bijective.",
                "solution": "One-to-one: Let f(x₁) = f(x₂). Then 2x₁ + 3 = 2x₂ + 3, so 2x₁ = 2x₂, hence x₁ = x₂. Therefore f is one-to-one. Onto: For any y ∈ R, we need x such that f(x) = y. So 2x + 3 = y, giving x = (y-3)/2. Since (y-3)/2 ∈ R for any y ∈ R, f is onto. Therefore f is bijective.",
                "tips": ["<li>For one-to-one: assume f(x₁) = f(x₂) and show x₁ = x₂</li>", "<li>For onto: for any y, find x such that f(x) = y</li>", "<li>Linear functions f(x) = ax + b with a ≠ 0 are bijective</li>", "<li>Check domain and codomain carefully</li>", "<li>Bijective = one-to-one + onto</li>"],
                "formulas": "One-to-one: f(x₁) = f(x₂) ⟹ x₁ = x₂; Onto: ∀y ∈ B, ∃x ∈ A such that f(x) = y",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><line x1="50" y1="75" x2="350" y2="75" stroke="#6b7280" stroke-width="2"/><text x="200" y="95" text-anchor="middle" font-size="12" fill="#374151">f(x) = 2x + 3</text><text x="200" y="110" text-anchor="middle" font-size="10" fill="#6b7280">One-to-one and Onto</text></svg>'
            },
            {
                "title": "Composition of Functions",
                "question": "If f(x) = x² and g(x) = x + 1, find (f∘g)(x) and (g∘f)(x).",
                "background": "The <strong>composition</strong> of functions f and g is defined as (f∘g)(x) = f(g(x)). Composition is generally not commutative, i.e., (f∘g)(x) ≠ (g∘f)(x). The domain of f∘g is the set of all x in the domain of g such that g(x) is in the domain of f. Composition is associative: (f∘g)∘h = f∘(g∘h).",
                "solution": "(f∘g)(x) = f(g(x)) = f(x + 1) = (x + 1)² = x² + 2x + 1. (g∘f)(x) = g(f(x)) = g(x²) = x² + 1. Note that (f∘g)(x) ≠ (g∘f)(x), showing that composition is not commutative.",
                "tips": ["<li>Use (f∘g)(x) = f(g(x))</li>", "<li>Substitute g(x) into f</li>", "<li>Composition is not commutative</li>", "<li>Check domains of composition</li>", "<li>Simplify the final expression</li>"],
                "formulas": "(f∘g)(x) = f(g(x)); (g∘f)(x) = g(f(x))",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><rect x="50" y="50" width="80" height="40" fill="#f3f4f6" stroke="#6b7280"/><text x="90" y="75" text-anchor="middle" font-size="10" fill="#374151">g(x)</text><rect x="200" y="50" width="80" height="40" fill="#f3f4f6" stroke="#6b7280"/><text x="240" y="75" text-anchor="middle" font-size="10" fill="#374151">f(x)</text><text x="150" y="30" text-anchor="middle" font-size="10" fill="#6b7280">f∘g</text></svg>'
            },
            {
                "title": "Inverse Functions",
                "question": "Find the inverse of f(x) = (2x + 3)/(x - 1), x ≠ 1.",
                "background": "The <strong>inverse function</strong> f⁻¹ of f satisfies f⁻¹(f(x)) = x and f(f⁻¹(x)) = x. To find f⁻¹: (1) Replace f(x) with y, (2) Swap x and y, (3) Solve for y, (4) Replace y with f⁻¹(x). A function has an inverse if and only if it is bijective. The domain of f⁻¹ is the range of f, and vice versa.",
                "solution": "Let y = (2x + 3)/(x - 1). Swap x and y: x = (2y + 3)/(y - 1). Cross multiply: x(y - 1) = 2y + 3, so xy - x = 2y + 3. Collect y terms: xy - 2y = x + 3, so y(x - 2) = x + 3. Therefore y = (x + 3)/(x - 2). So f⁻¹(x) = (x + 3)/(x - 2), x ≠ 2.",
                "tips": ["<li>Replace f(x) with y</li>", "<li>Swap x and y</li>", "<li>Solve for y</li>", "<li>Replace y with f⁻¹(x)</li>", "<li>Check domain restrictions</li>"],
                "formulas": "f⁻¹(f(x)) = x, f(f⁻¹(x)) = x; To find f⁻¹: y = f(x) → x = f(y) → solve for y",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><line x1="50" y1="75" x2="150" y2="75" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow)"/><line x1="150" y1="75" x2="50" y2="75" stroke="#6b7280" stroke-width="2" marker-end="url(#arrow)"/><text x="100" y="60" text-anchor="middle" font-size="10" fill="#374151">f</text><text x="100" y="90" text-anchor="middle" font-size="10" fill="#374151">f⁻¹</text></svg>'
            },
            {
                "title": "Binary Operations",
                "question": "Let * be a binary operation on Z defined by a * b = a + b - ab. Show that * is commutative and associative.",
                "background": "A <strong>binary operation</strong> * on set S is a function from S × S to S. It is <strong>commutative</strong> if a * b = b * a for all a, b ∈ S. It is <strong>associative</strong> if (a * b) * c = a * (b * c) for all a, b, c ∈ S. Binary operations are fundamental in algebra and abstract mathematics.",
                "solution": "Commutative: a * b = a + b - ab = b + a - ba = b * a. Associative: (a * b) * c = (a + b - ab) * c = (a + b - ab) + c - (a + b - ab)c = a + b + c - ab - ac - bc + abc. a * (b * c) = a * (b + c - bc) = a + (b + c - bc) - a(b + c - bc) = a + b + c - bc - ab - ac + abc. Since both expressions are equal, * is associative.",
                "tips": ["<li>For commutative: show a * b = b * a</li>", "<li>For associative: show (a * b) * c = a * (b * c)</li>", "<li>Expand both sides completely</li>", "<li>Compare the final expressions</li>", "<li>Use algebraic manipulation</li>"],
                "formulas": "Commutative: a * b = b * a; Associative: (a * b) * c = a * (b * c)",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><circle cx="100" cy="75" r="30" fill="#f3f4f6" stroke="#6b7280"/><text x="100" y="80" text-anchor="middle" font-size="10" fill="#374151">a</text><circle cx="200" cy="75" r="30" fill="#f3f4f6" stroke="#6b7280"/><text x="200" y="80" text-anchor="middle" font-size="10" fill="#374151">b</text><text x="150" y="50" text-anchor="middle" font-size="12" fill="#374151">*</text></svg>'
            },
            {
                "title": "Identity and Inverse Elements",
                "question": "For the binary operation * on Z defined by a * b = a + b - ab, find the identity element and inverse of element 3.",
                "background": "An <strong>identity element</strong> e for operation * satisfies a * e = e * a = a for all a. An <strong>inverse</strong> of element a is an element b such that a * b = b * a = e. Not all elements have inverses. The identity is unique if it exists. Inverses are unique if they exist.",
                "solution": "Identity: Let e be the identity. Then a * e = a, so a + e - ae = a, giving e - ae = 0, so e(1 - a) = 0. For this to hold for all a, we need e = 0. Check: a * 0 = a + 0 - a·0 = a ✓. Inverse of 3: Let 3 * x = 0, so 3 + x - 3x = 0, giving 3 + x(1 - 3) = 0, so 3 - 2x = 0, hence x = 3/2. But 3/2 ∉ Z, so 3 has no inverse in Z.",
                "tips": ["<li>For identity: solve a * e = a</li>", "<li>For inverse: solve a * x = e</li>", "<li>Check if solution is in the set</li>", "<li>Verify by substitution</li>", "<li>Not all elements have inverses</li>"],
                "formulas": "Identity: a * e = e * a = a; Inverse: a * a⁻¹ = a⁻¹ * a = e",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><circle cx="100" cy="75" r="30" fill="#f3f4f6" stroke="#6b7280"/><text x="100" y="80" text-anchor="middle" font-size="10" fill="#374151">a</text><circle cx="200" cy="75" r="30" fill="#f3f4f6" stroke="#6b7280"/><text x="200" y="80" text-anchor="middle" font-size="10" fill="#374151">e</text><text x="150" y="50" text-anchor="middle" font-size="12" fill="#374151">*</text></svg>'
            },
            {
                "title": "Even and Odd Functions",
                "question": "Determine if f(x) = x³ - 3x is even, odd, or neither.",
                "background": "A function f is <strong>even</strong> if f(-x) = f(x) for all x in its domain. A function f is <strong>odd</strong> if f(-x) = -f(x) for all x in its domain. Even functions are symmetric about the y-axis. Odd functions are symmetric about the origin. Most functions are neither even nor odd. The sum of even functions is even, sum of odd functions is odd.",
                "solution": "f(-x) = (-x)³ - 3(-x) = -x³ + 3x = -(x³ - 3x) = -f(x). Since f(-x) = -f(x), the function is odd. This means the graph is symmetric about the origin.",
                "tips": ["<li>Calculate f(-x)</li>", "<li>Compare with f(x) and -f(x)</li>", "<li>Even: f(-x) = f(x)</li>", "<li>Odd: f(-x) = -f(x)</li>", "<li>Neither: f(-x) ≠ f(x) and f(-x) ≠ -f(x)</li>"],
                "formulas": "Even: f(-x) = f(x); Odd: f(-x) = -f(x)",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><path d="M 50 75 Q 200 25 350 75" stroke="#6b7280" stroke-width="2" fill="none"/><text x="200" y="100" text-anchor="middle" font-size="10" fill="#374151">f(x) = x³ - 3x (Odd)</text></svg>'
            },
            {
                "title": "Periodic Functions",
                "question": "Find the period of f(x) = sin(3x + π/4).",
                "background": "A function f is <strong>periodic</strong> with period T if f(x + T) = f(x) for all x. The smallest positive T is called the fundamental period. For f(x) = sin(ax + b), the period is 2π/|a|. For f(x) = cos(ax + b), the period is also 2π/|a|. The phase shift is -b/a. Periodic functions repeat their values at regular intervals.",
                "solution": "For f(x) = sin(3x + π/4), comparing with sin(ax + b), we have a = 3. The period is T = 2π/|a| = 2π/3. The phase shift is -b/a = -(π/4)/3 = -π/12.",
                "tips": ["<li>Identify a in sin(ax + b)</li>", "<li>Use period = 2π/|a|</li>", "<li>Phase shift = -b/a</li>", "<li>Check with f(x + T) = f(x)</li>", "<li>Verify with graph</li>"],
                "formulas": "Period of sin(ax + b): T = 2π/|a|; Phase shift: -b/a",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><path d="M 50 75 L 100 25 L 150 125 L 200 25 L 250 125 L 300 25 L 350 75" stroke="#6b7280" stroke-width="2" fill="none"/><text x="200" y="140" text-anchor="middle" font-size="10" fill="#374151">Period = 2π/3</text></svg>'
            },
            {
                "title": "Domain and Range",
                "question": "Find the domain and range of f(x) = √(4 - x²).",
                "background": "The <strong>domain</strong> of a function is the set of all possible input values (x-values). The <strong>range</strong> is the set of all possible output values (y-values). For √f(x), we need f(x) ≥ 0. For rational functions, exclude values that make the denominator zero. For logarithmic functions, the argument must be positive.",
                "solution": "Domain: For √(4 - x²) to be real, we need 4 - x² ≥ 0, so x² ≤ 4, giving -2 ≤ x ≤ 2. Domain = [-2, 2]. Range: Since x² ≥ 0, we have 4 - x² ≤ 4, so √(4 - x²) ≤ 2. Also, √(4 - x²) ≥ 0. Range = [0, 2].",
                "tips": ["<li>For √f(x): solve f(x) ≥ 0</li>", "<li>For 1/f(x): exclude f(x) = 0</li>", "<li>For log f(x): solve f(x) > 0</li>", "<li>Consider all restrictions</li>", "<li>Express in interval notation</li>"],
                "formulas": "Domain: set of valid x-values; Range: set of possible y-values",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><path d="M 100 75 Q 200 25 300 75" stroke="#6b7280" stroke-width="2" fill="none"/><text x="200" y="100" text-anchor="middle" font-size="10" fill="#374151">f(x) = √(4-x²)</text><text x="200" y="115" text-anchor="middle" font-size="8" fill="#6b7280">Domain: [-2,2], Range: [0,2]</text></svg>'
            },
            {
                "title": "Piecewise Functions",
                "question": "Let f(x) = {x² if x < 0, 2x if 0 ≤ x < 2, 4 if x ≥ 2}. Find f(-1), f(1), f(2), and f(3).",
                "background": "A <strong>piecewise function</strong> is defined by different formulas on different intervals. To evaluate f(x), first determine which interval x belongs to, then use the corresponding formula. Piecewise functions are common in real-world applications where different rules apply in different situations.",
                "solution": "f(-1): Since -1 < 0, use f(x) = x². So f(-1) = (-1)² = 1. f(1): Since 0 ≤ 1 < 2, use f(x) = 2x. So f(1) = 2(1) = 2. f(2): Since 2 ≥ 2, use f(x) = 4. So f(2) = 4. f(3): Since 3 ≥ 2, use f(x) = 4. So f(3) = 4.",
                "tips": ["<li>Check which interval x belongs to</li>", "<li>Use the corresponding formula</li>", "<li>Be careful with boundary points</li>", "<li>Check continuity at boundaries</li>", "<li>Draw graph to visualize</li>"],
                "formulas": "f(x) = {formula₁ if condition₁, formula₂ if condition₂, ...}",
                "svg": '<svg viewBox="0 0 400 150" class="math-diagram"><path d="M 50 125 L 100 25" stroke="#6b7280" stroke-width="2"/><path d="M 100 25 L 200 75" stroke="#6b7280" stroke-width="2"/><path d="M 200 75 L 350 75" stroke="#6b7280" stroke-width="2"/><text x="200" y="140" text-anchor="middle" font-size="10" fill="#374151">Piecewise Function</text></svg>'
            }
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
            "\n".join(problem["tips"]), problem["formulas"], problem["svg"]
        )
        
        output_file = chapter_dir / f"problem-{chapter_num}-{i:02d}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {output_file}")

def main():
    """Generate all maths problems."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
