import os
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

# Настройки браузера
options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

BASE_URL = "https://ypmuseum.tn-cloud.ru/?id=1&sid=43"

driver.get(BASE_URL)

time.sleep(10)

events_content = driver.find_elements(By.CLASS_NAME, "events__content")

for event_content in events_content:
    action__text = event_content.find_element(By.CLASS_NAME, "action__text").text
    if action__text in ["Билет с экскурсионным обслуживанием по маршруту: Дом Толстого, Заповедник"]:
        buy__available = event_content.find_element(By.CLASS_NAME, "buy__available").text
        

        print(action__text)
        
        print(f"Всего билетов: {buy__available}")
        # message += f"Всего билетов: {buy__available}" + "\n"
        # message += "\n"

        buy__button = event_content.find_element(By.CLASS_NAME, "buy__button")
        buy__button.click()

        time.sleep(5)

        times__item  = driver.find_element(By.CLASS_NAME, "times__item")
        
        times__item.click()

        time.sleep(5)

        # payment-method-card payment-method-card--bank

        payment_method_card = driver.find_elements(By.CLASS_NAME, "payment-method-card")[1]
        payment_method_card.click()

        time.sleep(5)

        # minus-plus__btn minus-plus__btn--plus

        minus_plus__btn = driver.find_elements(By.CLASS_NAME, "minus-plus__btn")[1]
        minus_plus__btn.click()
        time.sleep(2)
        minus_plus__btn.click()
        time.sleep(2)
        minus_plus__btn.click()
        time.sleep(2)
        minus_plus__btn.click()
        time.sleep(10)


        # personal_data__input = driver.find_element(By.CLASS_NAME, "personal-data__input")

        datas = ['Иванов Иван Иванович','8 (917) 850-98-76','serjio_design@mail.ru','serjio_design@mail.ru']
        k =0 
        personal_data_groups = driver.find_elements(By.CLASS_NAME, "personal-data-group")
        for personal_data_group in personal_data_groups:
            input = personal_data_group.find_element(By.TAG_NAME, "input")
            input.send_keys(datas[k])
            time.sleep(5)
            k += 1
        

        custom_control_input = driver.find_elements(By.CLASS_NAME, "custom-control-input")[0]
        driver.execute_script("arguments[0].click();", custom_control_input) #.click()
        time.sleep(10)

        btn = driver.find_element(By.CLASS_NAME, "btn")
        btn.click()

        time.sleep(40)


        # try:
            # if driver.find_element(By.CLASS_NAME, "swiper-container") is not None:

                # sliders = driver.find_elements(By.CLASS_NAME, "slide")

                # print(sliders)
                # for slider in sliders:
                    
                    
                #     # slider.click()
                #     driver.execute_script("arguments[0].click();", slider)
        
                #     time.sleep(3)

                #     slide__day = slider.find_element(By.CLASS_NAME, "slide__day").text
                #     slide__month = slider.find_element(By.CLASS_NAME, "slide__month").text
                #     slide__weekday_text = slider.find_element(By.CLASS_NAME, "slide__weekday-text").text

                #     print(f"Дата: {slide__day} {slide__month} ({slide__weekday_text})")
                #     message += f"Дата: {slide__day} {slide__month} ({slide__weekday_text})" + "\n"

                #     times__item = driver.find_elements(By.CLASS_NAME, "times__item")
                #     for time__item in times__item:
                        
                #         times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
                #         times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

                #         print(f"Время: {times__time} - {times__amount}")
                #         message += f"Время: {times__time} - {times__amount}" + "\n"

                #     message += "\n"
        # except NoSuchElementException:
            # print("")
            # times__item = driver.find_elements(By.CLASS_NAME, "times__item")

            # calendar_one_date = driver.find_element(By.CLASS_NAME, "calendar-one-date").text
            # print(f"Дата: {calendar_one_date}")
            # message += f"Дата: {calendar_one_date}" + "\n"

            # for time__item in times__item:
                
            #     times__time = time__item.find_element(By.CLASS_NAME, "times__time").text
            #     times__amount = time__item.find_element(By.CLASS_NAME, "times__amount").text

            #     print(f"Время: {times__time} - {times__amount}")
            #     message += f"Время: {times__time} - {times__amount}" + "\n"     
        break