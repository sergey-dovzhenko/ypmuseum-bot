# import os
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
# import time

telegram_bot_key = "8127384745:AAH9Ce83P1lYegIOrRlW261g4YVvl9WXKyg"
telegram_chat_id = "-1003192948647"

bot = telebot.TeleBot(telegram_bot_key)

# Настройки браузера
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

BASE_URL = "https://ypmuseum.tn-cloud.ru/?id=1&sid=43"

def wait_for_element(by, value, timeout=10):
    """Ожидаем появления элемента"""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


def parse_event(event_name: str) -> str:
    driver.get(BASE_URL)
    wait_for_element(By.CLASS_NAME, "events__content")

    events_content = driver.find_elements(By.CLASS_NAME, "events__content")
    message = ""

    for event_content in events_content:
        try:
            action_text = event_content.find_element(By.CLASS_NAME, "action__text").text
        except NoSuchElementException:
            continue

        if action_text == event_name:
            available = event_content.find_element(By.CLASS_NAME, "buy__available").text

            message += f"<b>{action_text}</b>\n\n"
            message += f"Всего билетов: {available}\n\n"

            # Жмём кнопку купить
            event_content.find_element(By.CLASS_NAME, "buy__button").click()
            wait_for_element(By.CLASS_NAME, "times__item", timeout=15)

            try:
                if driver.find_elements(By.CLASS_NAME, "swiper-container"):
                    sliders = driver.find_elements(By.CLASS_NAME, "slide")
                    for slider in sliders:
                        driver.execute_script("arguments[0].scrollIntoView(true);", slider)
                        driver.execute_script("arguments[0].click();", slider)

                        WebDriverWait(driver, 5).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, "times__item"))
                        )

                        day = slider.find_element(By.CLASS_NAME, "slide__day").text
                        month = slider.find_element(By.CLASS_NAME, "slide__month").text
                        weekday = slider.find_element(By.CLASS_NAME, "slide__weekday-text").text
                        message += f"Дата: {day} {month} ({weekday})\n"

                        for t in driver.find_elements(By.CLASS_NAME, "times__item"):
                            time_ = t.find_element(By.CLASS_NAME, "times__time").text
                            amount = t.find_element(By.CLASS_NAME, "times__amount").text
                            message += f"Время: {time_} - {amount}\n"
                        message += "\n"
                else:
                    date = driver.find_element(By.CLASS_NAME, "calendar-one-date").text
                    message += f"Дата: {date}\n"

                    for t in driver.find_elements(By.CLASS_NAME, "times__item"):
                        time_ = t.find_element(By.CLASS_NAME, "times__time").text
                        amount = t.find_element(By.CLASS_NAME, "times__amount").text
                        message += f"Время: {time_} - {amount}\n"

            except Exception as e:
                message += f"⚠️ Ошибка: {e}\n"

            break
    return message



if __name__ == "__main__":
    events_to_check = [
        "Билет с экскурсионным обслуживанием по маршруту: Дом Толстого, Заповедник",
        "Билет с экскурсионным обслуживанием: дом Л.Н.Толстого, заповедник",
    ]

    for event in events_to_check:
        msg = parse_event(event)
        if msg:
            print(msg)
            bot.send_message(
                chat_id=telegram_chat_id,
                text=msg,
                disable_web_page_preview=True,
                parse_mode="Markdown"
            )

    driver.quit()
