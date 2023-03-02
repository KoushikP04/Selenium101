import os
from selenium import webdriver

os.environ['PATH'] += (r"C:\Users\paulk\Desktop\Selenium\Selenium101")

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
 