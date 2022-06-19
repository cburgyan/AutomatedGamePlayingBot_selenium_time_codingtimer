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


#Create selenium.webdriver.remote.webelement.WebElement
cookie_web = driver.find_element(by=By.ID, value="cookie")


#Program Flow
now = time.time()
end_game = now + 60 * 1

while now < end_game:
    purchase_time = now + 5
    # print(f"purchTime: {purchase_time}")
    # print("main loop")
    while True:
        # print("nested Loop")
        cookie_web.click()
        if time.time() > purchase_time:
            # print(time.time())
            break


    #Purchase Time
    #--Get Elements
    money_web = driver.find_element(by=By.ID, value="money")
    cursor_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b")
    grandma_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b")
    factory_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b")
    mine_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b")
    shipment_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b")
    portal_web = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b")
    alchemy_web = driver.find_element(by=By.ID, value="buyAlchemy lab")
    time_web = driver.find_element(by=By.ID, value="buyTime machine")

    #--Get ints for money and costs
    money = int(money_web.text.replace(",", ""))
    print(int(cursor_web.text.split(" ")[-1].replace(",", "")))
    cursor_cost = int(cursor_web.text.split(" ")[-1].replace(",", ""))
    grandma_cost = int(grandma_web.text.split(" ")[-1].replace(",", ""))
    factory_cost = int(factory_web.text.split(" ")[-1].replace(",", ""))
    mine_cost = int(mine_web.text.split(" ")[-1].replace(",", ""))
    shipment_cost = int(shipment_web.text.split(" ")[-1].replace(",", ""))
    portal_cost = int(portal_web.text.split(" ")[-1].replace(",", ""))
    alch_cost = int(alchemy_web.text.split("\n")[0].split(" ")[-1].replace(",", ""))
    time_cost = int(time_web.text.split("\n")[0].split(" ")[-1].replace(",", ""))

    #--Purchase most expensive
    if money >= time_cost:
        time_web.click()
    elif money >= portal_cost:
        portal_web.click()
    elif money >= alch_cost:
        alchemy_web.click()
    elif money >= shipment_cost:
        shipment_web.click()
    elif money >= mine_cost:
        mine_web.click()
    elif money >= factory_cost:
        factory_web.click()
    elif money >= grandma_cost:
        grandma_web.click()
    elif money >= cursor_cost:
        cursor_web.click()

    #--Set Now
    now = time.time()


#Print Cookies per Second
print(driver.find_element(by=By.ID, value="cps").text)


#Quit Driver
driver.quit()

timely3.stop_time("time_main.txt")