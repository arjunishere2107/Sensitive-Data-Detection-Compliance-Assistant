from services.vector_service import VectorService

from services.llm_service import LLMService


class RAGPipeline:

    @staticmethod
    def ask(document_id, question):
        vector_store = VectorService.load_vector_store(document_id)

        docs = vector_store.similarity_search(

            question,

            k=4

        )

        context = "\n\n".join(

            doc.page_content

            for doc in docs

        )

        prompt = f"""

You are an AI Compliance Assistant.

Answer ONLY using the provided document.

If the answer is unavailable say

"I could not find this information."

Document

{context}

Question

{question}

"""

        llm = LLMService()

        return llm.generate(prompt)