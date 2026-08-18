from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by

URL="https://en.wikipedia.org/wiki/Main_Page"
# Keeping the chrome browser open
opt=wd.ChromeOptions()
opt.add_argument('--ignore-certificate-errors-spki-list')
opt.add_argument('--ignore-ssl-errors')
opt.add_experimental_option('detach',True)	

# Opening chrome browser thorugh the bot
drv=wd.Chrome(options=opt)
drv.get(URL)

# Write your code here.
num=drv.find_element(by.XPATH,"//div[@id='articlecount']/a")
# Quitting the browser
drv.quit()