#!/usr/bin/env python3
"""
Generate 10 comprehensive Physics problems for each chapter for 12th Board 2026.
"""

import os
from pathlib import Path

def create_problem_html(chapter, problem_num, title, question, background, solution, tips, formulas, visualization_svg):
    """Create HTML for a single physics problem."""
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
    .physics-diagram {{ max-width:100%; height:auto; display:block; margin:12px auto; border:1px solid #e5e7eb; border-radius:8px; background:#fafafa; }}
    code {{ background:#f8fafc; border:1px solid #e5e7eb; padding:2px 6px; border-radius:6px; font-family: 'Courier New', monospace; }}
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

def get_chapter_data():
    """Get comprehensive data for all physics chapters."""
    return {
        1: {
            "title": "Physical World and Measurement",
            "problems": [
                {
                    "title": "Scientific Notation",
                    "question": "Express the following in scientific notation: (a) 0.000000000154 m (radius of hydrogen atom) (b) 0.000000000000000000000000000000910938356 kg (mass of electron) (c) 299792458 m/s (speed of light)",
                    "background": "Scientific notation is essential for expressing very large or very small numbers in physics. It follows the format a × 10ⁿ where 1 ≤ |a| < 10 and n is an integer. This notation makes calculations easier and reduces errors when dealing with extreme values common in physics.",
                    "solution": "(a) 1.54 × 10⁻¹⁰ m (3 significant figures) (b) 9.10938356 × 10⁻³¹ kg (9 significant figures) (c) 2.99792458 × 10⁸ m/s (9 significant figures)",
                    "tips": ["<li>Move decimal point to get number between 1 and 10</li>", "<li>Count places moved for exponent</li>", "<li>Left movement = positive exponent</li>", "<li>Right movement = negative exponent</li>", "<li>Preserve significant figures</li>"],
                    "formulas": "a × 10ⁿ where 1 ≤ |a| < 10",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Scientific Notation: a × 10ⁿ</text></svg>'
                },
                {
                    "title": "Dimensional Analysis",
                    "question": "Check the dimensional correctness of the equation: v² = u² + 2as, where v is final velocity, u is initial velocity, a is acceleration, and s is displacement.",
                    "background": "Dimensional analysis verifies equation correctness by ensuring all terms have identical dimensions. The principle of homogeneity states that both sides of an equation must have the same dimensions. This helps catch errors and derive relationships between physical quantities.",
                    "solution": "Left side: v² = [LT⁻¹]² = [L²T⁻²]. Right side: u² + 2as = [LT⁻¹]² + [LT⁻²][L] = [L²T⁻²] + [L²T⁻²] = [L²T⁻²]. Since both sides have [L²T⁻²], the equation is dimensionally correct.",
                    "tips": ["<li>Identify dimensions of each variable</li>", "<li>Constants are dimensionless</li>", "<li>Powers multiply dimensions by exponent</li>", "<li>Products add dimensions of factors</li>", "<li>All terms in sum must have same dimensions</li>"],
                    "formulas": "[v] = [LT⁻¹], [a] = [LT⁻²], [s] = [L]",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Dimensional Analysis: [L²T⁻²] = [L²T⁻²]</text></svg>'
                },
                {
                    "title": "Significant Figures",
                    "question": "Calculate the area of a rectangle with length 2.45 m and width 1.2 m. Express your answer with appropriate significant figures.",
                    "background": "Significant figures indicate the precision of measurements. Rules: (1) All non-zero digits are significant. (2) Zeros between non-zero digits are significant. (3) Leading zeros are not significant. (4) Trailing zeros after decimal are significant. (5) In multiplication/division, result has same sig figs as least precise measurement.",
                    "solution": "Area = length × width = 2.45 m × 1.2 m = 2.94 m². Since 1.2 has 2 significant figures (least precise), the answer should have 2 significant figures: 2.9 m².",
                    "tips": ["<li>Count significant figures in each measurement</li>", "<li>Use least number of sig figs for result</li>", "<li>Round to appropriate decimal places</li>", "<li>Include units in final answer</li>", "<li>Check reasonableness of result</li>"],
                    "formulas": "Area = length × width",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="100" y="50" width="200" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="120" text-anchor="middle" font-size="12" fill="#374151">Area = 2.45 × 1.2 = 2.9 m²</text></svg>'
                },
                {
                    "title": "Unit Conversion",
                    "question": "Convert 72 km/h to m/s and express in scientific notation.",
                    "background": "Unit conversion is fundamental in physics. The key is to multiply by conversion factors that equal 1. For speed: 1 km = 1000 m and 1 h = 3600 s. Always check that units cancel correctly and the result has the expected dimensions.",
                    "solution": "72 km/h = 72 × (1000 m)/(3600 s) = 72 × (1000/3600) m/s = 72 × 0.2778 m/s = 20 m/s = 2.0 × 10¹ m/s (2 significant figures).",
                    "tips": ["<li>Write conversion factors as fractions</li>", "<li>Ensure units cancel correctly</li>", "<li>Multiply numerators and denominators</li>", "<li>Check final units are correct</li>", "<li>Express in scientific notation if needed</li>"],
                    "formulas": "1 km = 1000 m, 1 h = 3600 s",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">72 km/h = 20 m/s</text></svg>'
                },
                {
                    "title": "Error Analysis",
                    "question": "A student measures the length of a rod as 15.2 cm ± 0.1 cm. Calculate the percentage error in the measurement.",
                    "background": "Error analysis is crucial in experimental physics. Absolute error is the uncertainty in measurement, while relative error is the ratio of absolute error to measured value. Percentage error = (absolute error/measured value) × 100%. This helps assess measurement quality.",
                    "solution": "Given: measured value = 15.2 cm, absolute error = 0.1 cm. Percentage error = (0.1/15.2) × 100% = 0.66% ≈ 0.7% (rounded to 1 significant figure).",
                    "tips": ["<li>Identify absolute and relative errors</li>", "<li>Use formula: % error = (Δx/x) × 100%</li>", "<li>Round to appropriate significant figures</li>", "<li>Express as percentage</li>", "<li>Compare with expected precision</li>"],
                    "formulas": "Percentage error = (Δx/x) × 100%",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Error = 0.1/15.2 × 100% = 0.7%</text></svg>'
                },
                {
                    "title": "Precision and Accuracy",
                    "question": "Three students measure the same object and get: Student A: 2.1 cm, 2.0 cm, 2.2 cm; Student B: 2.5 cm, 2.6 cm, 2.4 cm; Student C: 2.3 cm, 2.3 cm, 2.3 cm. Which student is most precise? Most accurate? (True value = 2.3 cm)",
                    "background": "Precision refers to consistency of measurements (how close measurements are to each other), while accuracy refers to how close measurements are to the true value. High precision means low scatter, high accuracy means close to true value. Both are important in experimental physics.",
                    "solution": "Student A: average = 2.1 cm (accurate), range = 0.2 cm (moderate precision). Student B: average = 2.5 cm (inaccurate), range = 0.2 cm (moderate precision). Student C: average = 2.3 cm (accurate), range = 0 cm (most precise). Student C is most precise and accurate.",
                    "tips": ["<li>Calculate average for accuracy</li>", "<li>Calculate range for precision</li>", "<li>Compare with true value</li>", "<li>Smaller range = higher precision</li>", "<li>Closer to true value = higher accuracy</li>"],
                    "formulas": "Average = Σx/n, Range = max - min",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Precision vs Accuracy</text></svg>'
                },
                {
                    "title": "Order of Magnitude",
                    "question": "Estimate the order of magnitude of the number of atoms in a human body. (Mass of human ≈ 70 kg, mass of atom ≈ 10⁻²⁶ kg)",
                    "background": "Order of magnitude estimation helps understand the scale of physical quantities. It involves rounding to the nearest power of 10. This is useful for checking if answers are reasonable and for quick approximations in complex problems.",
                    "solution": "Number of atoms = mass of body/mass of atom = 70 kg / 10⁻²⁶ kg = 7 × 10²⁷. Order of magnitude = 10²⁸ atoms. This means there are approximately 10²⁸ atoms in a human body.",
                    "tips": ["<li>Round numbers to nearest power of 10</li>", "<li>Use scientific notation</li>", "<li>Compare with known values</li>", "<li>Check if result is reasonable</li>", "<li>Express as 10ⁿ format</li>"],
                    "formulas": "Order of magnitude = 10ⁿ where n is the exponent",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Order of magnitude ≈ 10²⁸</text></svg>'
                },
                {
                    "title": "Derived Units",
                    "question": "Express the unit of force in terms of fundamental units and verify using Newton's second law.",
                    "background": "Derived units are combinations of fundamental units. Force has dimensions [MLT⁻²] from F = ma. The SI unit of force is the newton (N), which equals kg⋅m/s². Understanding derived units helps in dimensional analysis and unit conversions.",
                    "solution": "From F = ma: [F] = [m][a] = [M][LT⁻²] = [MLT⁻²]. SI unit: kg⋅m/s² = newton (N). Verification: F = ma → N = kg × m/s² = kg⋅m/s². The units are consistent.",
                    "tips": ["<li>Use dimensional analysis</li>", "<li>Apply fundamental laws</li>", "<li>Check unit consistency</li>", "<li>Verify with known formulas</li>", "<li>Express in SI units</li>"],
                    "formulas": "F = ma, [F] = [MLT⁻²], 1 N = 1 kg⋅m/s²",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Force = [MLT⁻²] = N</text></svg>'
                },
                {
                    "title": "Measurement Uncertainty",
                    "question": "A ruler has markings every 1 mm. What is the uncertainty in measuring a length of 15.3 cm with this ruler?",
                    "background": "Measurement uncertainty depends on the precision of the measuring instrument. For a ruler with 1 mm markings, the uncertainty is typically ±0.5 mm (half the smallest division). This represents the range within which the true value likely lies.",
                    "solution": "Ruler has 1 mm divisions, so uncertainty = ±0.5 mm = ±0.05 cm. Length = 15.3 cm ± 0.05 cm. The measurement should be reported as 15.30 cm ± 0.05 cm to show the uncertainty clearly.",
                    "tips": ["<li>Uncertainty = half smallest division</li>", "<li>Express in same units</li>", "<li>Report with appropriate precision</li>", "<li>Use ± notation</li>", "<li>Consider instrument limitations</li>"],
                    "formulas": "Uncertainty = ±(smallest division)/2",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">15.3 cm ± 0.05 cm</text></svg>'
                },
                {
                    "title": "Physical Constants",
                    "question": "The speed of light in vacuum is c = 2.99792458 × 10⁸ m/s. Express this value with 3 significant figures and calculate the time for light to travel 1 km.",
                    "background": "Physical constants have high precision and are fundamental to physics. The speed of light is exactly 299,792,458 m/s by definition. When using constants in calculations, maintain appropriate significant figures based on the precision of other measurements in the problem.",
                    "solution": "c = 2.99792458 × 10⁸ m/s ≈ 3.00 × 10⁸ m/s (3 significant figures). Time = distance/speed = 1000 m / (3.00 × 10⁸ m/s) = 3.33 × 10⁻⁶ s = 3.33 μs.",
                    "tips": ["<li>Use appropriate significant figures</li>", "<li>Apply t = d/v formula</li>", "<li>Convert units as needed</li>", "<li>Check order of magnitude</li>", "<li>Express in convenient units</li>"],
                    "formulas": "c = 3.00 × 10⁸ m/s, t = d/v",
                    "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">t = 1 km / c = 3.33 μs</text></svg>'
                }
            ]
        }
    }

def generate_chapter_problems(chapter_num, chapter_data):
    """Generate all problems for a chapter."""
    chapter_dir = Path(f"Physics/ch{chapter_num}")
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
    """Generate all physics problems."""
    chapter_data = get_chapter_data()
    
    for chapter_num, data in chapter_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter_problems(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
