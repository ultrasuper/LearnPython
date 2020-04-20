# coding:utf-8
import pandas as pd 
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from xlrd import open_workbook
from xlwt import Workbook 
from multiprocessing import Pool
import time


IN_PATH = "D:\\Seans One Drive\\OneDrive\\桌面\\data\\origin\\"
OUT_PATH = "D:\\Seans One Drive\\OneDrive\\桌面\\data\\registered\\"
default_sheet = "Sheet1"
HomePage = "https://www.dtdjzx.gov.cn/"
register_page = "http://swgk.dtdjzx.gov.cn/sanwu_phone/zhuce.do"
PASSWORD = "yz666666"

def get_filenames(path):
	files = os.listdir(path)
	return files

def register(my_name, my_id):
	try:
		options = Options()
		# options.add_argument("--headless")
		# options.add_argument("--disable-gpu")
		driver = webdriver.Chrome(options=options)
		driver.get(register_page)
		# print("打开浏览器")
		# print(driver.title)

		name = driver.find_element_by_xpath("//input[@class='tz-input name' and  @placeholder='姓名']")
		name.send_keys(my_name)

		identity = driver.find_element_by_xpath("//input[@class='tz-input id' and @placeholder='身份证号']")
		identity.send_keys(my_id)

		pass_1 = driver.find_element_by_xpath("//input[@class='tz-input pwd1' and @placeholder='密码']")
		pass_1.send_keys(PASSWORD)

		pass_2 = driver.find_element_by_xpath("//input[@class='tz-input pwd2' and @placeholder='确认密码']")
		pass_2.send_keys(PASSWORD)

		confirm = driver.find_element_by_xpath("//input[@id='submit' and @class='tianze-regbtn']")
		confirm.click()

		
		# WebDriverWait(driver, 10).until(lambda  x:x.find_element_by_xpath("//div[@class='e-box-content']/div[1]/span").is_displayed())
		# pop_info = driver.find_element_by_xpath("//div[@class='e-box-content']/div[1]/span").text
		alert = driver.switch_to_alert()
		alert.accept()
		# time.sleep(100)

		driver.quit()
		return 1

		# if pop_info == "请勿重复注册":
		# 	print("请勿重复注册")
		# 	return 2
		# elif pop_info == "注册成功":
		# 	print("注册成功")
		# 	return 1
	except:
		print("注册失败用户：", my_name, my_id)
		return -1

def handle_a_sheet(file_name):
	infile = os.path.join(IN_PATH, file_name)
	print(file_name)
	outfile = os.path.join(OUT_PATH, file_name)

	output_workbook = Workbook()
	output_worksheet = output_workbook.add_sheet(file_name)
	with open_workbook(infile) as workbook:
		print("Open success")
		print(workbook.sheets())
		# work_sheet = workbook.sheets()[0]
		work_sheet = workbook.sheet_by_name(default_sheet)
		# print(work_sheet)
		p = Pool(8)
		for row_index in range(1, work_sheet.nrows):

			name = work_sheet.cell_value(row_index, 0)
			identity = work_sheet.cell_value(row_index, 1)
			p.apply_async(register, args=(name, identity,))

			# result = register(name, identity)
			# result = 1
			# print(name, identity, result)

			output_worksheet.write(row_index, 0, name)
			output_worksheet.write(row_index, 1, identity)
			# output_worksheet.write(row_index, 2, result)
		p.close()
		p.join()
	if not os.path.exists(outfile):
		output_workbook.save(outfile)


if __name__ == "__main__":

	files = get_filenames(IN_PATH)
	print(files)
	# l = ['南寨村.xls', '台上村.xls', '山下村.xls', '岛子村.xls', '康家夼村.xls', '沟东村.xls', '矫家泊村.xls', '转山头村.xls']
	# handle_a_sheet(l[0])

	# p = Pool(8)
	for i in range(len(files)):
		# p.apply_async(handle_a_sheet, args=(files[i],))
		handle_a_sheet(files[i])
