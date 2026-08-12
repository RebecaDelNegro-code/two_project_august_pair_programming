import json
import os
import unicodedata
from tkinter import *
from tkinter import messagebox, ttk
from faker import Faker

fake = Faker("pt_BR")


class NailDesignerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Studio de Nail Design - Sistema Profissional")
        self.root.geometry("450x680")
        self.root.config(bg="#FFF5F7")
        self.root.resizable(False, False)

        # Configuração de Estilo Visual (TTK)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", padding=5)
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 9, "bold"),
            background="#FCE4EC",
            foreground="#880E4F",
        )
        style.configure("Treeview", font=("Segoe UI", 9), rowheight=26)

        # Dicionário com os 4 modelos e preços
        self.modelos_data = {
            "Glazed Donut (Perola)": {"preco": "R$ 110,00"},
            "Ombre com Glitter": {"preco": "R$ 130,00"},
            "Metalizada (Foil)": {"preco": "R$ 140,00"},
            "Abstrata Minimalista": {"preco": "R$ 160,00"},
        }

        # --- Cabeçalho Moderno ---
        header_frame = Frame(root, bg="#C2185B", height=60)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)

        Label(
            header_frame,
            text="💅 Studio de Nail Design & Gestão",
            font=("Segoe UI", 14, "bold"),
            bg="#C2185B",
            fg="white",
        ).pack(side=LEFT, padx=20)

        # --- Frame Principal (Layout Vertical otimizado) ---
        main_frame = Frame(root, bg="#FFF5F7")
        main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

        # --- Seção Superior: Cadastro de Clientes e Serviços ---
        top_frame = LabelFrame(
            main_frame,
            text=" Novo Agendamento ",
            bg="#FFFFFF",
            fg="#C2185B",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=10,
        )
        top_frame.pack(fill=X, pady=(0, 10))

        Label(
            top_frame,
            text="Nome da Cliente:",
            bg="#FFFFFF",
            font=("Segoe UI", 9),
            fg="#333333",
        ).pack(anchor=W, pady=(2, 0))
        self.entry_nome = Entry(
            top_frame, font=("Segoe UI", 10), relief=SOLID, bd=1
        )
        self.entry_nome.pack(fill=X, pady=(2, 8))

        Label(
            top_frame,
            text="Telefone:",
            bg="#FFFFFF",
            font=("Segoe UI", 9),
            fg="#333333",
        ).pack(anchor=W)
        self.entry_tel = Entry(
            top_frame, font=("Segoe UI", 10), relief=SOLID, bd=1
        )
        self.entry_tel.pack(fill=X, pady=(2, 8))

        btn_faker = Button(
            top_frame,
            text="✨ Gerar Cliente Falso",
            bg="#F8BBD0",
            fg="#880E4F",
            font=("Segoe UI", 9, "bold"),
            relief=FLAT,
            cursor="hand2",
            command=self.gerar_faker,
        )
        btn_faker.pack(fill=X, pady=2)

        Label(
            top_frame,
            text="Selecione o Estilo:",
            bg="#FFFFFF",
            font=("Segoe UI", 9),
            fg="#333333",
        ).pack(anchor=W, pady=(8, 0))
        self.var_modelo = StringVar()
        self.combo_modelo = ttk.Combobox(
            top_frame,
            textvariable=self.var_modelo,
            values=list(self.modelos_data.keys()),
            state="readonly",
        )
        self.combo_modelo.pack(fill=X, pady=(2, 8))
        self.combo_modelo.bind("<<ComboboxSelected>>", self.atualizar_preco)

        self.lbl_preco = Label(
            top_frame,
            text="Preço: R$ 0,00",
            font=("Segoe UI", 11, "bold"),
            bg="#FFFFFF",
            fg="#C2185B",
        )
        self.lbl_preco.pack(anchor=W, pady=2)

        btn_cadastrar = Button(
            top_frame,
            text="Confirmar Agendamento",
            bg="#C2185B",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=FLAT,
            cursor="hand2",
            command=self.cadastrar,
        )
        btn_cadastrar.pack(fill=X, pady=(8, 2))

        # --- Seção Inferior: Tabela de Agendamentos ---
        bottom_frame = LabelFrame(
            main_frame,
            text=" Agendamentos Realizados ",
            bg="#FFFFFF",
            fg="#C2185B",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=10,
        )
        bottom_frame.pack(fill=BOTH, expand=True)

        tabela_container = Frame(bottom_frame, bg="#FFFFFF")
        tabela_container.pack(fill=BOTH, expand=True)

        self.tabela = ttk.Treeview(
            tabela_container,
            columns=("Nome", "Modelo", "Preço"),
            show="headings",
            height=5,
        )
        self.tabela.heading("Nome", text="Cliente")
        self.tabela.heading("Modelo", text="Serviço")
        self.tabela.heading("Preço", text="Valor")

        self.tabela.column("Nome", width=130)
        self.tabela.column("Modelo", width=140)
        self.tabela.column("Preço", width=80)

        self.tabela.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            tabela_container, orient="vertical", command=self.tabela.yview
        )
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tabela.configure(yscrollcommand=scrollbar.set)

        # Botão de Exportação Direta para JSON
        btn_exportar = Button(
            bottom_frame,
            text="💾 Exportar Agendamentos (JSON)",
            bg="#880E4F",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief=FLAT,
            cursor="hand2",
            command=self.exportar_json,
        )
        btn_exportar.pack(fill=X, pady=(8, 0))

        self.combo_modelo.current(0)
        self.atualizar_preco(None)

    def gerar_faker(self):
        self.entry_nome.delete(0, END)
        self.entry_nome.insert(0, fake.name())
        self.entry_tel.delete(0, END)
        self.entry_tel.insert(0, fake.phone_number())

    def atualizar_preco(self, event):
        modelo = self.var_modelo.get()
        if not modelo:
            return
        info = self.modelos_data[modelo]
        self.lbl_preco.config(text=f"Preço: {info['preco']}")

    def cadastrar(self):
        nome = self.entry_nome.get().strip()
        modelo = self.var_modelo.get()

        if not nome or not modelo:
            messagebox.showerror(
                "Erro", "Preencha o nome da cliente e selecione um modelo!"
            )
        else:
            preco = self.modelos_data[modelo]["preco"]
            self.tabela.insert("", END, values=(nome, modelo, preco))
            messagebox.showinfo(
                "Sucesso", f"Agendamento para {nome} realizado com sucesso!"
            )
            self.entry_nome.delete(0, END)
            self.entry_tel.delete(0, END)

    def exportar_json(self):
        # Obtém todos os itens cadastrados na tabela
        itens = self.tabela.get_children()

        if not itens:
            messagebox.showwarning(
                "Aviso", "Não há nenhum agendamento na tabela para exportar!"
            )
            return

        agendamentos = []
        for item in itens:
            valores = self.tabela.item(item, "values")
            agendamentos.append(
                {"cliente": valores[0], "servico": valores[1], "valor": valores[2]}
            )

        # Salva diretamente na pasta onde o arquivo .py está localizado
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(pasta_atual, "agendamentos.json")

        try:
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump(agendamentos, f, ensure_ascii=False, indent=4)
            messagebox.showinfo(
                "Sucesso",
                f"Dados salvos com sucesso na pasta do projeto!\n\nArquivo: agendamentos.json",
            )
        except Exception as e:
            messagebox.showerror(
                "Erro ao Salvar", f"Ocorreu um erro ao salvar o arquivo:\n{e}"
            )


if __name__ == "__main__":
    root = Tk()
    app = NailDesignerApp(root)
    root.mainloop()