# models/db_models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, JSON

Base = declarative_base()

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    brand_name = Column(String(255))
    website = Column(String(255))
    product_catalog = Column(JSON)
    hero_products = Column(JSON)
    privacy_policy = Column(Text)
    refund_policy = Column(Text)
    faqs = Column(JSON)
    social_handles = Column(JSON)
    contact = Column(JSON)
    brand_about = Column(Text)
    important_links = Column(JSON)
