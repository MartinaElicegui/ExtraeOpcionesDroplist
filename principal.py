from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import *
from selenium import webdriver
from random import randint
from time import sleep
from easygui import *
import os
import codecs

rutaDriver = os.path.join(os.getcwd(),"chromedriver")
driver = webdriver.Chrome(rutaDriver, chrome_options=Options()) 
Options().add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36")

driver.get('https://sisfe.justiciasantafe.gov.ar/login-matriculado')
driver.maximize_window()
botonIngresar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@id="ingresar"]'))
            )
informacion = codecs.open("datos.csv","r")
count = 0
while True:
    count += 1
    linea = informacion.readline()

    if (len(linea) == 0):
        break
    else:
        datosIngreso = linea.split(',')
        circunscripcion = datosIngreso[0]
        matricula = datosIngreso[2]
        contraseña = datosIngreso[3]

        elementoCircunscripcion = driver.find_element_by_id("circunscripcion")
        elementoCircunscripcion.send_keys(circunscripcion)
        elementoColegio = driver.find_element_by_id("colegio")
        objetoColegio = Select(elementoColegio)
        objetoColegio.select_by_visible_text("Abogados")
        textAreaMatricula = driver.find_element_by_id("matricula")
        textAreaMatricula.send_keys(matricula)
        textAreaContraseña = driver.find_element_by_id("password")
        textAreaContraseña.send_keys(contraseña)
        # input("Complete el captcha y presione enter para continuar")
        msgbox("Complete el captcha. Cuando termine, presione OK para continuar.")
        
        botonIngresar.click()

    sleep(10)
    
    organismo = driver.find_element_by_id("organismo")
    msgbox("Seleccione la localidad")
    d = Select(organismo)
    for opt in d.options:
        print(opt.text)
    input("Fin de la ejecución")



