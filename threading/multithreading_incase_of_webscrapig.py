# real world example : multithreading for i/o bound tasks
#     scenario: webscraping
# webscraping involves mking numerous network requests to fetch data from websites.
# these tasks are i/o bound because they spend a significant amount of time waiting for responses from web servers.
# multithreading can help improve the efficiency of webscraping by allowing multiple requests to be made concurrently.

"""https://httpbin.org/delay/1

https://quotes.toscrape.com/

https://books.toscrape.com/"""

import threading
import requests
from bs4 import BeautifulSoup # for parsing HTML ,parsing means extracting data from HTML content

urls=[
    "https://httpbin.org/delay/1",
    "https://quotes.toscrape.com/",
    "https://books.toscrape.com/"
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser') # parse the HTML content using BeautifulSoup
    print(f"Fetched {len(soup.text)} characters from {url}")# print the length of the text content fetched from the URL


threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)# append the thread to the list of threads
    thread.start()# start the thread to begin execution


for thread in threads:
    thread.join()# wait for all threads to complete before exiting the program

print("All web scraping tasks completed.")
