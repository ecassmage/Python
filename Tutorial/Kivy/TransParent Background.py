import tkinter as tk

root = tk.Tk()
root2 = tk.Tk()
root.wm_attributes('-transparentcolor', 'red')
root.wm_attributes('-transparentcolor', 'red')
Canvas2 = tk.Canvas(root, width=1250, height=1250, bg='black')

#root.attributes('-alpha', 0.5)
Canvas = tk.Canvas(root, width=1000, height=1000, bg='red')
circle = Canvas.create_oval(25, 25, 100, 100, fill='white')
Canvas.place(x=0, y=0, height=1000, width=1000)
Canvas2.place(x=0, y=0, height=1250, width=1250)
root.minsize(1000, 1000)
root.maxsize(1000, 1000)

root.mainloop()
