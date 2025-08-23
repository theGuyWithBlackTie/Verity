import pymupdf as PdfReader

class PDFExtractor:
    def extract_text_all(self, file_path):
        """Extract text from the entire PDF file."""
        reader = PdfReader.open(file_path)
        text = ""
        for page in reader:
            text += page.get_text()
        return text
    
    def extract_text_page(self, file_path, page_number):
        """Extract text from a specific page in the PDF file."""
        reader = PdfReader.open(file_path)
        if page_number < 1 or page_number > reader.page_count:
            raise ValueError("Page number out of range.")
        page = reader[page_number - 1]
        return page.get_text()