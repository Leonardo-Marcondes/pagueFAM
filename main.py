from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
 
import time
 
# Iniciar o navegador Chrome
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

wait = WebDriverWait(browser, timeout=80)
usuario = "*******" # Coloque o seu usuário do portal do Aluno FAM
senha = "*******" # Coloque a sua senha do portal do Aluno FAM
    
# Navegar para a página
browser.get('https://portaldoaluno.eusoufam.com.br/FrameHTML/web/app/Edu/PortalEducacional/login/#xd_co_f=Zjk0YmFiMWEtZDk5MS00MThiLWFjM2ItYzQwMGJmMDBmYWQ0~')
 
 # Espera até que os campos de usuário e senha estejam visíveis
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="User"]'))
)
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Pass"]'))
)
 
# Preencher os campos e clica no botão de login
browser.find_element(By.XPATH, '//*[@id="User"]').send_keys(usuario)
browser.find_element(By.XPATH, '//*[@id="Pass"]').send_keys(senha)
browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/input').click()

# Espera até o menu carregar
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="show-menu"]')))

# Navega pelo menu lateral até a área de financeiro
browser.find_element(By.XPATH, '//*[@id="show-menu"]').click()
browser.find_element(By.XPATH, '//*[@id="EDU_PORTAL_FINANCEIRO_NOVO"]').click()

# Espera o boleto carregar
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="check-box-select-boleto ng-pristine ng-untouched ng-valid"]')))

# Navega pelos pop-ups 
browser.find_element(By.XPATH, '//*[@class="check-box-select-boleto ng-pristine ng-untouched ng-valid"]').click()
browser.find_element(By.XPATH, '//*[@ng-click="controller.exibirDadosPix()"]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="payments-botao-content payments-botaoAzul payments-formapgto alerta-prox-vencimento-buttons ng-binding ng-scope"]')))

# Clica no botão de Gerar QR CODE
browser.find_element(By.XPATH, '//*[@class="payments-botao-content payments-botaoAzul payments-formapgto alerta-prox-vencimento-buttons ng-binding ng-scope"]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@download="qrCode.png"]')))

# Baixa o QR CODE
browser.find_element(By.XPATH, '//*[@download="qrCode.png"]').click()

time.sleep(60)

browser.quit()
# Aguarda 2 minutos para o encerramento da página (temporário)