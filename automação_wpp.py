import time
import pyautogui

# Função para abrir o WhatsApp
def abrir_whatsapp():
    # Pressionar a tecla do Windows para abrir o menu Iniciar
    pyautogui.press('win')
    time.sleep(1)  # Aguardar o menu Iniciar abrir

    # Digitar "WhatsApp" para pesquisar o aplicativo
    pyautogui.write('WhatsApp')
    time.sleep(1)  # Aguardar a pesquisa ser concluída

    # Pressionar Enter para abrir o WhatsApp
    pyautogui.press('enter')
    time.sleep(10)  # Aguardar o WhatsApp abrir (ajuste conforme necessário)

# Função para enviar a mensagem para o contato "Bê"
def enviar_mensagem():
    # Aguardar um pouco para garantir que o WhatsApp esteja pronto
    time.sleep(5)

    # Pressionar Ctrl + F para abrir a barra de pesquisa
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    # Digitar o nome do contato "Bê"
    pyautogui.write('Survivor')
    time.sleep(2)  # Aguardar a pesquisa ser concluída

    # Pressionar Enter para abrir o chat com o contato
    pyautogui.press('enter')
    time.sleep(2)

    # Digitar a mensagem "tá bom bb"
    pyautogui.write('Bom dia!')
    time.sleep(1)

    # Pressionar Enter para enviar a mensagem
    pyautogui.press('enter')

# Executar o programa
abrir_whatsapp()
enviar_mensagem()