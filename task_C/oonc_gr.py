import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def test_oonc_gr():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\Desktop\\Allot\\task_C\\chromedriver.exe', options=options)
    driver.get("https://www.metric-conversions.org/weight/ounces-to-grams.htm")
    element = driver.find_element_by_id('argumentConv')
    oonc = 12.6
    element.send_keys(str(oonc))
    result = driver.find_element_by_id('answer').get_attribute('textContent')
    result = re.findall(r'[^a-z= ]+', result)[1]
    digits_for_round = len(str(re.split(r'\.', result)[1]))
    expected_result = round((oonc / 0.03527396), digits_for_round)  # 1g = 0.03527396oz
    assert float(result) == expected_result
    driver.close()

