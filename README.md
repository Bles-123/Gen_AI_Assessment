# 🛍️ Shopify Brand Scraper

This is a FastAPI-based service that scrapes a Shopify store and returns structured brand insights such as product catalog, policies, contact info, and more.

---

## 🚀 API Overview

### ✅ POST `/scrape_store`
Scrapes data from a given Shopify store and returns structured JSON.

**Example Request and Response:**

![Scrape Store - Request & Response](images/Screenshot 2025-07-18 153654.png)

---

## 📘 Swagger UI

### 🔹 Base UI and GET `/` Endpoint
The root endpoint gives basic API info.

![Root Endpoint Swagger](images/Screenshot%202025-07-18%20153557.png)

---


### 🔹 POST `/scrape_store` - Input Example

Submit a JSON body with a `website_url` key.

```json
{
  "website_url": "https://www.hairoriginals.com/"
}
