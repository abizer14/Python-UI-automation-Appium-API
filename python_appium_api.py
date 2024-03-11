import requests
from requests.auth import HTTPBasicAuth
from appium import webdriver
import time

desired_caps = {
    "device" : "Samsung Galaxy S22",
    "os_version" : "12.0",
    "os" : "android",
    "app" : "bs://APP_ID"
}

username = "BS_USERNAME"
access_key = "BS_ACCESSKEY"

driver = webdriver.Remote(f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub", desired_caps)

#Retrieving the BrowserStack session ID during runtime
session_hash_id = driver.session_id
time.sleep(5)

#Directly execute the close app Appium API instead of using the driver.close_app() command
close_app_appium_url = f'https://hub-cloud.browserstack.com/wd/hub/session/{session_hash_id}/appium/app/close'
requests.post(close_app_appium_url, auth=HTTPBasicAuth(username, access_key))

driver.quit()