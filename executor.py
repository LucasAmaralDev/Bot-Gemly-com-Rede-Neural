from selenium.webdriver.common.by import By
import navegador
import random

walletpai = "P1095567886"

sobresalentes = """

















185.72.242.252:5935:nqpczzte:mkj1eruejzwi
185.72.242.170:5853:nqpczzte:mkj1eruejzwi"""


contas2 = [
    {'login': 'lucassantosvsc13p1', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1103.157 Safari/537.36',   'proxy': '23.129.252.94:6362:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096107918'},
    {'login': 'lanceluc',           'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1103.157 Safari/537.36',   'proxy': '45.157.126.127:6083:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096309916'},
    {'login': 'eujogodeyorick',     'userAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.157 Safari/537.36',                     'proxy': '45.157.126.244:6200:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310229'},
    {'login': 'capivarias',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2454.85 Safari/537.36',   'proxy': '185.72.242.5:5688:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096310439'},
    {'login': 'xulianinho',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2403.157 Safari/537.36',   'proxy': '45.157.125.165:5792:nqpczzte:mkj1eruejzwi', 'wallet': 'P1096379412'},
    {'login': 'luisacba98',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2454.85 Safari/537.36',   'proxy': '185.72.242.101:5784:nqpczzte:mkj1eruejzwi',   'wallet': 'P1100016574'}, 
    {'login': 'joaopitao2',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2454.85 Safari/537.36',   'proxy': '45.157.126.164:6120:nqpczzte:mkj1eruejzwi',  'wallet': 'P1100016633'},
    {'login': 'dragodianode',       'userAgent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2403.155 Safari/537.36',              'proxy': '185.72.242.69:5752:nqpczzte:mkj1eruejzwi',  'wallet': 'P1100016658'},
    {'login':"caninrodil",          'userAgent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2403.155 Safari/537.36',              'proxy':'23.129.252.81:6349:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100149666'},
    {'login':'aicarlycaal',         'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2403.157 Safari/537.36',   'proxy':'23.129.254.132:6114:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100153693'},
    {'login':'virgilxinigami',      'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2403.157 Safari/537.36',  'proxy':'23.129.254.0:5982:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100153998'},
    {'login':'acracatulika',        'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2484.85 Safari/537.36',   'proxy':'45.157.125.83:5710:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100154320'},
     ]

contas = [
    {'login': "craudiclivar30", 'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36', 'proxy':'23.129.253.187:6805:nqpczzte:mkj1eruejzwi', "wallet":"P1100434141"},
    {'login': "juaojaquetao1", 'userAgent': "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8381.56 Safari/537.36", 'proxy': "185.72.242.14:5697:nqpczzte:mkj1eruejzwi", "wallet":"P1100434972"},
    {'login': "erickbuenoms96", 'userAgent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9739.75 Safari/537.36", 'proxy': "45.157.125.208:5835:nqpczzte:mkj1eruejzwi", "wallet":"P1100436337"},
    {'login': 'carlosmonoyilol', 'userAgent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3312.41 Safari/537.36", 'proxy': "185.72.242.167:5850:nqpczzte:mkj1eruejzwi", "wallet":"P1100437345"},
    {'login': 'renatoandrade198', 'userAgent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3501.29 Safari/537.36', 'proxy': '23.129.254.26:6008:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100441969'},
    {'login': 'josephjonvondon3', 'userAgent': 'Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6235.81 Safari/537.36', 'proxy': '23.129.254.92:6074:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100442862'},
    {'login': 'lucreciomalta349', 'userAgent': 'Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6235.81 Safari/537.36', 'proxy': '23.129.253.122:6740:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100443369'},
    {'login': 'kinenintomadl8', 'userAgent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4251.30 Safari/537.36', 'proxy': '23.129.254.112:6094:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100444280'},
    {'login': 'imperadorklks9', 'userAgent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6435.23 Safari/537.36', 'proxy': '45.157.125.53:5680:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100448911'},
    {'login': 'lubudaespada91', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4800.20 Safari/537.36', 'proxy': '23.129.253.140:6758:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100449794'},
    {'login': 'rickpaqueta87',  'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7061.74 Safari/537.36', 'proxy': '23.129.253.31:6649:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100450472'},
    {'login': 'duardujon209',   'userAgent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4811.89 Safari/537.36', 'proxy':'23.129.254.169:6151:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100451256'},
    {'login': 'lascaninor403',  'userAgent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7427.29 Safari/537.36', 'proxy': '45.157.125.124:5751:nqpczzte:mkj1eruejzwi', 'wallet': 'P1100451996'},
]

criarConta = []


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
        conta = contas[8]
        nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
        nav.somenteLogin()

else:
    conta = criarConta[12]
    nav = navegador.Navegador(conta['login'], conta['userAgent'], conta['proxy'], conta['wallet'])
    nav.somenteAbrir((random.choice(contas))['login'])