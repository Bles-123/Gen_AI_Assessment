# 🛍️ Shopify Brand Scraper

This is a FastAPI-based service that scrapes a Shopify store and returns structured brand insights such as product catalog, policies, contact info, and more.

---

## 🚀 API Overview


## 📘 Swagger UI

### 🔹 Base UI and GET `/` Endpoint
The root endpoint gives basic API info.

![Root Endpoint Swagger](images/Screenshot%202025-07-18%20153557.png)

---

### ✅ POST `/scrape_store`
Scrapes data from a given Shopify store and returns structured JSON.

**Example Request and Response:**

![Scrape Store - Request & Response](images/Screenshot 2025-07-18 153716.png)

![POST Body Input](images/Screenshot%202025-07-18%20153654.png)

![Scraped Response Preview](images/Screenshot%202025-07-18%20153716.png)

![Product Catalog Example](images/Screenshot%202025-07-18%20153738.png)

![Schema & Validation Error](images/Screenshot%202025-07-18%20153757.png)


---


### 🔹 POST `/scrape_store` - Input Example

Submit a JSON body with a `website_url` key.

```json
{
  "website_url": "https://www.hairoriginals.com/"
}
