from docx import Document

def extract_resume_content():
    # Read the resume
    doc = Document('resume.docx')
    
    # Extract all text content
    resume_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            resume_text.append(paragraph.text.strip())
    
    # Convert to HTML format (preserve line breaks)
    html_resume_text = '<br>\n'.join(resume_text)
    
    # Update the HTML file
    update_html_with_resume(html_resume_text)
    
    print("Resume content extracted and updated in index.html")

def update_html_with_resume(resume_content):
    with open('index.html', 'r') as f:
        html = f.read()
    
    # Replace the {{RESUME_CONTENT}} placeholder
    new_html = html.replace('{{RESUME_CONTENT}}', resume_content)
    
    with open('index.html', 'w') as f:
        f.write(new_html)

if __name__ == '__main__':
    extract_resume_content()
