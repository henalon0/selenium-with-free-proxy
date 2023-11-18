import time
import random 
from utils.free_proxies import FreeProxy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

free_proxy = FreeProxy() 
print("Getting proxy list...")

proxy_list = free_proxy.get_proxy_list()
print(proxy_list)

for _ in range(2):
    random_proxy = random.choice(proxy_list)
    print(random_proxy)

    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server={random_proxy}")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://duckduckgo.com/?q=what+is+my+ip")

        time.sleep(5)
        driver.close()
    except:
        time.sleep(5)
        driver.close()
