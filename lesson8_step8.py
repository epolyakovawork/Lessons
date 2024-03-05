from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ekaterina")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Polyakova")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@123.ru")
    button1 = browser.find_element(By.ID, "file")
    #button1 = os.path.join(current_dir, 'test.txt')
    file_path = os.path.join(current_dir, 'test.txt')
    button1.send_keys(file_path)
    # получаем путь к директории текущего исполняемого файла 
    print(os.path.abspath(os.path.dirname(__file__)))
    print(file_path)
    # добавляем к этому пути имя файла 
    
    
    
# javascript
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
