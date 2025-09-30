# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telebot
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



telegram_bot_key = "8127384745:AAH9Ce83P1lYegIOrRlW261g4YVvl9WXKyg"
telegram_chat_id = "-4849379875"
bot = telebot.TeleBot(telegram_bot_key)


# driver = webdriver.Chrome (

#     #executable_path = "/Users/sergeydovzhenko/Documents/skolkovo/chromedriver_mac64/chromedriver"
# )

op = webdriver.ChromeOptions()
# op.add_argument('--headless')
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=op)

driver.maximize_window()

BASE_URL = "https://ypmuseum.tn-cloud.ru/?id=1&sid=43"

driver.get(BASE_URL)

time.sleep(10)

events_content = driver.find_elements(By.CLASS_NAME, "events__content")
message = ""

for event_content in events_content:
    action__text = event_content.find_element(By.CLASS_NAME, "action__text").text
    if action__text in ["Билет с экскурсионным обслуживанием по маршруту: Дом Толстого, Заповедник"]:
        buy__available = event_content.find_element(By.CLASS_NAME, "buy__available").text
        
        message += "*" + action__text + "*" + "\n"
        print(action__text)
        
        print(f"Всего билетов: {buy__available}")
        message += f"Всего билетов: {buy__available}" + "\n"

        buy__button = event_content.find_element(By.CLASS_NAME, "buy__button")
        buy__button.click()

        time.sleep(10)

        try:
            if driver.find_element(By.CLASS_NAME, "swiper-container") is not None:

                sliders = driver.find_elements(By.CLASS_NAME, "slide")
                for slider in sliders:
                    slider.click()
                    time.sleep(3)

                    slide__day = slider.find_element(By.CLASS_NAME, "slide__day").text
                    slide__month = slider.find_element(By.CLASS_NAME, "slide__month").text
                    slide__weekday_text = slider.find_element(By.CLASS_NAME, "slide__weekday-text").text

                    print(f"Дата: {slide__day} {slide__month} ({slide__weekday_text})")
                    message += f"Дата: {slide__day} {slide__month} ({slide__weekday_text})" + "\n"

                    times__item = driver.find_elements(By.CLASS_NAME, "times__item")
                    for time__item in times__item:
                        
                        times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
                        times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

                        print(f"Время: {times__time} - {times__amount}")
                        message += f"Время: {times__time} - {times__amount}" + "\n"

                    message += "\n"
        except NoSuchElementException:
            times__item = driver.find_elements(By.CLASS_NAME, "times__item")

            calendar_one_date = driver.find_element(By.CLASS_NAME, "calendar-one-date").text
            print(f"Дата: {calendar_one_date}")
            message += f"Дата: {calendar_one_date}" + "\n"

            for time__item in times__item:
                
                times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
                times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

                print(f"Время: {times__time} - {times__amount}")
                message += f"Время: {times__time} - {times__amount}" + "\n"     
        break

bot.send_message(chat_id=telegram_chat_id, text=message, disable_web_page_preview=False, parse_mode='Markdown')

driver.get(BASE_URL)

time.sleep(10)

events_content = driver.find_elements(By.CLASS_NAME, "events__content")
message = ""

for event_content in events_content:
    action__text = event_content.find_element(By.CLASS_NAME, "action__text").text
    if action__text in ["Билет с экскурсионным обслуживанием: дом Л.Н.Толстого, заповедник"]:
        buy__available = event_content.find_element(By.CLASS_NAME, "buy__available").text
        
        message += "*" + action__text + "*" + "\n"
        print(action__text)
        
        print(f"Всего билетов: {buy__available}")
        message += f"Всего билетов: {buy__available}" + "\n"

        buy__button = event_content.find_element(By.CLASS_NAME, "buy__button")
        buy__button.click()

        time.sleep(10)

        try:
            if driver.find_element(By.CLASS_NAME, "swiper-container") is not None:

                sliders = driver.find_elements(By.CLASS_NAME, "slide")
                for slider in sliders:
                    slider.click()
                    time.sleep(3)

                    slide__day = driver.find_element(By.CLASS_NAME, "slide__day").text
                    slide__month = driver.find_element(By.CLASS_NAME, "slide__month").text
                    slide__weekday_text = driver.find_element(By.CLASS_NAME, "slide__weekday-text").text

                    print(f"Дата: {slide__day} {slide__month} ({slide__weekday_text})")
                    message += f"Дата: {slide__day} {slide__month} ({slide__weekday_text})" + "\n"

                    times__item = driver.find_elements(By.CLASS_NAME, "times__item")
                    for time__item in times__item:
                        
                        times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
                        times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

                        print(f"Время: {times__time} - {times__amount}")
                        message += f"Время: {times__time} - {times__amount}" + "\n"
                    message += "\n"
                    
        except NoSuchElementException:
            times__item = driver.find_elements(By.CLASS_NAME, "times__item")

            calendar_one_date = driver.find_element(By.CLASS_NAME, "calendar-one-date").text
            print(f"Дата: {calendar_one_date}")
            message += f"Дата: {calendar_one_date}" + "\n"

            for time__item in times__item:
                
                times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
                times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

                print(f"Время: {times__time} - {times__amount}")
                message += f"Время: {times__time} - {times__amount}" + "\n"     
        break

bot.send_message(chat_id=telegram_chat_id, text=message, disable_web_page_preview=False, parse_mode='Markdown')
