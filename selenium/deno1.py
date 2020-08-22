from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver",chrome_options=option)
# driver.get('http://www.dianping.com/shop/131346422')
driver.get('https://lanshan.meituan.com/meishi/')


