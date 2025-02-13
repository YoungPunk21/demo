import sqlite3

DB_NAME = "family_budget.db"

def init_db():
    """Создает базу данных и таблицы, если они еще не существуют."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Создаем таблицу для членов семьи
    cursor.execute('''CREATE TABLE IF NOT EXISTS family_members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        job TEXT NOT NULL,
                        workplace TEXT NOT NULL,
                        salary REAL NOT NULL)''')

    # Создаем таблицу для расходов
    cursor.execute('''CREATE TABLE IF NOT EXISTS family_expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        member_id INTEGER NOT NULL,
                        expense_name TEXT NOT NULL,
                        amount REAL NOT NULL,
                        FOREIGN KEY (member_id) REFERENCES family_members (id) ON DELETE CASCADE)''')
    
    conn.commit()
    conn.close()
