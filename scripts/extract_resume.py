from docx import Document
import re

def extract_resume_content():
    # Read the Word document
    doc = Document('resume.docx')
    
    # Extract all paragraphs
    content = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            content.append(f"<p>{paragraph.text}</p>")
    
    # Join all content
    resume_html = '\n'.join(content)
    
    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Replace the placeholder with actual resume content
    updated_html = html_content.replace('{{RESUME_CONTENT}}', resume_html)
    
    # Write back to index.html
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(updated_html)
    
    print("Resume content extracted and inserted into index.html")

if __name__ == "__main__":
    extract_resume_content()
