import tkinter as tk
from tkinter import messagebox

# إنشاء نافذة رئيسية
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#f0f4f8")  # لون خلفية هادي (أزرق فاتح)

tasks = []

# دالة لإظهار المهام في القائمة
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i}. {task['title']} {status}")

# دالة لإضافة مهمة
def add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# دالة لوضع المهمة كمكتملة
def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

# دالة لحذف المهمة
def delete_task():
    try:
        index = listbox.curselection()[0]
        del tasks[index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

# واجهة المستخدم
entry = tk.Entry(root, width=30, bg="#ffffff")  # خلفية بيضاء للحقل
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#a8dadc")
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark Done", command=mark_done, bg="#a8dadc")
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#a8dadc")
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, bg="#ffffff")
listbox.pack(pady=20)

# تشغيل النافذة
root.mainloop()


