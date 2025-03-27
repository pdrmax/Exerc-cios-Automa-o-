import time
import pyautogui

# Função para abrir o Word usando a tecla do Windows
def abrir_word():
    # Pressionar a tecla do Windows para abrir o menu Iniciar
    pyautogui.press('win')
    time.sleep(1)  # Aguardar o menu Iniciar abrir

    # Digitar "Word" para pesquisar o aplicativo
    pyautogui.write('Word')
    time.sleep(1)  # Aguardar a pesquisa ser concluída

    # Pressionar Enter para abrir o Word
    pyautogui.press('enter')
    time.sleep(5)  # Aguardar o Word abrir

# Função para digitar a mensagem
def digitar_mensagem():
    # Aguardar um pouco para garantir que o Word esteja pronto
    time.sleep(2)
    
    # Digitar a mensagem
    pyautogui.write("Bom dia, Bom dia, Max!", interval=0.2)  # Intervalo entre as teclas (opcional)

# Executar o programa
abrir_word()
digitar_mensagem()