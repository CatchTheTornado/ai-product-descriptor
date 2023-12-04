from fastapi import FastAPI, HTTPException
from .chatgpt_strategy import ChatGPTStrategy
from .llm_strategy import LLMStrategy
from .models import ImageDescriptionRequest  # assuming the model is in models.py

app = FastAPI()
llm_processor: LLMStrategy = ChatGPTStrategy()

@app.post("/describe/")
async def describe_image(request: ImageDescriptionRequest):
    try:
        return llm_processor.describe(request.image_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))