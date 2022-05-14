from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import requests


excel = Workbook() #Open an excel workbook
sheet = excel.active   #Telling python to open an active sheet in the workbook
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Name', 'Year', 'IMDB Rating']) #Telling python to add column headings to cells(shown by the commas) 

try:
    web = 'https://www.imdb.com/chart/top/'
    req = requests.get(web).text
    soup = bs(req, 'lxml')
    parent = soup.find('tbody', class_ ='lister-list').find_all('tr')
    for x in parent:
        name = x.find('td', class_ ='titleColumn').a.text #Am saying, find the a tag in this td
        year = x.find('span', class_ ='secondaryInfo').text.strip('()')
        rating = x.find('td', class_ ='ratingColumn imdbRating').text
        print(f"Title: {name}")
        print(f"Year: {year}")
        print(f"Rating: {rating.strip()} \n")
        sheet.append([name, year, rating.strip()])  #Doing this so python automatically updates the cell via BeauttifulSoup
except:
    pass
excel.save('Web scrapping IMDB Top Movies.xlsx') # .xlsx is file extension for excel




