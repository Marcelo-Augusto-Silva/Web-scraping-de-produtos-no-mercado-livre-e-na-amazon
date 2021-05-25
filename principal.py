from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from time import sleep

escolha = str(input('Qual produto voce quer ?? '))
print('PESQUISANDO NO SITE DA AMAZON....')
print()

chrome_options = Options()
chrome_options.add_argument('--headless')
navegador = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
navegador.get('https://www.amazon.com.br/')


barra = navegador.find_element_by_id('twotabsearchtextbox')
barra.send_keys(escolha)
barra.send_keys(Keys.ENTER)

navegador.implicitly_wait(10)
produto = navegador.find_elements_by_xpath('//div[@class="s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section"]')


achar = re.compile('R\$\d*\.*,*\d*')
d = re.compile('\d*\.\d*')
lista = []
dici = {}
for c in range(0,5):
    dici['Produto'] = produto[c].text
    p = achar.search(produto[c].text)
    z = d.search(produto[c].text)
    try:
        dici['Preco'] = p.group()

    except:
        # sem preço
        'sem preço'
    lista.append(dici.copy())

    del dici['Produto']
    try:
        del dici['Preco']
    except:
        'sem preço'

print('Os produtos encontrados no site da amazon foram')
for c in lista:
    print()
    sleep(2)
    print(c['Produto'][:50])
    try:
        print(f'custa {c["Preco"]}')
    except:
        print('Sem preço')
navegador.close()

print()
print('PESQUISANDO NO MERCADO LIVRE...')
navegador = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
navegador.get('https://www.mercadolivre.com.br/')

navegador.implicitly_wait(10)
we = navegador.find_element_by_xpath('//input[@class="nav-search-input"]')
we.send_keys(escolha)
we.send_keys(Keys.ENTER)

navegador.implicitly_wait(15)

# desc = navegador.find_elements_by_xpath('//div[@class="andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default"]')
try:
    desc = navegador.find_elements_by_xpath('//h2[@class="ui-search-item__title"]')
except:
    'sem descriçao'
try:
    preco = navegador.find_elements_by_xpath('//div[@class="ui-search-result__content-wrapper"]')
except:
    'sem preço'

achar = re.compile('\d{,3}\.+?\d*')

print()
print('No mercado livre achei os seguintes produtos')
for c in range(0,3):
    try:
        print()
        sleep(2)
        z = achar.findall(preco[c].text)
        print(desc[c].text)
        print('custa',end=' ')
        try:
            try:
                print(z[1])
            except:
                print(z[0])
        except:
            print('Sem preço')
    except:
        print('Produto não encontrado')

navegador.close()