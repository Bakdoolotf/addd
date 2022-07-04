# import requests

# response =requests.get('https://api.telegram.org/bot5434542892:AAFCMU6J7IDWw9uVNOUy_9Zmck9VBDhEVD4/getMe')

# for i in response.headers:
#     print(f"{i}  =    {response.headers.get(i)}")

# data = response.json()
# print(data)

# import requests
# TOKEN = "5434542892:AAFCMU6J7IDWw9uVNOUy_9Zmck9VBDhEVD4"
# chat_id = "1084941430"
# phone_number= "+996 501 600701"
# first_name = "Нуся"
# url = f"https://api.telegram.org/bot{TOKEN}/sendContact?chat_id={chat_id}&phone_number={phone_number}&first_name={first_name}"
# # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# r = requests.get(url)
# print(r.json())

import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.


currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
