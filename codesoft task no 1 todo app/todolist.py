import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        pass

def update_task():
    try:
        selected_task = listbox.curselection()[0]
        updated_task = entry.get()
        listbox.delete(selected_task)
        listbox.insert(selected_task, updated_task)
        entry.delete(0, tk.END)
    except IndexError:
        pass

def mark_complete():
    try:
        selected_task = listbox.curselection()[0]
        listbox.itemconfig(selected_task, {'bg': 'light green'})
    except IndexError:
        pass

def unmark_complete():
    try:
        selected_task = listbox.curselection()[0]
        listbox.itemconfig(selected_task, {'bg': 'white'})
    except IndexError:
        pass

def exit_btn():
    try:
        exit()
    except IndexError:
        exit()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a text entry field
entry = tk.Entry(root, width=50,bd=4)
entry.pack(pady=5)

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectbackground="grey",width=50, selectforeground="black", bd=4)
listbox.pack(pady=20)

# Create buttons for add, delete, update, and mark complete
add_button = tk.Button(root, text="Add Task",width=40,bg="#9aeb2a",activebackground='#81c423',bd=4, command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task",width=40,bg="#f72f39",activebackground='#d42831',bd=4, command=delete_task)
delete_button.pack(pady=5)
update_button = tk.Button(root, text="Update Task",width=40,bg="#3392d6",activebackground='#216ea6',bd=4, command=update_task)
update_button.pack(pady=5)
complete_button = tk.Button(root, text="Mark Complete",width=40,bg="#158a40",activebackground='#0e7333',bd=4, command=mark_complete)
complete_button.pack(pady=5)
incomplete_button = tk.Button(root, text="Mark Incomplete",width=40,bg="#e64515",activebackground='#cf3406',bd=4, command=unmark_complete)
incomplete_button.pack(pady=5)
exit_btnn=tk.Button(root, text="Exit",width=20,bg="#de842a",activebackground='#b0651a',bd=4, command=exit_btn)

add_button.pack()
delete_button.pack()
update_button.pack()
complete_button.pack()
incomplete_button.pack()
exit_btnn.pack()

root.mainloop()