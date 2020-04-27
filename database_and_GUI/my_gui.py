import tkinter
import tkinter.messagebox


def button_click():
    print('click!')
    # to print in terminal what i write in entry_1
    print(entry_1.get())
    entry = entry_1.get()

    # print all from entry_2
    # 1.0 is the start in first line 0 charactr, END is end of field
    print(entry_2.get('1.0', tkinter.END))
    # print first line can be 3.5 is mean 3 line 5 character,
    # line ends when prees Enter
    print(entry_2.get('1.0', '2.0'))
    # clear field
    entry_2.delete('1.0', tkinter.END)

    # messagebox.showerror/showwarrning
    tkinter.messagebox.showerror('This is a window name', 'The date from entry_1: '+entry)
    # insert value to entry_2
    entry_2.insert('1.0', 'the secound line\n')
    entry_2.insert('2.0', 'the last line\n')
    entry_2.insert('1.0', 'the first line\n')


def create_squere(event):
    # this is a mouse coordinates
    print(event.x, event.y)
    # draw squere, coordinates, border
    canvas.create_rectangle(event.x+5, event.y+5, event.x-5, event.y-5, outline='pink', fill='blue')


def clear_canvas(event):
    # print all squeres coordinates
    print(canvas.find_all())
    # this delete all squeres from canvas
    list(map(lambda i: canvas.delete(i), canvas.find_all()))


def on_select(event):
    # no idea what is doing
    list_select = event.widget

    if list_select.curselection():
        # return index of first select object
        index = int(list_select.curselection()[0])
        # pritn selected object
        print(index, '->', list_select.get(index))

        if entry_1.get() == 'del' and list_field.size() > 1:
            # delete element on list
            list_field.delete(index)
        elif entry_1.get() == 'add':
            list_field.insert(index, entry_2.get(1.0, 2.0).strip())


# create a window
root = tkinter.Tk(className='My first GUI')
root.resizable(width=False, height=True)

# create a text in window
text_1 = tkinter.Label(root, text='Welcome in my app')
# put it to app
text_1.grid(row=0, column=0)

frame_1 = tkinter.Frame(root, borderwidth=4)
frame_1.grid(row=0, column=1)
# to config
frame_1.config(background='black')

text_2 = tkinter.Label(frame_1, text='text in frame')
# sticky is a geographical direction like East/West/North/South
# padx and pady is padding x and y
text_2.grid(sticky=tkinter.E, row=0, column=1, padx=5, pady=5)

# to put the text
entry_1 = tkinter.Entry(frame_1, width=20)
entry_1.grid(sticky=tkinter.W, row=0, column=0, padx=5, pady=5)

button_1 = tkinter.Button(frame_1, text='Click me!', command=button_click)
button_1.grid(row=1, column=0)
# foreground is a font color
button_1.config(background='red', foreground='blue')

# this create multilines entry field
entry_2 = tkinter.Text(frame_1, width=20, heigh=10)
entry_2.grid(row=2, column=0)

# thic create list
list_field = tkinter.Listbox(root)
list_field.grid(row=1, column=1)
# add item to list (index, value)
list_field.insert(0, 'secound')
list_field.insert(1, 'middle')
list_field.insert(tkinter.END, 'end')
list_field.insert(0, 'first')
# events in list
list_field.bind('<<ListboxSelect>>', on_select)

# this is a canvas to painting for example
canvas = tkinter.Canvas(frame_1, width=100, height=175)
canvas.grid(sticky=tkinter.S, row=2, column=1, padx=5, pady=5)
canvas.config(background='green')
# use the events (events, function)
canvas.bind('<B1-Motion>', create_squere)
canvas.bind('<Button-1>', create_squere)
canvas.bind('<Button-3>', clear_canvas)
# list of events
'''
  B1/2/3/4-Motion ruch z trzymanym przyciskiem
  Button-1/2/3/4 klik
  ButtonPress-1/2/3/4 wciśk
  ButtonRelease-1/2/3/4  wycisk
  Double-Button-1/2/3/4
  Enter (wjazd myszy na płótno)
  Leave (zjazd myszy z płótna)
  Return,Shift_L,BackSpace,Tab, F1, Control_R itd.
  FocusIn - klawiatura fokusuje płótno lub jego zawartość
  FocusOut
'''

# start a window
root.mainloop()
