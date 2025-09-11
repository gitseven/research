#!/usr/bin/env python3
"""Generate all Physics problems for 12th Board 2026."""

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
    .physics-diagram {{ max-width:100%; height:auto; display:block; margin:12px auto; border:1px solid #e5e7eb; border-radius:8px; background:#fafafa; }}
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

# Comprehensive problem data for all chapters
chapters_data = {
    3: {
        "title": "Laws of Motion",
        "problems": [
            {"title": "Newton's First Law", "question": "A 5 kg block rests on a frictionless surface. A 20 N force is applied horizontally. Calculate acceleration.", "background": "Newton's first law states that an object at rest stays at rest unless acted upon by a net external force. F = ma relates force, mass, and acceleration.", "solution": "F = ma → a = F/m = 20 N / 5 kg = 4 m/s²", "tips": ["<li>Draw free-body diagram</li>", "<li>Identify all forces</li>", "<li>Apply F = ma</li>", "<li>Check units</li>", "<li>Verify reasonableness</li>"], "formulas": "F = ma"},
            {"title": "Friction", "question": "A 10 kg block slides on a surface with μ = 0.3. Calculate frictional force.", "background": "Friction opposes motion and is proportional to normal force. f = μN where μ is coefficient of friction and N is normal force.", "solution": "N = mg = (10)(9.8) = 98 N. f = μN = (0.3)(98) = 29.4 N", "tips": ["<li>Calculate normal force first</li>", "<li>Use f = μN</li>", "<li>Check coefficient value</li>", "<li>Verify direction</li>", "<li>Consider static vs kinetic</li>"], "formulas": "f = μN, N = mg"},
            {"title": "Tension", "question": "Two masses 3 kg and 5 kg are connected by a string over a pulley. Find acceleration.", "background": "For connected masses, treat as a system. Net force = total mass × acceleration. Tension is internal force that cancels out.", "solution": "Net force = m₂g - m₁g = (5-3)(9.8) = 19.6 N. Total mass = 8 kg. a = 19.6/8 = 2.45 m/s²", "tips": ["<li>Treat as single system</li>", "<li>Net force = difference in weights</li>", "<li>Total mass for acceleration</li>", "<li>Check direction</li>", "<li>Verify with individual analysis</li>"], "formulas": "a = (m₂-m₁)g/(m₁+m₂)"},
            {"title": "Circular Motion", "question": "A 2 kg mass moves in a circle of radius 5 m at 10 m/s. Find centripetal force.", "background": "Circular motion requires centripetal force toward center. F = mv²/r. This force changes direction but not speed.", "solution": "F = mv²/r = (2)(10)²/5 = 200/5 = 40 N", "tips": ["<li>Identify centripetal force</li>", "<li>Use F = mv²/r</li>", "<li>Check units</li>", "<li>Direction toward center</li>", "<li>Speed not velocity</li>"], "formulas": "F = mv²/r"},
            {"title": "Momentum", "question": "A 0.5 kg ball moving at 20 m/s hits a wall and rebounds at 15 m/s. Find impulse.", "background": "Impulse equals change in momentum. J = Δp = m(v_f - v_i). Consider direction for velocity.", "solution": "J = m(v_f - v_i) = 0.5(15 - (-20)) = 0.5(35) = 17.5 N⋅s", "tips": ["<li>Define coordinate system</li>", "<li>Use J = Δp</li>", "<li>Consider direction</li>", "<li>Check units</li>", "<li>Verify with FΔt</li>"], "formulas": "J = Δp = m(v_f - v_i)"},
            {"title": "Collision", "question": "Two balls of masses 2 kg and 3 kg collide. Before: v₁ = 5 m/s, v₂ = -2 m/s. After: v₁ = -1 m/s. Find v₂.", "background": "Momentum is conserved in collisions. Total momentum before = total momentum after. m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'", "solution": "Conservation: (2)(5) + (3)(-2) = (2)(-1) + (3)v₂'. 10 - 6 = -2 + 3v₂'. 4 = -2 + 3v₂'. v₂' = 2 m/s", "tips": ["<li>Apply momentum conservation</li>", "<li>Use proper signs</li>", "<li>Solve for unknown</li>", "<li>Check units</li>", "<li>Verify total momentum</li>"], "formulas": "m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'"},
            {"title": "Inclined Plane", "question": "A 4 kg block slides down a 30° incline with μ = 0.2. Find acceleration.", "background": "On inclined plane, weight has components: mg sinθ along plane and mg cosθ normal to plane. Friction opposes motion.", "solution": "Along plane: mg sinθ - μmg cosθ = ma. a = g(sinθ - μ cosθ) = 9.8(sin30° - 0.2 cos30°) = 9.8(0.5 - 0.173) = 3.2 m/s²", "tips": ["<li>Resolve weight into components</li>", "<li>Use a = g(sinθ - μ cosθ)</li>", "<li>Check angle</li>", "<li>Verify direction</li>", "<li>Consider friction direction</li>"], "formulas": "a = g(sinθ - μ cosθ)"},
            {"title": "Atwood Machine", "question": "Masses 2 kg and 4 kg are connected over a pulley. Find acceleration and tension.", "background": "Atwood machine has two masses connected by a string over a pulley. Net force = difference in weights, total mass = sum of masses.", "solution": "a = (m₂-m₁)g/(m₁+m₂) = (4-2)(9.8)/(2+4) = 19.6/6 = 3.27 m/s². T = m₁(g+a) = 2(9.8+3.27) = 26.1 N", "tips": ["<li>Use a = (m₂-m₁)g/(m₁+m₂)</li>", "<li>Calculate tension separately</li>", "<li>Check direction</li>", "<li>Verify with both masses</li>", "<li>Consider pulley mass</li>"], "formulas": "a = (m₂-m₁)g/(m₁+m₂), T = m₁(g+a)"},
            {"title": "Banked Curve", "question": "A car rounds a banked curve of radius 100 m at 30 m/s. Find banking angle for no friction.", "background": "On banked curve, normal force has horizontal component providing centripetal force. tanθ = v²/(rg) for no friction needed.", "solution": "tanθ = v²/(rg) = (30)²/(100×9.8) = 900/980 = 0.918. θ = tan⁻¹(0.918) = 42.6°", "tips": ["<li>Use tanθ = v²/(rg)</li>", "<li>Check units</li>", "<li>Calculate angle</li>", "<li>Verify with centripetal force</li>", "<li>Consider friction if given</li>"], "formulas": "tanθ = v²/(rg)"},
            {"title": "Rocket Propulsion", "question": "A rocket of mass 1000 kg ejects 100 kg at 200 m/s. Find final velocity if initial velocity was 50 m/s.", "background": "Rocket propulsion uses conservation of momentum. Initial momentum = final momentum. Consider ejected mass and remaining mass.", "solution": "Initial p = (1000)(50) = 50,000 kg⋅m/s. Final: (900)v + (100)(200) = 50,000. 900v = 30,000. v = 33.3 m/s", "tips": ["<li>Apply momentum conservation</li>", "<li>Consider ejected mass</li>", "<li>Use proper signs</li>", "<li>Check units</li>", "<li>Verify total momentum</li>"], "formulas": "m₁v₁ = m₂v₂ + m₃v₃"}
        ]
    },
    4: {
        "title": "Work, Energy and Power",
        "problems": [
            {"title": "Work Done by Force", "question": "A 50 N force pushes a 10 kg block 5 m along a horizontal surface. Calculate work done.", "background": "Work is done when a force causes displacement. W = F⋅d = Fd cosθ where θ is angle between force and displacement. Work is scalar.", "solution": "W = Fd cosθ = (50)(5)cos0° = 250 J", "tips": ["<li>Use W = Fd cosθ</li>", "<li>Check angle</li>", "<li>Verify units</li>", "<li>Consider direction</li>", "<li>Work is scalar</li>"], "formulas": "W = F⋅d = Fd cosθ"},
            {"title": "Kinetic Energy", "question": "A 2 kg object moves at 10 m/s. Calculate its kinetic energy.", "background": "Kinetic energy is energy due to motion. KE = ½mv². It's always positive and depends on speed, not velocity direction.", "solution": "KE = ½mv² = ½(2)(10)² = ½(2)(100) = 100 J", "tips": ["<li>Use KE = ½mv²</li>", "<li>Check units</li>", "<li>Always positive</li>", "<li>Depends on speed</li>", "<li>Verify calculation</li>"], "formulas": "KE = ½mv²"},
            {"title": "Potential Energy", "question": "A 5 kg object is lifted 3 m above ground. Calculate gravitational potential energy.", "background": "Gravitational potential energy depends on height above reference level. PE = mgh where h is height and g is acceleration due to gravity.", "solution": "PE = mgh = (5)(9.8)(3) = 147 J", "tips": ["<li>Use PE = mgh</li>", "<li>Choose reference level</li>", "<li>Check units</li>", "<li>Height is vertical</li>", "<li>Can be negative</li>"], "formulas": "PE = mgh"},
            {"title": "Work-Energy Theorem", "question": "A 4 kg block starts from rest and reaches 8 m/s after 2 m. Find applied force.", "background": "Work-energy theorem states that work done equals change in kinetic energy. W = ΔKE = ½mv² - ½mv₀²", "solution": "W = ΔKE = ½(4)(8)² - 0 = 128 J. W = Fd → F = W/d = 128/2 = 64 N", "tips": ["<li>Apply work-energy theorem</li>", "<li>Calculate ΔKE</li>", "<li>Use W = Fd</li>", "<li>Check units</li>", "<li>Verify with kinematics</li>"], "formulas": "W = ΔKE = ½mv² - ½mv₀²"},
            {"title": "Conservation of Energy", "question": "A 2 kg ball is dropped from 10 m height. Find speed just before hitting ground.", "background": "When only conservative forces act, total mechanical energy is conserved. KE + PE = constant. Initial PE converts to final KE.", "solution": "Initial: PE = mgh = (2)(9.8)(10) = 196 J, KE = 0. Final: PE = 0, KE = ½mv². Conservation: 196 = ½(2)v². v² = 196. v = 14 m/s", "tips": ["<li>Apply energy conservation</li>", "<li>Set initial = final</li>", "<li>Choose reference level</li>", "<li>Check units</li>", "<li>Verify with kinematics</li>"], "formulas": "KE + PE = constant"},
            {"title": "Power", "question": "A motor lifts 100 kg mass 5 m in 10 seconds. Calculate power.", "background": "Power is rate of doing work. P = W/t = Fd/t = Fv. It's measured in watts (W) or horsepower. Average power = total work/time.", "solution": "W = mgh = (100)(9.8)(5) = 4900 J. P = W/t = 4900/10 = 490 W", "tips": ["<li>Calculate work first</li>", "<li>Use P = W/t</li>", "<li>Check units</li>", "<li>Consider time</li>", "<li>Verify with P = Fv</li>"], "formulas": "P = W/t = Fv"},
            {"title": "Efficiency", "question": "An engine produces 1000 W but only 800 W is useful. Calculate efficiency.", "background": "Efficiency is ratio of useful output to total input. η = (useful output/total input) × 100%. It's always less than 100%.", "solution": "η = (800/1000) × 100% = 80%", "tips": ["<li>Use η = (useful/total) × 100%</li>", "<li>Check units</li>", "<li>Always < 100%</li>", "<li>Consider losses</li>", "<li>Verify calculation</li>"], "formulas": "η = (useful output/total input) × 100%"},
            {"title": "Spring Energy", "question": "A spring with k = 200 N/m is compressed 0.1 m. Calculate elastic potential energy.", "background": "Elastic potential energy is stored in deformed springs. PE = ½kx² where k is spring constant and x is displacement from equilibrium.", "solution": "PE = ½kx² = ½(200)(0.1)² = ½(200)(0.01) = 1 J", "tips": ["<li>Use PE = ½kx²</li>", "<li>Check units</li>", "<li>Always positive</li>", "<li>Depends on displacement</li>", "<li>Verify calculation</li>"], "formulas": "PE = ½kx²"},
            {"title": "Collision Energy", "question": "Two 2 kg balls collide. Before: v₁ = 5 m/s, v₂ = -3 m/s. After: v₁ = -2 m/s, v₂ = 4 m/s. Is kinetic energy conserved?", "background": "In elastic collisions, both momentum and kinetic energy are conserved. In inelastic collisions, only momentum is conserved. Check if total KE before = total KE after.", "solution": "KE before = ½(2)(5)² + ½(2)(-3)² = 25 + 9 = 34 J. KE after = ½(2)(-2)² + ½(2)(4)² = 4 + 16 = 20 J. Not conserved (inelastic)", "tips": ["<li>Calculate KE before and after</li>", "<li>Compare totals</li>", "<li>If equal: elastic</li>", "<li>If different: inelastic</li>", "<li>Check momentum too</li>"], "formulas": "KE = ½mv²"},
            {"title": "Variable Force", "question": "A force F = 2x acts on a 1 kg object from x = 0 to x = 3 m. Calculate work done.", "background": "For variable forces, work is calculated by integration. W = ∫F dx. For F = 2x, W = ∫₀³ 2x dx = [x²]₀³ = 9 J", "solution": "W = ∫₀³ 2x dx = [x²]₀³ = 3² - 0² = 9 J", "tips": ["<li>Use W = ∫F dx</li>", "<li>Integrate over displacement</li>", "<li>Check limits</li>", "<li>Verify units</li>", "<li>Consider force direction</li>"], "formulas": "W = ∫F dx"}
        ]
    }
}

def generate_chapter(chapter_num, chapter_data):
    """Generate all problems for a chapter."""
    chapter_dir = Path(f"Physics/ch{chapter_num}")
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
    """Generate all remaining physics problems."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All problems generated successfully!")

if __name__ == "__main__":
    main()
