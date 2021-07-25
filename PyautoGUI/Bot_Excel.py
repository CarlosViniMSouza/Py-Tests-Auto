# Passo-a-Passo a ser seguido (para que o bot faça minha tarefa):

# 1 - Abrir o Excel / LibreOffice Calc :
# 2 - Preencher Login
# 3 - Preencher Senha
# 4 - clicar em fazer login

import pyautogui as pag

pag.PAUSE = 2 # a cada comando executado, o python aguarda 2 seg para executar o prox. comando

pag.press("win") # pressionar tecla Windows
pag.write("Login.xlsx") # digitar arquivo 'Login.xlsx'
pag.press("backspace") # comando para apagar uma letra (caso nao seja reconhecido o programa de primeira)
pag.press("enter") # vai chamar o programa 'Login.xlsx'

"""
Para saber onde o programa deve clicar, use o código abaixo:

import time
time.sleep(5) # aguarda 5 segundos
pag.position() # Aqui ele vai imprimir as coordenadas do lugar onde meu mouse estava
<Exemplo:> Point(500, 186)
"""

# preenchendo login:
pag.click(x=400, y=122)
pag.write("<seu login>")

# preenchendo senha:
pag.click(x=400, y=112)
pag.write("<sua senha>")

# efetivar login:
pag.click(x=350, y=102)

# Pronto, login feito com sucesso.