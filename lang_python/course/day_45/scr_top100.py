from bs4 import BeautifulSoup as  bs
import requests as rq

# Getting the HTML file
site='https://'#web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
page=rq.get(site)
print(page)
data=page.text

# Parsing the HTML file
soup=bs(data,'html.parser')
con=soup.find('div',class_='gallery');	title=con.find_all('h3',class_='title')

lt=""
movie_name=[str(nam.text) for nam in title]
sz	=	len(movie_name)
for i in range(sz):
	lt=lt+movie_name[sz-1-i]+"\n"

# Writing the data in a file
with open(file='day_45\\top_100.txt',mode='w',encoding='utf-8') as fil:
	fil.write(lt)
	print('success')