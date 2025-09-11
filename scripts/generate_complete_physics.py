#!/usr/bin/env python3
"""Generate complete set of Physics problems for all chapters - 12th Board 2026."""

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

# Complete problem data for all chapters
chapters_data = {
    2: {
        "title": "Kinematics",
        "problems": [
            {"title": "Projectile Motion", "question": "A ball is thrown horizontally from a height of 20 m with an initial velocity of 10 m/s. Calculate: (a) time to hit ground, (b) horizontal distance, (c) velocity just before hitting ground.", "background": "Projectile motion involves two-dimensional motion under gravity. Horizontal and vertical components are independent. Horizontal velocity remains constant, while vertical velocity changes due to gravity. The trajectory is parabolic.", "solution": "(a) Using y = y₀ + v₀ᵧt + ½gt²: 0 = 20 + 0 + ½(9.8)t² → t = 2.02 s. (b) x = v₀ₓt = (10)(2.02) = 20.2 m. (c) vₓ = 10 m/s, vᵧ = gt = 19.8 m/s, v = √(vₓ² + vᵧ²) = 22.2 m/s.", "tips": ["<li>Draw clear diagram with coordinate system</li>", "<li>Separate horizontal and vertical motion</li>", "<li>Use kinematic equations for each direction</li>", "<li>Time is same for both directions</li>", "<li>Check units and reasonableness</li>"], "formulas": "x = v₀ₓt, y = y₀ + v₀ᵧt + ½gt², vᵧ = v₀ᵧ + gt"},
            {"title": "Uniform Acceleration", "question": "A car accelerates from rest at 2 m/s² for 10 seconds, then moves at constant velocity for 5 seconds. Calculate total distance traveled.", "background": "Uniform acceleration means constant acceleration. Use kinematic equations: v = v₀ + at, x = x₀ + v₀t + ½at². For constant velocity, x = vt. Break motion into phases with different accelerations.", "solution": "Phase 1: v = 0 + (2)(10) = 20 m/s, x₁ = 0 + 0 + ½(2)(10)² = 100 m. Phase 2: x₂ = (20)(5) = 100 m. Total distance = 100 + 100 = 200 m.", "tips": ["<li>Break motion into phases</li>", "<li>Use appropriate equations for each phase</li>", "<li>Final velocity of one phase = initial velocity of next</li>", "<li>Add distances from each phase</li>", "<li>Draw velocity-time graph if helpful</li>"], "formulas": "v = v₀ + at, x = x₀ + v₀t + ½at², x = vt (constant velocity)"},
            {"title": "Relative Motion", "question": "A boat crosses a river 200 m wide flowing at 3 m/s. The boat's speed in still water is 5 m/s. Find: (a) time to cross, (b) downstream drift, (c) actual velocity.", "background": "Relative motion involves analyzing motion from different reference frames. For river crossing, resolve velocity into components perpendicular and parallel to flow. The actual path is the vector sum of boat velocity and river velocity.", "solution": "(a) Time = width/velocity perpendicular to flow = 200/5 = 40 s. (b) Drift = river velocity × time = 3 × 40 = 120 m. (c) Actual velocity = √(5² + 3²) = √34 = 5.83 m/s at angle θ = tan⁻¹(3/5) = 30.96°", "tips": ["<li>Resolve velocities into components</li>", "<li>Use perpendicular component for crossing time</li>", "<li>Use parallel component for drift</li>", "<li>Add velocities vectorially</li>", "<li>Check with Pythagoras theorem</li>"], "formulas": "v_actual = √(v_boat² + v_river²), θ = tan⁻¹(v_river/v_boat)"},
            {"title": "Circular Motion", "question": "A particle moves in a circle of radius 2 m with constant speed 4 m/s. Find: (a) angular velocity, (b) centripetal acceleration, (c) time period.", "background": "Circular motion involves constant speed but changing direction. Angular velocity ω = v/r relates linear and angular speeds. Centripetal acceleration a = v²/r points toward center. Time period T = 2πr/v = 2π/ω.", "solution": "(a) ω = v/r = 4/2 = 2 rad/s. (b) a = v²/r = 4²/2 = 8 m/s². (c) T = 2πr/v = 2π(2)/4 = π s = 3.14 s", "tips": ["<li>Use ω = v/r for angular velocity</li>", "<li>Apply a = v²/r for centripetal acceleration</li>", "<li>Use T = 2π/ω for time period</li>", "<li>Check units (rad/s, m/s², s)</li>", "<li>Verify with f = 1/T</li>"], "formulas": "ω = v/r, a = v²/r, T = 2π/ω"},
            {"title": "Free Fall", "question": "A stone is dropped from a height of 45 m. Find: (a) time to reach ground, (b) velocity on impact, (c) distance fallen in last second.", "background": "Free fall is motion under gravity only. Use kinematic equations with a = g = 9.8 m/s². For dropped objects, initial velocity v₀ = 0. Distance in last second = total distance - distance in (t-1) seconds.", "solution": "(a) Using h = ½gt²: 45 = ½(9.8)t² → t = 3.03 s. (b) v = gt = 9.8(3.03) = 29.7 m/s. (c) Distance in 2.03 s = ½(9.8)(2.03)² = 20.2 m. Last second = 45 - 20.2 = 24.8 m", "tips": ["<li>Use h = ½gt² for time</li>", "<li>Apply v = gt for final velocity</li>", "<li>Calculate distance in (t-1) seconds</li>", "<li>Subtract from total height</li>", "<li>Check with v² = 2gh</li>"], "formulas": "h = ½gt², v = gt, v² = 2gh"},
            {"title": "Motion Under Gravity", "question": "A ball is thrown upward with velocity 20 m/s. Find: (a) maximum height, (b) time to reach maximum height, (c) total time in air.", "background": "Motion under gravity involves constant acceleration g = 9.8 m/s² downward. At maximum height, velocity becomes zero. Time to go up equals time to come down. Use v = v₀ + at and h = v₀t + ½at².", "solution": "(a) At max height, v = 0. Using v² = v₀² + 2ah: 0 = 20² + 2(-9.8)h → h = 20.4 m. (b) Using v = v₀ + at: 0 = 20 + (-9.8)t → t = 2.04 s. (c) Total time = 2 × 2.04 = 4.08 s", "tips": ["<li>At max height, v = 0</li>", "<li>Use v² = v₀² + 2ah for height</li>", "<li>Apply v = v₀ + at for time</li>", "<li>Total time = 2 × time to max height</li>", "<li>Check with h = v₀t - ½gt²</li>"], "formulas": "h_max = v₀²/(2g), t_up = v₀/g, t_total = 2v₀/g"},
            {"title": "Velocity-Time Graph", "question": "From the v-t graph: v = 2t for 0 ≤ t ≤ 5, v = 10 for 5 ≤ t ≤ 8, v = 10 - 2(t-8) for 8 ≤ t ≤ 13. Find total displacement.", "background": "Velocity-time graphs show how velocity changes with time. Displacement equals area under the v-t curve. For piecewise functions, calculate area for each segment and add them. Positive area = forward motion, negative area = backward motion.", "solution": "Segment 1 (0-5s): Area = ½(5)(10) = 25 m. Segment 2 (5-8s): Area = (3)(10) = 30 m. Segment 3 (8-13s): Area = ½(5)(10) = 25 m. Total displacement = 25 + 30 + 25 = 80 m", "tips": ["<li>Calculate area under each segment</li>", "<li>Use appropriate formulas (triangle, rectangle)</li>", "<li>Add all areas</li>", "<li>Consider positive/negative areas</li>", "<li>Check units (m/s × s = m)</li>"], "formulas": "Displacement = ∫v dt = area under v-t graph"},
            {"title": "Acceleration-Time Graph", "question": "An object starts from rest. Acceleration: a = 2 m/s² for 0-4s, a = 0 for 4-6s, a = -1 m/s² for 6-10s. Find velocity at t = 10s.", "background": "Acceleration-time graphs show how acceleration changes. Velocity change equals area under a-t curve. Initial velocity plus change in velocity gives final velocity. For constant acceleration, use v = v₀ + at.", "solution": "Segment 1: Δv₁ = (2)(4) = 8 m/s. Segment 2: Δv₂ = 0. Segment 3: Δv₃ = (-1)(4) = -4 m/s. Total change = 8 + 0 - 4 = 4 m/s. Final velocity = 0 + 4 = 4 m/s", "tips": ["<li>Calculate area under each segment</li>", "<li>Add velocity changes</li>", "<li>Add to initial velocity</li>", "<li>Check signs carefully</li>", "<li>Verify with v = v₀ + ∫a dt</li>"], "formulas": "Δv = ∫a dt = area under a-t graph"},
            {"title": "Two-Dimensional Motion", "question": "A particle moves with position vector r = (3t²)i + (4t)j. Find: (a) velocity at t = 2s, (b) acceleration, (c) speed at t = 2s.", "background": "Two-dimensional motion involves x and y components. Position vector r = xi + yj. Velocity v = dr/dt = (dx/dt)i + (dy/dt)j. Acceleration a = dv/dt = (d²x/dt²)i + (d²y/dt²)j. Speed = |v| = √(vₓ² + vᵧ²).", "solution": "(a) v = dr/dt = (6t)i + (4)j. At t = 2s: v = 12i + 4j m/s. (b) a = dv/dt = 6i + 0j = 6i m/s². (c) Speed = |v| = √(12² + 4²) = √160 = 12.65 m/s", "tips": ["<li>Differentiate position to get velocity</li>", "<li>Differentiate velocity to get acceleration</li>", "<li>Use magnitude formula for speed</li>", "<li>Check units for each component</li>", "<li>Verify with calculus</li>"], "formulas": "v = dr/dt, a = dv/dt, |v| = √(vₓ² + vᵧ²)"},
            {"title": "Uniform Circular Motion", "question": "A particle moves in a circle of radius 5 m with angular velocity 2 rad/s. Find: (a) linear speed, (b) centripetal acceleration, (c) angular displacement in 3 seconds.", "background": "Uniform circular motion has constant angular velocity ω. Linear speed v = rω. Centripetal acceleration a = v²/r = rω². Angular displacement θ = ωt. The motion is periodic with period T = 2π/ω.", "solution": "(a) v = rω = (5)(2) = 10 m/s. (b) a = rω² = (5)(2)² = 20 m/s². (c) θ = ωt = (2)(3) = 6 rad = 6(180/π) = 343.8°", "tips": ["<li>Use v = rω for linear speed</li>", "<li>Apply a = rω² for centripetal acceleration</li>", "<li>Use θ = ωt for angular displacement</li>", "<li>Convert radians to degrees if needed</li>", "<li>Check with a = v²/r</li>"], "formulas": "v = rω, a = rω², θ = ωt"}
        ]
    },
    5: {
        "title": "Motion of System of Particles and Rigid Body",
        "problems": [
            {"title": "Center of Mass", "question": "Three particles of masses 2 kg, 3 kg, and 5 kg are at positions (0,0), (2,0), and (1,3) respectively. Find center of mass coordinates.", "background": "Center of mass is the weighted average position of all particles. For discrete particles: x_cm = Σ(mᵢxᵢ)/Σmᵢ, y_cm = Σ(mᵢyᵢ)/Σmᵢ. It represents the point where the entire mass can be considered concentrated.", "solution": "x_cm = (2×0 + 3×2 + 5×1)/(2+3+5) = (0+6+5)/10 = 1.1 m. y_cm = (2×0 + 3×0 + 5×3)/(2+3+5) = (0+0+15)/10 = 1.5 m. Center of mass is at (1.1, 1.5) m", "tips": ["<li>Use x_cm = Σ(mᵢxᵢ)/Σmᵢ</li>", "<li>Calculate y_cm = Σ(mᵢyᵢ)/Σmᵢ</li>", "<li>Sum all masses for denominator</li>", "<li>Check units (kg·m/kg = m)</li>", "<li>Verify with symmetry if applicable</li>"], "formulas": "x_cm = Σ(mᵢxᵢ)/Σmᵢ, y_cm = Σ(mᵢyᵢ)/Σmᵢ"},
            {"title": "Linear Momentum", "question": "A 2 kg object moves at 5 m/s collides with a 3 kg object at rest. After collision, first object moves at 2 m/s. Find velocity of second object.", "background": "Linear momentum p = mv is conserved in collisions. Total momentum before = total momentum after. For elastic collisions, both momentum and kinetic energy are conserved. For inelastic collisions, only momentum is conserved.", "solution": "Conservation of momentum: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. (2)(5) + (3)(0) = (2)(2) + (3)v₂'. 10 = 4 + 3v₂'. v₂' = 2 m/s", "tips": ["<li>Apply momentum conservation</li>", "<li>Use proper signs for direction</li>", "<li>Solve for unknown velocity</li>", "<li>Check units (kg·m/s)</li>", "<li>Verify total momentum is conserved</li>"], "formulas": "m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'"},
            {"title": "Angular Momentum", "question": "A particle of mass 0.5 kg moves in a circle of radius 2 m with speed 4 m/s. Find angular momentum about center.", "background": "Angular momentum L = r × p = rmv sinθ. For circular motion, L = rmv = mr²ω. It's conserved in absence of external torque. Angular momentum is a vector quantity with direction given by right-hand rule.", "solution": "L = rmv = (2)(0.5)(4) = 4 kg·m²/s. Since motion is circular, L = mr²ω = (0.5)(2)²(2) = 4 kg·m²/s. Angular momentum = 4 kg·m²/s", "tips": ["<li>Use L = rmv for linear motion</li>", "<li>Apply L = mr²ω for circular motion</li>", "<li>Check units (kg·m²/s)</li>", "<li>Consider direction (perpendicular to plane)</li>", "<li>Verify with ω = v/r</li>"], "formulas": "L = r × p = rmv, L = mr²ω"},
            {"title": "Moment of Inertia", "question": "Three masses 1 kg, 2 kg, 3 kg are at distances 1 m, 2 m, 3 m from axis. Find moment of inertia about the axis.", "background": "Moment of inertia I = Σ(mᵢrᵢ²) measures rotational inertia. It depends on mass distribution relative to axis. For point masses, I = Σ(mᵢrᵢ²). For continuous bodies, I = ∫r²dm. It's analogous to mass in linear motion.", "solution": "I = Σ(mᵢrᵢ²) = (1)(1)² + (2)(2)² + (3)(3)² = 1 + 8 + 27 = 36 kg·m²", "tips": ["<li>Use I = Σ(mᵢrᵢ²) for point masses</li>", "<li>Square each distance</li>", "<li>Multiply by corresponding mass</li>", "<li>Add all terms</li>", "<li>Check units (kg·m²)</li>"], "formulas": "I = Σ(mᵢrᵢ²)"},
            {"title": "Rotational Kinetic Energy", "question": "A disc of mass 2 kg and radius 0.5 m rotates at 10 rad/s. Find rotational kinetic energy. (I_disc = ½mr²)", "background": "Rotational kinetic energy KE_rot = ½Iω². It's analogous to linear kinetic energy KE = ½mv². For rolling motion, total KE = KE_translational + KE_rotational. The moment of inertia depends on shape and axis.", "solution": "I = ½mr² = ½(2)(0.5)² = 0.25 kg·m². KE_rot = ½Iω² = ½(0.25)(10)² = ½(0.25)(100) = 12.5 J", "tips": ["<li>Calculate moment of inertia first</li>", "<li>Use KE_rot = ½Iω²</li>", "<li>Check units (kg·m²·rad²/s² = J)</li>", "<li>Verify with I = ½mr² for disc</li>", "<li>Consider rolling motion if applicable</li>"], "formulas": "KE_rot = ½Iω², I_disc = ½mr²"},
            {"title": "Torque", "question": "A force of 10 N is applied at 30° to a 2 m lever. Find torque about the pivot.", "background": "Torque τ = r × F = rF sinθ measures rotational effect of force. It depends on force magnitude, distance from axis, and angle. Maximum torque occurs when θ = 90°. Torque causes angular acceleration according to τ = Iα.", "solution": "τ = rF sinθ = (2)(10)sin30° = (2)(10)(0.5) = 10 N·m", "tips": ["<li>Use τ = rF sinθ</li>", "<li>Check angle (30° from lever)</li>", "<li>Calculate sin30° = 0.5</li>", "<li>Check units (m·N = N·m)</li>", "<li>Consider direction (into/out of page)</li>"], "formulas": "τ = r × F = rF sinθ"},
            {"title": "Rolling Motion", "question": "A solid sphere of mass 2 kg and radius 0.1 m rolls without slipping down an incline. If linear acceleration is 2 m/s², find angular acceleration.", "background": "Rolling without slipping means v = rω and a = rα. The condition relates linear and angular quantities. For rolling motion, total kinetic energy includes both translational and rotational parts. Friction provides the necessary torque.", "solution": "For rolling without slipping: a = rα. α = a/r = 2/0.1 = 20 rad/s²", "tips": ["<li>Use a = rα for rolling without slipping</li>", "<li>Solve for angular acceleration</li>", "<li>Check units (m/s² ÷ m = rad/s²)</li>", "<li>Verify with v = rω</li>", "<li>Consider friction requirement</li>"], "formulas": "a = rα, v = rω"},
            {"title": "Conservation of Angular Momentum", "question": "A skater with arms extended has moment of inertia 5 kg·m² and spins at 2 rad/s. When arms are pulled in, I becomes 2 kg·m². Find new angular velocity.", "background": "Angular momentum is conserved when no external torque acts. L = Iω = constant. When moment of inertia changes, angular velocity changes inversely to maintain constant angular momentum. This is the ice skater effect.", "solution": "Conservation: I₁ω₁ = I₂ω₂. (5)(2) = (2)ω₂. 10 = 2ω₂. ω₂ = 5 rad/s", "tips": ["<li>Apply L = Iω = constant</li>", "<li>Use I₁ω₁ = I₂ω₂</li>", "<li>Solve for new angular velocity</li>", "<li>Check units (kg·m²·rad/s)</li>", "<li>Verify angular momentum is conserved</li>"], "formulas": "L = Iω = constant, I₁ω₁ = I₂ω₂"},
            {"title": "Parallel Axis Theorem", "question": "A rod of mass 1 kg and length 2 m rotates about an axis through one end. Find moment of inertia. (I_cm = 1/12 mL²)", "background": "Parallel axis theorem: I = I_cm + Md². It relates moment of inertia about any axis to that about center of mass. The distance d is between the two parallel axes. This theorem is essential for calculating moments of inertia.", "solution": "I_cm = (1/12)mL² = (1/12)(1)(2)² = 1/3 kg·m². Distance from center to end = L/2 = 1 m. I = I_cm + Md² = 1/3 + (1)(1)² = 1/3 + 1 = 4/3 kg·m²", "tips": ["<li>Calculate I_cm first</li>", "<li>Find distance between axes</li>", "<li>Use I = I_cm + Md²</li>", "<li>Check units (kg·m²)</li>", "<li>Verify with direct calculation</li>"], "formulas": "I = I_cm + Md²"},
            {"title": "Rotational Dynamics", "question": "A wheel of moment of inertia 0.5 kg·m² is subjected to torque 2 N·m. Find angular acceleration.", "background": "Rotational dynamics relates torque to angular acceleration: τ = Iα. This is analogous to F = ma in linear motion. The moment of inertia I is the rotational equivalent of mass. Greater torque or smaller moment of inertia gives greater angular acceleration.", "solution": "τ = Iα. α = τ/I = 2/0.5 = 4 rad/s²", "tips": ["<li>Use τ = Iα</li>", "<li>Solve for angular acceleration</li>", "<li>Check units (N·m ÷ kg·m² = rad/s²)</li>", "<li>Verify with F = ma analogy</li>", "<li>Consider direction of rotation</li>"], "formulas": "τ = Iα"}
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
