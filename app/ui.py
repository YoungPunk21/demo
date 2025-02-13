import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.controllers import handle_add_member, show_budget_info, refresh_family_list, handle_add_expense
from app.models import get_family_members_by_id

def add_member_window(root, tree):
    add_window = tk.Toplevel(root)
    add_window.title("Добавление члена семьи")

    tk.Label(add_window, text="ФИО:").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Возраст:").pack()
    age_entry = tk.Entry(add_window)
    age_entry.pack()

    tk.Label(add_window, text="Должность:").pack()
    job_entry = tk.Entry(add_window)
    job_entry.pack()

    tk.Label(add_window, text="Место работы:").pack()
    workplace_entry = tk.Entry(add_window)
    workplace_entry.pack()

    tk.Label(add_window, text="Оклад:").pack()
    salary_entry = tk.Entry(add_window)
    salary_entry.pack()

    tk.Button(add_window, text="Сохранить", 
              command=lambda: handle_add_member(name_entry.get(), age_entry.get(), 
                                                job_entry.get(), workplace_entry.get(), 
                                                salary_entry.get(), add_window, tree)).pack()

def add_expense_window(root, tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Ошибка", "Выберите члена семьи")
        return
    
    member_id = tree.item(selected_item[0])['values'][0]
    add_window = tk.Toplevel(root)
    add_window.title("Добавление расхода")

    tk.Label(add_window, text="Название расхода:").pack()
    expense_name_entry = tk.Entry(add_window)
    expense_name_entry.pack()

    tk.Label(add_window, text="Сумма:").pack()
    amount_entry = tk.Entry(add_window)
    amount_entry.pack()

    tk.Button(add_window, text="Сохранить", 
              command=lambda: handle_add_expense(member_id, expense_name_entry.get(), 
                                                 amount_entry.get(), add_window)).pack()

def create_main_window():
    root = tk.Tk()
    root.title("Учет семьи")

    tree = ttk.Treeview(root, columns=("ID", "ФИО", "Возраст", "Должность", "Место работы", "Оклад"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for col in ("ID", "ФИО", "Возраст", "Должность", "Место работы", "Оклад"):
        tree.heading(col, text=col)

    refresh_family_list(tree)

    tk.Button(root, text="Добавить", command=lambda: add_member_window(root, tree)).pack(side=tk.LEFT)
    tk.Button(root, text="Добавить расход", command=lambda: add_expense_window(root, tree)).pack(side=tk.LEFT)
    tk.Button(root, text="Показать бюджет", command=show_budget_info).pack(side=tk.LEFT)

    root.mainloop()
