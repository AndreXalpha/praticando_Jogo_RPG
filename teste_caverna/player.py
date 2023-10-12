from monstro import Monstro
from caverna import Caverna
class Player:
    def __init__(self, nome=None, hp=100, dano=10, defesa=5):
        self.nome = nome
        self.hp = hp
        self.dano = dano
        self.defesa = defesa

    def ataque(monstro):
        if Caverna.get_qnt_monstro() == 1:
            Caverna.get_m1(Monstro.set_hpmonstro())