import tkinter as tk
from tkinter import messagebox

# def restrictNetworkButton():
#     my_listbox.get(my_listbox.curselection())

def onReturnEnterNetwork(event):
    my_listbox.insert(my_listbox.size(), " " + entry1.get())
    entry1.delete(0, 'end')

def add():
    text = entry1.get()
    if len(text) <= 0:
        return
    else:
        my_listbox.insert(my_listbox.size(), " " + text)
        entry1.delete(0, 'end')

def getSelection(myListBox):
    values = myListBox.curselection()
    if values:
        index = values[0]
        val = myListBox.get(index)
        messagebox.showinfo("Selection", val)

if __name__ == "__main__":
    root = tk.Tk()
    root.update_idletasks()
    width = 500
    height = 300
    root.title('WifiLockPC')

    x = (root.winfo_screenwidth() // 2) - (width //2)
    y = (root.winfo_screenheight() // 2) - (height //2)
    root.geometry("{}x{}+{}+{}".format(width,height, x, y))
    root.resizable(0,0)

    myLabel = tk.Label(root, text="Restricted Networks", anchor="w",justify="left")
    myLabel.pack(padx=10, fill=tk.X)

    frame0 = tk.Frame(root, height=20)
    frame0.pack(padx=10, pady=1, fill=tk.X)

    my_listbox = tk.Listbox(frame0, width=40, height=5, font=10, activestyle=tk.NONE, selectbackground='black')
    # tk.Button(root, text="Button", command=
    my_listbox.pack(padx=10, pady=5, side="left", fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame0)
    scrollbar.pack(side = 'left', pady=5, fill=tk.BOTH)
    
    # Attach Scrollbar to listbox
    my_listbox.config(yscrollcommand = scrollbar.set)

    scrollbar.config(command=my_listbox.yview)

    frame1 = tk.Frame(root, height=20)
    frame1.pack(padx=10, pady=1, fill=tk.X)

    entry1 = tk.Entry(frame1, width=60)
    entry1.bind('<Return>', onReturnEnterNetwork)
    # entry1.grid(column=0, row=1)
    entry1.pack( side='left', padx=10, fill=tk.X)

    button1 = tk.Button(frame1,width=20, text="Restrict Network", command=add)
    # button1.grid(column=1, row=1)
    button1.pack( side='left',fill=tk.X)


    root.mainloop()