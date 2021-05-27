import pandas as pd
import time
import glob
import numpy as np
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

enlace = "https://testhector.users.earthengine.app/view/climaautomatico"

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

def fechaA():
    date = datetime.now()
    date = date.strftime('%d-%m-%Y')
    return date



if __name__ == '__main__':
    print("Descargando datos...")
    
    descargarDatos()