from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()
assert 'Selenium Easy Demo' in chrome_browser.title
close_popup = chrome_browser.find_element_by_id('at-cv-lightbox-close').click()
text_box = chrome_browser.find_element_by_id('sum1').send_keys('5')
text_box = chrome_browser.find_element_by_id('sum2').send_keys('5')
send_btn = chrome_browser.find_element_by_xpath('//*[@id="gettotal"]/button').click()
answer = chrome_browser.find_element_by_id('displayvalue').text
print(f'answer is {answer}')
chrome_browser.close()
