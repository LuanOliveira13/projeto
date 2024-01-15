import random
from typing import Optional

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.conta = Conta()
        self.estoque = Estoque()

    def transferir(self, valor: float):
        self.conta.depositar(valor)

    def adicionar_produto(self, produto):
        self.estoque.adicionar_produto(produto)

    def vender_produto(self, nome: str, quantidade: int):
        produto = self.estoque.pesquisar_produto(nome)
        if produto and produto.quantidade >= quantidade:
            self.conta.sacar(produto.calcular_total(quantidade))
            produto.quantidade -= quantidade
        else:
            print("Produto não encontrado ou quantidade insuficiente.")

class Conta:
    def __init__(self, numero=None, saldo=0.0):
        self.numero = numero or self.gerar_numero()
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado na conta {self.numero}.")

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado na conta {self.numero}.")
        else:
            print("Saldo insuficiente.")
            
    def mostra_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    @staticmethod
    def gerar_numero() -> int:
        return random.randint(100000, 999999)

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self, quantidade: int) -> float:
        return self.preco * quantidade

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)

    def pesquisar_produto(self, nome: str) -> Optional[Produto]:
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def exibir_estoque(self) -> None:
        for produto in self.produtos:
            print(f"Nome: {produto.nome} | Preço: R${produto.preco} | Quantidade: {produto.quantidade}")

# Exemplo de uso
cliente = Cliente("João")
cliente.conta.depositar(500)
cliente.adicionar_produto(Produto("Lápis", 0.5, 10))
cliente.adicionar_produto(Produto("Caderno", 20, 5))

cliente.vender_produto("Lápis", 2)
cliente.vender_produto("Caneta", 1) # Produto não encontrado

cliente.conta.sacar(100)
cliente.conta.mostra_saldo()
cliente.estoque.exibir_estoque()