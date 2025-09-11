#!/usr/bin/env python3
"""
Extract questions and solutions from Physics PDFs and generate detailed HTML pages.
"""

import os
import re
import sys
from pathlib import Path
import fitz  # PyMuPDF
import json

def extract_text_pymupdf(pdf_path):
    """Extract text using PyMuPDF (fitz)."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text() + "\n"
        doc.close()
        return text
    except Exception as e:
        print(f"PyMuPDF failed for {pdf_path}: {e}")
        return None

def extract_questions_and_solutions(text, pdf_name):
    """Extract questions and solutions from text content."""
    if not text:
        return []
    
    problems = []
    
    # Enhanced patterns for physics questions and solutions
    patterns = [
        # Exercise questions with solutions
        r'(?:^|\n)\s*(\d+[\.\)]\s+[^?\n]+\?)\s*(.*?)(?=\n\s*\d+[\.\)]|\n\s*$|\Z)',
        r'(?:^|\n)\s*Problem\s+(\d+\.\d+)[:\s]+([^?\n]+\?)\s*(.*?)(?=\n\s*Problem|\n\s*$|\Z)',
        r'(?:^|\n)\s*Example\s+(\d+)[:\s]+([^?\n]+\?)\s*(.*?)(?=\n\s*Example|\n\s*$|\Z)',
        r'(?:^|\n)\s*Q(\d+)[\.\)]\s+([^?\n]+\?)\s*(.*?)(?=\n\s*Q\d+|\n\s*$|\Z)',
        r'(?:^|\n)\s*(\d+[\.\)]\s+[^?\n]+(?:calculate|find|determine|show|prove|derive)[^?\n]*\?)\s*(.*?)(?=\n\s*\d+[\.\)]|\n\s*$|\Z)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE | re.DOTALL)
        for match in matches:
            if len(match.groups()) >= 2:
                question_text = match.group(1).strip() if match.group(1) else match.group(2).strip()
                solution_text = match.group(2).strip() if len(match.groups()) >= 2 and match.group(2) else ""
                if len(match.groups()) >= 3:
                    solution_text = match.group(3).strip()
                
                if len(question_text) > 10:  # Filter out very short matches
                    problems.append({
                        'question': question_text,
                        'solution': solution_text,
                        'source': pdf_name,
                        'pattern': pattern
                    })
    
    return problems

def get_chapter_info(pdf_name):
    """Get chapter information based on PDF name."""
    chapter_map = {
        'leph101': {'title': 'Physical World and Measurement', 'chapter': 1, 'topics': ['measurement', 'units', 'dimensions', 'significant figures', 'errors', 'uncertainty']},
        'leph102': {'title': 'Kinematics', 'chapter': 2, 'topics': ['motion', 'velocity', 'acceleration', 'displacement', 'projectile motion', 'relative motion']},
        'leph103': {'title': 'Laws of Motion', 'chapter': 3, 'topics': ['newton laws', 'force', 'momentum', 'friction', 'tension', 'normal force']},
        'leph104': {'title': 'Work, Energy and Power', 'chapter': 4, 'topics': ['work', 'energy', 'power', 'kinetic energy', 'potential energy', 'conservation']},
        'leph105': {'title': 'Motion of System of Particles and Rigid Body', 'chapter': 5, 'topics': ['center of mass', 'momentum', 'angular momentum', 'torque', 'rotation', 'rolling motion']},
        'leph106': {'title': 'Gravitation', 'chapter': 6, 'topics': ['gravitation', 'kepler laws', 'orbital motion', 'escape velocity', 'satellites', 'weightlessness']},
        'leph107': {'title': 'Properties of Bulk Matter', 'chapter': 7, 'topics': ['elasticity', 'viscosity', 'surface tension', 'fluid mechanics', 'bernoulli principle', 'archimedes principle']},
        'leph108': {'title': 'Thermodynamics', 'chapter': 8, 'topics': ['heat', 'temperature', 'thermal expansion', 'heat transfer', 'laws of thermodynamics', 'entropy']},
        'leph1ps': {'title': 'Problem Solving', 'chapter': 'PS', 'topics': ['problem solving strategies', 'mathematical reasoning', 'physics concepts']},
        'leph1an': {'title': 'Answers', 'chapter': 'AN', 'topics': ['answers', 'solutions', 'verification']}
    }
    
    base_name = pdf_name.replace('.pdf', '')
    return chapter_map.get(base_name, {'title': 'Physics', 'chapter': 'Unknown', 'topics': ['physics']})

def generate_background_concept(chapter_info, problem_text):
    """Generate detailed background concept explanation (200-500 words)."""
    topics = chapter_info['topics']
    title = chapter_info['title']
    chapter = chapter_info['chapter']
    
    # Define detailed explanations for each physics topic
    topic_explanations = {
        'measurement': """
        <strong>Measurement and Units:</strong> Physics is fundamentally about measuring physical quantities. The International System of Units (SI) provides seven base units: meter (m) for length, kilogram (kg) for mass, second (s) for time, ampere (A) for electric current, kelvin (K) for temperature, mole (mol) for amount of substance, and candela (cd) for luminous intensity. All other units are derived from these base units. For example, velocity is measured in m/s, acceleration in m/s², and force in kg⋅m/s² = newton (N). <br><br>
        <strong>Dimensional Analysis:</strong> Every physical quantity has dimensions expressed in terms of fundamental quantities [M], [L], [T] for mass, length, and time respectively. Dimensional analysis helps verify equations and derive relationships between physical quantities. The principle of homogeneity states that both sides of an equation must have the same dimensions.
        """,
        'kinematics': """
        <strong>Kinematics:</strong> The branch of mechanics that describes motion without considering its causes. Key concepts include displacement (Δx = x_f - x_i), velocity (v = dx/dt), and acceleration (a = dv/dt). For constant acceleration, we use the kinematic equations: v = v₀ + at, x = x₀ + v₀t + ½at², v² = v₀² + 2a(x-x₀), and x = x₀ + ½(v₀ + v)t. <br><br>
        <strong>Projectile Motion:</strong> Two-dimensional motion under gravity where horizontal and vertical components are independent. Horizontal velocity remains constant (v_x = v₀cosθ), while vertical velocity changes due to gravity (v_y = v₀sinθ - gt). The trajectory is parabolic, and the range R = (v₀²sin2θ)/g.
        """,
        'laws of motion': """
        <strong>Newton's Laws of Motion:</strong> (1) First Law (Law of Inertia): An object at rest stays at rest, and an object in motion stays in motion with constant velocity, unless acted upon by a net external force. (2) Second Law: F = ma, where F is net force, m is mass, and a is acceleration. (3) Third Law: For every action, there is an equal and opposite reaction. <br><br>
        <strong>Force and Momentum:</strong> Force is a vector quantity that causes acceleration. Momentum (p = mv) is conserved in isolated systems. Impulse (J = FΔt = Δp) relates force to momentum change. Friction opposes motion and is proportional to normal force: f = μN, where μ is the coefficient of friction.
        """,
        'work energy power': """
        <strong>Work, Energy, and Power:</strong> Work (W = F⋅d = Fdcosθ) is done when a force causes displacement. Energy is the capacity to do work. Kinetic energy (KE = ½mv²) depends on mass and velocity. Potential energy (PE = mgh for gravitational, PE = ½kx² for spring) depends on position. The work-energy theorem states W = ΔKE. <br><br>
        <strong>Conservation of Energy:</strong> In isolated systems, total energy (KE + PE + other forms) remains constant. Power (P = W/t = F⋅v) is the rate of doing work, measured in watts (W = J/s). Efficiency = (useful output energy)/(total input energy) × 100%.
        """,
        'motion of system': """
        <strong>Center of Mass:</strong> The point where the entire mass of a system can be considered concentrated. For discrete particles: x_cm = (Σm_i x_i)/(Σm_i). For continuous bodies, integration is used. The center of mass moves as if all external forces act on it. <br><br>
        <strong>Angular Motion:</strong> Angular displacement (θ), angular velocity (ω = dθ/dt), and angular acceleration (α = dω/dt). For constant angular acceleration: ω = ω₀ + αt, θ = θ₀ + ω₀t + ½αt². Torque (τ = r × F = rFsinθ) causes angular acceleration: τ = Iα, where I is moment of inertia.
        """,
        'gravitation': """
        <strong>Newton's Law of Gravitation:</strong> F = G(m₁m₂)/r², where G = 6.67 × 10⁻¹¹ N⋅m²/kg² is the gravitational constant. This describes the attractive force between any two masses. <br><br>
        <strong>Kepler's Laws:</strong> (1) Planets move in elliptical orbits with the Sun at one focus. (2) A line joining a planet and the Sun sweeps equal areas in equal times. (3) The square of the orbital period is proportional to the cube of the semi-major axis: T² ∝ a³. <br><br>
        <strong>Orbital Mechanics:</strong> Escape velocity v_esc = √(2GM/R) allows an object to escape gravitational field. Orbital velocity v_orb = √(GM/r) for circular orbits. Satellites in geostationary orbit have T = 24 hours at altitude h ≈ 35,786 km.
        """,
        'properties of bulk matter': """
        <strong>Elasticity:</strong> Stress (σ = F/A) is force per unit area. Strain (ε = ΔL/L) is relative deformation. Young's modulus (Y = σ/ε) measures stiffness. Hooke's law: F = -kx for springs, where k is spring constant. <br><br>
        <strong>Fluid Mechanics:</strong> Pressure (P = F/A) in fluids increases with depth: P = P₀ + ρgh. Pascal's principle: pressure applied to confined fluid is transmitted undiminished. Archimedes' principle: buoyant force equals weight of displaced fluid. Bernoulli's equation: P + ½ρv² + ρgh = constant for steady, incompressible flow.
        """,
        'thermodynamics': """
        <strong>Heat and Temperature:</strong> Temperature measures average kinetic energy of particles. Heat (Q) is energy transfer due to temperature difference. Specific heat capacity (c = Q/mΔT) is energy needed to raise 1 kg by 1 K. Latent heat (L = Q/m) is energy for phase changes. <br><br>
        <strong>Laws of Thermodynamics:</strong> (1) Zeroth Law: If A = B and B = C, then A = C (temperature equilibrium). (1) First Law: ΔU = Q - W (conservation of energy). (2) Second Law: Entropy of isolated systems never decreases. (3) Third Law: Entropy approaches zero as temperature approaches absolute zero.
        """
    }
    
    # Find relevant topics in the problem
    relevant_topics = []
    problem_lower = problem_text.lower()
    for topic in topics:
        if any(keyword in problem_lower for keyword in topic.split()):
            relevant_topics.append(topic)
    
    if not relevant_topics:
        relevant_topics = topics[:2]  # Default to first two topics
    
    background = f"""
    <h2>Background Concept — {title}</h2>
    <p>This problem involves fundamental concepts from Chapter {chapter}: {title}. Understanding these concepts is crucial for solving physics problems systematically.</p>
    """
    
    for topic in relevant_topics[:2]:  # Limit to 2 topics for detailed explanation
        if topic in topic_explanations:
            background += f"<div class='concept-section'><h3>{topic.title()}</h3><p>{topic_explanations[topic]}</p></div>"
    
    return background

def generate_visualization(chapter_info, problem_text):
    """Generate SVG visualizations for physics concepts."""
    chapter = chapter_info['chapter']
    title = chapter_info['title']
    
    visualizations = {
        1: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6" />
                </marker>
            </defs>
            <rect x="50" y="50" width="300" height="100" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/>
            <text x="200" y="80" text-anchor="middle" font-size="14" fill="#374151">Measurement and Units</text>
            <text x="200" y="100" text-anchor="middle" font-size="12" fill="#6b7280">Length (m), Mass (kg), Time (s)</text>
            <text x="200" y="120" text-anchor="middle" font-size="12" fill="#6b7280">Dimensional Analysis: [M]ᵃ[L]ᵇ[T]ᶜ</text>
            <line x1="100" y1="140" x2="300" y2="140" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
            <text x="200" y="160" text-anchor="middle" font-size="12" fill="#3b82f6">Physical Quantities</text>
        </svg>""",
        
        2: """<svg viewBox="0 0 400 250" class="physics-diagram">
            <defs>
                <marker id="arrowhead2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#ef4444" />
                </marker>
            </defs>
            <line x1="50" y1="200" x2="350" y2="200" stroke="#374151" stroke-width="2"/>
            <circle cx="100" cy="200" r="8" fill="#ef4444"/>
            <path d="M 100 200 Q 200 100 300 200" stroke="#ef4444" stroke-width="3" fill="none"/>
            <text x="100" y="190" text-anchor="middle" font-size="12" fill="#ef4444">v₀</text>
            <text x="200" y="90" text-anchor="middle" font-size="12" fill="#ef4444">Projectile Path</text>
            <text x="300" y="190" text-anchor="middle" font-size="12" fill="#ef4444">Range</text>
            <line x1="100" y1="200" x2="120" y2="180" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowhead2)"/>
            <text x="130" y="175" font-size="10" fill="#ef4444">θ</text>
        </svg>""",
        
        3: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <rect x="50" y="50" width="80" height="60" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
            <text x="90" y="85" text-anchor="middle" font-size="12" fill="#92400e">Mass m</text>
            <line x1="130" y1="80" x2="200" y2="80" stroke="#3b82f6" stroke-width="3" marker-end="url(#arrowhead)"/>
            <text x="165" y="75" font-size="12" fill="#3b82f6">F = ma</text>
            <text x="200" y="100" font-size="14" fill="#374151">Newton's Second Law</text>
            <text x="200" y="120" font-size="12" fill="#6b7280">Force causes acceleration</text>
        </svg>""",
        
        4: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <circle cx="100" cy="100" r="30" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <text x="100" y="105" text-anchor="middle" font-size="12" fill="white">KE</text>
            <circle cx="300" cy="100" r="30" fill="#8b5cf6" stroke="#7c3aed" stroke-width="2"/>
            <text x="300" y="105" text-anchor="middle" font-size="12" fill="white">PE</text>
            <line x1="130" y1="100" x2="270" y2="100" stroke="#374151" stroke-width="2" marker-end="url(#arrowhead)"/>
            <text x="200" y="90" font-size="12" fill="#374151">Energy Conservation</text>
            <text x="200" y="140" font-size="12" fill="#6b7280">KE + PE = Constant</text>
        </svg>""",
        
        5: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <circle cx="200" cy="100" r="40" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/>
            <circle cx="200" cy="100" r="3" fill="#ef4444"/>
            <text x="200" y="95" text-anchor="middle" font-size="10" fill="#ef4444">CM</text>
            <line x1="200" y1="100" x2="250" y2="100" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
            <text x="225" y="90" font-size="10" fill="#3b82f6">ω</text>
            <text x="200" y="160" text-anchor="middle" font-size="12" fill="#374151">Rotational Motion</text>
            <text x="200" y="175" text-anchor="middle" font-size="10" fill="#6b7280">τ = Iα</text>
        </svg>""",
        
        6: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <circle cx="200" cy="100" r="20" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
            <text x="200" y="105" text-anchor="middle" font-size="10" fill="#92400e">M</text>
            <ellipse cx="200" cy="100" rx="80" ry="40" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="5,5"/>
            <text x="200" y="160" text-anchor="middle" font-size="12" fill="#374151">Gravitational Orbit</text>
            <text x="200" y="175" text-anchor="middle" font-size="10" fill="#6b7280">F = GMm/r²</text>
        </svg>""",
        
        7: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <rect x="50" y="80" width="300" height="40" fill="#3b82f6" opacity="0.3"/>
            <line x1="200" y1="60" x2="200" y2="140" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowhead)"/>
            <text x="210" y="100" font-size="10" fill="#ef4444">P = ρgh</text>
            <text x="200" y="160" text-anchor="middle" font-size="12" fill="#374151">Fluid Pressure</text>
            <text x="200" y="175" text-anchor="middle" font-size="10" fill="#6b7280">Pressure increases with depth</text>
        </svg>""",
        
        8: """<svg viewBox="0 0 400 200" class="physics-diagram">
            <rect x="50" y="50" width="100" height="100" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
            <text x="100" y="105" text-anchor="middle" font-size="12" fill="#92400e">Hot</text>
            <rect x="250" y="50" width="100" height="100" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
            <text x="300" y="105" text-anchor="middle" font-size="12" fill="white">Cold</text>
            <line x1="150" y1="100" x2="250" y2="100" stroke="#ef4444" stroke-width="3" marker-end="url(#arrowhead)"/>
            <text x="200" y="90" font-size="12" fill="#ef4444">Heat Flow</text>
            <text x="200" y="170" text-anchor="middle" font-size="12" fill="#374151">Thermodynamics</text>
        </svg>"""
    }
    
    return visualizations.get(int(chapter) if str(chapter).isdigit() else 1, visualizations[1])

def generate_tips_to_solve(chapter_info, problem_text):
    """Generate comprehensive tips for solving similar problems."""
    tips_by_chapter = {
        'Physical World and Measurement': [
            "Always check units and dimensions - they must be consistent throughout",
            "Use significant figures rules: multiplication/division uses least sig figs, addition/subtraction uses least decimal places",
            "Convert all quantities to SI units before calculations",
            "Estimate answers to check if they're reasonable",
            "Use dimensional analysis to verify derived formulas"
        ],
        'Kinematics': [
            "Draw a clear diagram showing initial and final positions",
            "Choose a coordinate system and stick to it consistently",
            "List given quantities and what you need to find",
            "Use the appropriate kinematic equation based on what's given",
            "Check if acceleration is constant before using kinematic equations"
        ],
        'Laws of Motion': [
            "Draw a free-body diagram showing all forces acting on the object",
            "Choose coordinate axes to simplify the problem (usually along motion and perpendicular)",
            "Apply Newton's second law in each direction: ΣF = ma",
            "Identify action-reaction pairs for Newton's third law problems",
            "Check that your answer makes physical sense"
        ],
        'Work, Energy and Power': [
            "Identify the system and decide if energy is conserved",
            "Choose reference points for potential energy calculations",
            "Use work-energy theorem when forces are variable",
            "Remember that work done by conservative forces equals negative change in potential energy",
            "Power problems often involve efficiency calculations"
        ],
        'Motion of System of Particles and Rigid Body': [
            "Locate the center of mass first for system problems",
            "Use conservation of momentum for isolated systems",
            "For rotational problems, identify the axis of rotation",
            "Use parallel axis theorem for moment of inertia calculations",
            "Angular momentum is conserved when net torque is zero"
        ],
        'Gravitation': [
            "Use Newton's law of gravitation: F = GMm/r²",
            "For orbital problems, equate gravitational force to centripetal force",
            "Remember that gravitational potential energy is negative",
            "Use Kepler's laws for planetary motion problems",
            "Escape velocity is independent of mass of the escaping object"
        ],
        'Properties of Bulk Matter': [
            "For elasticity problems, use stress = F/A and strain = ΔL/L",
            "Apply Archimedes' principle for buoyancy problems",
            "Use Bernoulli's equation for fluid flow problems",
            "Remember that pressure in fluids increases with depth",
            "Surface tension problems often involve minimizing surface area"
        ],
        'Thermodynamics': [
            "Use the first law of thermodynamics: ΔU = Q - W",
            "Be careful with signs: Q is positive for heat added, W is positive for work done by system",
            "For ideal gases, use PV = nRT and related equations",
            "Efficiency = (useful output)/(total input) × 100%",
            "Entropy always increases in irreversible processes"
        ]
    }
    
    title = chapter_info['title']
    tips = tips_by_chapter.get(title, [
        "Read the problem carefully and identify what is given and what needs to be found",
        "Draw a clear diagram showing the physical situation",
        "List all relevant formulas and principles",
        "Work step by step and show all calculations clearly",
        "Check your answer for reasonableness and correct units"
    ])
    
    tips_html = "<h2>Tips to Solve</h2><ul>"
    for tip in tips:
        tips_html += f"<li>{tip}</li>"
    tips_html += "</ul>"
    
    return tips_html

def generate_html_page(problem, chapter_info, problem_number):
    """Generate a complete HTML page for a physics problem."""
    title = chapter_info['title']
    chapter = chapter_info['chapter']
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Ch {chapter} Problem {problem_number} — {title}</title>
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
    <h1>Chapter {chapter} · Problem {problem_number}</h1>
    <div class="panel q">
      <h2>Question</h2>
      <p>{problem['question']}</p>
    </div>

    {generate_background_concept(chapter_info, problem['question'])}

    <div class="panel">
      <h2>Visualization</h2>
      {generate_visualization(chapter_info, problem['question'])}
    </div>

    <div class="panel solution">
      <h2>Solution</h2>
      <p>{problem['solution'] if problem['solution'] else 'Solution not found in source material.'}</p>
    </div>

    {generate_tips_to_solve(chapter_info, problem['question'])}

    <div class="panel">
      <h2>Key Formulas</h2>
      <div class="formula">
        {get_key_formulas(chapter_info)}
      </div>
    </div>

    <div class="panel">
      <h2>Source</h2>
      <p class="muted">Extracted from: {problem['source']}</p>
    </div>
  </div>
</body>
</html>"""
    
    return html

def get_key_formulas(chapter_info):
    """Get key formulas for the chapter."""
    formulas = {
        'Physical World and Measurement': 'Dimensional Analysis: [M]ᵃ[L]ᵇ[T]ᶜ',
        'Kinematics': 'v = v₀ + at, x = x₀ + v₀t + ½at², v² = v₀² + 2a(x-x₀)',
        'Laws of Motion': 'F = ma, p = mv, J = FΔt = Δp',
        'Work, Energy and Power': 'W = F⋅d, KE = ½mv², PE = mgh, P = W/t',
        'Motion of System of Particles and Rigid Body': 'x_cm = Σmᵢxᵢ/Σmᵢ, τ = r × F, L = Iω',
        'Gravitation': 'F = GMm/r², v_esc = √(2GM/R), T² ∝ a³',
        'Properties of Bulk Matter': 'σ = F/A, ε = ΔL/L, P = P₀ + ρgh',
        'Thermodynamics': 'ΔU = Q - W, PV = nRT, η = (useful output)/(total input)'
    }
    
    title = chapter_info['title']
    return formulas.get(title, 'Physics formulas for this chapter')

def process_pdf(pdf_path):
    """Process a single PDF file and generate HTML pages."""
    pdf_name = os.path.basename(pdf_path)
    chapter_info = get_chapter_info(pdf_name)
    
    print(f"Processing {pdf_name}...")
    
    text = extract_text_pymupdf(pdf_path)
    if not text:
        print(f"Could not extract text from {pdf_name}")
        return []
    
    problems = extract_questions_and_solutions(text, pdf_name)
    print(f"Found {len(problems)} problems in {pdf_name}")
    
    # Create output directory
    chapter_dir = Path(f"Physics/ch{chapter_info['chapter']}")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate HTML pages
    for i, problem in enumerate(problems, 1):
        html_content = generate_html_page(problem, chapter_info, i)
        output_file = chapter_dir / f"problem-{chapter_info['chapter']}-{i:02d}.html"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    return problems

def main():
    """Main function to process all Physics PDFs."""
    physics_dir = Path("D:/repository/research/Physics")
    
    all_problems = []
    
    # Find all PDF files
    pdf_files = list(physics_dir.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_path in pdf_files:
        problems = process_pdf(pdf_path)
        all_problems.extend(problems)
    
    # Create Physics index
    create_physics_index(all_problems)
    
    print(f"Extraction complete! Generated HTML pages for {len(all_problems)} problems total.")

def create_physics_index(problems):
    """Create an index page for all physics problems."""
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Physics · Questions Index</title>
  <style>
    body { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; margin: 24px; line-height: 1.55; }
    h1 { color: #0ea5e9; margin: 0 0 12px; }
    h2 { color: #7c3aed; margin: 24px 0 12px; }
    .muted { color: #374151; }
    ul { margin: 12px 0 0 20px; }
    a { color: #2563eb; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .source { font-size: 0.9em; color: #6b7280; margin-left: 8px; }
  </style>
</head>
<body>
  <h1>Physics · Questions Index</h1>
  <p class="muted">Browse all extracted questions from Physics PDFs, organized by chapter.</p>
"""
    
    # Group problems by chapter
    by_chapter = {}
    for problem in problems:
        chapter = problem['source'].replace('.pdf', '')
        if chapter not in by_chapter:
            by_chapter[chapter] = []
        by_chapter[chapter].append(problem)
    
    # Add chapters
    chapter_order = ['leph101', 'leph102', 'leph103', 'leph104', 'leph105', 'leph106', 'leph107', 'leph108']
    chapter_names = {
        'leph101': 'Physical World and Measurement',
        'leph102': 'Kinematics', 
        'leph103': 'Laws of Motion',
        'leph104': 'Work, Energy and Power',
        'leph105': 'Motion of System of Particles and Rigid Body',
        'leph106': 'Gravitation',
        'leph107': 'Properties of Bulk Matter',
        'leph108': 'Thermodynamics'
    }
    
    for chapter in chapter_order:
        if chapter in by_chapter:
            chapter_name = chapter_names.get(chapter, chapter)
            chapter_num = chapter.replace('leph', '')
            index_html += f"""
  <h2>Chapter {chapter_num} - {chapter_name}</h2>
  <ul>"""
            
            for i, problem in enumerate(by_chapter[chapter], 1):
                problem_file = f"./ch{chapter_num}/problem-{chapter_num}-{i:02d}.html"
                index_html += f"""
    <li><a href="{problem_file}">Problem {chapter_num}.{i}: {problem['question'][:60]}...</a><span class="source">{chapter}.pdf</span></li>"""
            
            index_html += """
  </ul>"""
    
    index_html += """
  <p class="muted">Total: """ + str(len(problems)) + """ questions extracted from 10 PDF files</p>
</body>
</html>"""
    
    with open("Physics/index.html", 'w', encoding='utf-8') as f:
        f.write(index_html)

if __name__ == "__main__":
    main()
