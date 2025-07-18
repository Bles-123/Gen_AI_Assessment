from fastapi import FastAPI
from api.routes import router as scraper_router

app = FastAPI(
    title="Shopify Brand Scraper",
    description="Scrapes a Shopify store and returns brand insights",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Shopify Scraper API is running. Visit /docs for Swagger UI."}

app.include_router(scraper_router)
