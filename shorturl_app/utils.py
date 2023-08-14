import requests
from django.core.cache import cache
from bs4 import BeautifulSoup
import time
def scrape_nifty_data():
    try:
        url = "https://www.nseindia.com/"  # Update with the actual URL
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        headers = {"user-agent": USER_AGENT}
        # print(headers)
        try:
            response = requests.get(url)#headers=headers)
        except requests.exceptions as ae:
            print(ae)
        print(response.status_code)
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.contents)
        cache.set("nifty_data","Rishi",300)  # 5 minutes expiry
        # # time.sleep(10)
        # if response.status_code == 200:            
        #     soup = BeautifulSoup(response.content, "html.parser")
        #     print(soup)
        #     if soup.find_all('a')==[]:
        #         pass            
        #     for link in soup.find_all('a'):
        #         page_url=str(link.get('href'))
        #         print(page_url)
            # print(soup.prettify())

            #gainers_loosers
            
            # print(soup.find_all('div',id='tab1_tableGainer'))
            # print(soup.find_all("a"))
            # for d in soup.find_all("a"):
            #     print(d)
            # table = soup.find_all("tr")
            # print(table)

            # table = soup.find(lambda tag: tag.name=='table')
            # print(table)
            # with open ('content.html', 'w') as file:  
            #     file.write(soup.prettify())
            # div=soup.find_all("a")
            
            # for d  in div:
            #     if d.text=="View All":
        #         print(d)
    except Exception as e:
        print(e)

# scrape_nifty_data()
