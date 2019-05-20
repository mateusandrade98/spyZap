from selenium import webdriver
from time import sleep
import selenium.common.exceptions
import sys
from datetime import datetime

try:
    amigo = sys.argv[1]
except IndexError:
    raise Exception('expecifique o nome do chat alvo')

url = 'https://web.whatsapp.com'

Firefox = webdriver.Firefox()
Firefox.get(url)

def registrarData(info):
    online = 1 if info.lower() == 'online' else 0
    data_atual = datetime.now()
    data = str(data_atual.day)+'/'+str(data_atual.month)+'/'+str(data_atual.year)
    hora = data_atual.hour
    minuto = data_atual.minute
    segundos = data_atual.second
    dados = '"'+str(sys.argv[1])+'",'+str(online)+',"'+data+'",'\
            +str(hora)+','+str(minuto)+','+str(segundos)

    with open('data/spyZap.csv','a') as f:
        f.write('\n'+dados)
        f.close()
    return True

def gerarLogs(info):
    data_e_hora_atuais = datetime.now()
    registrarData(info)
    info = '['+str(data_e_hora_atuais)+'] ' + info
    print(info)
    with open('logs','a') as f:
        f.write(info)
        f.close()
    #Firefox.save_screenshot('screenshot/'+info+'.png')
    return True

while True:
    if not 'landing-title' in Firefox.page_source:
        break

print('[+] spyZap foi autenticado')

element = None
while element == None:
    try:
        element = Firefox.find_element_by_class_name('_1WliW')
    except selenium.common.exceptions.NoSuchElementException:
        continue

while True:
    try:
        element.click()
        break
    except selenium.common.exceptions.ElementNotInteractableException:
        continue

while True:
    if '_2S1VP' in Firefox.page_source:
        break;

sleep(2)

'''user = None
while user == None:
    if not '_2S1VP' in Firefox.page_source:
        Firefox.find_element_by_class_name('_1WliW').click()
    try:
        user = Firefox.find_element_by_class_name('_2S1VP').text
    except selenium.common.exceptions.StaleElementReferenceException:
        continue

print('[+] Usuário: '+user)'''

while True:
    if '_2S1VP' in Firefox.page_source:
        break

Firefox.find_element_by_class_name('_1aTxu').click()

while True:
    if '_2wP_Y' in Firefox.page_source:
        break

listaConversas = None
while listaConversas == None:
    listaConversas = Firefox.find_elements_by_class_name('_2wP_Y')

for conversa in listaConversas:
    try:
        chat = conversa.find_element_by_class_name('_1wjpf').text
    except selenium.common.exceptions.StaleElementReferenceException:
        continue
    if amigo in chat:
        print('click: '+chat)
        conversa.find_element_by_tag_name('div').click()
        break

print('[+] Chat selecionado...['+chat+']')

sender = None
while sender == None:
    sender = Firefox.find_element_by_class_name('_1Plpp')

sender.click()

listaMensagens = None
while listaMensagens == None:
    listaMensagens = Firefox.find_elements_by_class_name('vW7d1')

divTexto = None
while divTexto == None:
    divTexto = Firefox.find_element_by_class_name('_3zb-j')

def obterMensagens():
    textos = []
    for mensagem in Firefox.find_elements_by_class_name('vW7d1'):
        try:
            envio = mensagem.find_element_by_class_name('Tkt2p').find_element_by_class_name('copyable-text').get_attribute('data-pre-plain-text')
            texto = mensagem.find_element_by_class_name('Tkt2p').find_element_by_class_name('selectable-text').text
            #texto = tratamento.removerEmoji(texto)
            #texto = tratamento.removerLink(texto)
            if envio != None:
                envio = str(envio).split('2019]')
                envio = envio[1].replace(':','')
                envio = envio[1:(len(envio) - 1)]
            if texto != '':
                textos.append([envio,texto])
        except selenium.common.exceptions.NoSuchElementException:
            continue
        except selenium.common.exceptions.NoSuchAttributeException:
            print('NoSuchAttributeException')
            continue
        except selenium.common.exceptions.StaleElementReferenceException:
            print('StaleElementReferenceException')
            continue

    return textos

while True:
    sleep(10)

    try:
        online = Firefox.find_element_by_xpath('//*[@title="online"]')
        if online is not None:
            gerarLogs('Online')
    except selenium.common.exceptions.NoSuchElementException:
        gerarLogs('Offline')
