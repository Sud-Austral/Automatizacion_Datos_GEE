import pandas as pd
import time
import os
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

enlace = "https://app-data-i.users.earthengine.app/view/climaauto"

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

def descargarDatos():
    

    driver = getDriver()
    time.sleep(30)

    links = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/a")
    namefile = "Clima " +  fechaA()
    df = pd.read_csv(links[0].text)
    df["Fecha actual"] = fechaA()
    del df[".geo"]
    df.to_csv("Clima/"  + str(namefile) +".csv", index=False)

    """
    for i in range(len(links)):
        namefile = "Link" + str(i + 1)
        url = driver.find_element_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div[" + str(i+1) + "]/a")
        df = pd.read_csv(url.text)
        df["Fecha actual"] = fechaA()
        del df[".geo"]
        df.to_csv("datos_gee/" + ruta + "/" + str(namefile) +".csv", index=False)
    """
    driver.close()

if __name__ == '__main__':
    print("Descargando datos...")
    descargarDatos()
    print("Los datos se han descargado")