'''
Tabala ascii,
A Tabela ASCII (American Standard Code for Information Interchange) é 
como um "dicionário" que os computadores usam para entender letras, números e símbolos.
Como os computadores só entendem números (código binário: 0s e 1s), a Tabela ASCII atribui 
um número específico para cada caractere.

Tabela hexadecimal
Tabela Hexadecimal (ou tabela de base 16) é um sistema de
numeração muito usado na computação para representar números binários 
(0s e 1s) de uma forma muito mais curta e fácil de ler para nós, humanos.
'''





import secrets
import string
import tkinter as tk
from tkinter import messagebox

# ==========================================
# PALETA DE CORES DEFINIDA
# ==========================================
COLOR_AZUL_ESC = "#004d6e"  # Fundo da tela
COLOR_AZUL_MED = "#0081ab"  # Bordas e detalhes
COLOR_AZUL_CLA = "#00b1cd"  # Destaque do texto
COLOR_VERDE    = "#a6c844"  # Botão Gerar
COLOR_ROSA     = "#b83764"  # Alertas / Destaques secundários
COLOR_AMARELO  = "#edce01"  # Botão Copiar
COLOR_ACO      = "#4a3336"  # Fundo dos campos e cards
COLOR_TEXTO    = "#ffffff"  # Texto claro para contraste

# ==========================================
# FUNÇÕES LÓGICAS
# ==========================================
def gerar_senha():
    """Gera a senha com base no tamanho informado no campo de entrada."""
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            messagebox.showerror("Erro", "O tamanho deve ser maior que zero!")
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        
        # Atualiza o campo com a nova senha
        entry_senha.config(state="normal")
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
        entry_senha.config(state="readonly")
        
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite apenas números inteiros no tamanho!")

def copiar_senha():
    """Copia a senha gerada para a área de transferência do sistema."""
    senha = entry_senha.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Atenção", "Gere uma senha primeiro antes de copiar!")

# ==========================================
# CONSTRUÇÃO DA INTERFACE GRÁFICA (GUI)
# ==========================================
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x320")
janela.configure(bg=COLOR_AZUL_ESC)
janela.resizable(False, False)

# --- Título ---
label_titulo = tk.Label(
    janela, 
    text="🎀GERADOR DE SENHAS🎀", 
    font=("Arial", 14, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA
)
label_titulo.pack(pady=15)

# --- Frame Card (Aço) ---
card = tk.Frame(
    janela, 
    bg=COLOR_ACO, 
    padx=15, 
    pady=15, 
    highlightbackground=COLOR_AZUL_MED, 
    highlightthickness=2
)
card.pack(pady=5, fill="x", padx=20)

# --- Campo: Tamanho da Senha ---
label_tamanho = tk.Label(card, text="Tamanho da Senha:", font=("Arial", 10, "bold"), bg=COLOR_ACO, fg=COLOR_TEXTO)
label_tamanho.grid(row=0, column=0, sticky="w", pady=5)

entry_tamanho = tk.Entry(card, font=("Arial", 10), width=8, justify="center")
entry_tamanho.insert(0, "12")  # Valor padrão
entry_tamanho.grid(row=0, column=1, sticky="e", pady=5)

# --- Campo: Senha Gerada ---
label_resultado = tk.Label(card, text="Senha Gerada:", font=("Arial", 10, "bold"), bg=COLOR_ACO, fg=COLOR_TEXTO)
label_resultado.grid(row=1, column=0, sticky="w", pady=5)

entry_senha = tk.Entry(
    card, 
    font=("Arial", 11, "bold"), 
    bg=COLOR_AZUL_ESC, 
    fg=COLOR_AZUL_CLA, 
    state="readonly", 
    justify="center"
)
entry_senha.grid(row=1, column=1, pady=5)

# --- Botão: Gerar Senha ---
btn_gerar = tk.Button(
    janela, 
    text="GERAR SENHA", 
    font=("Arial", 11, "bold"), 
    bg=COLOR_VERDE, 
    fg="#000000", 
    activebackground=COLOR_AZUL_MED,
    command=gerar_senha,
    cursor="hand2",
    relief="flat"
)
btn_gerar.pack(pady=12, fill="x", padx=35)

# --- Botão: Copiar Senha ---
btn_copiar = tk.Button(
    janela, 
    text="COPIAR SENHA", 
    font=("Arial", 10, "bold"), 
    bg=COLOR_AMARELO, 
    fg="#000000", 
    activebackground=COLOR_ROSA,
    command=copiar_senha,
    cursor="hand2",
    relief="flat"
)
btn_copiar.pack(pady=2, fill="x", padx=35)

# Inicia a aplicação
if __name__ == "__main__":
    janela.mainloop()