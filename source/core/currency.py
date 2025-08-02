import requests
import xml.etree.ElementTree as ET

def dollar_tl_price():
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    for currency in root.findall("Currency"):
        if currency.attrib["CurrencyCode"] == "USD":
            return {
                "buy": float(currency.find("ForexBuying").text.replace(",", ".")),
                "sell": float(currency.find("ForexSelling").text.replace(",", "."))
            }

def euro_tl_price():
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    for currency in root.findall("Currency"):
        if currency.attrib["CurrencyCode"] == "EUR":
            return {
                "buy": float(currency.find("ForexBuying").text.replace(",", ".")),
                "sell": float(currency.find("ForexSelling").text.replace(",", "."))
            }
