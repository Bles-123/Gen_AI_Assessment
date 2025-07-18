import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def fetch_html(url: str) -> BeautifulSoup:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "lxml")
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=401, detail="Website not found or not accessible")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
