import pandas as pd
import numpy as np
import os, sys, re
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

# browser = webdriver.Ie()
browser = webdriver.Chrome()
# browser.maximize_window()
url = "http://www.xyzq.com.cn/"
# browser.set_window_size(800,500) # 不要调整窗体大小，否则会报错
browser.get(url)
# login = browser.find_element_by_id("amenunologinarea")
# login = browser.find_element_by_link_text("立即登录")
login = browser.find_element_by_xpath("//div[@class='lg-top']/a")
print(login.text)
login.click()
financial_account = browser.find_element_by_id("rtab")
print(financial_account.text)
financial_account.click()
input_account = browser.find_element_by_xpath("//p[@class='z-nomar']/input")
input_account.send_keys('320076588')

WebDriverWait(browser, 10).until(lambda  x:x.find_element_by_xpath("//p[@id='passwordtips']/input[2]").is_displayed())
input_password = browser.find_element_by_xpath("//p[@id='passwordtips']/input[2]")

hov = ActionChains(browser)
hov.move_to_element(input_password)
hov.click()
hov.send_keys('218226')
hov.perform()
browser.find_element_by_xpath("//p[@class='z-btn']/a").click()
try:
    WebDriverWait(browser, 10).until(EC.title_contains(u"兴业证券"))
except:
    browser.quit()
print(browser.title)

# licai_btn = browser.find_element_by_xpath("//a[@class='pro_two']")
licai_btn = browser.find_element_by_link_text(u"理财产品")
licai_btn.click()

try:
    WebDriverWait(browser, 10).until(EC.title_contains(u"优品城--理财产品"))
except:
    browser.quit()

# myitems = browser.find_element_by_link_text(u"我的专属")
myitems = browser.find_element_by_xpath("//div[@id='navList']/div/a[3]")
print(myitems.text)

myitems.click()
WebDriverWait(browser,10).until(lambda browser: browser.find_element_by_xpath("//div[@id='expandZone']/div/div[3]/div/a[4]").is_displayed())
myown = browser.find_element_by_xpath("//div[@id='expandZone']/div/div[3]/div/a[4]")
print(myown.text)
myown.click()

try:
    WebDriverWait(browser, 10).until(EC.title_contains(u"我的财富"))
except:
    browser.quit()

total_asset = browser.find_element_by_id("tdnetasset").text
total_asset = total_asset.replace(",", "")
total_asset = float(total_asset)
print(total_asset)
print(type(total_asset))
lst = []
lst.append(total_asset)
# 对该数字进行文本处理，可以用字符串，从-1方向开始替换掉逗号，然后转换为浮点数
# df = pd.DataFrame({'total_asset':total_asset})
df = pd.DataFrame({'total_asset':lst})
filepath = "E:\\Project\\hanyuntest\\spider\\selenium\\daily_data\\"
cur_date = datetime.datetime.now().strftime("%Y-%m-%d")
filename = filepath+cur_date+'.csv'
with open(filename, "w") as f:
    df.to_csv(f)
time.sleep(1)
browser.quit()