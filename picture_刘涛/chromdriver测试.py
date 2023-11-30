
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_driver_path = 'D:\Chrome低版本103内部版本\Chrome_1170582\chrome-win\chromedriver.exe'  # 请替换为您的ChromeDriver的实际路径
browser = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
