from selenium.webdriver.common.by import By
import navegador
import random




contas = [
    {'login': 'lucassantosvsc13p1', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10',      'proxy': '185.72.242.148:5831:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096107918'},
    {'login': 'lanceluc',           'userAgent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko',                                                  'proxy': '45.157.126.168:6124:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096309916'},
    {'login': 'eujogodeyorick',     'userAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.157 Safari/537.36',                     'proxy': '23.129.254.197:6179:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310229'},
    {'login': 'capivarias',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2454.85 Safari/537.36',   'proxy': '23.129.252.39:6307:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310439'},
    {'login': 'xulianinho',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.157 Safari/537.36',   'proxy': '23.129.254.105:6087:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096379412'},
    {'login': 'luisacba98',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2454.85 Safari/537.36',    'proxy': '45.157.126.70:6026:nqpczzte:mkj1eruejzwi',   'wallet': ''}, 
    {'login': 'joaopitao2',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/7.1.4 Safari/537.85.13',       'proxy': '45.157.125.154:5781:nqpczzte:mkj1eruejzwi',  'wallet': ''},
    {'login': 'dragodianode',       'userAgent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.155 Safari/537.36',               'proxy': '45.157.126.223:6179:nqpczzte:mkj1eruejzwi',  'wallet': ''}
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
                    nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'])
                    nav.fazerLogin()
                except:
                    pass

    if uso == 2:
        conta = contas[4]
        nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'])
        nav.fazerLogin()

    if uso == 3:
        conta = contas[-1]
        nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'])
        nav.somenteLogin()

else:
    conta = criarConta[4]
    nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'])
    nav.somenteAbrir((random.choice(contas))['login'])