from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


userName = os.environ["BROWSERSTACK_USERNAME"]
accessKey =  os.environ["BROWSERSTACK_ACCESS_KEY"]

desired_caps = {
    "build": "Hitesh-Python Android",
    "device": "Samsung Galaxy S7",
    "app": "bs://8714898cbcd435a4f6a7cae7654ed9976721830c"
}

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

print "session id: "+ driver.session_id

search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(100)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()
