from pydantic import BaseModel
from typing import List, Optional, Dict

class FAQ(BaseModel):
    question: str
    answer: str

class Contact(BaseModel):
    emails: List[str]
    phones: List[str]

class BrandResponse(BaseModel):
    brand_name: str
    product_catalog: List[Dict[str, Optional[str]]]
    hero_products: List[str]
    privacy_policy: Optional[str]
    refund_policy: Optional[str]
    terms_of_service: Optional[str]
    faqs: List[FAQ]
    social_handles: Dict[str, str]
    contact: Contact
    brand_about: Optional[str]
    important_links: Dict[str, str]


