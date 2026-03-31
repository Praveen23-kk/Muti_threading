




'''https://python.langchain.com/docs/introduction/

https://python.langchain.com/docs/concepts/

https://python.langchain.com/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=['https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/docs/concepts/',

'https://python.langchain.com/docs/tutorials/'

]

def fetch_contents(url):
    reponse=requests.get(url)
    soup=BeautifulSoup(reponse.content,'html.parser')
    print(f"Fetched {len(soup.text)} charaters from {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
 
 
for thread in threads:
     thread.join()
     
print("ALL Webpapes pages fetched")     
    