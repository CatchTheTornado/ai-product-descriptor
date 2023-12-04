from pydantic import BaseModel

class ImageDescriptionRequest(BaseModel):
    image_url: str