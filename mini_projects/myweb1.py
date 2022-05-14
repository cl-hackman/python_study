from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import *


def wayup():
    excel = Workbook()
    sheet = excel.active
    sheet.title = 'WAY UP INTERNSHIPS ECON'
    headers = sheet.append(['Company Name', 'Position', 'Link'])

    web = requests.get(
        'https://www.wayup.com/s/internships/economics/new-york-ny/').text
    soup = bs(web, 'lxml')
    for x in soup.find_all('div', class_='sc-iCoHVE RjEGt'):
        # for space
        name = x.find('div', class_='FlexGrow-sc-qaf1ja-0 jhtqGx').text.upper()
        position = x.find('h3', class_='sc-fujyUd iohUvv').text.replace('', '')
        # The "a" is in the 'div' link that's why we use "soup" not "x"
        links = soup.find('div', class_='sc-iCoHVE RjEGt').a['href']
        print(f"Name: {name}")
        print(f"Position: {position}")
        print(f"Link: {links.strip()} \n")
        sheet.append([name, position, links.strip()])

    excel.save('WAY UP.xlsx')
