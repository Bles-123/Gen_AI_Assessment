import re
from bs4 import BeautifulSoup

def extract_social_handles(soup: BeautifulSoup):
    social = {}
    links = soup.find_all("a", href=True)
    for link in links:
        href = link["href"]
        if "instagram.com" in href:
            social["instagram"] = href
        elif "facebook.com" in href:
            social["facebook"] = href
        elif "tiktok.com" in href:
            social["tiktok"] = href
    return social

def extract_contact_info(soup: BeautifulSoup):
    text = soup.get_text()
    emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))
    phones = list(set(re.findall(r"\+?\d[\d\s\-\(\)]{7,}", text)))
    return {
        "emails": emails,
        "phones": phones
    }
