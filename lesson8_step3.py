from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def sum(x,y):
    return str(x+y)


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    x_el = browser.find_element(By.ID, "num1")
    x = x_el.text
    y_el = browser.find_element(By.ID, "num2")
    y = y_el.text
    print(str(x))
    print(str(y))
    s = sum(int(x),int(y))
    print(str(s))
    
    browser.find_element(By.ID, "dropdown").click()
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s)) 
    
   
    btn = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
