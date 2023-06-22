import tkinter as t
window=t.Tk()

def process():
    fir=int(Ent1.get())
    sec=int(Ent2.get())
    add=fir+sec
    print(add)

Ent1=t.Entry(window)
Ent2=t.Entry(window)
Ent1.pack()
Ent2.pack()

button=t.Button(window, text="SUM",command=process)
button.pack()

window.mainloop()
