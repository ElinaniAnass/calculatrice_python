from tkinter import *
window = Tk()
window.title("Calculatrice")
window.configure(bg='black')

def calc(i):
    if i == 'C':
        entry.delete(0, END)
    elif i == 'CE' :
        x = entry.get()
        entry.delete(len(x)-1, END)
    elif i == '=':
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    else:
        entry.insert(END, i)

entry = Entry(window,text ="123",bg="black",font='auto',fg="orange",bd=0,width=32, justify='right')
entry.grid(row=0, column=0, columnspan=4,ipady=17)

buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+', 'C','CE']
row = 1
col = 0
for i in buttons:

    Button(window, text=i ,command=lambda x=i: calc(x),width=9, height=4,bg="black",fg="orange",activebackground="orange").grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()