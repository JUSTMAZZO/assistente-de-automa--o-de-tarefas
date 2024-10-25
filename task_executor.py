import pyautogui
from tkinter import messagebox

def execute_task(script):
    try:
        exec(script)
    except Exception as e:
        messagebox.showerror("Erro de Execução", f"Ocorreu um erro ao executar a tarefa: {e}")
