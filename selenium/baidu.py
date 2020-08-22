from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=1, size=(1600, 902))
display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)

driver.get('https://bj.meituan.com/meishi/')