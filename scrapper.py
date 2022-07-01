from time import sleep
from chrome_driver import get_driver, find_element_by_xpath, wait_element_load
import csv

driver = get_driver()
f = open('housing_data.csv', 'w', newline='',  encoding='utf-8')
w = csv.writer(f)

districts = {'ANTARES': 1, 'BARRO DURO': 2, 'BEBEDOURO': 3, 'BENEDITO BENTES': 4, 'BOM PARTO': 5, 
            'CANAÃ': 6, 'CENTRO': 7, 'CHÃ DE JAQUEIRA': 8, 'CHÃ DE BEBEDOURO': 9, 'CIDADE UNIVERSITÁRIA': 10, 
            'CLIMA BOM': 11, 'CRUZ DAS ALMAS': 12, 'FAROL': 13, 'FEITOSA': 14, 'FERNÃO VELHO': 15, 
            'GARÇA TORTA': 16, 'GRUTA DE LOURDES': 17, 'GUAXUMA': 18, 'IPIOCA': 19, 'JACARECICA': 20, 
            'JACINTINHO': 21, 'JARAGUÁ': 22, 'JARDIM PETRÓPOLIS': 23, 'JATIÚCA': 24, 'LEVADA': 25, 
            'MANGABEIRAS': 26, 'MUTANGE': 27, 'OURO PRETO': 28, 'PAJUÇARA': 29, 'PESCARIA': 30, 
            'PETRÓPOLIS': 31, 'PINHEIRO': 32, 'PITANGUINHA': 33, 'POÇO': 34, 'PONTA DA TERRA': 35, 
            'PONTA GROSSA': 36, 'PONTA VERDE': 37, 'PONTAL DA BARRA': 38, 'PRADO': 39, 'RIACHO DOCE': 40, 
            'RIO NOVO': 41, 'SANTA AMÉLIA': 42, 'SANTA LÚCIA': 43, 'SANTO AMARO': 44, 'SANTOS DUMONT': 45, 
            'SÃO JORGE': 46, 'SERRARIA': 47, 'TABULEIRO DO MARTINS': 48, 'TRAPICHE DA BARRA': 49, 'VERGEL DO LAGO': 50}

for page in range(10):
    #driver.get(f'https://al.olx.com.br/alagoas/maceio/imoveis/venda/apartamentos?o={str(page + 1)}')
    driver.get(f'https://al.olx.com.br/alagoas/maceio/ponta-verde/imoveis/venda/apartamentos?o={str(page + 1)}&pe=900000&ps=200000&ss=1&ips=5&cos=100')
    
    wait_element_load('ad-list')
    wait_element_load('cookie-notice-ok-button')
    
    if find_element_by_xpath('//*[@id="cookie-notice-ok-button"]'):
        button = find_element_by_xpath('//*[@id="cookie-notice-ok-button"]')
        button.click()

    for item in range(50):
        try:
        
            link_base_xpath = '//*[@id="ad-list"]/li[' + str(item + 1) + ']'
            product_link_xpath = f'{link_base_xpath}/div/a/div'
            product_link_element = find_element_by_xpath(xpath=product_link_xpath)            

            product_link_element_class = product_link_element.get_attribute('class')
            pub_classes = ['yap-gemini-pub-item', 'listing-native-list-item-1-pub', 'sc-1fcmfeb-1 kntIvV', 'duvuxf-0 h3us20-0 clhToU']
            if product_link_element_class in pub_classes:
                continue
            #sc-1fcmfeb-1 kntIvV
            sleep(5)
            product_link_element.click()
            driver.switch_to.window(driver.window_handles[-1])

            wait_element_load('content')
            sleep(5)
            content_base_xpath = '//*[@id="content"]/div[2]/div/div[2]/div[1]/'
            
            housing_category = find_element_by_xpath(content_base_xpath + 'div[26]/div/div/div/div[2]/div[1]/div/a').text.upper()   
            district = find_element_by_xpath(content_base_xpath + 'div[32]/div/div/div/div[1]/div[2]/div[3]/div/dd').text.upper()
            value = find_element_by_xpath(content_base_xpath + 'div[14]/div/div/div/div/div[1]/div/h2').text.upper()
            area = find_element_by_xpath(content_base_xpath + 'div[26]/div/div/div/div[2]/div[5]/div/dd').text.upper()
            condominium_value = find_element_by_xpath(content_base_xpath + 'div[26]/div/div/div/div[2]/div[3]/div/dd').text.upper()
            iptu = find_element_by_xpath(content_base_xpath + 'div[24]/div/div/div/div[2]/div[4]/div/dd').text.upper()
            bedrooms = find_element_by_xpath(content_base_xpath + 'div[26]/div/div/div/div[2]/div[6]/div/a').text.upper()
            bathrooms = find_element_by_xpath(content_base_xpath + 'div[26]/div/div/div/div[2]/div[7]/div/dd').text.upper()      

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            value = '{:06.2f}'.format(float(value[3:].replace('.', '').replace(',', '.')))
            area = int(area[:-2])
            condominium_value = '{:06.2f}'.format(float(condominium_value[3:].replace('.', '').replace(',', '.')))
            bedrooms = int(bedrooms)
            bathrooms = int(bathrooms[0])
            district_cod = int(districts[district])

            if housing_category == 'APARTAMENTOS':
                w.writerow([district_cod, area, iptu, condominium_value, bedrooms, bathrooms, value])
                print(f'Categoria: {housing_category}, Bairro: {district}, Codigo do Bairro: {district_cod}, Area: {area}, IPTU: {iptu}, Valor do Conominio: {condominium_value}, Quartos: {bedrooms}, Banheiros: {bathrooms}, Valor: {value}')   
        
        except Exception as e:
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            print(e)
            continue

f.close
driver.quit()
