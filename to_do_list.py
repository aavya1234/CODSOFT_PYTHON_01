import tkinter as tk
from tkinter import messagebox,simpledialog

class TodoApp:
    def __init__(self,root):
        self.root=root
        self.root.title("To Do List Application")
        self.task=[]
        self.root.geometry('350x600')
        self.root.config(bg='purple')
        self.root.resizable(False, False)
    

        self.add_title=tk.Label(self.root,text="To Do List Application",fg='white',bg='purple',font=('Helvetica', 20, 'bold'))
        self.add_title.pack(pady=10)

        self.task_entry=tk.Entry(self.root,width=35,bg='white',fg='black',font=('Arial', 13))
        self.task_entry.pack(pady=15,padx=20)  

        self.add_button=tk.Button(self.root,text='Add task',bg='white',fg='black',font=('Arial', 13,'bold'),command=self.add_task)
        self.add_button.pack(pady=5)  

        self.edit_button=tk.Button(self.root,text='Edit task',bg='white',fg='black',font=('Arial', 13,'bold'),command=self.edit_task)
        self.edit_button.pack(padx=5) 

        self.task_listbox=tk.Listbox(self.root,width=40,height=15,bg='white',fg='black',font=('Helvetica', 13,'bold'),selectbackground='#87CEFA')
        self.task_listbox.pack(pady=15,padx=20) 

        self.delete_button=tk.Button(self.root,text='Delete task',bg='white',fg='black',font=('Arial', 13,'bold'),command=self.delete_task)
        self.delete_button.pack(pady=5) 

        self.update_task_listbox()
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning","Please enter a task.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task_info in self.task:
            self.task_listbox.insert(tk.END, task_info)
        
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.task[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showinfo("Info", "Please select a task to delete.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index=selected_task_index[0]
            selected_task = self.task[index]
            new_task_details = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task)
            if new_task_details:
                self.task[index] = new_task_details
                self.update_task_listbox()
        else:
            messagebox.showinfo("Info", "Please select a task to edit.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
