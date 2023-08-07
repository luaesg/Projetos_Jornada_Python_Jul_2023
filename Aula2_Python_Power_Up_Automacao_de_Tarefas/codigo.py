"""Passo a passo do projeto
Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
    1.1: abrir o navegador
    1.2: entrar no link acima
Passo 2: Fazer login
    2.1: selecionar o campo de email
    2.2: escrever email
Passo 3: Importar a base de produtos para cadastrar
Passo 4: Cadastrar um produto
Passo 5: Repetir o processo de cadastro até o fim
"""
# 1. Entrar no sistema
import pyautogui # vai controlar teclado e mouse
import time # contrala o tempo das coisas
import pandas as pd # manipulação de base de dados # as serve para mudar o nome
pyautogui.PAUSE = 0.3 # PAUSE -> regra de tempo de espera entre comandos. O valor é dado em segundos

    # 1.1 abrir navegador
pyautogui.press("win") # press -> preciona uma tecla do teclado # win -> para apertar a tecla windows
pyautogui.write("chrome") # write -> escreve algo
pyautogui.press("enter")

    # 1.2 Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # sleep -> coloca essa linha para esperar 3 segundos. Útil para esperar sites carregarem
 
# 2. Fazer Login
    # 2.1 selecionar campo de email
pyautogui.click(x=790, y=503) # click -> insere a posição do mouse para clickar. 

        # X -> distancia horizontal, sendo 0 a extremidade esquerda superior da tela
    # 2.2 escrever email
pyautogui.write("teste@gmail.com") # email
pyautogui.press("tab")
pyautogui.write("TESTE") # senha
pyautogui.press("tab")
pyautogui.press("enter") # logar
time.sleep(3)

# 3. Importar a base de dados do produto
tabela = pd.read_csv("produtos.csv")
print (tabela)

# 4. Cadastrar um produto/5. Repetir o processo de cadastro até o fim
for linha in tabela.index: # para cada linha do indice da tabela

#   4.1 pegar da tabela o valor do campo que queremos preencher
    pyautogui.click(x=919, y=348) # clicar no campo de código do produto no site
    codigo = tabela.loc[linha, "codigo"] # loc identifica linha e coluna a pegar # codigo -> é uam coluna da tabela 

#   4.2 preencher o campo do site
    pyautogui.write(str(codigo)) # Write apenas consegue escrever texto, logo todo valor número precisa ser escrito em forma de texto
#   4.3 passar para o próximo campo
    pyautogui.press("tab")
#marca = tabela.loc[linha,"marca"] 
#pyautogui.write(str(marca)) 
    pyautogui.write(str(tabela.loc[linha, "marca"])) # método masi rápido para escrever o código
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]): # pd.isna é para verificar se o valor da tabela é vazio
        pyautogui.write(str(tabela.loc[linha, "obs"])) # caso não esteja vazio, é escrito seu conteúdo no site
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000) # positivo é para ir para cima. Negativo é para baixo




