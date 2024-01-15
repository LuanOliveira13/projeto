import random
from typing import Optional

# Importa o módulo 'random' para gerar números aleatórios e 'Optional' do 'typing'.

class Cliente:
    def __init__(self, nome: str):
        self.nome = nome
        self.conta = Conta()
        self.estoque = Estoque()

# A classe 'Cliente' representa um cliente.
# Cada cliente tem um nome , uma conta bancária e um estoque.

    def transferir(self, valor: float):
        self.conta.sacar(valor)

# O método 'transferir' permite que o cliente deposite ('depositar')
# uma certa quantia ('valor') em sua conta.

    def adicionar_produto(self, produto):
        self.estoque.adicionar_produto(produto)

# O método 'adicionar_produto' permite que o cliente
# adicione um produto ('produto') ao seu estoque.

    def vender_produto(self, nome: str, quantidade: int) -> None:
        produto = self.estoque.pesquisar_produto(nome)
        if produto:
            if self.estoque.validar_venda(produto, quantidade):
                self.conta.depositar(produto.calcular_total(quantidade))
                produto.quantidade -= quantidade
            else:
                print("Erro ao realizar a venda.")
        else:
            print("Saldo insuficiente.")
            
# O método 'vender_produto' permite que o cliente venda um produto.
# Ele primeiro verifica se o produto está no estoque,
# depois verifica se o saldo da conta é suficiente para a transação e,
# finalmente, valida a venda. Se todas as verificações passarem,
# a venda é feita e a quantidade do produto é reduzida.

            
    def comprar_produto(self, nome: str, preco: float, quantidade: int) -> None:
        produto_existente = self.estoque.pesquisar_produto(nome)
        if produto_existente:
            if self.saldo_suficiente(quantidade * preco):
                self.conta.sacar(quantidade * preco)
                produto_existente.quantidade += quantidade
            else:
                print("Saldo insuficiente.")
        else:
            produto = Produto(nome, preco, quantidade)
            if self.saldo_suficiente(quantidade * preco):
                self.conta.sacar(quantidade * preco)
                self.estoque.adicionar_produto(produto)
            else:
                print("Saldo insuficiente.")


# O método comprar_produto funciona de maneira semelhante ao método vender_produto,
# exceto que ele pesquisa um produto, e caso ele não encontre,
# adiciona um novo produto e chama o método sacar da conta do cliente com o valor da compra,
# o que diminui o saldo do cliente.


    def saldo_suficiente(self, valor: float) -> bool:
        return self.conta.saldo >= valor

# O método 'saldo_suficiente' verifica se o saldo da conta
# é suficiente para uma determinada quantia.

class Conta:
    def __init__(self, numero=None, saldo=0.0):
        self.numero = numero or self.gerar_numero()
        self.saldo = saldo

    # A classe 'Conta' representa uma conta bancária.

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado na conta {self.numero}.")

    # O método 'depositar' permite que o cliente deposite uma certa quantia ('valor') em sua conta.

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado na conta {self.numero}.")
        else:
            print("Saldo insuficiente.")

    # O método 'sacar' permite que o cliente retire uma certa quantia ('valor') de sua conta.

    def mostra_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    # O método 'mostra_saldo' exibe o saldo atual da conta.

    @staticmethod
    def gerar_numero() -> int:
        return random.randint(100000, 999999)

    # O método 'gerar_numero' gera um número aleatório para a conta.

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

# A classe 'Produto' representa um produto.
# Cada produto tem um nome, um preço e uma quantidade.

    def calcular_total(self, quantidade: int) -> float:
        return self.preco * quantidade

    # O método 'calcular_total' calcula o custo total de uma certa quantidade de um produto.

class Estoque:
    def __init__(self):
        self.produtos = []

    # A classe 'Estoque' representa um estoque. Cada estoque tem uma lista de produtos ('produtos').

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)


# O método 'adicionar_produto' permite que o cliente adicione
# um produto ('produto') ao seu estoque.

    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)

    # O método 'remover_produto' permite que o cliente remova um produto ('produto') do seu estoque.

    def pesquisar_produto(self, nome: str) -> Optional[Produto]:
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

# O método 'pesquisar_produto' permite que o cliente pesquise
# um produto pelo nome em seu estoque.

    def exibir_estoque(self) -> None:
        for produto in self.produtos:
            print(f"Nome: {produto.nome} | Preço: R${produto.preco} | Quantidade: {produto.quantidade}")

    # O método 'exibir_estoque' exibe todos os produtos no estoque.

    def validar_venda(self, produto: Produto, quantidade: int) -> bool:
        if self.pesquisar_produto(produto.nome):
            if produto.quantidade >= quantidade:
                return True
            else:
                print("Produtos insuficientes em estoque.")
                return False
        else:
            print("Produto não encontrado.")
            return False

# O método 'validar_venda' valida uma venda.
# Ele verifica se o produto está no estoque
# e se a quantidade do produto é suficiente para a venda.

# Exemplo de uso
cliente = Cliente("João")
cliente.conta.depositar(500)
cliente.adicionar_produto(Produto("Lápis", 50, 10))
cliente.adicionar_produto(Produto("Caderno", 20.0, 5))
cliente.comprar_produto("Criptomoeda", 20.0, 5)
cliente.comprar_produto("Criptomoeda", 20.0, 6)
cliente.vender_produto("Lápis", 10)
cliente.conta.mostra_saldo()
cliente.estoque.exibir_estoque()
