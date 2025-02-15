from bs4 import BeautifulSoup
import requests
#--------------------------
url = 'https://news.ycombinator.com/'
response = requests.get(url)
html_text = response.text
#-------------------------
soup = BeautifulSoup(html_text, 'lxml')
time = input("Please input a valid time: ") #ask user to input a valid time

news = soup.find_all('tr', class_='athing')
for new in news:
    subtext = new.find_next_sibling('tr').find('td', class_='subtext')
    if subtext:
        date = subtext.find('span', class_='age')
        if date and time in date.text:
            title = new.find('span', class_='titleline')
            site = subtext.find('span', class_='sitestr')
            user = subtext.find('a', class_='hnuser')
            print(f'The News is: {title.text}')
            print(f'The date of the news is: {date.text.strip()}')
            print(f'The website that published it: {site.text.strip() if site else "N/A"}')#after stip() is really nice error handling
            print(f'The user that published it: {user.text.strip() if user else "N/A"}')
            print("-"*40)

#conclusion this website scraper gives us the news based on the time we have inputed displays
#the user that published and the website with good and improevd error handling
