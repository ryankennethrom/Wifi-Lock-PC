import tkinter as tk

def entry_focus_in(event):
    if entry1.get() == "Enter message...":
        entry1.delete(0, 'end')
        entry1.config(fg='black')

def entry_focus_out(event):
    if entry1.get() == "":
        entry1.insert(0, "Enter message...")
        entry1.config(fg="gray")

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

    my_listbox = tk.Listbox(root, bg='green')
    # tk.Button(root, text="Button", command=
    my_listbox.pack(padx=10, pady=5, fill=tk.X)

    frame1 = tk.Frame(root, height=20, bg="green")
    frame1.pack(padx=10, pady=1, fill=tk.X)

    entry1 = tk.Entry(frame1, width=60, bg="green")
    # entry1.grid(column=0, row=1)
    entry1.pack( side='left', fill=tk.X)

    button1 = tk.Button(frame1,width=20, text="Restrict Network")
    # button1.grid(column=1, row=1)
    button1.pack(padx=5, side='left',fill=tk.X)


    root.mainloop()