from bs4 import BeautifulSoup
from services.html_fetcher import fetch_html
from utils.parser_utils import extract_social_handles, extract_contact_info
from models.response import BrandResponse, FAQ, Contact

import requests

def scrape_shopify_store(base_url: str) -> BrandResponse:
    base_url = base_url.rstrip("/")
    homepage_soup = fetch_html(base_url)

    return BrandResponse(
        brand_name=get_brand_name(base_url),
        product_catalog=extract_products_from_collection(base_url),
        hero_products=extract_home_products(base_url),
        privacy_policy=extract_policy(base_url, "privacy-policy"),
        refund_policy=extract_policy(base_url, "refund-policy"),
        terms_of_service=extract_policy(base_url, "terms-of-service"),
        faqs=extract_faqs(base_url),
        social_handles=extract_social_handles(homepage_soup),
        contact=extract_contact_info(homepage_soup),
        brand_about=extract_about_text(base_url),
        important_links=extract_footer_links(homepage_soup)
    )

# --- Each of the functions below mirror what you had before ---
def get_brand_name(url):
    return url.split("//")[-1].split(".")[0]

def extract_products_from_collection(base_url):
    soup = fetch_html(base_url + "/collections/all")
    products = []
    for product in soup.select(".grid-product, .product-card, .productgrid--item"):
        title = product.select_one(".product-card__title, .grid-product__title")
        price = product.select_one(".price, .product-price")
        img = product.find("img")
        products.append({
            "title": title.text.strip() if title else None,
            "price": price.text.strip() if price else None,
            "image": img["src"] if img and "src" in img.attrs else None
        })
    return products

def extract_home_products(base_url):
    soup = fetch_html(base_url)
    hero = []
    for product in soup.select(".product-card, .grid-product"):
        title = product.select_one(".product-card__title, .grid-product__title")
        if title:
            hero.append(title.text.strip())
    return hero

def extract_policy(base_url, policy_type):
    try:
        soup = fetch_html(f"{base_url}/policies/{policy_type}")
        return soup.get_text(separator="\n")[:1000]
    except:
        return None

def extract_faqs(base_url):
    faqs = []
    try:
        soup = fetch_html(f"{base_url}/pages/faqs")
        questions = soup.find_all(["h2", "h3", "strong"])
        for q in questions:
            answer = q.find_next("p")
            if answer:
                faqs.append(FAQ(question=q.get_text(strip=True), answer=answer.get_text(strip=True)))
    except:
        pass
    return faqs

def extract_about_text(base_url):
    try:
        soup = fetch_html(f"{base_url}/pages/about-us")
        return soup.get_text(separator="\n")[:1000]
    except:
        return None

def extract_footer_links(soup: BeautifulSoup):
    links = {}
    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True).lower()
        href = a["href"]
        if "order" in text and "track" in text:
            links["order_tracking"] = href
        elif "contact" in text:
            links["contact_us"] = href
        elif "blog" in text:
            links["blog"] = href
    return links
