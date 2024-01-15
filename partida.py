import random

from typing import List

class Jogador:
    def __init__(self, nome: str, habilidade: int, estrela: bool = False) -> None:
        self.nome = nome
        self.habilidade = habilidade
        self.estrela = estrela

    def __str__(self):
        return f"{self.nome} (habilidade: {self.habilidade}, Star: {self.estrela})"

class Time:
    def __init__(self, nome: str, jogadores: List[Jogador]) -> None:
        self.nome = nome
        self.jogadores = jogadores

    def __str__(self) -> str:
        return f"{self.nome} - Star: {self.jogadores[0].nome}"

def mostra_time(time: Time) -> None:
    print(f"\n{time.nome} Roster:")
    for i, Jogador in enumerate(time.jogadores):
        print(f"{i+1}. {Jogador}")

def play_basketball() -> None:
    times: List[Time] = [
        Time("Golden State Warriors", [
            Jogador("Curry", 92, estrela=True),
            Jogador("klay", 80),
            Jogador("Kuminga", 80),
            Jogador("Green", 85),
            Jogador("Dario", 60),
        ]),
        Time("Los Angeles Lakers", [
            Jogador("Russel", 70),
            Jogador("Austin", 76),
            Jogador("Lebron", 89 , estrela=True),
            Jogador("Hachimura", 70),
            Jogador("Davis", 90),
        ]),
        Time("Milhaucke Bucks", [
            Jogador("Lillard", 88),
            Jogador("Middleton", 70),
            Jogador("Beasley", 73),
            Jogador("Lopez", 75),
            Jogador("Antepokoumpo", 90 , estrela=True),
        ]),
        Time("Boston Celtics", [
            Jogador("Holiday", 78),
            Jogador("Brown", 80),
            Jogador("Tatum,", 86 , estrela=True),
            Jogador("Horford", 78),
            Jogador("Porzings", 80),
        ]),
    ]

    print("Vamos jogar!")
    mostra_time(times[0])
    mostra_time(times[1])
    mostra_time(times[2])
    mostra_time(times[3])

    time_usuario = int(input("Escolha seu time (0-3): "))
    time_oponente = int(input("Escolha um oponente (0-3, excluindo seu time): "))

    time_atual = times[time_usuario]
    oponente = times[time_oponente]

    print(f"\n{time_atual.nome} vs {oponente.nome}")

    jogador_atual = 0
    pontuacao_adversario = 0
    pontuacao_usuario = 0
    posse_de_bola = True

    while pontuacao_adversario and pontuacao_usuario < 12:
        if posse_de_bola:
            print(f"\n{time_atual.nome} vem. {time_atual.jogadores[jogador_atual]} com a bola.")
            action = input("Escolha uma ação (passe, falta, infiltracao, arremesso): ").lower()

            if action == "passe":
                if jogador_atual < len(time_atual.jogadores) - 1:
                    jogador_atual += 1
                else:
                    jogador_atual = 0
            elif action == "falta":
                if random.randint(1, 100) <= time_atual.jogadores[jogador_atual].habilidade:
                    pontuacao_usuario += 1
                    print(f"Primeiro lance livre convertido. {pontuacao_usuario}")
                if random.randint(1, 100) <= time_atual.jogadores[jogador_atual].habilidade:
                    pontuacao_usuario += 1
                    print(f"Segundo lance livre convertido. {pontuacao_usuario}")
                else:
                    print("Errou!")
                posse_de_bola = False
            elif action == "infiltracao":
                if random.randint(1, 100) <= time_atual.jogadores[jogador_atual].habilidade:
                    pontuacao_usuario += 2
                    print(f"Cesta. Pontuação: {pontuacao_usuario}")
                else:
                    print("Errou!")
                posse_de_bola = False
            elif action == "arremesso":
                if random.randint(1, 100) <= time_atual.jogadores[jogador_atual].habilidade:
                    pontuacao_usuario += 3
                    print(f"Para três pontos! Pontuação: {pontuacao_usuario}")
                else:
                    print("Turnover!")
                posse_de_bola = False
            else:
                print("Ação inválida. Tente novamente.")
        else:
            print(f"\n{oponente.nome} com a bola.")
            if random.randint(1, 100) <= oponente.jogadores[0].habilidade:
                pontuacao_adversario += random.randint(1, 3)
                print(f"O oponente faz a cesta. Pontuação: {pontuacao_adversario}")
            else:
                print("Turnover do adversario")
            posse_de_bola = True

    print(f"\n{time_atual.nome} ganhou com a pontução de {pontuacao_usuario}!")


play_basketball()
