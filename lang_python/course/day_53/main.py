from bs4 import BeautifulSoup as bs
import requests as rq
import selenium.webdriver as wd
from selenium.webdriver.common.keys import Keys as ky
from selenium.webdriver.common.by import By as by

URL_SITE="https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"


pg=rq.get(URL_SITE)
print(pg)
data=pg.text

soup=bs(data,'html.parser')
LIST_OF_MOVIES=soup.find_all('tr',style="background:#EEDD82")
scr_data={'name':[],	'link':[],	'year':[],	'awards':[],	'nom':[]	}

for elm in LIST_OF_MOVIES:
	temp=elm.find_all('td')
	# 
	scr_data['name'].append(	str(	temp[0].text	)	)
	scr_data['link'].append(	"https://en.wikipedia.org"+str(	temp[0].find('a')['href']	)	)
	scr_data['year'].append(	temp[1].text	)
	scr_data['awards'].append(	str(	temp[2].text)	)
	scr_data['nom'].append(		str(temp[3].text)	)

# Here we enter the url 
URL_FORM=""

# Keeping the chrome browser open
opt=wd.ChromeOptions()
opt.add_argument('--ignore-certificate-errors-spki-list')

opt.add_argument('--ignore-ssl-errors')
opt.add_argument('--disable-gpu')
opt.add_argument('--disable-extensions')
opt.add_experimental_option('detach',True)	

# Opening chrome browser thorugh the bot
drv=wd.Chrome(options=opt)
drv.get(URL_FORM)
# Write your code here.
ln=len(	scr_data['name']	)

# Write your code here.
"""
for i in range(ln):
	# Opening the url
	div=drv.find_elements(by.CLASS_NAME,value='Qr7Oae')[1:6]
	inp=([elm.find_element(by.TAG_NAME, value='input') for elm in div])

	# Filling the form's different questions
	inp[0].send_keys(scr_data['year'][i])
	inp[1].send_keys(scr_data['name'][i])
	inp[2].send_keys(scr_data['awards'][i])
	inp[3].send_keys(	scr_data['nom'][i])
	inp[4].send_keys(	scr_data['link'][i])

	# Finding the submit element and clicking it.
	re=drv.find_element(by.CLASS_NAME,value='lRwqcd')
	bt=re.find_element(by.XPATH,	value='//div/span/span')
	bt.click()

	new_res=drv.find_element(by.CLASS_NAME,	value='c2gzEf')
	bt2=new_res.find_element(by.XPATH,	value='//a')
	bt2.click()
"""
# Quitting the browser
