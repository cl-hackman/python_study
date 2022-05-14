import bs4
import requests

# print(help(site)) will give us all the methods in the requests module
# print(site.text()) will give us the html document of the webpage
# print(site.status_code) will tell us if our request was successful
site = requests.get('https://scans-hot.leanbox.us/manga/Onepunch-Man/0153-008.png')
print(site.content) # for getting images on webpages
with open('manga.png', 'wb') as f:
    f.write(site.content)

site = requests.get('https://scans-hot.leanbox.us/manga/Onepunch-Man/0153-012.png')
print(site.content) # for getting images on webpages
with open('manga2.png', 'wb') as f:
    f.write(site.content)

    
site = requests.get('http://curiosity.lib.harvard.edu/crime-broadsides/catalog?search_field=all_fields')
print(site.content) # for getting images on webpages
with open('slides.pdf', 'wb') as f:
    f.write(site.content)

'''def Rarbg(self):
    movie = requests.get('https://rarbg.to/torrents.php?category=movies')
    print(movie.status_code)
    soup = bs4.BeautifulSoup(movie.text, 'html parser') # the html version of the file, the parser is optional so # we don't get a warning'''