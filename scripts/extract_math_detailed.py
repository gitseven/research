#!/usr/bin/env python3
"""
Extract questions and solutions from Maths PDFs and generate detailed HTML pages.
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
    
    # Enhanced patterns for questions and solutions
    patterns = [
        # Exercise questions with solutions
        r'(?:^|\n)\s*(\d+[\.\)]\s+[^?\n]+\?)\s*(.*?)(?=\n\s*\d+[\.\)]|\n\s*$|\Z)',
        r'(?:^|\n)\s*Problem\s+(\d+\.\d+)[:\s]+([^?\n]+\?)\s*(.*?)(?=\n\s*Problem|\n\s*$|\Z)',
        r'(?:^|\n)\s*Example\s+(\d+)[:\s]+([^?\n]+\?)\s*(.*?)(?=\n\s*Example|\n\s*$|\Z)',
        r'(?:^|\n)\s*Q(\d+)[\.\)]\s+([^?\n]+\?)\s*(.*?)(?=\n\s*Q\d+|\n\s*$|\Z)',
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
        'lemh101': {'title': 'Relations and Functions', 'chapter': 1, 'topics': ['relations', 'functions', 'domain', 'range', 'inverse functions', 'composition']},
        'lemh102': {'title': 'Inverse Trigonometric Functions', 'chapter': 2, 'topics': ['inverse trig functions', 'arcsin', 'arccos', 'arctan', 'domain restrictions']},
        'lemh103': {'title': 'Matrices', 'chapter': 3, 'topics': ['matrices', 'matrix operations', 'determinants', 'inverse matrices', 'elementary operations']},
        'lemh104': {'title': 'Determinants', 'chapter': 4, 'topics': ['determinants', 'properties', 'cofactors', 'adjoint', 'cramer\'s rule']},
        'lemh105': {'title': 'Complex Numbers', 'chapter': 5, 'topics': ['complex numbers', 'imaginary unit', 'modulus', 'argument', 'polar form', 'de moivre\'s theorem']},
        'lemh106': {'title': 'Linear Inequalities', 'chapter': 6, 'topics': ['linear inequalities', 'graphing', 'systems', 'optimization', 'feasible region']},
        'lemh1a1': {'title': 'Mathematical Induction', 'chapter': 'A1', 'topics': ['mathematical induction', 'base case', 'inductive step', 'proof by induction']},
        'lemh1a2': {'title': 'Mathematical Induction (Advanced)', 'chapter': 'A2', 'topics': ['advanced induction', 'strong induction', 'recursive sequences', 'inductive proofs']},
        'lemh1ps': {'title': 'Problem Solving', 'chapter': 'PS', 'topics': ['problem solving strategies', 'mathematical reasoning', 'proof techniques']},
        'lemh1an': {'title': 'Answers', 'chapter': 'AN', 'topics': ['answers', 'solutions', 'verification']}
    }
    
    base_name = pdf_name.replace('.pdf', '')
    return chapter_map.get(base_name, {'title': 'Mathematics', 'chapter': 'Unknown', 'topics': ['mathematics']})

def generate_background_concept(chapter_info, problem_text):
    """Generate background concept explanation."""
    topics = chapter_info['topics']
    title = chapter_info['title']
    chapter = chapter_info['chapter']
    
    # Define detailed explanations for each topic
    topic_explanations = {
        'relations': """
        A relation R from set A to set B is a subset of A × B. If (a,b) ∈ R, we say 'a is related to b' and write aRb. 
        The domain of R is the set of all first elements, and the range is the set of all second elements. 
        Types include: reflexive (aRa for all a), symmetric (aRb implies bRa), transitive (aRb and bRc implies aRc), and equivalence relations (all three properties).
        """,
        'functions': """
        A function f: A → B is a relation where each element of A has exactly one image in B. 
        Domain (A): set of all possible inputs. Range: set of all outputs. Codomain (B): set containing the range.
        One-one (injective): f(x₁) = f(x₂) implies x₁ = x₂. Onto (surjective): range = codomain. Bijective: both one-one and onto.
        """,
        'matrices': """
        A matrix is a rectangular array of numbers arranged in rows and columns. An m×n matrix has m rows and n columns.
        Elements are denoted as aᵢⱼ where i is row number and j is column number. Types: square (m=n), row matrix (1×n), 
        column matrix (m×1), zero matrix (all elements 0), identity matrix (diagonal elements 1, others 0).
        """,
        'complex numbers': """
        Complex numbers are numbers of the form z = a + ib where a,b ∈ ℝ and i = √(-1). 
        Real part: Re(z) = a, Imaginary part: Im(z) = b. Modulus: |z| = √(a² + b²). 
        Argument: arg(z) = θ where tan θ = b/a. Polar form: z = |z|(cos θ + i sin θ) = |z|e^(iθ).
        """,
        'linear inequalities': """
        Linear inequalities involve expressions like ax + by ≤ c, ax + by ≥ c, ax + by < c, or ax + by > c.
        The solution set is a half-plane. For systems, the solution is the intersection of all half-planes (feasible region).
        Corner points of the feasible region are found by solving the system of equations formed by boundary lines.
        """,
        'mathematical induction': """
        Mathematical induction proves statements for all natural numbers n. Two steps: (1) Base case: verify P(1) is true.
        (2) Inductive step: assume P(k) is true, then prove P(k+1) is true. This establishes P(n) for all n ∈ ℕ.
        Strong induction: assume P(1), P(2), ..., P(k) are all true, then prove P(k+1).
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
    <p>This problem involves concepts from Chapter {chapter}: {title}. The key mathematical concepts include:</p>
    """
    
    for topic in relevant_topics[:3]:  # Limit to 3 topics
        if topic in topic_explanations:
            background += f"<h3>{topic.title()}</h3><p>{topic_explanations[topic].strip()}</p>"
    
    return background

def generate_tips_to_solve(chapter_info, problem_text):
    """Generate tips for solving similar problems."""
    tips_by_chapter = {
        'Relations and Functions': [
            "Always identify the domain and range clearly before solving",
            "For function composition, remember (f∘g)(x) = f(g(x))",
            "Check if a function is one-one by using f(x₁) = f(x₂) → x₁ = x₂",
            "For inverse functions, swap x and y and solve for y",
            "Verify your answer by checking if f(f⁻¹(x)) = x"
        ],
        'Matrices': [
            "Write matrices clearly with proper row and column alignment",
            "For matrix multiplication, ensure the number of columns of first matrix equals rows of second",
            "Use elementary row operations systematically for finding inverse",
            "Check your work by verifying A × A⁻¹ = I",
            "Remember that matrix multiplication is not commutative"
        ],
        'Complex Numbers': [
            "Convert to polar form when dealing with powers: z^n = |z|^n e^(inθ)",
            "Use De Moivre's theorem: (cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)",
            "For roots, remember there are n distinct nth roots of a complex number",
            "Visualize complex numbers on the Argand plane for geometric understanding",
            "Use conjugate properties: z + z̄ = 2Re(z), z - z̄ = 2iIm(z)"
        ],
        'Linear Inequalities': [
            "Graph each inequality as a half-plane first",
            "Test a point (like origin) to determine which side to shade",
            "Find corner points by solving systems of boundary equations",
            "For optimization, evaluate the objective function at all corner points",
            "Check if the feasible region is bounded or unbounded"
        ],
        'Mathematical Induction': [
            "Always start with the base case - verify P(1) or P(0) is true",
            "In the inductive step, clearly state your assumption P(k)",
            "Show how P(k) leads to P(k+1) step by step",
            "End with 'Therefore, by mathematical induction, P(n) is true for all n'",
            "For strong induction, assume P(1) through P(k) are all true"
        ]
    }
    
    title = chapter_info['title']
    tips = tips_by_chapter.get(title, [
        "Read the problem carefully and identify what is given and what needs to be found",
        "Draw diagrams or graphs when helpful for visualization",
        "Work step by step and show all your work clearly",
        "Check your answer by substituting back into the original problem",
        "Practice similar problems to build confidence and speed"
    ])
    
    tips_html = "<h2>Tips to Solve</h2><ul>"
    for tip in tips:
        tips_html += f"<li>{tip}</li>"
    tips_html += "</ul>"
    
    return tips_html

def generate_html_page(problem, chapter_info, problem_number):
    """Generate a complete HTML page for a problem."""
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
    code {{ background:#f8fafc; border:1px solid #e5e7eb; padding:2px 6px; border-radius:6px; }}
    .muted {{ color:#374151; }}
    ul {{ margin:8px 0 8px 20px; }}
    li {{ margin:4px 0; }}
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

    <div class="panel solution">
      <h2>Solution</h2>
      <p>{problem['solution'] if problem['solution'] else 'Solution not found in source material.'}</p>
    </div>

    {generate_tips_to_solve(chapter_info, problem['question'])}

    <div class="panel">
      <h2>Source</h2>
      <p class="muted">Extracted from: {problem['source']}</p>
    </div>
  </div>
</body>
</html>"""
    
    return html

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
    chapter_dir = Path(f"Maths/ch{chapter_info['chapter']}")
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate HTML pages
    for i, problem in enumerate(problems, 1):
        html_content = generate_html_page(problem, chapter_info, i)
        output_file = chapter_dir / f"problem-{chapter_info['chapter']}-{i:02d}.html"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    return problems

def main():
    """Main function to process all PDFs."""
    maths_dir = Path("D:/repository/research/Maths")
    
    all_problems = []
    
    # Find all PDF files
    pdf_files = list(maths_dir.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_path in pdf_files:
        problems = process_pdf(pdf_path)
        all_problems.extend(problems)
    
    print(f"Extraction complete! Generated HTML pages for {len(all_problems)} problems total.")

if __name__ == "__main__":
    main()
