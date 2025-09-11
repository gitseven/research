#!/usr/bin/env python3
"""Generate Chapter 2 - Kinematics problems."""

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

# Chapter 2 - Kinematics problems
problems = [
    {
        "title": "Projectile Motion",
        "question": "A ball is thrown horizontally from a height of 20 m with an initial velocity of 10 m/s. Calculate: (a) time to hit ground, (b) horizontal distance, (c) velocity just before hitting ground.",
        "background": "Projectile motion involves two-dimensional motion under gravity. Horizontal and vertical components are independent. Horizontal velocity remains constant, while vertical velocity changes due to gravity. The trajectory is parabolic.",
        "solution": "(a) Using y = y₀ + v₀ᵧt + ½gt²: 0 = 20 + 0 + ½(9.8)t² → t = 2.02 s. (b) x = v₀ₓt = (10)(2.02) = 20.2 m. (c) vₓ = 10 m/s, vᵧ = gt = 19.8 m/s, v = √(vₓ² + vᵧ²) = 22.2 m/s.",
        "tips": ["<li>Draw clear diagram with coordinate system</li>", "<li>Separate horizontal and vertical motion</li>", "<li>Use kinematic equations for each direction</li>", "<li>Time is same for both directions</li>", "<li>Check units and reasonableness</li>"],
        "formulas": "x = v₀ₓt, y = y₀ + v₀ᵧt + ½gt², vᵧ = v₀ᵧ + gt",
        "svg": '<svg viewBox="0 0 400 200" class="physics-diagram"><path d="M 50 150 Q 200 50 350 150" stroke="#ef4444" stroke-width="3" fill="none"/><circle cx="50" cy="150" r="5" fill="#ef4444"/><text x="50" y="140" text-anchor="middle" font-size="10" fill="#ef4444">v₀</text></svg>'
    },
    {
        "title": "Uniform Acceleration",
        "question": "A car accelerates from rest at 2 m/s² for 10 seconds, then moves at constant velocity for 5 seconds. Calculate total distance traveled.",
        "background": "Uniform acceleration means constant acceleration. Use kinematic equations: v = v₀ + at, x = x₀ + v₀t + ½at². For constant velocity, x = vt. Break motion into phases with different accelerations.",
        "solution": "Phase 1: v = 0 + (2)(10) = 20 m/s, x₁ = 0 + 0 + ½(2)(10)² = 100 m. Phase 2: x₂ = (20)(5) = 100 m. Total distance = 100 + 100 = 200 m.",
        "tips": ["<li>Break motion into phases</li>", "<li>Use appropriate equations for each phase</li>", "<li>Final velocity of one phase = initial velocity of next</li>", "<li>Add distances from each phase</li>", "<li>Draw velocity-time graph if helpful</li>"],
        "formulas": "v = v₀ + at, x = x₀ + v₀t + ½at², x = vt (constant velocity)",
        "svg": '<svg viewBox="0 0 400 150" class="physics-diagram"><rect x="50" y="50" width="300" height="50" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Acceleration then Constant Velocity</text></svg>'
    }
]

def main():
    chapter_dir = Path("Physics/ch2")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    for i, problem in enumerate(problems, 1):
        html_content = create_problem_html(
            2, i, problem["title"], problem["question"],
            problem["background"], problem["solution"], 
            "\n".join(problem["tips"]), problem["formulas"], problem["svg"]
        )
        
        output_file = chapter_dir / f"problem-2-{i:02d}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {output_file}")

if __name__ == "__main__":
    main()
