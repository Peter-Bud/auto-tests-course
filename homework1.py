from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input0 = browser.find_element_by_id('#input_value')


    input01 = browser.find_element_by_id('num2')

    z=int(input0.text) + int(input01.text)
    print(z)

    select = browser.find_element_by_id("dropdown").click()

    select1 = browser.find_element_by_css_selector("[value='" + str(z) + "']").click()

    #select.select_by_value()


    # Отправляем заполненную форму
    input4 = browser.find_element_by_css_selector('.btn')
    input4.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()