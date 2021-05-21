import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_cels_fahr():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Allot\\task_C\\chromedriver.exe', options=options)
    driver.get("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")
    element = driver.find_element_by_id('argumentConv')
    cels = 100.88
    element.send_keys(str(cels))
    result = driver.find_element_by_id('answer').get_attribute('textContent')
    result = re.findall(r'\w+.\w+', result)[1]
    digits_for_round = len(str(re.split(r'\.', result)[1]))
    expected_result = round((cels * 1.8 + 32), digits_for_round) 
    assert float(result) == expected_result
    driver.close()








