from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as ky

URL="http://secure-retreat-92358.herokuapp.com/"
# Keeping the chrome browser open
opt=wd.ChromeOptions()
opt.add_argument('--ignore-certificate-errors-spki-list')
opt.add_argument('--ignore-ssl-errors')
opt.add_experimental_option('detach',True)	

# Opening chrome browser thorugh the bot
drv=wd.Chrome(options=opt)
drv.get(URL)

# Write your code here.
form=drv.find_elements(by.TAG_NAME,value="input")
sub=drv.find_element(by.TAG_NAME,value="button")

form[0].send_keys("akfj")
form[1].send_keys("fmdsf")
form[2].send_keys("nsdffn@sjdvnskv")
sub.send_keys(ky.ENTER)

# Quitting the browser
drv.quit()