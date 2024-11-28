import pyautogui
import time
import tkinter as tk

def start():
    try:
        click = int(entry.get())  
        time.sleep(3)  
        for i in range(click):
            pyautogui.click() 
    except ValueError:
        result_label.config(text="Nombre pas valide", fg="red")

def stop():
    root.destroy()

root = tk.Tk()
root.title("Autoclicker")
root.geometry("200x150")


label = tk.Label(root, text="Nombre de click :")
label.pack(padx=10, pady=5)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

start_button = tk.Button(root, text="start", command=start)
start_button.pack(padx=10, pady=10)
start_button = tk.Button(root, text="stop", command=stop)
start_button.pack(padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=5)

root.mainloop()