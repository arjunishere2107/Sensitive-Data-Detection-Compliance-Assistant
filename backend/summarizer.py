from services.llm_service import LLMService
from prompts import SUMMARY_PROMPT


class ComplianceSummarizer:

    @staticmethod
    def generate(document, detection):

        prompt = SUMMARY_PROMPT.format(

            document=document,

            detection=detection

        )

        llm = LLMService()

        return llm.generate(prompt)