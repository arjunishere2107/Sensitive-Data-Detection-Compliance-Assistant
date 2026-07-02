import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from services.embedding_service import EmbeddingService


class VectorService:
    """
    Handles creation and retrieval of FAISS vector databases
    for document-based Retrieval-Augmented Generation (RAG).
    """

    BASE_VECTOR_PATH = "vector_db"

    @classmethod
    def create_vector_store(cls, document_id: str, text: str) -> int:
        """
        Splits the document into chunks, creates embeddings,
        builds a FAISS index, and saves it locally.

        Args:
            document_id (str): Unique document identifier.
            text (str): Extracted document text.

        Returns:
            int: Number of chunks created.
        """

        if not text.strip():
            raise ValueError("Document contains no text.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_text(text)

        embeddings = EmbeddingService.get_embeddings()

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

        save_path = os.path.join(
            cls.BASE_VECTOR_PATH,
            document_id
        )

        os.makedirs(save_path, exist_ok=True)

        vector_store.save_local(save_path)

        return len(chunks)

    @classmethod
    def load_vector_store(cls, document_id: str):
        """
        Loads an existing FAISS vector store.

        Args:
            document_id (str): Unique document identifier.

        Returns:
            FAISS: Loaded vector database.
        """

        load_path = os.path.join(
            cls.BASE_VECTOR_PATH,
            document_id
        )

        if not os.path.exists(load_path):
            raise FileNotFoundError(
                f"No vector database found for document: {document_id}"
            )

        embeddings = EmbeddingService.get_embeddings()

        return FAISS.load_local(
            folder_path=load_path,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )