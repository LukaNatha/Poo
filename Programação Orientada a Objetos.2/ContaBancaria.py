import tkinter as tk
from tkinter import messagebox, simpledialog

class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self.__bairro

    def get_cidade(self):
        return self.__cidade

    def exibir_dados(self):
        return f"Rua: {self.__rua}, Nº {self.__numero} - {self.__bairro}, {self.__cidade}"


class Cliente:
    def __init__(self, nome, cpf, rua, numero, bairro, cidade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = Endereco(rua, numero, bairro, cidade)
        self.__contas = []

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def exibir_dados(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\n{self.__endereco.exibir_dados()}"

    def __str__(self):
        return self.__nome
    

class ContaBancaria:
    def __init__(self, cliente, numero, saldo_inicial=0.0):
        self.__titular = cliente
        self.__numero = numero
        self.__saldo = saldo_inicial

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo = self.__saldo - valor
                return True
            else:
                return False
        else:
            return False

    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo = self.__saldo - valor
                conta_destino.depositar(valor)
                return True
            else:
                return False
        else:
            return False

    def exibir_dados(self):
        nome = self.__titular.get_nome()
        cpf = self.__titular.get_cpf()
        endereco_obj = self.__titular.get_endereco()
        rua = endereco_obj.get_rua()
        bairro = endereco_obj.get_bairro()
        
        return f"Nome do Cliente: {nome}\nCPF: {cpf}\nNome da Rua: {rua}\nNome do Bairro: {bairro}\nNúmero da Conta: {self.__numero}\nSaldo: R$ {self.__saldo:.2f}"

class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo_inicial, limite, tarifa_mensal):
        super().__init__(cliente, numero, saldo_inicial)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal
    
    
    






class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1  = Cliente("Ana", "004.045")
        cliente2 = Cliente("Arthur", "023.450")        

        self.contas = [
            ContaBancaria("João", 1001, 500),
            ContaBancaria("Maria", 1002, 1000),
            ContaBancaria("Pedro", 1003, 300),
            ContaBancaria("Esther", 1004, 20)
        ]

        messagebox.showinfo("Sucesso", "Depósito realizado.")

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )
            btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_taxa(c)
            )
            btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
    
    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_taxa()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")
        
        Cliente1 = Cliente("João", "111.111.111-11", "Av Horizonte ao longe", 1000, "Centro", "Espírito Santo")
        Cliente2 = Cliente("Maria", "222.222.222-22", "Rua das Flores", 50, "Bairro Alto", "Santa Cruz")
        Cliente3 = Cliente("Pedro", "333.333.333-33", "Av Central", 200, "Praia", "Drumond")
        Cliente4 = Cliente("Esther", "444.444.444-44", "Rua Nova", 12, "Vila Nova", "Compinense")
        Cliente5 = Cliente("Carlos", "555.555.555-55", "Rua Oito", 77, "Interior", "Soladolândia")

        self.contas = [
            ContaBancaria(Cliente1, 1001, 500),
            ContaBancaria(Cliente2, 1002, 1000),
            ContaBancaria(Cliente3, 1003, 300),
            ContaBancaria(Cliente4, 1004, 20),
            ContaBancaria(Cliente5, 1005, 150)
        ]

        if self.existe_conta_duplicada():
            duplicados = self.obter_numeros_duplicados()
            texto_duplicados = ", ".join(str(num) for num in duplicados)
            messagebox.showerror(
                "Erro Crítico", 
                f"Foram encontrados números de contas duplicados: {texto_duplicados}"
            )
            self.janela.destroy()

        self.criar_interface()

    def existe_conta_duplicada(self):
        numeros = []
        for conta in self.contas:
            numero = conta.get_numero()
            if numero in numeros:
                return True
            else:
                numeros.append(numero)
        return False

    def obter_numeros_duplicados(self):
        numeros = []
        numeros_duplicados = []
        for conta in self.contas:
            numero = conta.get_numero()
            if numero in numeros:
                if numero not in numeros_duplicados:
                    numeros_duplicados.append(numero)
            else:
                numeros.append(numero)
        return numeros_duplicados

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            btn_dados.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")
        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")
        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")
        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")
        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")
        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None
        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())


janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()