import pandas as pd
import shutil
import time
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

    exist = 0

    while (exist == 0):
        enlace = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div/a")
        # time.sleep(1)

        if (len(enlace) == 0):
            exist = 0
            time.sleep(60)
        else:
            exist = 1

    # print(len(enlace))

    # Generar directamente el consolidado, sin archivos.
    salida = []

    for i in range(len(enlace)):

        namefile = str(i+1) + ". Clima " +  fechaA()
        df = pd.read_csv(enlace[i].text)
        
        print(enlace[i].text)
        df = pd.read_csv(enlace[i].text)

        df["Fecha actual"] = fechaA()
        del df[".geo"]

        # df.to_excel("Clima/"  + str(namefile) +".xlsx", index=False)
        salida.append(df.copy())

    dataFinal = pd.concat(salida)
    dataFinal.to_excel("Clima/Clima " + str(fechaA()) +".xlsx", index=False)

    driver.close()

if __name__ == '__main__':
    print("Descargando datos...")
    descargarDatos()
    print("Los datos se han descargado")