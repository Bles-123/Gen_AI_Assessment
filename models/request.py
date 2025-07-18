from pydantic import BaseModel

class WebsiteInput(BaseModel):
    website_url: str
