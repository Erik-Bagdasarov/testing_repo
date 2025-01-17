from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Настройка веб-драйвера (например, Chrome)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Открыть веб-сайт
driver.get("https://example.com")

# Эмулировать сочетание клавиш для открытия консоли разработчика
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('i').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()

# Добавьте паузу, чтобы убедиться, что консоль открылась
import time
time.sleep(5)

# Закрыть браузер
driver.quit()
