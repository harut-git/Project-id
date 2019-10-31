#encoding: utf-8


from selenium import webdriver

# my_options = webdriver.ChromeOptions()
# my_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="C:\\Users\\QTLab\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=mj0XInqZMHY&list=RDQMgEzdN5RuCXE&start_radio=1")
a = driver.find_elements_by_id("video-title")
for i in a:
    print(i.text)
