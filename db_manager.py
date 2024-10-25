import sqlite3

def init_db():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            script TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_task(task_name):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT script FROM tarefas WHERE nome = ?", (task_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def add_task(task_name, task_script):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (nome, script) VALUES (?, ?)", (task_name, task_script))
    conn.commit()
    conn.close()
