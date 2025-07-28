from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
 
import time
 
# Iniciar o navegador Firefox
download_dir = os.path.join(os.getcwd(), "my_downloads")
chrome_options = webdriver.ChromeOptions()
prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,  # Disable download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0 # Disable pop-ups
    }
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=chrome_options)


    
# Navegar para a página
browser.get('https://portaldoaluno.eusoufam.com.br/FrameHTML/web/app/Edu/PortalEducacional/login/#xd_co_f=Zjk0YmFiMWEtZDk5MS00MThiLWFjM2ItYzQwMGJmMDBmYWQ0~')
 
time.sleep(2)
 
# Preencher os campos e submeter o formulário
browser.find_element(By.XPATH, '//*[@id="User"]').send_keys('********')
browser.find_element(By.XPATH, '//*[@id="Pass"]').send_keys('********')
browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/input').click()

time.sleep(10)

browser.find_element(By.XPATH, '//*[@id="show-menu"]').click()#Xpah do click 
browser.find_element(By.XPATH, '//*[@id="EDU_PORTAL_FINANCEIRO_NOVO"]').click()

time.sleep(3)

browser.find_element(By.XPATH, '//*[@class="check-box-select-boleto ng-pristine ng-untouched ng-valid"]').click()
browser.find_element(By.XPATH, '//*[@ng-click="controller.exibirDadosPix()"]').click()

time.sleep(5)

browser.find_element(By.XPATH, '//*[@class="payments-botao-content payments-botaoAzul payments-formapgto alerta-prox-vencimento-buttons ng-binding ng-scope"]').click()

time.sleep(8)

browser.find_element(By.XPATH, '//*[@download="qrCode.png"]').click()

time.sleep(3)

browser.quit()
# Aguardar 2 segundos para o carregamento da página