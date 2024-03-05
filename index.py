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


# clicar no botão da login
pyautogui.click(x=663, y=422)

# Importar a base de dados
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # Preenchimento 
    # clicar no primeiro campo de entrada
    pyautogui.click(x=477, y=217)

    # codigo do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")


    # Preço
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Observação
    obs = tabela.loc[linha, "obs"]
    
    if not pd.isna(obs): # Verificar se está vazio
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    pyautogui.press("enter")

    # para rodar para o topo da tabela valor alto
    pyautogui.scroll(5000)

