from selenium.webdriver.common.by import By
import navegador
import random

walletpai = "P1095567886"

sobresalentes = """
23.129.252.81:6349:nqpczzte:mkj1eruejzwi
23.129.254.132:6114:nqpczzte:mkj1eruejzwi
23.129.254.0:5982:nqpczzte:mkj1eruejzwi
45.157.125.83:5710:nqpczzte:mkj1eruejzwi
23.129.253.187:6805:nqpczzte:mkj1eruejzwi
185.72.242.14:5697:nqpczzte:mkj1eruejzwi
45.157.125.208:5835:nqpczzte:mkj1eruejzwi
185.72.242.167:5850:nqpczzte:mkj1eruejzwi
23.129.254.26:6008:nqpczzte:mkj1eruejzwi
23.129.254.92:6074:nqpczzte:mkj1eruejzwi
23.129.253.122:6740:nqpczzte:mkj1eruejzwi
23.129.254.112:6094:nqpczzte:mkj1eruejzwi
45.157.125.53:5680:nqpczzte:mkj1eruejzwi
23.129.253.140:6758:nqpczzte:mkj1eruejzwi
23.129.253.31:6649:nqpczzte:mkj1eruejzwi
23.129.254.169:6151:nqpczzte:mkj1eruejzwi
45.157.125.124:5751:nqpczzte:mkj1eruejzwi
185.72.242.252:5935:nqpczzte:mkj1eruejzwi
185.72.242.170:5853:nqpczzte:mkj1eruejzwi"""


contas = [
    {'login': 'lucassantosvsc13p1', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1103.157 Safari/537.36',      'proxy': '23.129.252.94:6362:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096107918'},
    {'login': 'lanceluc',           'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1103.157 Safari/537.36',                                                  'proxy': '45.157.126.127:6083:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096309916'},
    {'login': 'eujogodeyorick',     'userAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.157 Safari/537.36',                     'proxy': '45.157.126.244:6200:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310229'},
    {'login': 'capivarias',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2454.85 Safari/537.36',   'proxy': '185.72.242.5:5688:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310439'},
    {'login': 'xulianinho',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2403.157 Safari/537.36',   'proxy': '45.157.125.165:5792:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096379412'},
    {'login': 'luisacba98',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2454.85 Safari/537.36',    'proxy': '185.72.242.101:5784:nqpczzte:mkj1eruejzwi',   'wallet': 'P1100016574'}, 
    {'login': 'joaopitao2',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2454.85 Safari/537.36',       'proxy': '45.157.126.164:6120:nqpczzte:mkj1eruejzwi',  'wallet': 'P1100016633'},
    {'login': 'dragodianode',       'userAgent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.155 Safari/537.36',               'proxy': '185.72.242.69:5752:nqpczzte:mkj1eruejzwi',  'wallet': 'P1100016658'}
     ]

criarConta = [
    
]

criando = False

uso = 1

if criando == False:
    if uso == 1:
        while True:
            for conta in contas:
                try:
                    nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
                    nav.fazerLogin()
                except:
                    pass

    if uso == 2:
        conta = contas[4]
        nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
        nav.fazerLogin()

    if uso == 3:
        conta = contas[1]
        nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
        nav.somenteLogin()

else:
    conta = criarConta[4]
    nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
    nav.somenteAbrir((random.choice(contas))['login'])