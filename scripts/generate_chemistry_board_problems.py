#!/usr/bin/env python3
"""Generate comprehensive Chemistry board problems for 12th Board 2026 - Chapters 3, 4, 8, 9."""

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
      <p class="muted">Expected 12th Board 2026 - Chapter {chapter}</p>
    </div>
  </div>
</body>
</html>"""

# Chemistry board problems for chapters 3, 4, 8, 9
chapters_data = {
    3: {
        "title": "Electrochemistry",
        "problems": [
            {
                "title": "Galvanic Cell and Cell Potential",
                "question": "A galvanic cell consists of Zn/Zn²⁺ and Cu/Cu²⁺ half-cells. If E°(Zn²⁺/Zn) = -0.76 V and E°(Cu²⁺/Cu) = +0.34 V, calculate the standard cell potential and write the cell reaction.",
                "background": "A galvanic cell converts chemical energy to electrical energy through redox reactions. The standard cell potential E°cell = E°cathode - E°anode. The more positive electrode acts as cathode (reduction) and the more negative as anode (oxidation). The cell reaction is the sum of half-reactions with electrons canceling out.",
                "solution": "E°cell = E°cathode - E°anode = E°(Cu²⁺/Cu) - E°(Zn²⁺/Zn) = 0.34 - (-0.76) = 1.10 V. Cell reaction: Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s). The zinc electrode is the anode (oxidation) and copper electrode is the cathode (reduction).",
                "tips": ["<li>Identify cathode (more positive E°) and anode (more negative E°)</li>", "<li>Use E°cell = E°cathode - E°anode</li>", "<li>Write half-reactions with electrons</li>", "<li>Balance the overall reaction</li>", "<li>Check that electrons cancel out</li>"],
                "formulas": "E°cell = E°cathode - E°anode; Anode: oxidation, Cathode: reduction",
                "svg": '<svg viewBox="0 0 400 200" class="chemistry-diagram"><rect x="50" y="50" width="100" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="110" text-anchor="middle" font-size="12" fill="#374151">Zn/Zn²⁺</text><rect x="250" y="50" width="100" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="300" y="110" text-anchor="middle" font-size="12" fill="#374151">Cu/Cu²⁺</text><line x1="150" y1="100" x2="250" y2="100" stroke="#6b7280" stroke-width="2"/><text x="200" y="90" text-anchor="middle" font-size="10" fill="#374151">Salt Bridge</text></svg>'
            },
            {
                "title": "Nernst Equation",
                "question": "Calculate the cell potential for the reaction Zn(s) + Cu²⁺(aq) → Zn²⁺(aq) + Cu(s) at 25°C when [Cu²⁺] = 0.1 M and [Zn²⁺] = 0.01 M. Given E°cell = 1.10 V.",
                "background": "The Nernst equation relates cell potential to concentrations: Ecell = E°cell - (RT/nF)lnQ, where Q is the reaction quotient. At 25°C, (RT/F) = 0.0257 V. For the reaction aA + bB → cC + dD, Q = [C]ᶜ[D]ᵈ/[A]ᵃ[B]ᵇ. The Nernst equation shows how cell potential changes with concentration.",
                "solution": "Ecell = E°cell - (0.0257/n)lnQ. For the reaction: n = 2, Q = [Zn²⁺]/[Cu²⁺] = 0.01/0.1 = 0.1. Ecell = 1.10 - (0.0257/2)ln(0.1) = 1.10 - 0.01285(-2.303) = 1.10 + 0.0296 = 1.13 V.",
                "tips": ["<li>Identify n (number of electrons transferred)</li>", "<li>Calculate Q = [products]/[reactants]</li>", "<li>Use Ecell = E°cell - (0.0257/n)lnQ at 25°C</li>", "<li>Check units and signs</li>", "<li>Verify with Le Chatelier's principle</li>"],
                "formulas": "Ecell = E°cell - (RT/nF)lnQ; At 25°C: Ecell = E°cell - (0.0257/n)lnQ",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Nernst Equation: Ecell = E°cell - (RT/nF)lnQ</text></svg>'
            },
            {
                "title": "Electrolysis and Faraday's Laws",
                "question": "How many grams of copper will be deposited when 2 amperes of current is passed through CuSO₄ solution for 30 minutes? (Atomic mass of Cu = 63.5 g/mol)",
                "background": "Faraday's first law states that the amount of substance deposited is proportional to the quantity of electricity passed. W = (E × I × t)/96500, where E is the equivalent mass, I is current, t is time in seconds, and 96500 C is Faraday's constant. For Cu²⁺ + 2e⁻ → Cu, equivalent mass = atomic mass/2.",
                "solution": "Equivalent mass of Cu = 63.5/2 = 31.75 g. Time = 30 × 60 = 1800 seconds. W = (31.75 × 2 × 1800)/96500 = 114300/96500 = 1.185 g. Therefore, 1.185 g of copper will be deposited.",
                "tips": ["<li>Calculate equivalent mass = atomic mass/valency</li>", "<li>Convert time to seconds</li>", "<li>Use W = (E × I × t)/96500</li>", "<li>Check units (grams)</li>", "<li>Verify with stoichiometry</li>"],
                "formulas": "W = (E × I × t)/96500; E = atomic mass/valency; 1 Faraday = 96500 C",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Electrolysis: Cu²⁺ + 2e⁻ → Cu</text></svg>'
            },
            {
                "title": "Conductance and Molar Conductivity",
                "question": "The resistance of 0.1 M KCl solution in a conductivity cell is 100 Ω. If the cell constant is 0.1 cm⁻¹, calculate the conductivity and molar conductivity of the solution.",
                "background": "Conductivity (κ) is the reciprocal of resistivity and depends on the cell constant (G). κ = G/R, where G is cell constant and R is resistance. Molar conductivity (Λm) = κ/C, where C is concentration. Molar conductivity increases with dilution due to increased ionization. The unit of conductivity is S cm⁻¹.",
                "solution": "Conductivity κ = G/R = 0.1/100 = 0.001 S cm⁻¹. Molar conductivity Λm = κ/C = 0.001/0.1 = 0.01 S cm² mol⁻¹. Therefore, conductivity = 0.001 S cm⁻¹ and molar conductivity = 0.01 S cm² mol⁻¹.",
                "tips": ["<li>Use κ = G/R for conductivity</li>", "<li>Calculate Λm = κ/C for molar conductivity</li>", "<li>Check units carefully</li>", "<li>Convert concentration to mol/L</li>", "<li>Verify with known values</li>"],
                "formulas": "κ = G/R; Λm = κ/C; G = cell constant, R = resistance, C = concentration",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Conductivity Cell with KCl Solution</text></svg>'
            },
            {
                "title": "Kohlrausch's Law",
                "question": "The molar conductivities at infinite dilution for NaCl, HCl, and CH₃COONa are 126.4, 426.2, and 91.0 S cm² mol⁻¹ respectively. Calculate the molar conductivity of CH₃COOH at infinite dilution.",
                "background": "Kohlrausch's law states that the molar conductivity of an electrolyte at infinite dilution is the sum of the molar conductivities of its constituent ions. For CH₃COOH: Λ°(CH₃COOH) = λ°(CH₃COO⁻) + λ°(H⁺). We can find λ°(CH₃COO⁻) from CH₃COONa and λ°(H⁺) from HCl.",
                "solution": "From CH₃COONa: λ°(CH₃COO⁻) = Λ°(CH₃COONa) - λ°(Na⁺) = 91.0 - λ°(Na⁺). From HCl: λ°(H⁺) = Λ°(HCl) - λ°(Cl⁻) = 426.2 - λ°(Cl⁻). From NaCl: λ°(Na⁺) + λ°(Cl⁻) = 126.4. Solving: λ°(CH₃COO⁻) = 91.0 - (126.4 - λ°(Cl⁻)) = 91.0 - 126.4 + λ°(Cl⁻). λ°(H⁺) = 426.2 - λ°(Cl⁻). Λ°(CH₃COOH) = λ°(CH₃COO⁻) + λ°(H⁺) = (91.0 - 126.4 + λ°(Cl⁻)) + (426.2 - λ°(Cl⁻)) = 91.0 - 126.4 + 426.2 = 390.8 S cm² mol⁻¹.",
                "tips": ["<li>Use Kohlrausch's law: Λ° = λ°(cation) + λ°(anion)</li>", "<li>Find individual ion conductivities</li>", "<li>Set up equations from given data</li>", "<li>Solve for unknown conductivities</li>", "<li>Check the final answer</li>"],
                "formulas": "Λ° = λ°(cation) + λ°(anion); Kohlrausch's law for weak electrolytes",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Kohlrausch Law: Sum of Ion Conductivities</text></svg>'
            },
            {
                "title": "Battery and Fuel Cell",
                "question": "Write the cell reactions for a lead-acid battery and explain why it can be recharged.",
                "background": "A lead-acid battery is a secondary cell that can be recharged. During discharge: Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O. During charging, the reaction is reversed. The battery can be recharged because the products (PbSO₄) are insoluble and remain on the electrodes, allowing the reverse reaction to occur when external voltage is applied.",
                "solution": "Discharge reactions: Anode: Pb + SO₄²⁻ → PbSO₄ + 2e⁻. Cathode: PbO₂ + 4H⁺ + SO₄²⁻ + 2e⁻ → PbSO₄ + 2H₂O. Overall: Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O. The battery can be recharged because PbSO₄ is insoluble and remains on the electrodes, allowing the reverse reaction when external voltage is applied.",
                "tips": ["<li>Write half-reactions for discharge</li>", "<li>Balance electrons and charges</li>", "<li>Explain recharging mechanism</li>", "<li>Consider solubility of products</li>", "<li>Compare with primary cells</li>"],
                "formulas": "Discharge: Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O; Recharge: Reverse reaction",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="100" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="80" text-anchor="middle" font-size="10" fill="#374151">Pb</text><rect x="250" y="50" width="100" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="300" y="80" text-anchor="middle" font-size="10" fill="#374151">PbO₂</text><text x="200" y="120" text-anchor="middle" font-size="10" fill="#374151">Lead-Acid Battery</text></svg>'
            },
            {
                "title": "Corrosion and Prevention",
                "question": "Explain the mechanism of rusting of iron and suggest two methods to prevent it.",
                "background": "Rusting is an electrochemical process where iron acts as anode and gets oxidized to Fe²⁺, while oxygen acts as cathode and gets reduced to OH⁻. The overall reaction is 4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃. Prevention methods include galvanizing, painting, cathodic protection, and alloying. The process requires both oxygen and water.",
                "solution": "Mechanism: Anode: Fe → Fe²⁺ + 2e⁻. Cathode: O₂ + 2H₂O + 4e⁻ → 4OH⁻. Overall: 4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃ (rust). Prevention methods: (1) Galvanizing: Coating with zinc, (2) Painting: Creating a barrier to oxygen and water, (3) Cathodic protection: Connecting to a more reactive metal, (4) Alloying: Making stainless steel.",
                "tips": ["<li>Write electrochemical half-reactions</li>", "<li>Identify anode and cathode</li>", "<li>Explain the role of oxygen and water</li>", "<li>Suggest practical prevention methods</li>", "<li>Consider cost and effectiveness</li>"],
                "formulas": "Anode: Fe → Fe²⁺ + 2e⁻; Cathode: O₂ + 2H₂O + 4e⁻ → 4OH⁻; Overall: 4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Iron Rusting: Fe + O₂ + H₂O → Fe(OH)₃</text></svg>'
            },
            {
                "title": "pH and Buffer Solutions",
                "question": "Calculate the pH of a buffer solution containing 0.1 M CH₃COOH and 0.1 M CH₃COONa. Given Ka for CH₃COOH = 1.8 × 10⁻⁵.",
                "background": "A buffer solution resists changes in pH when small amounts of acid or base are added. For a weak acid and its conjugate base: pH = pKa + log([A⁻]/[HA]). The Henderson-Hasselbalch equation is pH = pKa + log([salt]/[acid]). Buffer capacity is maximum when [A⁻] = [HA], giving pH = pKa.",
                "solution": "Using Henderson-Hasselbalch equation: pH = pKa + log([CH₃COO⁻]/[CH₃COOH]). pKa = -log(1.8 × 10⁻⁵) = 4.74. pH = 4.74 + log(0.1/0.1) = 4.74 + log(1) = 4.74 + 0 = 4.74. Therefore, the pH of the buffer solution is 4.74.",
                "tips": ["<li>Use Henderson-Hasselbalch equation</li>", "<li>Calculate pKa = -log(Ka)</li>", "<li>Identify acid and conjugate base</li>", "<li>Substitute concentrations</li>", "<li>Check the result</li>"],
                "formulas": "pH = pKa + log([A⁻]/[HA]); pKa = -log(Ka); Buffer pH = pKa when [A⁻] = [HA]",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Buffer: CH₃COOH + CH₃COO⁻</text></svg>'
            },
            {
                "title": "Standard Hydrogen Electrode",
                "question": "Explain the construction and working of a standard hydrogen electrode (SHE) and why it is assigned zero potential.",
                "background": "The standard hydrogen electrode (SHE) is the reference electrode with zero potential. It consists of a platinum electrode coated with platinum black, immersed in 1 M H⁺ solution, and hydrogen gas at 1 atm pressure. The half-reaction is 2H⁺ + 2e⁻ → H₂. It is assigned zero potential by convention to establish a reference point for measuring other electrode potentials.",
                "solution": "Construction: Platinum electrode coated with platinum black, immersed in 1 M H⁺ solution, with H₂ gas at 1 atm pressure bubbling over it. Half-reaction: 2H⁺ + 2e⁻ → H₂. It is assigned zero potential by international convention to provide a reference point. All other electrode potentials are measured relative to SHE. The platinum black provides a large surface area for the reaction.",
                "tips": ["<li>Describe the physical construction</li>", "<li>Write the half-reaction</li>", "<li>Explain the role of platinum black</li>", "<li>State the standard conditions</li>", "<li>Explain why it's assigned zero potential</li>"],
                "formulas": "SHE: 2H⁺ + 2e⁻ → H₂; E° = 0 V by convention; Standard conditions: 1 M H⁺, 1 atm H₂, 25°C",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="100" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="110" text-anchor="middle" font-size="10" fill="#374151">Pt electrode</text><text x="100" y="125" text-anchor="middle" font-size="8" fill="#374151">H₂ gas</text><text x="100" y="140" text-anchor="middle" font-size="8" fill="#374151">1 M H⁺</text></svg>'
            },
            {
                "title": "Concentration Cell",
                "question": "A concentration cell consists of two hydrogen electrodes, one in 0.1 M HCl and another in 0.01 M HCl. Calculate the cell potential at 25°C.",
                "background": "A concentration cell has the same electrodes but different concentrations. The cell potential arises from the concentration difference. For a concentration cell: Ecell = (0.0591/n)log(C₂/C₁), where C₂ is the higher concentration and C₁ is the lower concentration. The electrode in the more concentrated solution acts as cathode.",
                "solution": "For concentration cell: Ecell = (0.0591/n)log(C₂/C₁). Here, n = 1 (one electron), C₂ = 0.1 M, C₁ = 0.01 M. Ecell = (0.0591/1)log(0.1/0.01) = 0.0591 × log(10) = 0.0591 × 1 = 0.0591 V. The electrode in 0.1 M HCl acts as cathode and the one in 0.01 M HCl acts as anode.",
                "tips": ["<li>Identify it as a concentration cell</li>", "<li>Use Ecell = (0.0591/n)log(C₂/C₁)</li>", "<li>Identify higher and lower concentrations</li>", "<li>Calculate the ratio</li>", "<li>Check units and sign</li>"],
                "formulas": "Concentration cell: Ecell = (0.0591/n)log(C₂/C₁); Higher concentration = cathode",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="100" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="80" text-anchor="middle" font-size="10" fill="#374151">0.1 M HCl</text><rect x="250" y="50" width="100" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="300" y="80" text-anchor="middle" font-size="10" fill="#374151">0.01 M HCl</text></svg>'
            }
        ]
    }
}

def generate_chapter(chapter_num, chapter_data):
    """Generate all problems for a chapter."""
    chapter_dir = Path(f"Chemistry/ch{chapter_num}")
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
    """Generate chemistry board problems for chapter 3."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
