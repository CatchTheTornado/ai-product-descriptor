import os
import openai
from .llm_strategy import LLMStrategy
import app.prompts as prompts
import json

class ChatGPTStrategy(LLMStrategy):
    def __init__(self):
        # Set the OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )


    def describe(self, image_url: str):
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompts.DESCRIBE_PROMPT },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                    },
                ],
                }
            ],
            max_tokens=1000,
        )


        # Extract and return the description from the response
        description = json.loads(response.choices[0].message.content.split("```json")[1].split("```")[0])
        return description