#!/usr/bin/env python3
"""
Generate HTML presentation from markdown slides using Jinja2 template.

Usage:
    python generate.py [slides.md] [output.html]

Features:
- Converts markdown to HTML slides
- Supports audio buttons with [audio:filename.mp3] syntax
- Uses ---- as slide separators
- Generates from template.html
"""

import sys
import os
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import markdown

def parse_slides(markdown_content):
    """Parse markdown content into slides separated by ----"""
    slides = []
    
    # Split on slide separators (4 hyphens)
    slide_blocks = re.split(r'\n----\n', markdown_content.strip())
    
    for i, block in enumerate(slide_blocks):
        if not block.strip():
            continue
            
        # Process left-aligned text FIRST: [left]...[/left] -> left-aligned paragraph
        processed_content = process_left_align(block)
        
        # Process audio buttons: [audio:filename.mp3] -> HTML button
        processed_content = process_audio_buttons(processed_content)
        
        # Convert markdown to HTML
        html_content = markdown.markdown(
            processed_content,
            extensions=['fenced_code', 'tables', 'toc']
        )
        
        slides.append({
            'content': html_content,
            'slide_number': i + 1
        })
    
    return slides

def process_audio_buttons(content):
    """Convert [audio:filename.mp3] syntax to HTML audio buttons"""
    def replace_audio(match):
        filename = match.group(1)
        # Create a button with the filename as display text
        button_text = os.path.splitext(filename)[0].replace('_', ' ').title()
        return f'<button class="audio-button" data-src="assets/{filename}">{button_text}</button>'
    
    # Replace [audio:filename.mp3] with HTML buttons
    content = re.sub(r'\[audio:([^\]]+\.mp3)\]', replace_audio, content)
    return content

def process_left_align(content):
    """Convert [left]...[/left] syntax to left-aligned paragraphs"""
    def replace_left_align(match):
        text = match.group(1).strip()
        # Convert line breaks to <br/> tags for proper formatting
        text = text.replace('\n', '<br/>')
        return f'<div class="left-align">{text}</div>'
    
    # Replace [left]...[/left] with left-aligned divs
    content = re.sub(r'\[left\](.*?)\[/left\]', replace_left_align, content, flags=re.DOTALL)
    return content

def main():
    # Default file paths
    slides_file = 'slides.md'
    output_file = 'index.html'
    template_file = 'template.html'
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        slides_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Check if files exist
    if not os.path.exists(slides_file):
        print(f"Error: {slides_file} not found")
        sys.exit(1)
    
    if not os.path.exists(template_file):
        print(f"Error: {template_file} not found")
        sys.exit(1)
    
    # Read markdown content
    try:
        with open(slides_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        print(f"Error reading {slides_file}: {e}")
        sys.exit(1)
    
    # Parse slides
    slides = parse_slides(markdown_content)
    
    if not slides:
        print("Error: No slides found in markdown file")
        sys.exit(1)
    
    print(f"Found {len(slides)} slides")
    
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)
    
    # Generate HTML
    try:
        html_output = template.render(
            slides=slides,
            title="Music Theory Presentation"
        )
    except Exception as e:
        print(f"Error rendering template: {e}")
        sys.exit(1)
    
    # Write output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Generated {output_file} successfully")
    except Exception as e:
        print(f"Error writing {output_file}: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
