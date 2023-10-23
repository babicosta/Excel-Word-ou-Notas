import pyautogui

opcao = pyautogui.confirm('Clique no botao desejado',
                              buttons=['Excel', 'Word', 'Notas'])

if opcao == 'Excel':

    pyautogui.press('win')
    pyautogui.sleep(2)
    pyautogui.typewrite('Excel')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.click(716, 281)


elif opcao == 'Word':

    pyautogui.press('win')
    pyautogui.sleep(2)
    pyautogui.typewrite('Word')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.click(698, 258)
    #print(pyautogui.position())

else:
    pyautogui.press('win')
    pyautogui.sleep(2)
    pyautogui.typewrite('Bloco de Notas')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    # print(pyautogui.position())




