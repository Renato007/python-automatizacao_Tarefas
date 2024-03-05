import pyautogui
import time
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
pyautogui.PAUSE = 2

# Acessar o sistema da empresa - 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=569, y=304)

# cadastro login 
pyautogui.write("nome@dominio.com")
pyautogui.press("tab")

pyautogui.write("gdfonj359gbvhehera")

# clicar no botão da logo
pyautogui.click(x=663, y=422)



# Importar a base de dados
tabela = pd.read_csv("produtos.csv")

# Preenchimento 
# clicar no primeiro campo de entrada
pyautogui.click(x=477, y=217)

# codigo do produto
pyautogui.write("produto")
pyautogui.press("tab")

# marca
pyautogui.write("marca")
pyautogui.press("tab")

# tipo
pyautogui.write("tipo")
pyautogui.press("tab")

# categoria
pyautogui.write("categoria")
pyautogui.press("tab")


# Preço
pyautogui.write("preco")
pyautogui.press("tab")

# Custo
pyautogui.write("custo")
pyautogui.press("tab")

# Observação
pyautogui.write("obs")
pyautogui.press("tab")

pyautogui.press("enter")


