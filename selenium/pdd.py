# *-* coding:utf8 *-*
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'http://mobile.yangkeduo.com/login.html?from=http%3A%2F%2Fmobile.yangkeduo.com%2Fpersonal.html%3Frefer_page_name%3Dindex%26refer_page_id%3D10002_1564927439453_owyPsMDiNt%26refer_page_sn%3D10002&refer_page_name=personal&refer_page_id=10001_1564927441827_6M8hSfcVeD&refer_page_sn=10001')
driver.find_elements_by_xpath('//*[@id="first"]/div[1]/div[2]')[0].click()
# phone = "获取手机号"
driver.find_elements_by_xpath('//*[@id="user-mobile"]')[0].send_keys(16625158447)

driver.find_elements_by_xpath('//*[@id="code-button"]')[0].click()
# SMS = "获取短信验证码"
# while True:
#     if SMS:
#         break
time.sleep(50)
driver.find_elements_by_xpath('//*[@id="input-code"]')[0].send_keys()
driver.find_elements_by_xpath('//*[@id="submit-button"]')[0].click()
print(driver.get_cookies())

driver.close()

