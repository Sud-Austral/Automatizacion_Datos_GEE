import pandas as pd
import time
import os
import shutil
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

def descargarDatos():
    
    driver = getDriver()
    # time.sleep(200)

    exist = 0

    while(exist == 0):
        try:
            links = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/a")
            exist = 1
        except:
            exist = 0
            print("No se han encontrado enlaces.")
            time.sleep(60)

    if (exist == 1):
        for i in range(len(links)):
            namefile = "Clima " +  fechaA()
            print(links[i].text)
            df = pd.read_csv(links[i].text)

        '''df["Fecha actual"] = fechaA()
            del df[".geo"]
            df.to_csv("Clima/"  + str(namefile) +".xlsx", index=False)'''

        driver.close()
    
    else:
        pass
if __name__ == '__main__':
    print("Descargando datos...")
    descargarDatos()
    print("Los datos se han descargado.")