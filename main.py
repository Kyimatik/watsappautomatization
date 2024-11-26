import webbrowser
from urllib.parse import quote 
import pyautogui
import time 
message = '''Привет , мы Адамар групп. Если тебе интересно чтобы мы помогли тебе с бесплатной консультацией , переходи пожалуйста по ссылке!
Номер для связи - 777
'''
safe_message = quote(message) # через urllib.parse испортируем quote , и делаем безопасный текст чтобы браузер не ругался 

phone_num = "+996550223324"



webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_num}&text={safe_message}") # Открываем сам браузер 

time.sleep(10) # ждем полной загрузки 

pyautogui.press("Enter") # Нажимаем кнопку энтер < то есть отправка самого сообщения 



