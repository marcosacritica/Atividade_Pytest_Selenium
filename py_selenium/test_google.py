from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inicializando o navegador (usando o Chrome no exemplo)
driver = webdriver.Chrome()  # Ou use o driver correspondente ao seu navegador
driver.maximize_window()
# Acesse o Google
driver.get("https://www.google.com")

# Encontre a barra de pesquisa
search_box = driver.find_element(By.NAME, "q")

# Digite "FIFA 25 preço" e pressione Enter
search_box.send_keys("FIFA 25 preço")
search_box.send_keys(Keys.RETURN)

# Aguarde alguns segundos para garantir que a página foi carregada
time.sleep(3)

# Procure o primeiro link de resultado (você pode ajustar isso para pegar o preço diretamente)
results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

# Extraia o texto do primeiro resultado e imprima
if results:
    first_result = results[0].text
    print("Primeiro resultado encontrado:", first_result)
else:
    print("Nenhum resultado encontrado")

# Fechar o navegador
driver.quit()
