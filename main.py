from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

# Список номеров
phone_numbers = ["+996550223324", "+324322", "+43242432"]  # Добавь свои номера сюда

message = '''Привет , мы Адамар групп. Если тебе интересно чтобы мы помогли тебе с бесплатной консультацией , переходи пожалуйста по ссылке!
Номер для связи - 777
'''
safe_message = quote(message)  # Безопасный текст для URL

# Функция для создания настроек Chrome
def create_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options

# Инициализация драйвера
chrome_options = create_chrome_options()
driver = webdriver.Chrome(options=chrome_options)
phone_num = "+996550223324"


driver.get("https://web.whatsapp.com")

# Проверяем вход в WhatsApp Web
try:
    print("Проверяем вход в WhatsApp Web...")
    # Ждем появления заголовка "Скачайте WhatsApp для Windows"
    WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class="_al_e" and text()="Скачайте WhatsApp для Windows"]'))
    )
    print("Вход в WhatsApp Web выполнен. Начинаем рассылку.")
except:
    print("Не удалось подтвердить вход. Убедитесь, что вы вошли через QR-код.")
    driver.quit()
    exit()

# Обработка номеров
for phone_num in phone_numbers:
    try:
        # Открытие WhatsApp Web с номером и текстом
        url = f"https://web.whatsapp.com/send?phone={phone_num}&text={safe_message}"
        driver.get(url)
        # Проверяем, загрузился ли интерфейс для отправки сообщения
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))
            )
        except:
            print(f"Сообщение для номера {phone_num} не готово. Возможно, проблема с номером.")
            continue
        
        # Проверка на недействительный номер
        try:

            invalid_message = driver.find_element(By.CLASS_NAME, "x12lqup9.x1o1kx08")
            if "Номер телефона, отправленный по ссылке, недействительный" in invalid_message.text:
                print(f"Номер {phone_num} недействительный. Нужно позвонить лично.")
                continue  # Переходим к следующему номеру
        except:
            print(f"Номер {phone_num} действителен.")
        
        # Ожидание появления кнопки отправки сообщения
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()  # Нажатие кнопки "Отправить"
        print(f"Сообщение отправлено на номер {phone_num}.")
        
        time.sleep(5)  # Ждем отправки сообщения
        
        # Открытие новой вкладки
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])  # Переключение на новую вкладку
        
        # Закрытие предыдущей вкладки
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
    
    except Exception as e:
        print(f"Произошла ошибка с номером {phone_num}: {e}")


# Завершаем работу драйвера
driver.quit()


# Пусть пока решение чтобы не закрывалось окно было time.sleep(10000) , таска на завтра приехать , сделать чтобы он закрывал лучше первый wats и каждый раз перезаходил 
# если там выходит нету такого номер записываем его в определенное место можно даже в txt файл , если все успешно тогда идем дальше и все!
