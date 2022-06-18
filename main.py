import timely3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# timely3.start_time("time_main.txt")


#Create Chrome Driver
CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get("http://orteil.dashnet.org/experiments/cookie/")


#Create selenium.webdriver.remote.webelement.WebElements
cookie_webelem = driver.find_element(by=By.ID, value="cookie")
money_webelem = driver.find_element(by=By.ID, value="money")


#Use WebElements
end_game = time.time() + 60 * 5

while True:
    timeout = time.time() + 5
    while True:
        cookie_webelem.click()
        if time.time() > timeout:
            break
    if time.time() > end_game:
        break
    money = int(money_webelem.text.replace(",", ""))

    cursor_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b")
    grandma_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b")
    factory_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b")
    mine_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b")
    shipment_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b")
    alchemy_webelem = driver.find_element(by=By.ID, value="buyAlchemy lab")
    portal_webelem = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b")
    time_webelem = driver.find_element(by=By.ID, value="buyTime machine")
    if money >= int(time_webelem.text.split("\n")[0].split(" ")[-1].replace(",", "").strip()):
        time_webelem.click()
    elif money >= int(portal_webelem.text.split(" ")[-1].replace(",", "")):
        portal_webelem.click()
    elif money >= int(alchemy_webelem.text.split("\n")[0].split(" ")[-1].replace(",", "")):
        alchemy_webelem.click()
    elif money >= int(shipment_webelem.text.split(" ")[-1].replace(",", "")):
        shipment_webelem.click()
    elif money >= int(mine_webelem.text.split(" ")[-1].replace(",", "")):
        mine_webelem.click()
    elif money >= int(factory_webelem.text.split(" ")[-1].replace(",", "")):
        factory_webelem.click()
    elif money >= int(grandma_webelem.text.split(" ")[-1].replace(",", "")):
        grandma_webelem.click()
    elif money >= int(cursor_webelem.text.split(" ")[-1].replace(",", "")):
        cursor_webelem.click()

driver.quit()
