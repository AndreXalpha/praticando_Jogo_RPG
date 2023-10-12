#Criar um questionário a fim de recomendar para o jogador uma das classes disponíveis
#O questionário vai ser baseado em dicionários que vão definir as perguntas e respostas
#Não vai ter resposta errada, cada resposta vai definir a personalidade do jogador
#Com base nas respostas vão ser atribuidos pontos para cada classe
#A classe que no final do questionário tiver mais pontos, vai ser recomendada para o jogador



class questionario:
    guerreiro = 0
    gatuno = 0
    clerigo = 0
    mago = 0
    recomendacao = ''
    lista_valor = []
    perguntas = [{
        "pergunta": "1) quando você vê um dinheiro perdido no chão, o que você faz?",
        "a": "a) pego para mim",
        "b": "b) levo para uma autoridade",
        "c": "c) eu mesmo procuro o dono",
        "d": "d) ignoro, não preciso disso"
    }, {
        "pergunta": "2) quando você vê uma pessoa em apuros, o que você faz?",
        "a": "a) espero a briga acabar para roubar a pessoa",
        "b": "b) procuro saber oque está acontecendo antes de fazer algo",
        "c": "c) bato nas pessoas que estão batendo nela",
        "d": "d) Não me importo, não é problema meu"
    }]

    def __init__(self, resposta):
        self.resposta = resposta
        
    def quest(self):
        valores_certos = 'abcd'
        for i in range(len(self.perguntas)):
            values = self.perguntas[i].values()
            print('\n')
            for value in values:
                print(f'{value}')
            print('\n')
            self.resposta = input("Digite a resposta: \n")
            while self.resposta not in valores_certos or len(self.resposta) > 1:
                print('Você digitou um valor inválido, tente de novo!')
                print('\n')
                for value in values:
                    print(f'{value}')
                print('\n')
                self.resposta = input("Digite a resposta: \n")
            questionario.atribui_pontos(questionario)
    
    def atribui_pontos(self):
        if self.resposta == "a":
            self.gatuno += 1
        elif self.resposta == "b":
            self.guerreiro += 1
        elif self.resposta == "c":
            self.clerigo += 1
        elif self.resposta == "d":
            self.mago += 1 

    def compara_valores(self):
        value = f'gatuno={self.gatuno}\nguerreiro={self.guerreiro}\nclerigo={self.clerigo}\nmago={self.mago}'
        dic_class = dict([i.split('=') for i in value.strip().split('\n')])
        lista = []
        for i in dic_class.items():
            x = tuple(i)
            lista.append(x)
        for k, j in lista:
            self.lista_valor.append(j)
        self.lista_valor.sort()
        maior_valor = self.lista_valor[-1]
        for classe in lista:
            if classe[1] == maior_valor:
                print(f"\nA classe recomendada para você é {classe[0]}\n")


questionario.quest(questionario)
questionario.compara_valores(questionario)





    