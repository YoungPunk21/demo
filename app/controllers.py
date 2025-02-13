from app.models import add_family_member, get_family_members, delete_family_member, update_family_member, calculate_budget, add_expense
from tkinter import messagebox

def refresh_family_list(tree):
    for row in tree.get_children():
        tree.delete(row)
    for member in get_family_members():
        tree.insert("", "end", values=member)

def handle_add_member(name, age, job, workplace, salary, window, tree):
    if not name:
        messagebox.showerror("Ошибка", "ФИО не может быть пустым")
        return
    try:
        age = int(age)
        salary = float(salary)
        if salary < 0:
            raise ValueError("Оклад не может быть отрицательным")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректные данные в поле возраст или оклад")
        return

    add_family_member(name, age, job or "Безработный", workplace or "-", salary)
    messagebox.showinfo("Успех", "Член семьи добавлен!")
    window.destroy()
    refresh_family_list(tree)

def show_budget_info():
    budget_info = calculate_budget()
    messagebox.showinfo("Рассчет бюджета", budget_info)

def handle_add_expense(member_id, expense_name, amount, window):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректная сумма")
        return
    
    add_expense(member_id, expense_name, amount)
    messagebox.showinfo("Успех", "Расход добавлен!")
    window.destroy()
