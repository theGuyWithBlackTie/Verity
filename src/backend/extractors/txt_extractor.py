class TxtExtractor:
    def extract_text_all(self, file_path):
        """Extract text from a TXT file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    def extract_text_page(self, file_path, page_number):
        """Simulate page-wise extraction for TXT files (if applicable)."""
        raise NotImplementedError("Page-wise extraction is not supported for TXT files.")