#importando a biblioteca de automação de comandos teclado/mouse/monitor
import pyautogui
#importando biblioteca de tempo para as pausas feitas no decorrer do programa
import time

#mensagem de alerta no inicio
pyautogui.alert("ATENÇÂO codigo em execução aguarde")

#um comando para intervalo de cada comando
pyautogui.PAUSE = 1.5

#pressionar comando win+I 
pyautogui.hotkey('win','i')

#tempo de espera
time.sleep(1)

#digita a palavra Bluetooth no teclado
pyautogui.write('Bluetooth')

#pressiona enter
pyautogui.press('enter')

#pressiona enter novamente
pyautogui.press('enter')

#leva o mouse no lugar da chave de seleção
pyautogui.moveTo(380, 257)

#clica com o mouse no local da chave de seleção 
pyautogui.mouseDown()

#soltar o botao pressionado do mouse
pyautogui.mouseUp()

#fecha a janela
pyautogui.hotkey('alt','f4')

#exibir caixa de mensagem para saber que o programa funcionou
pyautogui.alert("Bluetooth Ligado")