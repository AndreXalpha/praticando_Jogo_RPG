import numpy as np
from monstro import Monstro

class Caverna:
    tipos_monstros = ["ogro", "morcego", "slime", "goblin", "topera", "zumbi", "mumia", "esqueleto"]

    def __init__(self, andar=1, nivel=1, qnt_monstro=None, m1=None, m2=None, m3=None):
        self.andar = andar
        self.nivel = nivel
        self.qnt_monstro = qnt_monstro
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_qnt_monstro(self):
        return self.qnt_monstro
    
    def get_m1(self):
        return self.m1
    
    def get_m2(self):
        return self.m2
    
    def get_m3(self):
        return self.m3

    def spown(self):
        self.qnt_monstro = np.random.randint(1,3)
        loc_tipo = np.random.randint(0,7)
        loc_tipo2 = np.random.randint(0,7)
        loc_tipo3 = np.random.randint(0,7)

        nm1 = self.tipos_monstros[loc_tipo]
        nm2 = self.tipos_monstros[loc_tipo2]
        nm3 = self.tipos_monstros[loc_tipo3]

        if self.qnt_monstro == 1:
            self.m1 = Monstro(nm1, 1)
            print("1 -", self.m1.get_nome(), self.m1.get_hpmonstro())
        elif self.qnt_monstro == 2:
            self.m1 = Monstro(nm1, 1)
            self.m2 = Monstro(nm2, 2)
            print("1 -", self.m1.get_nome(), self.m1.get_hpmonstro())
            print("2 -", self.m2.get_nome(), self.m2.get_hpmonstro())

        elif self.qnt_monstro == 3:
            loc_tipo = np.random.randint(0,7)
            self.m1 = Monstro(nm1, 1)
            self.m2 = Monstro(nm2, 2)
            self.m3 = Monstro(nm3, 3)
            print("1 -", self.m1.get_nome(), self.m1.get_hpmonstro())
            print("2 -", self.m2.get_nome(), self.m2.get_hpmonstro())
            print("3 -", self.m3.get_nome(), self.m3.get_hpmonstro())
