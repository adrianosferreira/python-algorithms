from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyfiglet import Figlet
import csv
f = Figlet(font='slant', width=80)
print(f.renderText('Corona Exporter'))
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://who.maps.arcgis.com/apps/opsdashboard/index.html#/bf48be9799364068be4706c56b1916f5')
driver.implicitly_wait(10)
els = driver.find_elements_by_xpath("//strong[contains(text(), 'Countries, areas or territories with cases')]/../../../../../div/nav/span/div/div/p")

outfile = open('./corona.csv', 'w')
writer = csv.writer(outfile)
writer.writerow(["Country", "Cases"])
items = []
for el in els:
    exploded = el.text.split(':')
    items.append([exploded[0].strip(), exploded[1].replace('cases', '').strip()])


writer.writerows(items)
