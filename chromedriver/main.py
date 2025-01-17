from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройка Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме (необязательно)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")

# Установка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открытие страницы
    driver.get("https://www.bayut.com/property/details-7999436.html")

    # Дождитесь загрузки (если необходимо)
    driver.implicitly_wait(10)

    # Получение cookies
    cookies = driver.get_cookies()

    # Вывод cookies
    # for cookie in cookies:
    #     print(f"{cookie['name']}: {cookie['value']}")

finally:
    driver.quit()
