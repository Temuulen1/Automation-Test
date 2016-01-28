import time
from selenium import webdriver

print ('Checking to see if maximum digit input of calculator is 16')


browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

digitElem = browser.find_element_by_name('one')
digitElem.click()

digitElem = browser.find_element_by_name('two')
digitElem.click()
digitElem = browser.find_element_by_name('three')
digitElem.click()
digitElem = browser.find_element_by_name('four')
digitElem.click()
digitElem = browser.find_element_by_name('five')
digitElem.click()
digitElem = browser.find_element_by_name('six')
digitElem.click()
digitElem = browser.find_element_by_name('seven')
digitElem.click()
digitElem = browser.find_element_by_name('eight')
digitElem.click()
digitElem = browser.find_element_by_name('nine')
digitElem.click()
digitElem = browser.find_element_by_name('zero')
digitElem.click()
digitElem = browser.find_element_by_name('one')
digitElem.click()
digitElem = browser.find_element_by_name('two')
digitElem.click()
digitElem = browser.find_element_by_name('three')
digitElem.click()
digitElem = browser.find_element_by_name('four')
digitElem.click()
digitElem = browser.find_element_by_name('five')
digitElem.click()
digitElem = browser.find_element_by_name('six')
digitElem.click()
digitElem = browser.find_element_by_name('seven')
digitElem.click()
digitElem = browser.find_element_by_name('eight')
digitElem.click()

inputElem = browser.find_element_by_name('Input')
inputElem.click()
inputElem.get_attribute('value')

numbers = (inputElem.get_attribute('value'))

print('There were %s numbers numbers numbers in the input box.' % (len(numbers)))

if len(numbers) > 16:
	print ('Failed. It is more than 16')






