from bs4 import BeautifulSoup
import sys
import requests
import time

# From timesjobs.com (new york location)
print("put a skill you want to search")
want_skill = input('>')
def timesjobs():
    req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=intern&txtLocation=new+york').text
    soup = BeautifulSoup(req, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for x in jobs:
        posted_date = x.find('span', class_='sim-posted').span.text
        if 'few' in posted_date:  # we filter out the dates without the string "few"
            skill = x.find('span', class_='srp-skills').text.replace('', '')
            Company = x.find('h3', class_='joblist-comp-name').text.replace('', '')
            description = x.header.a['href'] # this is for the link
            if want_skill in skill:
                print(f"Company Name: {Company.strip()}")
                print(f"Date posted: {posted_date.strip()}")
                print(f"Click link for more description:{description.strip()}")
                
if __name__ == '__main__':  # yet to find out
    while True:
        timesjobs()
        time.sleep(30)  # in seconds
        print("wait for 30 seconds", end='')
        print("Or press q to end")
        close = input('>')
        if close == "q":
            sys.exit



'''When requesting in scrapping, request as text: request.get(link).text
The for loop helps the local variables loop over the elements in jobs which reps the whole page'''
