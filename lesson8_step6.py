from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    print(x)
    input1 = browser.find_element(By.ID, "answer")
    y = calc(x)
    print(y)
    input1.send_keys(y)
    #browser.execute_script("window.scrollBy(0,100);")
    browser.execute_script("return arguments[100].scrollIntoView(true);")
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    
    
# javascript
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
