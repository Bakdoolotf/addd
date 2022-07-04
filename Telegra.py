import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.3
time.sleep(2)

def fanc(name,number):
    pyautogui.click(26,49)#Меню
    pyautogui.click(96,395)#Контакты
    pyautogui.click(890,807)#Добавить контакт
    pyautogui.write(name)
    pyautogui.click(925,608)#Ввод номер
    pyautogui.write(number)
    pyautogui.click(1090,672)#Добавить
    time.sleep(0.2)
    pyautogui.click(530,47)#Клик по профилю
    pyautogui.rightClick(859,260)#Клик
    pyautogui.rightClick(967,280)#Клик
    print(pyperclip.paste())
    pyautogui.rightClick(860,316)#Клик по нику
    pyautogui.rightClick(936,332)#Клик по нику
    print(pyperclip.paste())
    if (len(pyperclip.paste()) < 39):
        pyautogui.rightClick(849,375)#Клик по нику
        pyautogui.rightClick(863,394)#Клик по нику
        print(pyperclip.paste())
    elif(len(pyperclip.paste()) > 39):
        pyautogui.rightClick(847,393)#Клик по нику
        pyautogui.rightClick(860,410)#Клик по нику
        print(pyperclip.paste())
    print("________________________")
    pyautogui.click(943,93)#Отвлекающий    
    pyautogui.click(1087,93)#Удалить
    pyautogui.click(998,277)#Удалить
    pyautogui.click(1073,578)#Подтвердить
    pyautogui.click(1589,157)#Подтвердить
    pyautogui.click(1500,157)#Подтвердить

a = ["507 919100","704 032525","550 904068"]
    
for i in a:
    fanc("User",i)
# fanc("User","507 919100")
