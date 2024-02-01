import requests
from bs4 import BeautifulSoup

URL = "https://privatbank.ua/rates-archive"

pageSourceCode = requests.get(URL)
soup = BeautifulSoup(pageSourceCode.content, 'html.parser')


# nameEurUah = exchangeRate.span.get_text(strip=True)
# print(exchangeRate.find("div", class_="names").span.text.strip())
def currencyRate():
    currencyName = []
    purchaseVal = []
    saleVal = []
    exchangeRate = soup.find("div", class_="courses-currencies")
    for i in exchangeRate.find_all("div", class_="currency-pairs"):
        currencyName.append(i.find("div", class_="names").span.get_text(strip=True).replace("UAH", ""))
        purchaseVal.append(i.find("div", class_="purchase").span.get_text(strip=True))
        saleVal.append(i.find("div", class_="sale").span.get_text(strip=True))

        #print(f"They purchase {currencyName} for {purchaseVal} UAH; They sale {currencyName} for {saleVal} UAH")
    privatExchangeRate = [currencyName, purchaseVal, saleVal]
    return privatExchangeRate
<<<<<<< HEAD
# print(exchangeRate.prettify())
=======
# print(exchangeRate.prettify())
>>>>>>> a66846bca394aa37b79068a272abe0c9be35f9fa
