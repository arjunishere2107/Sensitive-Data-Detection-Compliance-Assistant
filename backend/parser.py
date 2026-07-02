import fitz  # PyMuPDF
import pandas as pd
import os


class DocumentParser:

    @staticmethod
    def parse_pdf(file_path: str) -> str:
        """Extract text from a PDF file."""
        text = []

        doc = fitz.open(file_path)

        for page in doc:
            page_text = page.get_text()
            if page_text:
                text.append(page_text)

        doc.close()

        return "\n".join(text)

    @staticmethod
    def parse_txt(file_path: str) -> str:
        """Extract text from a TXT file."""
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    @staticmethod
    def parse_csv(file_path: str) -> str:
        """Convert CSV contents into plain text."""
        df = pd.read_csv(file_path)

        rows = []

        for _, row in df.iterrows():
            rows.append(" | ".join(map(str, row.values)))

        return "\n".join(rows)

    @staticmethod
    def parse(file_path: str) -> str:
        """Automatically detect file type and parse."""

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return DocumentParser.parse_pdf(file_path)

        elif extension == ".txt":
            return DocumentParser.parse_txt(file_path)

        elif extension == ".csv":
            return DocumentParser.parse_csv(file_path)

        raise ValueError(f"Unsupported file format: {extension}")