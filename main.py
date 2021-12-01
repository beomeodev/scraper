import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l=")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find('div', class_="pagination")

pages = pagination.find_all('a')

spans = []

for page in pages:
    spans.append(page.find('span'))

print(spans[:-1])
