from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

message = '''Привет , мы Адамар групп. Если тебе интересно чтобы мы помогли тебе с бесплатной консультацией , переходи пожалуйста по ссылке!
Номер для связи - 777
'''
safe_message = quote(message)  # безопасный текст для URL

phone_num = "+996550223324"

# Функция для создания настроек Chrome
def create_chrome_options():
    chrome_options = Options()
    
    # Добавляем параметры для Chrome
    chrome_options.add_argument("--disable-extensions")  # Отключение расширений
    chrome_options.add_argument("--disable-gpu")  # Отключение GPU ускорения
    chrome_options.add_argument("--no-sandbox")  # Отключение песочницы (для Linux)
    chrome_options.add_argument("--start-maximized")  # Открывать окно браузера на весь экран
    chrome_options.add_argument("--disable-infobars")  # Отключение информационных панелей
    chrome_options.add_argument("--disable-dev-shm-usage")  # Используется для улучшения производительности в Docker
    chrome_options.add_argument("--keep-alive")  # Сохранение сессии (если нужно)
    
    return chrome_options   



# Инициализация драйвера
chrome_options = create_chrome_options()

# Запуск Chrome с заданными параметрами
driver = webdriver.Chrome(options=chrome_options)



# Открытие WhatsApp Web с номером и текстом
url = f"https://web.whatsapp.com/send?phone={phone_num}&text={safe_message}"
driver.get(url)

time.sleep(100000000)


# Пусть пока решение чтобы не закрывалось окно было time.sleep(10000) , таска на завтра приехать , сделать чтобы он закрывал лучше первый wats и каждый раз перезаходил 
# если там выходит нету такого номер записываем его в определенное место можно даже в txt файл , если все успешно тогда идем дальше и все!
