# Controlling browser with selenuium module
# Clicking the page

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click() 
# follows the "Read It Online" link