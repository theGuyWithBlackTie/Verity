import tiktoken
import os
import json

from ..extractors.pdf_extractor import PDFExtractor
from ..extractors.docx_extractor import DocxExtractor
from ..extractors.txt_extractor import TxtExtractor

from ..llm_clients.base_client import BaseLLMClient

from .prompt_templates import INTRODUCTORY_SUMMARY

class IntroductorySummaryService:
    def __init__(self, llm_client:BaseLLMClient):
        self.llm_client = llm_client
        self.extractors = {
            ".pdf": PDFExtractor(),
            ".docx": DocxExtractor(),
            ".txt": TxtExtractor()
        }
        self.encoding = tiktoken.encoding_for_model(self.llm_client.model_name)

    def generate_summary(self, file_paths: list[str]) -> str:
        summaries = {}
        for file_path in file_paths:
            ext = file_path.lower().rsplit('.', 1)[-1]
            extractor = self.extractors.get(f".{ext}")
            if not extractor:
                raise ValueError(f"Unsupported file type: {ext}")

            text = extractor.extract_text_all(file_path)
            file_name = os.path.basename(file_path)
            summaries[file_name] = self._generate_paginated_summary(file_name, text)

        return summaries
    
    def _generate_paginated_summary(self, file_name:str, text:str):
        tokens = self.encoding.encode(text)

        is_summary_enough = False
        previous_summary = ""
        tokens_counter = 0

        while is_summary_enough == False:
            page_content = self.encoding.decode(tokens[tokens_counter: tokens_counter+1000])
            metadata = {"file_name": file_name}
            
            print(f"Generating summary for {file_name}, tokens {tokens_counter} to {tokens_counter+1000}")
            prompt = INTRODUCTORY_SUMMARY.format(
                metadata=json.dumps(metadata),
                previous_summary=previous_summary,
                page_content=page_content
            )
            response = self.llm_client.generate_text(prompt)
            previous_summary = response["summary"]
            is_summary_enough = True if str(response["is_summary_introductory_enough"]).lower() == "true" else False
            tokens_counter += 1000
            if tokens_counter >= len(tokens):
                break
        return previous_summary