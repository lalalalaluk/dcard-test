from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import bs4
import requests

options = Options()

# options.add_argument("--incognito")  # 啟動進入無痕模式
# options.add_argument("--window-size=1,1")  # 頁面長度寬度調整
# # chrome_options.add_argument('--headless')  # 啟動Headless 無頭(隱藏瀏覽器)

# # 隱藏"Chrome正在受到自動軟體的控制"
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# options.add_argument('--disable-gpu')  # 關閉GPU 避免某些系統或是網頁出錯
# options.add_argument('--hide-scrollbars')  # 隱藏滾動條, 應對一些特殊頁面

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), chrome_options=options)


driver.get("https://www.dcard.tw/service/api/v2/posts")
data = driver.page_source
root = bs4.BeautifulSoup(data, "html.parser")

# titles = root.find("div", class_="atm_vv_1btx8ck atm_w4_1hnarqo c1ehvwc9")

# result = ""
# for title in titles:
#     result += title.text.strip().replace('\n', '').replace(' ', '')

print(root)
# driver.close()
