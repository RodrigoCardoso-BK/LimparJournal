import tkinter as tk
from tkinter import messagebox
import time
import service


def limpar_journal():
    service.deleta_arquivos_journal()
    messagebox.showinfo("Resultado", "Limpeza executada com sucesso!")

# Configuração da interface Tkinter
janela = tk.Tk()
janela.title("Limpar Journal")
janela.geometry("200x100")

# Botão para iniciar a função
btn_iniciar = tk.Button(janela, text="Iniciar Função", command=limpar_journal)
btn_iniciar.pack(pady=20)

# Executa a interface
janela.mainloop()
