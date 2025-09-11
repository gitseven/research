#!/usr/bin/env python3
"""Generate remaining Chemistry board problems for chapters 4, 8, 9 - 12th Board 2026."""

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

# Remaining Chemistry chapters data
chapters_data = {
    4: {
        "title": "Chemical Kinetics",
        "problems": [
            {
                "title": "Rate of Reaction",
                "question": "For the reaction 2A + B → 3C, the rate of disappearance of A is 0.1 mol L⁻¹ s⁻¹. Calculate the rate of appearance of C.",
                "background": "The rate of a chemical reaction is the change in concentration of reactants or products per unit time. For the reaction aA + bB → cC + dD, the rate is related by: Rate = -(1/a)(d[A]/dt) = -(1/b)(d[B]/dt) = (1/c)(d[C]/dt) = (1/d)(d[D]/dt). The negative sign indicates decrease in reactant concentration.",
                "solution": "For the reaction 2A + B → 3C: Rate = -(1/2)(d[A]/dt) = (1/3)(d[C]/dt). Given d[A]/dt = -0.1 mol L⁻¹ s⁻¹. Therefore: (1/3)(d[C]/dt) = -(1/2)(-0.1) = 0.05. So d[C]/dt = 0.05 × 3 = 0.15 mol L⁻¹ s⁻¹. The rate of appearance of C is 0.15 mol L⁻¹ s⁻¹.",
                "tips": ["<li>Use the stoichiometric relationship</li>", "<li>Apply Rate = (1/coefficient)(d[concentration]/dt)</li>", "<li>Watch signs for reactants vs products</li>", "<li>Check units consistency</li>", "<li>Verify with stoichiometry</li>"],
                "formulas": "Rate = -(1/a)(d[A]/dt) = (1/c)(d[C]/dt); For 2A + B → 3C: Rate = -(1/2)(d[A]/dt) = (1/3)(d[C]/dt)",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">2A + B → 3C</text></svg>'
            },
            {
                "title": "Order of Reaction",
                "question": "The rate of reaction A + B → C is given by Rate = k[A]²[B]. What is the order of reaction with respect to A, B, and overall order?",
                "background": "The order of reaction with respect to a reactant is the power to which its concentration is raised in the rate law. The overall order is the sum of all individual orders. For Rate = k[A]ᵐ[B]ⁿ, the order with respect to A is m, with respect to B is n, and the overall order is m + n. The order must be determined experimentally.",
                "solution": "Given Rate = k[A]²[B]. Order with respect to A = 2 (exponent of [A]). Order with respect to B = 1 (exponent of [B]). Overall order = 2 + 1 = 3. Therefore, the reaction is second order with respect to A, first order with respect to B, and third order overall.",
                "tips": ["<li>Identify the exponents in the rate law</li>", "<li>Order with respect to each reactant = its exponent</li>", "<li>Overall order = sum of all exponents</li>", "<li>Check the units of rate constant</li>", "<li>Verify with experimental data</li>"],
                "formulas": "For Rate = k[A]ᵐ[B]ⁿ: Order w.r.t. A = m, Order w.r.t. B = n, Overall order = m + n",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Rate = k[A]²[B]</text></svg>'
            },
            {
                "title": "Integrated Rate Law",
                "question": "For a first-order reaction A → B, if the initial concentration of A is 0.1 M and after 100 seconds it becomes 0.05 M, calculate the rate constant.",
                "background": "For a first-order reaction A → B, the integrated rate law is ln([A]₀/[A]ₜ) = kt, where [A]₀ is initial concentration, [A]ₜ is concentration at time t, k is rate constant, and t is time. The half-life of a first-order reaction is t₁/₂ = 0.693/k and is independent of initial concentration.",
                "solution": "Using the integrated rate law for first-order reaction: ln([A]₀/[A]ₜ) = kt. Given [A]₀ = 0.1 M, [A]ₜ = 0.05 M, t = 100 s. ln(0.1/0.05) = k × 100. ln(2) = 100k. 0.693 = 100k. Therefore k = 0.693/100 = 0.00693 s⁻¹.",
                "tips": ["<li>Use ln([A]₀/[A]ₜ) = kt for first-order</li>", "<li>Calculate the ratio [A]₀/[A]ₜ</li>", "<li>Take natural logarithm</li>", "<li>Solve for k</li>", "<li>Check units (s⁻¹ for first-order)</li>"],
                "formulas": "First-order: ln([A]₀/[A]ₜ) = kt; Half-life: t₁/₂ = 0.693/k",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">First-order: A → B</text></svg>'
            },
            {
                "title": "Arrhenius Equation",
                "question": "The rate constant of a reaction at 300 K is 2.0 × 10⁻⁵ s⁻¹ and at 320 K is 8.0 × 10⁻⁵ s⁻¹. Calculate the activation energy.",
                "background": "The Arrhenius equation relates rate constant to temperature: k = A e^(-Ea/RT), where A is pre-exponential factor, Ea is activation energy, R is gas constant, and T is temperature. The logarithmic form is ln(k₂/k₁) = (Ea/R)(1/T₁ - 1/T₂). Activation energy is the minimum energy required for reactants to form products.",
                "solution": "Using Arrhenius equation: ln(k₂/k₁) = (Ea/R)(1/T₁ - 1/T₂). Given k₁ = 2.0 × 10⁻⁵ s⁻¹ at T₁ = 300 K, k₂ = 8.0 × 10⁻⁵ s⁻¹ at T₂ = 320 K. ln(8.0 × 10⁻⁵/2.0 × 10⁻⁵) = (Ea/8.314)(1/300 - 1/320). ln(4) = (Ea/8.314)(0.00333 - 0.00313). 1.386 = (Ea/8.314)(0.0002). Ea = (1.386 × 8.314)/0.0002 = 57,600 J/mol = 57.6 kJ/mol.",
                "tips": ["<li>Use ln(k₂/k₁) = (Ea/R)(1/T₁ - 1/T₂)</li>", "<li>Convert temperatures to Kelvin</li>", "<li>Calculate the ratio k₂/k₁</li>", "<li>Solve for Ea</li>", "<li>Convert to kJ/mol</li>"],
                "formulas": "Arrhenius: ln(k₂/k₁) = (Ea/R)(1/T₁ - 1/T₂); k = A e^(-Ea/RT)",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Arrhenius: k = A e^(-Ea/RT)</text></svg>'
            },
            {
                "title": "Catalyst and Activation Energy",
                "question": "Explain how a catalyst affects the rate of reaction and why it does not affect the equilibrium constant.",
                "background": "A catalyst increases the rate of reaction by providing an alternative pathway with lower activation energy. It does not change the thermodynamics of the reaction (ΔG, ΔH, ΔS remain the same) but only affects the kinetics. Since equilibrium constant K = e^(-ΔG/RT), and ΔG is unchanged, K remains the same. The catalyst speeds up both forward and reverse reactions equally.",
                "solution": "A catalyst increases the rate of reaction by lowering the activation energy, providing an alternative reaction pathway. It does not change the equilibrium constant because: (1) It affects only the kinetics, not thermodynamics, (2) ΔG remains unchanged, (3) Since K = e^(-ΔG/RT), K is unchanged, (4) The catalyst speeds up both forward and reverse reactions equally, maintaining the same equilibrium position.",
                "tips": ["<li>Explain the role in lowering activation energy</li>", "<li>Distinguish between kinetics and thermodynamics</li>", "<li>Use K = e^(-ΔG/RT) relationship</li>", "<li>Explain equal effect on forward and reverse</li>", "<li>Give examples of catalysts</li>"],
                "formulas": "Catalyst lowers Ea; K = e^(-ΔG/RT) unchanged; Rate = A e^(-Ea/RT)",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Catalyst lowers activation energy</text></svg>'
            }
        ]
    },
    8: {
        "title": "The d- and f- Block Elements",
        "problems": [
            {
                "title": "Electronic Configuration of d-Block Elements",
                "question": "Write the electronic configuration of chromium (Z = 24) and explain why it is an exception to the general rule.",
                "background": "The d-block elements have their valence electrons in d orbitals. The general rule is to fill orbitals in order of increasing energy, but chromium and copper are exceptions due to extra stability of half-filled and completely filled d orbitals. Chromium has configuration [Ar] 3d⁵ 4s¹ instead of [Ar] 3d⁴ 4s² because half-filled d orbital is more stable.",
                "solution": "Electronic configuration of chromium (Z = 24): [Ar] 3d⁵ 4s¹. This is an exception because chromium has one electron in 4s and five electrons in 3d, giving a half-filled d orbital. The half-filled d orbital (3d⁵) is more stable than 3d⁴ 4s² due to exchange energy, which is maximum for half-filled and completely filled orbitals.",
                "tips": ["<li>Write the noble gas core first</li>", "<li>Fill 4s before 3d</li>", "<li>Consider stability of half-filled orbitals</li>", "<li>Explain exchange energy concept</li>", "<li>Compare with expected configuration</li>"],
                "formulas": "Cr: [Ar] 3d⁵ 4s¹; Exception due to half-filled d orbital stability",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Cr: [Ar] 3d⁵ 4s¹</text></svg>'
            },
            {
                "title": "Oxidation States of Transition Elements",
                "question": "Explain why transition elements show variable oxidation states and give examples of common oxidation states of manganese.",
                "background": "Transition elements show variable oxidation states because they have incompletely filled d orbitals. The energy difference between (n-1)d and ns orbitals is small, so electrons from both can participate in bonding. The common oxidation states are +2, +3, +4, +5, +6, +7. The maximum oxidation state equals the number of valence electrons (s + d electrons).",
                "solution": "Transition elements show variable oxidation states because: (1) They have incompletely filled d orbitals, (2) The energy difference between (n-1)d and ns orbitals is small, (3) Both s and d electrons can participate in bonding. Common oxidation states of manganese: +2 (Mn²⁺), +3 (Mn³⁺), +4 (MnO₂), +6 (MnO₄²⁻), +7 (MnO₄⁻). The maximum oxidation state is +7, equal to the total number of valence electrons (2s + 5d).",
                "tips": ["<li>Explain the role of d orbitals</li>", "<li>Mention energy difference between orbitals</li>", "<li>Give specific examples for manganese</li>", "<li>Connect to maximum oxidation state</li>", "<li>Compare with s-block elements</li>"],
                "formulas": "Variable oxidation states due to d orbitals; Max oxidation state = s + d electrons",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Mn: +2, +3, +4, +6, +7</text></svg>'
            },
            {
                "title": "Magnetic Properties",
                "question": "Explain the magnetic properties of transition elements and calculate the magnetic moment of Fe²⁺ ion.",
                "background": "Transition elements are paramagnetic due to unpaired electrons in d orbitals. The magnetic moment is calculated using μ = √[n(n+2)] BM, where n is the number of unpaired electrons. Diamagnetic substances have no unpaired electrons and are weakly repelled by magnetic field. Paramagnetic substances have unpaired electrons and are attracted by magnetic field.",
                "solution": "Transition elements are paramagnetic due to unpaired electrons in d orbitals. For Fe²⁺: Electronic configuration is [Ar] 3d⁶. In octahedral field, the configuration is t₂g⁴ eg², giving 4 unpaired electrons. Magnetic moment μ = √[n(n+2)] = √[4(4+2)] = √24 = 4.9 BM. Therefore, Fe²⁺ is paramagnetic with magnetic moment 4.9 BM.",
                "tips": ["<li>Count unpaired electrons in d orbitals</li>", "<li>Use μ = √[n(n+2)] formula</li>", "<li>Consider crystal field splitting</li>", "<li>Check units (BM)</li>", "<li>Compare with experimental values</li>"],
                "formulas": "μ = √[n(n+2)] BM; n = number of unpaired electrons",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Fe²⁺: 4 unpaired electrons</text></svg>'
            },
            {
                "title": "Formation of Colored Compounds",
                "question": "Why do transition elements form colored compounds? Explain with reference to d-d transitions.",
                "background": "Transition elements form colored compounds due to d-d transitions. When white light falls on a compound, certain wavelengths are absorbed by electrons jumping from lower energy d orbitals to higher energy d orbitals. The remaining wavelengths are transmitted, giving the compound its color. The color is complementary to the absorbed color. The energy difference between d orbitals corresponds to visible light energy.",
                "solution": "Transition elements form colored compounds due to d-d transitions. When white light falls on the compound, electrons absorb specific wavelengths to jump from lower energy d orbitals (t₂g) to higher energy d orbitals (eg). The absorbed wavelengths correspond to the energy difference between d orbitals. The transmitted light gives the compound its color, which is complementary to the absorbed color. For example, if blue light is absorbed, the compound appears orange.",
                "tips": ["<li>Explain d-d transitions</li>", "<li>Mention absorption of specific wavelengths</li>", "<li>Connect to energy difference between orbitals</li>", "<li>Explain complementary colors</li>", "<li>Give examples</li>"],
                "formulas": "d-d transitions cause color; Absorbed wavelength = energy difference between d orbitals",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">d-d transitions cause color</text></svg>'
            },
            {
                "title": "Lanthanoid Contraction",
                "question": "What is lanthanoid contraction? How does it affect the properties of elements in the same group?",
                "background": "Lanthanoid contraction is the gradual decrease in atomic and ionic radii of lanthanoids from La to Lu due to poor shielding effect of 4f electrons. This causes the elements in the same group to have similar sizes, making their properties very similar. For example, Zr and Hf have almost identical properties due to lanthanoid contraction.",
                "solution": "Lanthanoid contraction is the gradual decrease in atomic and ionic radii of lanthanoids from La to Lu due to poor shielding effect of 4f electrons. The 4f electrons are buried deep inside the atom and cannot shield the outer electrons effectively from the nuclear charge. This causes elements in the same group to have similar sizes, making their properties very similar. For example, Zr and Hf have almost identical properties due to lanthanoid contraction.",
                "tips": ["<li>Explain poor shielding of 4f electrons</li>", "<li>Mention gradual decrease in radii</li>", "<li>Connect to similar properties in groups</li>", "<li>Give examples of affected elements</li>", "<li>Compare with normal periodic trends</li>"],
                "formulas": "Lanthanoid contraction due to poor shielding of 4f electrons",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">4f electrons poor shielding</text></svg>'
            }
        ]
    },
    9: {
        "title": "Coordination Compounds",
        "problems": [
            {
                "title": "Werner's Theory",
                "question": "Explain Werner's theory of coordination compounds with reference to the compound [Co(NH₃)₆]Cl₃.",
                "background": "Werner's theory explains the structure and bonding in coordination compounds. It states that: (1) Metal atoms have two types of valencies - primary (ionizable) and secondary (non-ionizable), (2) Primary valency is satisfied by anions, (3) Secondary valency is satisfied by neutral molecules or negative ions, (4) Secondary valency is directed in space and determines the geometry. The coordination number equals the secondary valency.",
                "solution": "For [Co(NH₃)₆]Cl₃: According to Werner's theory, Co has primary valency 3 (satisfied by 3 Cl⁻ ions) and secondary valency 6 (satisfied by 6 NH₃ molecules). The compound exists as [Co(NH₃)₆]³⁺ and 3Cl⁻. The 6 NH₃ molecules are coordinated to Co³⁺ ion, giving octahedral geometry. The 3 Cl⁻ ions are ionizable and are outside the coordination sphere.",
                "tips": ["<li>Identify primary and secondary valencies</li>", "<li>Explain ionizable vs non-ionizable groups</li>", "<li>Determine coordination number</li>", "<li>Predict geometry</li>", "<li>Write the structure correctly</li>"],
                "formulas": "Primary valency = ionizable, Secondary valency = coordination number",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">[Co(NH₃)₆]Cl₃</text></svg>'
            },
            {
                "title": "IUPAC Nomenclature",
                "question": "Write the IUPAC name of [Co(NH₃)₄Cl₂]Cl and [Pt(NH₃)₂Cl₂].",
                "background": "IUPAC nomenclature of coordination compounds follows specific rules: (1) Cation is named first, then anion, (2) In complex ion, ligands are named in alphabetical order, (3) Ligands ending in -ide become -ido, -ite becomes -ito, -ate becomes -ato, (4) Neutral ligands retain their names, (5) Greek prefixes indicate number of ligands, (6) Metal oxidation state is indicated by Roman numerals in parentheses.",
                "solution": "[Co(NH₃)₄Cl₂]Cl: Tetraamminedichloridocobalt(III) chloride. [Pt(NH₃)₂Cl₂]: Diamminedichloridoplatinum(II). In the first compound, Co has oxidation state +3 (4×0 + 2×(-1) + 1×(-1) = +3). In the second compound, Pt has oxidation state +2 (2×0 + 2×(-1) = +2). The ligands are named in alphabetical order: ammine, chlorido.",
                "tips": ["<li>Name ligands in alphabetical order</li>", "<li>Use appropriate endings for ligands</li>", "<li>Calculate oxidation state of metal</li>", "<li>Use Greek prefixes for numbers</li>", "<li>Write in correct order</li>"],
                "formulas": "Ligands in alphabetical order; Metal oxidation state in Roman numerals",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">IUPAC Nomenclature Rules</text></svg>'
            },
            {
                "title": "Isomerism in Coordination Compounds",
                "question": "Draw the structures of cis and trans isomers of [Pt(NH₃)₂Cl₂] and explain the difference.",
                "background": "Coordination compounds show various types of isomerism. Geometric isomerism occurs when ligands can be arranged differently around the central metal atom. In square planar complexes like [Pt(NH₃)₂Cl₂], cis isomer has identical ligands adjacent to each other, while trans isomer has them opposite to each other. This affects physical and chemical properties.",
                "solution": "Cis-[Pt(NH₃)₂Cl₂]: NH₃ and Cl are adjacent to each other. Trans-[Pt(NH₃)₂Cl₂]: NH₃ and Cl are opposite to each other. The difference is in the spatial arrangement of ligands. Cis isomer has a dipole moment and is polar, while trans isomer has no dipole moment and is non-polar. This affects their physical properties like solubility and chemical reactivity.",
                "tips": ["<li>Draw the structures clearly</li>", "<li>Show spatial arrangement of ligands</li>", "<li>Explain cis vs trans</li>", "<li>Mention dipole moment difference</li>", "<li>Connect to properties</li>"],
                "formulas": "Cis: adjacent ligands, Trans: opposite ligands",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="100" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="100" y="110" text-anchor="middle" font-size="10" fill="#374151">Cis</text><rect x="250" y="50" width="100" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="300" y="110" text-anchor="middle" font-size="10" fill="#374151">Trans</text></svg>'
            },
            {
                "title": "Crystal Field Theory",
                "question": "Explain crystal field splitting in octahedral complexes and calculate CFSE for [Fe(CN)₆]³⁻.",
                "background": "Crystal field theory explains the electronic structure and properties of coordination compounds. In octahedral complexes, the d orbitals split into two sets: t₂g (lower energy) and eg (higher energy). The energy difference is called crystal field splitting energy (Δo). CFSE = (0.4n₁ - 0.6n₂)Δo, where n₁ is electrons in t₂g and n₂ is electrons in eg.",
                "solution": "In octahedral complexes, d orbitals split into t₂g (dxy, dxz, dyz) and eg (dx²-y², dz²). For [Fe(CN)₆]³⁻: Fe³⁺ has d⁵ configuration. In strong field (CN⁻), all 5 electrons pair up in t₂g orbitals: t₂g⁵ eg⁰. CFSE = (0.4×5 - 0.6×0)Δo = 2.0Δo. This is a low-spin complex with maximum CFSE due to strong field ligand CN⁻.",
                "tips": ["<li>Identify the d orbital splitting</li>", "<li>Determine electron configuration</li>", "<li>Apply CFSE formula</li>", "<li>Consider field strength of ligand</li>", "<li>Check for high-spin vs low-spin</li>"],
                "formulas": "CFSE = (0.4n₁ - 0.6n₂)Δo; t₂g (lower), eg (higher)",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">Octahedral d orbital splitting</text></svg>'
            },
            {
                "title": "Bonding in Coordination Compounds",
                "question": "Explain the bonding in coordination compounds using valence bond theory with reference to [Ni(CN)₄]²⁻.",
                "background": "Valence bond theory explains bonding in coordination compounds by considering hybridization of metal orbitals. The type of hybridization depends on the coordination number and geometry. For square planar complexes like [Ni(CN)₄]²⁻, the metal uses dsp² hybridization. The hybrid orbitals overlap with ligand orbitals to form coordinate bonds.",
                "solution": "For [Ni(CN)₄]²⁻: Ni²⁺ has d⁸ configuration. To form square planar geometry, Ni²⁺ uses dsp² hybridization (one d, one s, two p orbitals). The four hybrid orbitals point towards the corners of a square and overlap with CN⁻ orbitals to form four coordinate bonds. This explains the square planar geometry and the formation of coordinate bonds.",
                "tips": ["<li>Identify the geometry and hybridization</li>", "<li>Write the electronic configuration</li>", "<li>Explain orbital overlap</li>", "<li>Connect hybridization to geometry</li>", "<li>Mention coordinate bond formation</li>"],
                "formulas": "Square planar: dsp² hybridization; Coordinate bonds by orbital overlap",
                "svg": '<svg viewBox="0 0 400 150" class="chemistry-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="12" fill="#374151">[Ni(CN)₄]²⁻: dsp² hybridization</text></svg>'
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
    """Generate chemistry board problems for chapters 4, 8, 9."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
