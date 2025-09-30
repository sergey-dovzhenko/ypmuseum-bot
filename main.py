# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import os
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome (

#     #executable_path = "/Users/sergeydovzhenko/Documents/skolkovo/chromedriver_mac64/chromedriver"
# )

op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=op)

driver.maximize_window()

driver.get("https://ypmuseum.tn-cloud.ru/?id=1&sid=43")

time.sleep(10)

events_content = driver.find_elements(By.CLASS_NAME, "events__content")

for event_content in events_content:
    action__text = event_content.find_element(By.CLASS_NAME, "action__text").text
    if action__text == "Билет с экскурсионным обслуживанием: дом Л.Н.Толстого, заповедник":
        buy__available = event_content.find_element(By.CLASS_NAME, "buy__available").text
        print(action__text)
        print(buy__available)

        buy__button = event_content.find_element(By.CLASS_NAME, "buy__button")
        buy__button.click()

        time.sleep(10)

        times__item = driver.find_elements(By.CLASS_NAME, "times__item")
        for time__item in times__item:
            times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
            times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

            print(times__time)
            print(times__amount)
        break



# bt2 = prjs_len[1].click()

# time.sleep(10)

# print(prjs_len)