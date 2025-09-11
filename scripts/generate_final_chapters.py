#!/usr/bin/env python3
"""Generate final Physics chapters 6, 7, 8 - 12th Board 2026."""

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

# Final chapters data
chapters_data = {
    6: {
        "title": "Gravitation",
        "problems": [
            {"title": "Newton's Law of Gravitation", "question": "Two masses 5 kg and 10 kg are 2 m apart. Find gravitational force between them.", "background": "Newton's law of universal gravitation states that every particle attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between them. F = Gm₁m₂/r² where G = 6.67 × 10⁻¹¹ N⋅m²/kg².", "solution": "F = Gm₁m₂/r² = (6.67×10⁻¹¹)(5)(10)/(2)² = (6.67×10⁻¹¹)(50)/4 = 8.34×10⁻¹⁰ N", "tips": ["<li>Use F = Gm₁m₂/r²</li>", "<li>Check units carefully</li>", "<li>G = 6.67 × 10⁻¹¹ N⋅m²/kg²</li>", "<li>Square the distance</li>", "<li>Verify with order of magnitude</li>"], "formulas": "F = Gm₁m₂/r², G = 6.67 × 10⁻¹¹ N⋅m²/kg²"},
            {"title": "Gravitational Field", "question": "Find gravitational field strength at a distance 2R from Earth's center, where R is Earth's radius.", "background": "Gravitational field strength g = GM/r² represents force per unit mass. At Earth's surface, g₀ = GM/R². At height h above surface, g = GM/(R+h)². The field strength decreases as 1/r² with distance from center.", "solution": "At Earth's surface: g₀ = GM/R². At distance 2R: g = GM/(2R)² = GM/(4R²) = g₀/4. If g₀ = 9.8 m/s², then g = 9.8/4 = 2.45 m/s²", "tips": ["<li>Use g = GM/r²</li>", "<li>Compare with surface value</li>", "<li>Apply inverse square law</li>", "<li>Check units (m/s²)</li>", "<li>Verify with g₀ = 9.8 m/s²</li>"], "formulas": "g = GM/r², g = g₀(R/r)²"},
            {"title": "Gravitational Potential Energy", "question": "A 2 kg mass is moved from Earth's surface to height 3R above surface. Find change in gravitational potential energy.", "background": "Gravitational potential energy U = -GMm/r is negative because work is done against gravity. The reference point is at infinity where U = 0. Change in PE = U_final - U_initial. Work done equals negative change in PE.", "solution": "U_surface = -GMm/R. U_3R = -GMm/(4R). ΔU = U_3R - U_surface = -GMm/(4R) - (-GMm/R) = -GMm/(4R) + GMm/R = 3GMm/(4R) = 3mg₀R/4 = 3(2)(9.8)(6.37×10⁶)/4 = 9.37×10⁷ J", "tips": ["<li>Use U = -GMm/r</li>", "<li>Calculate at both positions</li>", "<li>Find difference</li>", "<li>Use g₀ = GM/R²</li>", "<li>Check units (J)</li>"], "formulas": "U = -GMm/r, ΔU = U_final - U_initial"},
            {"title": "Escape Velocity", "question": "Calculate escape velocity from Earth's surface. (M_Earth = 5.97×10²⁴ kg, R_Earth = 6.37×10⁶ m)", "background": "Escape velocity is minimum speed needed to escape gravitational field. At escape velocity, total energy = 0 (KE + PE = 0). This gives v_escape = √(2GM/R). Escape velocity depends only on mass and radius of the planet.", "solution": "v_escape = √(2GM/R) = √(2×6.67×10⁻¹¹×5.97×10²⁴/6.37×10⁶) = √(1.25×10⁸) = 1.12×10⁴ m/s = 11.2 km/s", "tips": ["<li>Use v_escape = √(2GM/R)</li>", "<li>Check units carefully</li>", "<li>Convert to km/s</li>", "<li>Verify with known value</li>", "<li>Consider energy conservation</li>"], "formulas": "v_escape = √(2GM/R)"},
            {"title": "Orbital Velocity", "question": "A satellite orbits Earth at height 400 km. Find orbital velocity. (R_Earth = 6.37×10⁶ m)", "background": "Orbital velocity is speed needed for circular orbit. Centripetal force = gravitational force. mv²/r = GMm/r² gives v = √(GM/r). For circular orbits, orbital velocity is less than escape velocity by factor √2.", "solution": "r = R + h = 6.37×10⁶ + 4×10⁵ = 6.77×10⁶ m. v = √(GM/r) = √(6.67×10⁻¹¹×5.97×10²⁴/6.77×10⁶) = √(5.88×10⁷) = 7.67×10³ m/s = 7.67 km/s", "tips": ["<li>Use v = √(GM/r)</li>", "<li>Calculate total radius</li>", "<li>Check units</li>", "<li>Compare with escape velocity</li>", "<li>Verify with v_escape/√2</li>"], "formulas": "v = √(GM/r)"},
            {"title": "Kepler's Laws", "question": "A planet orbits Sun with period 2 years at distance 2 AU. Find period at distance 4 AU.", "background": "Kepler's third law: T² ∝ r³ or T₁²/T₂² = r₁³/r₂³. This relates orbital period to semi-major axis. For circular orbits, r is the radius. The law applies to all planets orbiting the same central body.", "solution": "T₁²/T₂² = r₁³/r₂³. (2)²/T₂² = (2)³/(4)³. 4/T₂² = 8/64 = 1/8. T₂² = 32. T₂ = √32 = 5.66 years", "tips": ["<li>Use T₁²/T₂² = r₁³/r₂³</li>", "<li>Substitute given values</li>", "<li>Solve for unknown period</li>", "<li>Check units (years)</li>", "<li>Verify with T² ∝ r³</li>"], "formulas": "T₁²/T₂² = r₁³/r₂³"},
            {"title": "Gravitational Potential", "question": "Find gravitational potential at distance 3R from Earth's center due to Earth alone.", "background": "Gravitational potential V = -GM/r is potential energy per unit mass. It's a scalar quantity. The potential is negative and approaches zero at infinity. Work done = mΔV. Potential difference between two points is independent of path.", "solution": "V = -GM/r = -GM/(3R) = -(6.67×10⁻¹¹×5.97×10²⁴)/(3×6.37×10⁶) = -2.08×10⁷ J/kg", "tips": ["<li>Use V = -GM/r</li>", "<li>Calculate total distance</li>", "<li>Check units (J/kg)</li>", "<li>Verify sign (negative)</li>", "<li>Compare with surface value</li>"], "formulas": "V = -GM/r"},
            {"title": "Satellite Energy", "question": "A 1000 kg satellite orbits Earth at 500 km altitude. Find total energy.", "background": "Total energy of satellite = KE + PE = ½mv² - GMm/r. For circular orbit, KE = -PE/2, so total energy = PE/2 = -GMm/(2r). The energy is negative, indicating bound orbit.", "solution": "r = R + h = 6.37×10⁶ + 5×10⁵ = 6.87×10⁶ m. E_total = -GMm/(2r) = -(6.67×10⁻¹¹×5.97×10²⁴×1000)/(2×6.87×10⁶) = -2.90×10¹⁰ J", "tips": ["<li>Use E = -GMm/(2r)</li>", "<li>Calculate orbital radius</li>", "<li>Check units (J)</li>", "<li>Verify negative sign</li>", "<li>Compare with escape energy</li>"], "formulas": "E_total = -GMm/(2r)"},
            {"title": "Tidal Forces", "question": "Explain why tides occur twice daily and why they're stronger during new moon and full moon.", "background": "Tides are caused by differential gravitational forces. Moon's gravity is stronger on near side than far side of Earth. This creates tidal bulges. Sun also contributes to tides. Spring tides (strongest) occur when Sun, Moon, and Earth are aligned (new/full moon).", "solution": "Tides occur twice daily because Earth rotates under two tidal bulges (near and far side of Moon). Spring tides are strongest because Sun and Moon gravitational forces add together during new moon (same side) and full moon (opposite sides), creating maximum tidal range.", "tips": ["<li>Consider differential gravity</li>", "<li>Think about Earth's rotation</li>", "<li>Add Sun and Moon effects</li>", "<li>Consider alignment</li>", "<li>Explain twice daily occurrence</li>"], "formulas": "F_tidal ∝ 1/r³"},
            {"title": "Black Holes", "question": "Calculate Schwarzschild radius for a 10 solar mass black hole. (M_sun = 1.99×10³⁰ kg)", "background": "Schwarzschild radius is the radius at which escape velocity equals speed of light. R_s = 2GM/c². Within this radius, nothing can escape, not even light. This defines the event horizon of a black hole. The radius is proportional to mass.", "solution": "M = 10M_sun = 10×1.99×10³⁰ = 1.99×10³¹ kg. R_s = 2GM/c² = 2×6.67×10⁻¹¹×1.99×10³¹/(3×10⁸)² = 2.95×10⁴ m = 29.5 km", "tips": ["<li>Use R_s = 2GM/c²</li>", "<li>Calculate total mass</li>", "<li>Use c = 3×10⁸ m/s</li>", "<li>Check units (m)</li>", "<li>Convert to km</li>"], "formulas": "R_s = 2GM/c²"}
        ]
    },
    7: {
        "title": "Properties of Bulk Matter",
        "problems": [
            {"title": "Elasticity", "question": "A steel wire of length 2 m and cross-sectional area 1 mm² is stretched by 1 mm. Find stress and strain. (Young's modulus = 2×10¹¹ Pa)", "background": "Elasticity is the property of materials to return to original shape after deformation. Stress = Force/Area, Strain = Change in length/Original length. Young's modulus Y = Stress/Strain. Hooke's law applies for small deformations.", "solution": "Stress = F/A = (Y×Strain) = Y×(ΔL/L) = 2×10¹¹×(1×10⁻³/2) = 2×10¹¹×5×10⁻⁴ = 10⁸ Pa. Strain = ΔL/L = 1×10⁻³/2 = 5×10⁻⁴", "tips": ["<li>Use Stress = F/A</li>", "<li>Apply Strain = ΔL/L</li>", "<li>Check units (Pa, dimensionless)</li>", "<li>Verify with Y = Stress/Strain</li>", "<li>Convert mm to m</li>"], "formulas": "Stress = F/A, Strain = ΔL/L, Y = Stress/Strain"},
            {"title": "Fluid Pressure", "question": "Find pressure at depth 10 m in water. (ρ_water = 1000 kg/m³, g = 9.8 m/s²)", "background": "Pressure in fluids increases with depth due to weight of fluid above. P = P₀ + ρgh where P₀ is atmospheric pressure, ρ is density, g is acceleration due to gravity, and h is depth. This is hydrostatic pressure.", "solution": "P = P₀ + ρgh = 1.01×10⁵ + (1000)(9.8)(10) = 1.01×10⁵ + 9.8×10⁴ = 1.01×10⁵ + 0.98×10⁵ = 1.99×10⁵ Pa", "tips": ["<li>Use P = P₀ + ρgh</li>", "<li>Add atmospheric pressure</li>", "<li>Check units (Pa)</li>", "<li>Verify with known values</li>", "<li>Consider depth units</li>"], "formulas": "P = P₀ + ρgh"},
            {"title": "Buoyant Force", "question": "A 2 kg iron block is submerged in water. Find buoyant force. (ρ_iron = 7870 kg/m³, ρ_water = 1000 kg/m³)", "background": "Buoyant force is upward force exerted by fluid on submerged object. Archimedes' principle: F_b = ρ_fluid × V_displaced × g. The force equals weight of displaced fluid. Objects float when buoyant force equals weight.", "solution": "V_iron = m/ρ = 2/7870 = 2.54×10⁻⁴ m³. F_b = ρ_water × V_iron × g = 1000 × 2.54×10⁻⁴ × 9.8 = 2.49 N", "tips": ["<li>Calculate volume of object</li>", "<li>Use F_b = ρ_fluid × V × g</li>", "<li>Check units (N)</li>", "<li>Compare with weight</li>", "<li>Verify Archimedes' principle</li>"], "formulas": "F_b = ρ_fluid × V_displaced × g"},
            {"title": "Surface Tension", "question": "A soap bubble of radius 2 cm has surface tension 0.03 N/m. Find excess pressure inside.", "background": "Surface tension is force per unit length acting along surface. For spherical surfaces, excess pressure P = 4T/r where T is surface tension and r is radius. This is Laplace's law. Soap bubbles have two surfaces, so pressure is 4T/r.", "solution": "P = 4T/r = 4×0.03/0.02 = 4×0.03/0.02 = 6 Pa", "tips": ["<li>Use P = 4T/r for soap bubble</li>", "<li>Convert cm to m</li>", "<li>Check units (Pa)</li>", "<li>Consider two surfaces</li>", "<li>Verify with capillary rise</li>"], "formulas": "P = 4T/r (soap bubble), P = 2T/r (droplet)"},
            {"title": "Viscosity", "question": "A sphere of radius 1 cm falls through oil with terminal velocity 2 cm/s. Find viscosity. (ρ_sphere = 8000 kg/m³, ρ_oil = 900 kg/m³)", "background": "Viscosity is resistance to flow. For sphere falling through fluid, terminal velocity v = 2r²g(ρ_s - ρ_f)/(9η) where η is viscosity. At terminal velocity, drag force equals weight minus buoyant force.", "solution": "v = 2r²g(ρ_s - ρ_f)/(9η). η = 2r²g(ρ_s - ρ_f)/(9v) = 2×(0.01)²×9.8×(8000-900)/(9×0.02) = 2×10⁻⁴×9.8×7100/0.18 = 0.077 Pa⋅s", "tips": ["<li>Use v = 2r²g(ρ_s - ρ_f)/(9η)</li>", "<li>Solve for viscosity</li>", "<li>Check units (Pa⋅s)</li>", "<li>Convert cm to m</li>", "<li>Verify with Stokes' law</li>"], "formulas": "v = 2r²g(ρ_s - ρ_f)/(9η)"},
            {"title": "Capillary Action", "question": "Water rises 2 cm in a capillary tube of radius 0.5 mm. Find surface tension. (θ = 0°, ρ = 1000 kg/m³)", "background": "Capillary action is rise of liquid in narrow tubes due to surface tension. Height h = 2T cosθ/(ρgr) where T is surface tension, θ is contact angle, ρ is density, g is gravity, and r is radius. For water, θ ≈ 0°.", "solution": "h = 2T cosθ/(ρgr). T = hρgr/(2 cosθ) = (0.02)(1000)(9.8)(0.5×10⁻³)/(2×1) = 0.02×1000×9.8×0.5×10⁻³/2 = 0.049 N/m", "tips": ["<li>Use h = 2T cosθ/(ρgr)</li>", "<li>Solve for surface tension</li>", "<li>Check units (N/m)</li>", "<li>Convert mm to m</li>", "<li>Use cos0° = 1</li>"], "formulas": "h = 2T cosθ/(ρgr)"},
            {"title": "Bernoulli's Principle", "question": "Water flows through a pipe with velocity 2 m/s at point A and 4 m/s at point B. If pressure at A is 2×10⁵ Pa, find pressure at B. (ρ = 1000 kg/m³)", "background": "Bernoulli's principle states that total energy (pressure + kinetic + potential) is constant along streamline. P + ½ρv² + ρgh = constant. For horizontal flow, P + ½ρv² = constant. Higher velocity means lower pressure.", "solution": "P_A + ½ρv_A² = P_B + ½ρv_B². 2×10⁵ + ½(1000)(2)² = P_B + ½(1000)(4)². 2×10⁵ + 2000 = P_B + 8000. P_B = 2×10⁵ + 2000 - 8000 = 1.94×10⁵ Pa", "tips": ["<li>Use P + ½ρv² = constant</li>", "<li>Apply to both points</li>", "<li>Solve for unknown pressure</li>", "<li>Check units (Pa)</li>", "<li>Verify pressure decreases</li>"], "formulas": "P + ½ρv² + ρgh = constant"},
            {"title": "Poiseuille's Law", "question": "Blood flows through an artery of radius 2 mm at rate 1 cm³/s. Find pressure drop per cm. (η = 4×10⁻³ Pa⋅s)", "background": "Poiseuille's law describes flow through cylindrical tubes. Flow rate Q = πr⁴ΔP/(8ηL) where r is radius, ΔP is pressure difference, η is viscosity, and L is length. This applies to laminar flow in circular tubes.", "solution": "Q = πr⁴ΔP/(8ηL). ΔP/L = 8ηQ/(πr⁴) = 8×4×10⁻³×10⁻⁶/(π×(2×10⁻³)⁴) = 32×10⁻⁹/(π×16×10⁻¹²) = 32×10⁻⁹/(50.3×10⁻¹²) = 636 Pa/m = 6.36 Pa/cm", "tips": ["<li>Use Q = πr⁴ΔP/(8ηL)</li>", "<li>Solve for pressure gradient</li>", "<li>Check units (Pa/m)</li>", "<li>Convert units carefully</li>", "<li>Verify with flow resistance</li>"], "formulas": "Q = πr⁴ΔP/(8ηL)"},
            {"title": "Thermal Expansion", "question": "A steel rod of length 1 m at 20°C is heated to 120°C. Find increase in length. (α = 12×10⁻⁶/°C)", "background": "Thermal expansion occurs when temperature increases. Linear expansion: ΔL = αL₀ΔT where α is coefficient of linear expansion, L₀ is original length, and ΔT is temperature change. Different materials have different expansion coefficients.", "solution": "ΔL = αL₀ΔT = 12×10⁻⁶×1×(120-20) = 12×10⁻⁶×1×100 = 12×10⁻⁴ = 1.2×10⁻³ m = 1.2 mm", "tips": ["<li>Use ΔL = αL₀ΔT</li>", "<li>Calculate temperature change</li>", "<li>Check units (m)</li>", "<li>Convert to mm</li>", "<li>Verify with known values</li>"], "formulas": "ΔL = αL₀ΔT"},
            {"title": "Heat Transfer", "question": "A 2 kg iron block at 100°C is dropped into 5 kg water at 20°C. Find final temperature. (c_iron = 450 J/kg⋅K, c_water = 4200 J/kg⋅K)", "background": "Heat transfer occurs until thermal equilibrium. Heat lost by hot object = Heat gained by cold object. Q = mcΔT where m is mass, c is specific heat, and ΔT is temperature change. Conservation of energy applies.", "solution": "Heat lost by iron = Heat gained by water. m₁c₁(T₁ - T_f) = m₂c₂(T_f - T₂). 2×450×(100 - T_f) = 5×4200×(T_f - 20). 900×(100 - T_f) = 21000×(T_f - 20). 90000 - 900T_f = 21000T_f - 420000. 510000 = 21900T_f. T_f = 23.3°C", "tips": ["<li>Apply heat conservation</li>", "<li>Use Q = mcΔT</li>", "<li>Set heat lost = heat gained</li>", "<li>Solve for final temperature</li>", "<li>Check units (°C)</li>"], "formulas": "Q = mcΔT, Heat lost = Heat gained"}
        ]
    },
    8: {
        "title": "Thermodynamics",
        "problems": [
            {"title": "First Law of Thermodynamics", "question": "A gas absorbs 500 J of heat and does 200 J of work. Find change in internal energy.", "background": "First law of thermodynamics: ΔU = Q - W where ΔU is change in internal energy, Q is heat added to system, and W is work done by system. Heat added is positive, work done by system is positive. Internal energy is a state function.", "solution": "ΔU = Q - W = 500 - 200 = 300 J", "tips": ["<li>Use ΔU = Q - W</li>", "<li>Check signs carefully</li>", "<li>Heat added is positive</li>", "<li>Work done by system is positive</li>", "<li>Check units (J)</li>"], "formulas": "ΔU = Q - W"},
            {"title": "Ideal Gas Law", "question": "2 moles of gas at 300 K occupy volume 0.05 m³. Find pressure. (R = 8.31 J/mol⋅K)", "background": "Ideal gas law: PV = nRT where P is pressure, V is volume, n is number of moles, R is gas constant, and T is absolute temperature. This applies to ideal gases at low pressure and high temperature. All gases approach ideal behavior at low density.", "solution": "PV = nRT. P = nRT/V = 2×8.31×300/0.05 = 4986/0.05 = 99720 Pa = 99.72 kPa", "tips": ["<li>Use PV = nRT</li>", "<li>Solve for pressure</li>", "<li>Check units (Pa)</li>", "<li>Convert to kPa</li>", "<li>Verify with R = 8.31 J/mol⋅K</li>"], "formulas": "PV = nRT"},
            {"title": "Isothermal Process", "question": "A gas expands isothermally from 2 L to 4 L at 300 K. Find work done. (n = 1 mol)", "background": "Isothermal process occurs at constant temperature. For ideal gas, PV = constant. Work done W = nRT ln(V_f/V_i). Since temperature is constant, internal energy change is zero, so Q = W. The process is reversible.", "solution": "W = nRT ln(V_f/V_i) = 1×8.31×300×ln(4/2) = 2493×ln(2) = 2493×0.693 = 1727 J", "tips": ["<li>Use W = nRT ln(V_f/V_i)</li>", "<li>Calculate volume ratio</li>", "<li>Use ln(2) = 0.693</li>", "<li>Check units (J)</li>", "<li>Verify with Q = W</li>"], "formulas": "W = nRT ln(V_f/V_i)"},
            {"title": "Adiabatic Process", "question": "A gas expands adiabatically from 1 L to 2 L. If initial pressure is 2×10⁵ Pa, find final pressure. (γ = 1.4)", "background": "Adiabatic process occurs without heat transfer (Q = 0). For ideal gas, PV^γ = constant where γ = C_p/C_v. Since Q = 0, ΔU = -W. The process is reversible and temperature changes.", "solution": "PV^γ = constant. P₁V₁^γ = P₂V₂^γ. P₂ = P₁(V₁/V₂)^γ = 2×10⁵×(1/2)^1.4 = 2×10⁵×(0.5)^1.4 = 2×10⁵×0.378 = 7.56×10⁴ Pa", "tips": ["<li>Use PV^γ = constant</li>", "<li>Calculate volume ratio</li>", "<li>Apply power law</li>", "<li>Check units (Pa)</li>", "<li>Verify pressure decreases</li>"], "formulas": "PV^γ = constant"},
            {"title": "Heat Engine", "question": "A heat engine operates between 500 K and 300 K. If it absorbs 1000 J of heat, find maximum work done and efficiency.", "background": "Heat engine converts heat to work. Maximum efficiency η = 1 - T_c/T_h where T_c is cold reservoir temperature and T_h is hot reservoir temperature. Maximum work W = ηQ_h where Q_h is heat absorbed from hot reservoir.", "solution": "η = 1 - T_c/T_h = 1 - 300/500 = 1 - 0.6 = 0.4 = 40%. W = ηQ_h = 0.4×1000 = 400 J", "tips": ["<li>Use η = 1 - T_c/T_h</li>", "<li>Calculate efficiency first</li>", "<li>Apply W = ηQ_h</li>", "<li>Check units (J, %)</li>", "<li>Verify with Carnot cycle</li>"], "formulas": "η = 1 - T_c/T_h, W = ηQ_h"},
            {"title": "Refrigerator", "question": "A refrigerator operates between -10°C and 30°C. If it removes 2000 J of heat from cold reservoir, find work input and COP.", "background": "Refrigerator transfers heat from cold to hot reservoir. Coefficient of performance COP = Q_c/W where Q_c is heat removed from cold reservoir and W is work input. COP = T_c/(T_h - T_c) for Carnot refrigerator.", "solution": "T_c = 273 - 10 = 263 K, T_h = 273 + 30 = 303 K. COP = T_c/(T_h - T_c) = 263/(303 - 263) = 263/40 = 6.575. W = Q_c/COP = 2000/6.575 = 304 J", "tips": ["<li>Convert to Kelvin</li>", "<li>Use COP = T_c/(T_h - T_c)</li>", "<li>Apply W = Q_c/COP</li>", "<li>Check units (J)</li>", "<li>Verify COP > 1</li>"], "formulas": "COP = Q_c/W = T_c/(T_h - T_c)"},
            {"title": "Entropy", "question": "1 kg of ice at 0°C melts to water at 0°C. Find entropy change. (L_f = 3.34×10⁵ J/kg)", "background": "Entropy is measure of disorder or randomness. For phase change at constant temperature, ΔS = Q/T where Q is heat added and T is absolute temperature. Entropy always increases in irreversible processes. It's a state function.", "solution": "Q = mL_f = 1×3.34×10⁵ = 3.34×10⁵ J. T = 273 K. ΔS = Q/T = 3.34×10⁵/273 = 1223 J/K", "tips": ["<li>Use ΔS = Q/T</li>", "<li>Calculate heat for phase change</li>", "<li>Use absolute temperature</li>", "<li>Check units (J/K)</li>", "<li>Verify positive entropy change</li>"], "formulas": "ΔS = Q/T"},
            {"title": "Second Law of Thermodynamics", "question": "Explain why heat cannot flow spontaneously from cold to hot object.", "background": "Second law of thermodynamics states that entropy of isolated system never decreases. Heat flows spontaneously from hot to cold because this increases total entropy. Reverse process would decrease entropy, violating second law. This defines direction of time.", "solution": "Heat cannot flow spontaneously from cold to hot because this would decrease total entropy of the system, violating the second law of thermodynamics. The second law requires that entropy always increases or stays constant in isolated systems, defining the natural direction of processes.", "tips": ["<li>Consider entropy change</li>", "<li>Apply second law</li>", "<li>Think about total system</li>", "<li>Consider direction of time</li>", "<li>Explain spontaneous processes</li>"], "formulas": "ΔS_total ≥ 0"},
            {"title": "Carnot Cycle", "question": "A Carnot engine operates between 400 K and 300 K. Find efficiency and work done per cycle if heat absorbed is 800 J.", "background": "Carnot cycle is most efficient heat engine. It consists of two isothermal and two adiabatic processes. Efficiency η = 1 - T_c/T_h. Work done W = ηQ_h. Carnot efficiency is maximum possible for given temperature difference.", "solution": "η = 1 - T_c/T_h = 1 - 300/400 = 1 - 0.75 = 0.25 = 25%. W = ηQ_h = 0.25×800 = 200 J", "tips": ["<li>Use η = 1 - T_c/T_h</li>", "<li>Calculate efficiency</li>", "<li>Apply W = ηQ_h</li>", "<li>Check units (J, %)</li>", "<li>Verify with Carnot theorem</li>"], "formulas": "η = 1 - T_c/T_h, W = ηQ_h"},
            {"title": "Heat Capacity", "question": "A 2 kg copper block is heated from 20°C to 80°C. Find heat required. (c_copper = 385 J/kg⋅K)", "background": "Heat capacity is amount of heat required to raise temperature by 1 K. Specific heat capacity c is heat capacity per unit mass. Q = mcΔT where m is mass, c is specific heat, and ΔT is temperature change. Different materials have different specific heats.", "solution": "Q = mcΔT = 2×385×(80-20) = 2×385×60 = 46200 J = 46.2 kJ", "tips": ["<li>Use Q = mcΔT</li>", "<li>Calculate temperature change</li>", "<li>Check units (J)</li>", "<li>Convert to kJ</li>", "<li>Verify with specific heat</li>"], "formulas": "Q = mcΔT"}
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
    """Generate final physics chapters."""
    for chapter_num, data in chapters_data.items():
        print(f"Generating Chapter {chapter_num}: {data['title']}")
        generate_chapter(chapter_num, data)
    
    print("All final chapters generated successfully!")

if __name__ == "__main__":
    main()
