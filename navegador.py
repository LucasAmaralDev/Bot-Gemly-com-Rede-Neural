from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import os
import zipfile
from selenium import webdriver
from time import sleep
import base64
from PIL import Image
import numpy as np
import keras
import cv2
import pickle
from Controller.navegadorComandos import *

train_data = np.load('train_data.npy')
train_labels = np.load('train_labels.npy')
# Carregar o modelo treinado salvo
model = keras.models.load_model('modelo_treinado.h5')



class Navegador:
    def __init__(self,login, userAgent, proxyUser, wallet):
        proxyUser = proxyUser.split(":")
        self.login = login
        self.continuar = False
        self.reinvestir = False
        self.wallet = wallet
        PROXY_HOST = proxyUser[0]  # rotating proxy or host
        PROXY_PORT = proxyUser[1] # port
        PROXY_USER = proxyUser[2] # username
        PROXY_PASS = proxyUser[3] # password
        manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
        background_js = """
        var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_driver_path = "/usr/local/bin/chromedriver"
        # Configurando as opções do Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_extension(pluginfile)
        chrome_options.add_extension('cp.zip')
        # Configurando o serviço do ChromeDriver
        service = webdriver.chrome.service.Service(chrome_driver_path)
        # Criando a instância do driver do Chrome
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        # Abrindo o Google Chrome
        self.driver.set_window_size(500, 950)
        stealth(
            self.driver,
            user_agent=userAgent,
            languages=["pt-BR", "pt"],
            vendor="Amazon Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        self.driver.set_page_load_timeout(8)

    def salvarCookies(self):
        if not os.path.exists('cookies'):
            os.makedirs('cookies')
        #entrando no site gemly
        cookies = self.driver.get_cookies()
        cookies_array = np.array(cookies)
        with open(f'./cookies/{self.login}.pkl', 'wb') as file:
            pickle.dump(cookies_array, file)
        sleep(1)

    def carregarCookies(self):
        try:
            with open(f'./cookies/{self.login}.pkl', 'rb') as file:
                cookies_array = pickle.load(file)
            for cookie in cookies_array:
                self.driver.add_cookie(cookie)
            self.driver.get("https://gemly.gg/account")
        except:
            return
        
    def somenteAbrir(self, indicado):
        print(indicado)
        self.driver.get(f"https://gemly.gg/?r={indicado}")

    def somenteLogin(self):
        self.driver.get("https://gemly.gg/account")
        self.carregarCookies()
        if self.driver.current_url == 'https://gemly.gg/account':
            print("Login com Cookie realizado com sucesso!")
        else:
            try:
                os.remove(f'./cookies/{self.login}.pkl')
            except:
                pass
            sleep(1)

            #Inserir o "self.login" no input de email
            inserir_email = inserir_name_texto(self.driver, 'login-email', self.login)
            if inserir_email == False:
                return False
            sleep(1)
            #Inserir a senha no input de senha
            inserir_senha = inserir_name_texto(self.driver, 'password', "@Luc97ari\n")
            if inserir_senha == False:
                return False
            sleep(1)

            #Verificar se o input de email está com o valor do self.login
            while True:
                try:
                    if input_email.get_attribute('value') == self.login:
                        sleep(3)
                    else:
                        break
                except:
                    break

            #Verificar se o login foi realizado com sucesso
            if self.driver.current_url == 'https://gemly.gg/account':
                print("Login realizado com sucesso!")


    def fazerLogin(self):
        self.driver.get("https://gemly.gg/account")
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.carregarCookies()
        if self.driver.current_url == 'https://gemly.gg/account':
            print("Login com Cookie realizado com sucesso!")
        else:
            try:
                os.remove(f'./cookies/{self.login}.pkl')
            except:
                pass
            sleep(1)
            #Inserir o "self.login" no input de email


            inserir_email = inserir_name_texto(self.driver, 'login-email', self.login)
            if inserir_email == False:
                return False
            sleep(1)
            #Inserir a senha no input de senha
            inserir_senha = inserir_name_texto(self.driver, 'password', "@Luc97ari\n")
            if inserir_senha == False:
                return False
            sleep(1)

            while True:
                try:
                    if "https://gemly.gg/auth" in self.driver.current_url:
                        sleep(3)
                    else:
                        break
                except:
                    break
            if self.driver.current_url == 'https://gemly.gg/account':
                print("Login realizado com sucesso!")
                self.salvarCookies()
            else:
                return
        self.procurarAcoes()
    

        
    def verBalanco(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(1)
        print('Vendo Balanco')
        try:
            div = self.driver.find_element(By.CLASS_NAME, 'amount')
            div = div.get_attribute('innerHTML')
            div = div.split("Seu saldo atual:</span><span class=\'value\'>")[1]
            saldo = int((div.split("</span>")[0]).replace(" ", ""))
        except:
            return
        if saldo > 15000:
                if self.driver.current_url != 'https://gemly.gg/game':
                    self.driver.get('https://gemly.gg/game')
                    sleep(3)
                divBuy = self.driver.find_element(By.CLASS_NAME, 'item--info')
                divBuy.click()
                sleep(2)
                self.driver.find_element(By.CLASS_NAME, 'collect').click()
                sleep(1)
        if self.reinvestir == False:
            if saldo > 63000:

                #mudar para a primeira aba
                self.driver.switch_to.window(self.driver.window_handles[0])
                
                #Clicar no elemento que contem o name com o valor "mobile-trigger"
                clicar_mobile_trigger = clicar_classname_sem_texto(self.driver, 'mobile-trigger')
                if clicar_mobile_trigger == False:
                    return False
                sleep(1)


                #clicar na div com o classname "title" e o texto "Finanças"
                clicar_financas = clicar_tagname_texto_class(self.driver, 'div', 'Finanças', 'title')
                if clicar_financas == False:
                    return False
                
                #clicar na tagname a com o texto "Saque"
                clicar_saque = clicar_tagname_texto(self.driver, 'a', 'Saque')
                if clicar_saque == False:
                    return False
                sleep(3)
                
                #clicar na div com o classname "item" e o data-path="rub"
                elemento_moedas = self.driver.find_element(By.CLASS_NAME, 'currency')
                elementodiv = elemento_moedas.find_elements(By.TAG_NAME, 'div')
                for elemento in elementodiv:
                    try:
                        if elemento.get_attribute('data-path') == 'rub' and elemento.get_attribute('class') == 'item':
                                elemento.click()
                                break
                    except:pass
                
                #procurando pelo tagname input com o nome="wallet" e e setando o valor dele para self.wallet
                inserir_wallet = inserir_tagname_atribute(self.driver, 'input', 'name', 'wallet', self.wallet)
                if inserir_wallet == False:
                    return False
                sleep(1)

                #procurar pelo button com o texto 'Fazer pagamento'
                elementbutton = self.driver.find_elements(By.TAG_NAME, 'button')
                for element in elementbutton:
                    if element.text == 'FAZER PAGAMENTO':
                        element.click()
                        break
                sleep(1)

                #salvar na ultima linha do arquivo 'pagamentos.txt' o self.login e o valor saldo
                with open('pagamentos.txt', 'a') as f:
                    f.write(self.login + " " + str(saldo) + " " + self.wallet + "\n")
                sleep(2)
                print("Pagamento realizado com sucesso!")
        else:
            while saldo > 15000:
                if self.driver.current_url != 'https://gemly.gg/game':
                    self.driver.get('https://gemly.gg/game')
                    sleep(3)
                divBuy = self.driver.find_element(By.CLASS_NAME, 'unit--number-4')
                try:
                    botao = divBuy.find_element(By.CLASS_NAME, 'buy')
                    sleep(1)
                    botao.click()
                    saldo -= 15000
                except:
                    pass
                                



    def procurarAcoes(self):
        self.fecharOutrasAbas()
        self.driver.switch_to.window(self.driver.window_handles[0])
        if self.driver.current_url != 'https://gemly.gg/surf':
            self.driver.get('https://gemly.gg/surf')
        sleep(1)
        # Procurando os anuncios e verificando se clickou
        adsClick = False
        elementAds = self.driver.find_elements(By.TAG_NAME, 'a')
        for e in elementAds:
            try:
                if e.text == 'ASSISTIR' or e.text == 'WATCH':
                    e.click()
                    adsClick = True
                    self.continuar = True
                    self.executandoAcao()
                    break
            except:pass
        if adsClick == True:
            self.procurarAcoes()
            pass
        elif self.continuar == True:
            sleep(20)
            self.driver.refresh()
            self.continuar = False
            self.procurarAcoes()

        else:
            self.verBalanco()
            self.driver.close()
            pass


    def fecharOutrasAbas(self):
        while True:
            try:
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.driver.close()
            except:
                break

    def executandoAcao(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        #Verfificando o tempo de espera
        cronometro = 0
        while True:
            try:
                tempo = int(self.driver.find_element(By.CLASS_NAME, 'counter').get_attribute('innerHTML')) + 1
                print(f'TEMPO DE ESPERA É {tempo}')
                break
            except:pass
            sleep(1)
            cronometro += 1
            if cronometro > 10:
                print('Tempo limite atingido!')
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                return
        sleep(tempo)
        self.verificarCaptcha()

    def baixar_imagem(self,div_captcha):
        imagem = div_captcha.find_element(By.TAG_NAME, 'img')
        image_base64 = self.driver.execute_script("return arguments[0].src.split(',')[1];", imagem)
        image_bytes = base64.b64decode(image_base64)
        with open("imagem.gif", "wb") as f:
            f.write(image_bytes)
        folder_path = './'
        for filename in os.listdir(folder_path):
            if filename.endswith('.gif'):
                file_path = os.path.join(folder_path, filename)
                with Image.open(file_path) as im:
                    im.convert('RGB').save(file_path.replace('.gif', '.jpg'))
                os.remove(file_path)


        # 
    
    def verificarCaptcha(self):
        contador = 0
        while True:
            sleep(2)
            contador += 1
            div_captcha = self.driver.find_element(By.CLASS_NAME, 'cell--captcha')
            self.baixar_imagem(div_captcha)
            numero = self.preverCaptcha()
            value = div_captcha.find_element(By.CLASS_NAME, 'value')
            opcoes = value.find_elements(By.CLASS_NAME, 'option')
            clicou = 0
            for item in opcoes:
                try:
                    if item.text == str(numero):
                        item.click()
                        clicou = 1
                        break
                except:
                    pass
            if clicou == 1:
                sleep(2)
                if 'https://gemly.gg' not in self.driver.current_url:
                    self.driver.close()
                    return
            else:
                if contador != 3:
                    value.find_element(By.CLASS_NAME, 'img').click()
                else:
                    sleep(4)
                    self.driver.refresh()
                    self.executandoAcao()
                    return  
    
    def preverCaptcha(self):
        new_image = cv2.imread('imagem.jpg', cv2.IMREAD_GRAYSCALE)
        prediction = model.predict(np.array([new_image]))
        predicted_label = np.argmax(prediction)
        os.remove('imagem.jpg')
        print("Captcha Previsto:", predicted_label)
        return predicted_label



