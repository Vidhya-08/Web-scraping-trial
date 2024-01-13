# %%
import requests
from bs4 import BeautifulSoup

# %%
#making a get request
r=requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

# %%
print(r.content)

# %%
#asks two arguments-where is the content,parser-parsing a html 
s=BeautifulSoup(r.content,'html.parser')
#s.find('title')
#s.find_all('div')
c=s.find_all('p')
for i in c:
    print(i.text)

# %%
#finding by id
print(s.find('div',id='p-navigation').text)
#finding by class
s.find('div',class_='printfooter').text


