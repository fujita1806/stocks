import requests
from bs4 import BeautifulSoup

url = "https://finance.stockweather.co.jp/contents/ranking.aspx?mkt=1&cat=0000&type=1"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
code_elements = soup.select(".responsiveTable2 > tbody:nth-child(2) > tr > td:nth-child(2) > span:nth-child(3)")

if code_elements:
    stocks = [int(code.text.strip('（）')) for code in code_elements]
    with open("stocks.txt", "w") as f:
        for stock in stocks:
            f.write(str(stock) + "\n")
