import sqlite3
from app.database import DB_NAME

def add_family_member(name, age, job, workplace, salary):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO family_members (name, age, job, workplace, salary)
                      VALUES (?, ?, ?, ?, ?)''', (name, age, job, workplace, salary))
    conn.commit()
    conn.close()

def update_family_member(member_id, name, age, job, workplace, salary):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''UPDATE family_members
                      SET name = ?, age = ?, job = ?, workplace = ?, salary = ?
                      WHERE id = ?''', (name, age, job, workplace, salary, member_id))
    conn.commit()
    conn.close()

def get_family_members():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM family_members')
    members = cursor.fetchall()
    conn.close()
    return members

def get_family_members_by_id(member_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM family_members WHERE id = ?', (member_id,))
    member = cursor.fetchone()
    conn.close()
    return member

def delete_family_member(member_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM family_members WHERE id = ?', (member_id,))
    cursor.execute('DELETE FROM family_expenses WHERE member_id = ?', (member_id,))  # Удаляем расходы
    conn.commit()
    conn.close()

# Добавляем расходы
def add_expense(member_id, expense_name, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO family_expenses (member_id, expense_name, amount)
                      VALUES (?, ?, ?)''', (member_id, expense_name, amount))
    conn.commit()
    conn.close()

def get_total_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM family_expenses")
    total_expenses = cursor.fetchone()[0] or 0
    conn.close()
    return total_expenses

def calculate_budget():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(salary) FROM family_members")
    total_income = cursor.fetchone()[0] or 0

    total_expenses = get_total_expenses()
    conn.close()

    if total_income == 0:
        return "Доходов нет, невозможно рассчитать бюджет."

    expense_ratio = (total_expenses / total_income) * 100
    if total_income >= total_expenses:
        return f"Профицит бюджета. Расходы составляют {expense_ratio:.2f}% от дохода."
    else:
        return f"Дефицит бюджета. Расходы составляют {expense_ratio:.2f}% от дохода."
