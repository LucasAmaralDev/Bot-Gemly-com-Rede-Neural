from time import sleep
from selenium.webdriver.common.by import By





def inserir_name_texto(driver, name, texto):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.NAME, name)
            for elemento in elementos:
                elemento.send_keys(texto)
                return True
        except:pass
        contador += 1
        sleep(1)
    return False


def clicar_name_sem_texto(driver, name):
    contador = 0
    while contador < 10:
        try:
            elemento = driver.find_element(By.NAME, name)
            elemento.click()
            return True
        except:pass
        contador += 1
        sleep(1)
    return False


def clicar_classname_sem_texto(driver, classname):
    contador = 0
    while contador < 10:
        try:
            elemento = driver.find_element(By.CLASS_NAME, classname)
            elemento.click()
            return True
        except:pass
        contador += 1
        sleep(1)
    return False


def clicar_tagname_texto_class(driver, tagname, texto, classe):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.text == texto and elemento.get_attribute('class') == classe:
                    elemento.click()
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False


def clicar_tagname_texto(driver, tagname, texto):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.text == texto:
                    elemento.click()
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False

def clicar_tagname_texto_atribute(driver, tagname, texto, atributo, valor):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.text == texto and elemento.get_attribute(atributo) == valor:
                    elemento.click()
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False


def clicar_tagname_atribute(driver, tagname, atributo, valor):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.get_attribute(atributo) == valor:
                    elemento.click()
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False

def inserir_tagname_texto_atribute(driver, tagname, texto, atributo, valor):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.text == texto and elemento.get_attribute(atributo) == valor:
                    elemento.clear()
                    elemento.send_keys(texto)
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False


def inserir_tagname_atribute(driver, tagname, atributo, valor, texto):
    contador = 0
    while contador < 10:
        try:
            elementos = driver.find_elements(By.TAG_NAME, tagname)
            for elemento in elementos:
                if elemento.get_attribute(atributo) == valor:
                    elemento.clear()
                    elemento.send_keys(texto)
                    return True
        except:pass
        contador += 1
        sleep(1)
    return False