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

def descargarDatos():

    driver = getDriver()

    while (exist == 0):
        enlace = driver.find_elements_by_xpath("/html/body/main/div/div[1]/div/div/div/div/div/div/div[4]/div/div/div/a")
        # time.sleep(1)

        if (len(enlace) == 0):
            exist = 0
            time.sleep(60)
        else:
            exist = 1

    
    for i in range(len(enlace)):
        
        namefile = str(i+1) + ". Clima " +  fechaA()
        print(enlace[i].text)
        
        df = pd.read_csv(enlace[i].text)

        df["Fecha actual"] = fechaA()
        del df["system:index"]
        del df["COMUNA"]
        del df["Malla16k"]
        del df["Malla1k"]
        del df["Malla2k"]
        del df["Malla4k"]
        del df["Malla8k"]
        del df["NOM_COMUNA"]
        del df["NOM_PROVIN"]
        del df["NOM_REGION"]
        del df["PROVINCIA"]
        del df["REGION"]
        del df["latitude"]
        del df["longitude"]
        del df[".geo"]

        df.to_excel("Clima/"  + str(namefile) +".xlsx", index=False)

    driver.close()

def unificar():
    file = "Clima/*.xlsx"
    files = glob.glob(file)

    archivos = np.array(files)
    final = "Clima/Consolidado.csv"
    
    df_inicial = pd.read_csv(final)
    df_inicial
    
    _df = df_inicial[df_inicial["Fecha actual"] == ""]
    _df.to_csv("Clima/Consolidado.csv", index=False)

    for i in range(len(files)):
        df_inicial = pd.read_csv(final)
        df_inicial

        if(str(archivos[i])!=final):
            df = pd.read_excel(archivos[i])

            n = df_inicial.append([df])
            n.to_csv(final, index=False)

if __name__ == '__main__':
    print("Descargando datos...")

    descargarDatos()
    unificar()

    print("Los datos se han descargado")