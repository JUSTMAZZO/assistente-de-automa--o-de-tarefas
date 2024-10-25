import tkinter as tk
from tkinter import messagebox
from db_manager import init_db, get_task, add_task
from task_executor import execute_task
from speech_recognition import recognize_speech

def process_command(command_text):
    task_script = get_task(command_text)
    if task_script:
        execute_task(task_script)
    else:
        messagebox.showinfo("Tarefa não encontrada", "A tarefa não existe no banco de dados.")
        # Adicione funcionalidade para criar uma nova tarefa, se necessário

def start_app():
    app = tk.Tk()
    app.title("Assistente de Tarefas Automáticas")

    tk.Label(app, text="Digite ou fale o comando da tarefa:").pack()
    command_entry = tk.Entry(app, width=50)
    command_entry.pack()

    tk.Button(app, text="Enviar", command=lambda: process_command(command_entry.get())).pack()
    tk.Button(app, text="Comando de Voz", command=lambda: recognize_speech(command_entry)).pack()

    init_db()  # Inicializa o banco de dados na primeira execução
    app.mainloop()

if __name__ == "__main__":
    start_app()
