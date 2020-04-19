# coding:utf-8
import pandas as pd 
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xlrd import open_workbook
from xlwt import Workbook 
from multiprocessing import Pool


IN_PATH = "D:\\Seans One Drive\\OneDrive\\桌面\\data\\"
OUT_PATH = "D:\\Seans One Drive\\OneDrive\\桌面\\registered\\"
default_sheet = "Sheet1"
HomePage = "https://www.dtdjzx.gov.cn/"
register_page = "http://swgk.dtdjzx.gov.cn/sanwu_phone/zhuce.do"
PASSWORD = "yz666666"

def get_filenames(path):
	files = os.listdir(path)
	return files

def register(my_name, my_id):
	try:
		driver = webdriver.Chrome()
		driver.get(register_page)
		print("打开浏览器")
		print(driver.title)

		name = driver.find_element_by_xpath("//input[@class='tz-input name' and  @placeholder='姓名']")
		name.send_keys("于娜")

		identity = driver.find_element_by_xpath("//input[@class='tz-input id' and @placeholder='身份证号']")
		identity.send_keys("371083198409291029")

		pass_1 = driver.find_element_by_xpath("//input[@class='tz-input pwd1' and @placeholder='密码']")
		pass_1.send_keys(PASSWORD)

		pass_2 = driver.find_element_by_xpath("//input[@class='tz-input pwd2' and @placeholder='确认密码']")
		pass_2.send_keys(PASSWORD)

		confirm = driver.find_element_by_xpath("//input[@id='submit' and @class='tianze-regbtn']")
		confirm.click()

		pop_info = driver.find_element_by_xpath("//div[@class='e-box-content']/div/span").text

		driver.close()
		if pop_info == "请勿重复注册":
			print("请勿重复注册")
			return 2
		elif pop_info == "注册成功":
			print("注册成功")
			return 1
	except:
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
		work_sheet = workbook.sheet_by_name(file_name)
		# print(work_sheet)
		for row_index in range(1, work_sheet.nrows):

			name = work_sheet.cell_value(row_index, 0)
			identity = work_sheet.cell_value(row_index, 1)
			result = register(name, identity)
			# result = 1
			print(name, identity, result)

			output_worksheet.write(row_index, 0, name)
			output_worksheet.write(row_index, 1, identity)
			output_worksheet.write(row_index, 2, result)
	if not os.path.exists(outfile):
		output_workbook.save(outfile)


if __name__ == "__main__":

	files = get_filenames(IN_PATH)
	print(files)
	p = Pool(4)
	for file in range(files):
		p.apply_async(handle_a_sheet, args=(file,))
	p.close()
	p.join()