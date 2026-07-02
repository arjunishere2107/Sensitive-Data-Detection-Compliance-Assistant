from groq import Groq

from config import Config


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=Config.GROQ_API_KEY
        )

    def generate(self, prompt: str):

        response = self.client.chat.completions.create(

            model=Config.MODEL_NAME,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            max_tokens=1000

        )

        return response.choices[0].message.content