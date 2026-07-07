from docx import Document

def extract_resume_text():
    # Read the Word document
    doc = Document('resume.docx')
    
    # Extract all text, preserving paragraph breaks
    text_content = []
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:  # Only add non-empty paragraphs
            text_content.append(text)
    
    # Join with double line breaks to preserve paragraph separation
    return '\n\n'.join(text_content)

def update_html():
    # Read the current HTML file
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Extract plain text from resume
    resume_text = extract_resume_text()
    
    # Replace the placeholder with plain text
    updated_html = html_content.replace('{{RESUME_CONTENT}}', resume_text)
    
    # Write back to the file
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(updated_html)
    
    print("Resume text extracted and inserted successfully!")

if __name__ == "__main__":
    update_html()
