import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



def test_met_feet():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Allot\\task_C\\chromedriver.exe', options=options)
    driver.get("https://www.metric-conversions.org/length/meters-to-feet.htm")
    element = driver.find_element_by_id('argumentConv')
    m = 100.6
    element.send_keys(str(m))
    select = Select(driver.find_element_by_id('format'))
    select.select_by_index(1)
    result = driver.find_element_by_id('answer').get_attribute('textContent')
    result = re.findall(r'[^a-z= ]+', result)[1]
    digits_for_round = len(str(re.split(r'\.', result)[1]))
    expected_result = round((m * 3.28084), digits_for_round)  # 1m = 3.28084 ft
    assert float(result) == expected_result
    driver.close()

