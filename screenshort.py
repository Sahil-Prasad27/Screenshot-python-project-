import time 
import pyautogui
import tkinter as tk

def screenshort():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/SAHIL/Desktop/python project/screenshorts data/{}.png'.format(name)
    time.sleep(0.3)
    img = pyautogui.screenshot(name)
    img.show()
    
    
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshort)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit)
close.pack(side=tk.LEFT)
root.mainloop()