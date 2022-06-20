import time

import selenium.common.exceptions

import timely3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


code_timer = timely3.CodingTimer("time_main.txt")
# code_timer.start_time()
# code_timer.pause_time()
# code_timer.unpause_time()
# code_timer.stop_time()


#Create Chrome Driver
CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"
servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
driver = webdriver.Chrome(service=servicer)


#Connect Driver to Website
driver.get("http://orteil.dashnet.org/experiments/cookie/")


#Create selenium.webdriver.remote.webelement.WebElements
cookie_WE = driver.find_element(by=By.ID, value="cookie")
money_WE = driver.find_element(by=By.ID, value="money")


#Program Flow
end_game = time.time() + 60 * 5

while True:
    purchase_time = time.time() + 10
    # print("outer loop")
    while True:
        if time.time() < purchase_time:
            cookie_WE.click()
        else:
            break
    if time.time() > end_game:
        break

    #Purchase Items
    try:
        #Create Purchaseable WebElements
        cursor_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b")
        grandma_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b")
        factory_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b")
        mine_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b")
        shipment_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b")
        portal_WE = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b")
        alch_WE = driver.find_element(by=By.ID, value="buyAlchemy lab")
        time_WE = driver.find_element(by=By.ID, value="buyTime machine")


        #Get Cost and Get Money Inventory
        money = int(money_WE.text.replace(",", ""))
        cursor_cost = int(cursor_WE.text.split(" ")[-1].replace(",", ""))
        grandma_cost = int(grandma_WE.text.split(" ")[-1].replace(",", ""))
        factory_cost = int(factory_WE.text.split(" ")[-1].replace(",", ""))
        mine_cost = int(mine_WE.text.split(" ")[-1].replace(",", ""))
        shipment_cost = int(shipment_WE.text.split(" ")[-1].replace(",", ""))
        portal_cost = int(portal_WE.text.split(" ")[-1].replace(",", ""))
        alch_cost = int(alch_WE.text.split("\n")[0].split(" ")[-1].replace(",", ""))
        time_cost = int(time_WE.text.split("\n")[0].split(" ")[-1].replace(",", ""))


        #Purchase Item/s
        if time_cost <= money:
            time_WE.click()
        elif portal_cost <= money:
            portal_WE.click()
        elif alch_cost <= money:
            alch_WE.click()
        elif shipment_cost <= money:
            shipment_WE.click()
        elif mine_cost <= money:
            mine_WE.click()
        elif factory_cost <= money:
            factory_WE.click()
        elif grandma_cost <= money:
            grandma_WE.click()
        elif cursor_cost <= money:
            cursor_WE.click()
        else:
            break

    except selenium.common.exceptions.StaleElementReferenceException:
        pass


print(driver.find_element(by=By.ID, value="cps").text)


#Quit Driver
driver.quit()
