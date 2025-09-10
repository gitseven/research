#!/usr/bin/env python3
"""
Extract questions from all PDFs in the Maths folder and generate an index.
"""

import os
import re
import sys
from pathlib import Path
import PyPDF2
import fitz  # PyMuPDF

def extract_text_pypdf2(pdf_path):
    """Extract text using PyPDF2."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"PyPDF2 failed for {pdf_path}: {e}")
        return None

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

def extract_questions_from_text(text, pdf_name):
    """Extract questions from text content."""
    if not text:
        return []
    
    questions = []
    
    # Common question patterns
    patterns = [
        # Exercise questions: "1. Question text..." or "Q1. Question text..."
        r'(?:^|\n)\s*(?:Exercise\s+)?(\d+[\.\)]\s+[^?\n]+\?)',
        r'(?:^|\n)\s*Q(\d+)[\.\)]\s+([^?\n]+\?)',
        r'(?:^|\n)\s*(\d+[\.\)]\s+[^?\n]+\?)',
        
        # Problem patterns: "Problem 1.1: Question text..."
        r'(?:^|\n)\s*Problem\s+(\d+\.\d+)[:\s]+([^?\n]+\?)',
        
        # Example patterns: "Example 1: Question text..."
        r'(?:^|\n)\s*Example\s+(\d+)[:\s]+([^?\n]+\?)',
        
        # Direct question patterns
        r'(?:^|\n)\s*([A-Z][^?\n]+\?)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.MULTILINE | re.IGNORECASE)
        for match in matches:
            question_text = match.group(0).strip()
            if len(question_text) > 10:  # Filter out very short matches
                questions.append({
                    'text': question_text,
                    'source': pdf_name,
                    'pattern': pattern
                })
    
    return questions

def process_pdf(pdf_path):
    """Process a single PDF file."""
    pdf_name = os.path.basename(pdf_path)
    print(f"Processing {pdf_name}...")
    
    # Try PyMuPDF first (usually better)
    text = extract_text_pymupdf(pdf_path)
    if not text or len(text.strip()) < 100:
        # Fallback to PyPDF2
        text = extract_text_pypdf2(pdf_path)
    
    if not text:
        print(f"Could not extract text from {pdf_name}")
        return []
    
    questions = extract_questions_from_text(text, pdf_name)
    print(f"Found {len(questions)} questions in {pdf_name}")
    return questions

def main():
    """Main function to process all PDFs."""
    maths_dir = Path("D:/repository/research/Maths")
    output_file = Path("D:/repository/research/maths_questions_extracted.txt")
    
    all_questions = []
    
    # Find all PDF files
    pdf_files = list(maths_dir.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_path in pdf_files:
        questions = process_pdf(pdf_path)
        all_questions.extend(questions)
    
    # Write results
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("MATHS QUESTIONS EXTRACTED FROM PDF FILES\n")
        f.write("=" * 50 + "\n\n")
        
        # Group by source file
        by_source = {}
        for q in all_questions:
            source = q['source']
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(q)
        
        for source, questions in sorted(by_source.items()):
            f.write(f"SOURCE: {source}\n")
            f.write("-" * 30 + "\n")
            
            for i, q in enumerate(questions, 1):
                f.write(f"Question {i}:\n")
                f.write(f"{q['text']}\n\n")
            
            f.write("\n" + "=" * 50 + "\n\n")
        
        f.write(f"TOTAL QUESTIONS EXTRACTED: {len(all_questions)} questions from {len(pdf_files)} files\n")
    
    print(f"Extraction complete! Found {len(all_questions)} questions total.")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
