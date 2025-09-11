#!/usr/bin/env python3
"""Restore all Chemistry problems from extracted file with comprehensive format."""

from pathlib import Path

def create_comprehensive_problem_html(chapter, problem_num, title, question, background, solution, tips, formulas, visualization_svg):
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
    .chemistry-diagram {{ max-width:100%; height:auto; display:block; margin:12px auto; border:1px solid #e5e7eb; border-radius:8px; background:#fafafa; }}
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
      <p class="muted">Textbook Chapter {chapter} - Problem {problem_num}</p>
    </div>
  </div>
</body>
</html>"""

# Comprehensive problems data from the extracted file
problems_data = {
    3: {
        "title": "Electrochemistry",
        "problems": [
            {
                "num": 11,
                "title": "Molar Conductivity and Dissociation Constant",
                "question": "The conductivity of 0.00241 M acetic acid is 7.896 × 10⁻⁵ S cm⁻¹. Calculate its molar conductivity and, given Λm⁰ for acetic acid is 390.5 S cm² mol⁻¹, determine its dissociation constant.",
                "background": "Molar conductivity Λm relates solution conductivity κ to concentration c by Λm = κ × (1000/c) for c in mol L⁻¹ and κ in S cm⁻¹, yielding Λm in S cm² mol⁻¹. For weak electrolytes such as acetic acid, Λm increases markedly on dilution because degree of ionization α increases. Using Kohlrausch's law at infinite dilution, Λm⁰ equals the sum of limiting ionic conductivities. For weak acids, Ostwald's dilution law links α to Λm via α = Λm/Λm⁰. The dissociation constant is Ka = cα²/(1−α). Combining these gives Ka = (cΛm²)/(Λm⁰(Λm⁰ − Λm)). This method is classical in physical chemistry labs for determining Ka of weak acids from conductance measurements.",
                "solution": "Given: κ = 7.896 × 10⁻⁵ S cm⁻¹, c = 0.00241 mol L⁻¹, Λm⁰ = 390.5 S cm² mol⁻¹. Λm = κ × 1000/c = (7.896×10⁻⁵ × 1000)/0.00241 ≈ 32.75 S cm² mol⁻¹. Ka = (cΛm²)/(Λm⁰(Λm⁰ − Λm)) = (0.00241×32.75²)/(390.5×(390.5 − 32.75)) ≈ 1.8 × 10⁻⁵. Thus, Λm ≈ 32.8 S cm² mol⁻¹ and Ka ≈ 1.8 × 10⁻⁵ at 298 K.",
                "tips": ["<li>Compute Λm first via Λm = 1000κ/c</li>", "<li>Use Ka = (cΛm²)/(Λm⁰(Λm⁰ − Λm)) for weak acids</li>", "<li>Keep units consistent; c in mol L⁻¹, κ in S cm⁻¹</li>", "<li>Verify that the solution is sufficiently dilute</li>", "<li>Check temperature dependence of Λm⁰</li>"],
                "formulas": "Λm = κ × 1000/c; Ka = (cΛm²)/(Λm⁰(Λm⁰ − Λm)); α = Λm/Λm⁰",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Weak Electrolyte: CH₃COOH ⇌ CH₃COO⁻ + H⁺</text></svg>'
            },
            {
                "num": 12,
                "title": "Faraday's Laws and Charge Requirements",
                "question": "The amount of charge required for the reduction of 1 mol of MnO₄⁻ to Mn²⁺ is: (i) 1 F (ii) 3 F (iii) 5 F (iv) 6 F",
                "background": "Faraday's laws relate the amount of substance deposited or liberated during electrolysis to the quantity of electricity passed. One Faraday (F) equals 96,500 coulombs and represents the charge on one mole of electrons. For the reduction MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O, five electrons are required per MnO₄⁻ ion. Therefore, 1 mole of MnO₄⁻ requires 5 moles of electrons, which equals 5 Faradays of charge. This is a fundamental concept in electrochemistry for calculating charge requirements in electrolytic processes.",
                "solution": "For the reduction: MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O. Each MnO₄⁻ ion requires 5 electrons for complete reduction to Mn²⁺. Therefore, 1 mole of MnO₄⁻ requires 5 moles of electrons. Since 1 Faraday = 1 mole of electrons, the charge required is 5 F. Answer: (iii) 5 F.",
                "tips": ["<li>Write the balanced half-reaction</li>", "<li>Count the number of electrons involved</li>", "<li>1 mole of substance requires moles of electrons equal to the electron coefficient</li>", "<li>1 Faraday = 1 mole of electrons</li>", "<li>Check the oxidation state change</li>"],
                "formulas": "MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O; 1 F = 1 mole of electrons",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">MnO₄⁻ + 5e⁻ → Mn²⁺</text></svg>'
            },
            {
                "num": 13,
                "title": "Electrolysis Calculations",
                "question": "The amount of electricity (in terms of Faraday) required to produce: (i) 20.0 g of Ca from molten CaCl₂ (ii) 40.0 g of Al from molten Al₂O₃",
                "background": "Electrolysis calculations involve Faraday's laws and stoichiometry. For Ca²⁺ + 2e⁻ → Ca, 1 mole of Ca requires 2 moles of electrons (2 F). For Al³⁺ + 3e⁻ → Al, 1 mole of Al requires 3 moles of electrons (3 F). The amount of electricity needed depends on the mass of metal to be produced and the number of electrons required per mole. Molar masses: Ca = 40 g/mol, Al = 27 g/mol. The general formula is: F = (mass/molar mass) × electrons per mole.",
                "solution": "(i) For Ca: Ca²⁺ + 2e⁻ → Ca. Moles of Ca = 20.0/40 = 0.5 mol. Electricity required = 0.5 × 2 = 1.0 F. (ii) For Al: Al³⁺ + 3e⁻ → Al. Moles of Al = 40.0/27 ≈ 1.48 mol. Electricity required = 1.48 × 3 ≈ 4.44 F. Therefore, (i) 1.0 F and (ii) 4.44 F.",
                "tips": ["<li>Write the reduction half-reaction</li>", "<li>Calculate moles of metal from mass</li>", "<li>Multiply by electrons required per mole</li>", "<li>Use correct molar masses</li>", "<li>Check units and significant figures</li>"],
                "formulas": "F = (mass/molar mass) × electrons per mole; Ca: 2e⁻, Al: 3e⁻",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Electrolysis: Mⁿ⁺ + ne⁻ → M</text></svg>'
            }
        ]
    }
}

def update_problem(chapter, problem_num, problem_data):
    """Update a single problem with comprehensive format."""
    chapter_dir = Path(f"Chemistry/ch{chapter}")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    html_content = create_comprehensive_problem_html(
        chapter, problem_num, problem_data["title"], problem_data["question"],
        problem_data["background"], problem_data["solution"], 
        "\n".join(problem_data["tips"]), problem_data["formulas"], problem_data["svg"]
    )
    
    output_file = chapter_dir / f"problem-{chapter}-{problem_num:02d}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Updated {output_file}")

def main():
    """Update remaining chemistry problems with comprehensive format."""
    for chapter_num, data in problems_data.items():
        print(f"Updating Chapter {chapter_num}: {data['title']}")
        for problem in data["problems"]:
            update_problem(chapter_num, problem["num"], problem)
    
    print("Problems updated successfully!")

if __name__ == "__main__":
    main()
