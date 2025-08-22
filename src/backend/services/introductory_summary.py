from ..extractors.pdf_extractor import PDFExtractor
from ..extractors.docx_extractor import DocxExtractor
from ..extractors.txt_extractor import TxtExtractor

class IntroductorySummaryService:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.extractors = {
            ".pdf": PDFExtractor(),
            ".docx": DocxExtractor(),
            ".txt": TxtExtractor()
        }

    def generate_summary(self, file_paths: list[str]) -> str:
        
        summaries = []
        for file_path in file_paths:
            ext = file_path.lower().rsplit('.', 1)[-1]
            extractor = self.extractors.get(f".{ext}")
            if not extractor:
                raise ValueError(f"Unsupported file type: {ext}")

            text = extractor.extract_text_all(file_path)
            prompt = f"Summarize the following document:\n\n{text}\n\nSummary:"
            summary = self.llm_client.generate_text(prompt)
            summaries.append(summary)

        combined_summary = "\n\n".join(summaries)
        final_prompt = f"Combine the following summaries into a concise introductory summary:\n\n{combined_summary}\n\nIntroductory Summary:"
        final_summary = self.llm_client.generate_text(final_prompt)
        return final_summary