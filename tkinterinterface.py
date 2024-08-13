import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    root.title('WifiLockPC')
    x = (root.winfo_screenwidth() // 2) - (width //2)
    y = (root.winfo_screenheight() // 2) - (height //2)
    root.geometry("{}x{}+{}+{}".format(width,height, x, y))
    myLabel = tk.Label(root, text="Restricted Networks", anchor="w",justify="left")
    myLabel.pack(padx=10, fill=tk.X)
    my_listbox = tk.Listbox(root)
    my_listbox.pack(padx=10, pady=5, fill=tk.X)
    root.mainloop()