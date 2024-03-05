from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    browser.execute_script("window.scrollBy(0,100);")
    #browser.execute_script("return arguments[200].scrollIntoView(true);")
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    print(x)
    input1 = browser.find_element(By.ID, "answer")
    y = calc(x)
    print(y)
    input1.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    #browser.execute_script("return arguments[0].scrollIntoView(true);")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
