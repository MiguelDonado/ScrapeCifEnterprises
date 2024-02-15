from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL_FIRST") + "{enterprise}" + os.getenv("URL_SECOND")


def put_name_desired_format(enterprise):
    return enterprise.replace(" ", "+")


def get_href_anchor_tag(enterprise):
    url_to_search = url.format(enterprise=enterprise)
    html_text = requests.get(url_to_search)
    soup = BeautifulSoup(html_text.text, "lxml")
    table_companies_names = soup.find("table", class_="t00")
    company_cell = table_companies_names.find("td")
    company_anchor_tag = company_cell.find("a")
    href_company = company_anchor_tag["href"]
    return href_company


def get_cif_from_href(href_url):
    html_text = requests.get(f"https:{href_url}")
    soup = BeautifulSoup(html_text.text, "lxml")
    cif_tag = soup.find("td", string="CIF:")
    return cif_tag.next_sibling.string
