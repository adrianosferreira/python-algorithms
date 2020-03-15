from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import pdfplumber

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports')
el = driver.find_element_by_xpath("//div[contains(@class, 'sf-content-block')]/div/p[1]/strong/a")
r = requests.get(el.get_attribute('href'))
open('report.pdf', 'wb').write(r.content)
test = pdfplumber.open('report.pdf')
tables = test.pages[2].extract_table()

import pandas as pd
df = pd.DataFrame(tables[1:], columns=tables[0])
print(df)