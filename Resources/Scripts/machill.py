import sys, subprocess
import tkinter as tk

f = open("/Applications/Mac Hill.app/Contents/Resources/server.txt", "w")
f.write(str(sys.argv[1])[26:])
f.close()

window = tk.Tk()
greeting = tk.Label(text="Close window to stop program")
greeting.pack()

p = subprocess.call(["open","/Applications/Mac Hill.app/Contents/Resources/Scripts/BrickHill.app"])

window.mainloop()