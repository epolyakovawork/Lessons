from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    button1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    input1 = browser.find_element(By.ID, "answer")
    y = calc(x)
    input1.send_keys(y)    
    
# javascript
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
