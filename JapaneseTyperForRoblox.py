import time
import io,sys
from time import sleep
import pyperclip
import pyautogui
import keyboard
import tkinter
from os import system
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#Set up the tkinter
root = tkinter.Tk()
root.title("Auto Typer")
root.geometry("300x30")
root.resizable(100, 100)
#Hide the top bar
root.overrideredirect(1)
#Allways on top
root.attributes("-topmost", True)

#Menu
menuBar = tkinter.Menu()
root.config(menu=menuBar)


settingWindow = None
#--------- Define Functions ----------#

#I don't know that this thing is doing, but it's inportant.
def stay_on_top():
   root.lift()
   root.after(2000, stay_on_top)

#Close the app
def CloseApp(button1):
    sys.exit()

#Set up the setting window
def CreateSettingWindows():
    global settingWindow
    settingWindow = tkinter.Toplevel(width=300, height=300)
    settingWindow.title("設定")

    #Toggle top bar
    def ToggleTopbar():
        root.overrideredirect(not root.overrideredirect())
        root.attributes("-topmost", True)
    toggleTopbarButton = tkinter.Button(settingWindow, width=30, text="Toggle Topbar", command=ToggleTopbar)
    toggleTopbarButton.pack()

#Toggle the setting window
def ToggleSettings():
    global settingWindow
    if settingWindow == None or not settingWindow.winfo_exists():
        CreateSettingWindows()


#Copy the input text, bouble click the window corner, paste the text into the roblox chat input, and hit enter to send the chat.
def SendChat(event):
    pyperclip.copy(chatInput.get())
    pyautogui.doubleClick(root.winfo_rootx()-5, root.winfo_rooty()-5)
    time.sleep(0.3)
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    chatInput.delete(0, tkinter.END)


#When a user hit "/" key, activate the window, and set the focus to the input.
def ActivateInputWidget(event):
    if event == None:
        return
    if event.scan_code == 44:
        #Activate the window, but this code doesn't work on builded app. not sure why.
        #I found this code here: https://stackoverflow.com/questions/17774859/tkinter-window-focus-on-mac-os-x
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        chatInput.focus_set()


#--------- Create GUIs ----------#

#Create character space count input
chatInput = tkinter.Entry(root, width=1000)
chatInput.insert(tkinter.END, 5)
chatInput.pack()
chatInput.bind("<Return>", SendChat)


#--------- Custom Menus & Commands ----------#

#Listen when a user hit any key.
keyboard.on_press(ActivateInputWidget)

#Setting Menu
WindowMenu = tkinter.Menu()
WindowMenu.add_command(label="Settings", command=ToggleSettings)
menuBar.add_cascade(label="ウィンドウ", menu=WindowMenu)

stay_on_top()

root.mainloop()