from docx import Document

class DocxExtractor:
    def extract_text_all(self, file_path):
        """Extract text from the entire DOCX file."""
        doc = Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])

    def extract_text_page(self, file_path, page_number):
        """Simulate page-wise extraction for DOCX (if applicable)."""
        raise NotImplementedError("Page-wise extraction is not supported for DOCX files.")