# *-* coding:utf8 *-*
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path=r"C:\Users\新兵蛋子1\AppData\Local\Google\Chrome\Application\chromedriver",chrome_options=option)
driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d94lXCjq&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')
time.sleep(2)
driver.find_elements_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]')[0].click()
driver.find_elements_by_id("TPL_username_1")[0].send_keys("")  # 账号
driver.find_elements_by_id("TPL_password_1")[0].send_keys("")  # 密码
driver.find_elements_by_xpath('//*[@id="J_SubmitStatic"]')[0].click()
time.sleep(0.30)
driver.find_elements_by_xpath('//*[@id="J_SiteNavMytaobao"]/div[1]/a/span')[0].click()
driver.find_elements_by_xpath('//*[@id="bought"]')[0].click()

print(driver.page_source)





# //*[@id="J_QRCodeLogin"]/div[5]/a[1]




