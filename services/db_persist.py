# services/db_persist.py
from models.db_models import Brand
from db.session import SessionLocal

def save_brand_data_to_db(data):
    db = SessionLocal()
    brand = Brand(
        brand_name=data["brand_name"],
        website=data.get("website_url", ""),
        product_catalog=data["product_catalog"],
        hero_products=data["hero_products"],
        privacy_policy=data["privacy_policy"],
        refund_policy=data["refund_policy"],
        faqs=data["faqs"],
        social_handles=data["social_handles"],
        contact=data["contact"],
        brand_about=data["brand_about"],
        important_links=data["important_links"]
    )
    db.add(brand)
    db.commit()
    db.close()
