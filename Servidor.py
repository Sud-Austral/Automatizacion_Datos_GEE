import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import http.client, urllib.request, urllib.parse, urllib.error, base64

enlace = "https://anin.users.earthengine.app/view/link"

def getDriver():
    
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    driver.get(enlace)
    return driver

def descargarDatos():
    driver = getDriver()
    time.sleep(5)
    
    nombre = "Link"
    
    links = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div")
    
    for i in range(len(links)):
        namefile = "Link" + str(i + 1)
        url = driver.find_element_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div[" + str(i+1) + "]/a")
        urllib.request.urlretrieve(url.text, "datos_geee/" + str(namefile) +".csv")
    
    driver.close()


if __name__ == '__main__':
    print("Descargando datos...")
    descargarDatos()
    print("Los datos se han descargado.")