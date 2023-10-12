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
    caçador = 0
    mercador = 0
    lista_valor = []
    perguntas = [
        {
        "pergunta": "1) quando você vê um dinheiro perdido no chão, o que você faz?",
        "1": "a) pego para mim",
        "2": "b) levo para uma autoridade",
        "3": "c) eu mesmo procuro o dono",
        "4": "d) ignoro, não preciso disso",
        "a": "gatuno",
        'b': 'guerreiro',
        'c': 'clerigo',
        'd': 'mago'
    }, 
        {
        "pergunta": "2) quando você vê uma pessoa em apuros, o que você faz?",
        "1": "a) espero a briga acabar para roubar a pessoa",
        "2": "b) procuro saber oque está acontecendo antes de fazer algo",
        "3": "c) bato nos agressores",
        "4": "d) Não me importo, não é problema meu",
        "a": "gatuno",
        'b': 'guerreiro',
        'c': 'clerigo',
        'd': 'mago'
    },
        {
        "pergunta": "3) O que você faz se ver alguém ferido?",
        "1": "a) Me aproveito da situação e roubo a pessoa",
        "2": "b) Pergunto para a pessoa quem fez isso com ela",
        "3": "c) Procuro ajudar com uma poção de cura ou milagre",
        "4": "d) Ignoro o indivíduo",
        "a": "gatuno",
        'b': 'guerreiro',
        'c': 'clerigo',
        'd': 'mago'
    },
        {
        "pergunta": "4) Ao encontrar uma caverna em uma região desconhecida, oque você faz?",
        "1": "a) Entro nela, pode ter ítens preciosos",
        "2": "b) Procuro pistas que podem indicar que tipos de perigos ha na caverna",
        "3": "c) Procuro o vilarejo mais próximo que pode ter mais informações da caverna",
        "4": "d) Apenas entro, que tipo de problema pode haver",
        "a": "mercador",
        'b': 'mago',
        'c': 'clerigo',
        'd': 'guerreio'
    },
        {
        "pergunta": "5) Qual sua arma favorita?",
        "1": "a) espadas, são letais em batalha",
        "2": "b) conhecimento, não existe uma arma melhor do que o conhecimento",
        "3": "c) arco e clecha, Com um arco e clecha é possível derrotar um inimico a distância",
        "4": "d) machado, O machado é versátio para se defender e para coletar recursos",
        "a": "guerreiro",
        'b': 'mago',
        'c': 'caçador',
        'd': 'mercador'
    },
        {
        "pergunta": "6) O seu parceiro caiu em uma armadilha, e agora você precisa resolver um enigma extremamente difícil.",
        "1": "a) espadas, são letais em batalha",
        "2": "b) conhecimento, não existe uma arma melhor do que o conhecimento",
        "3": "c) arco e clecha, Com um arco e clecha é possível derrotar um inimico a distância",
        "4": "d) machado, O machado é versátio para se defender e para coletar recursos",
        "a": "guerreiro",
        'b': 'mago',
        'c': 'caçador',
        'd': 'mercador'
    }
    ]

    def __init__(self, resposta):
        self.resposta = resposta
        

    def quest(self):
        valores_certos = 'abcd'
        for i in range(len(self.perguntas)):
            values = self.perguntas[i].values()

            questao = list(values)

            print('\n')
            for value in questao[:5]:
                print(f'{value}')
            print('\n')

            self.resposta = input("Digite a resposta: ").lower()
            while self.resposta not in valores_certos or len(self.resposta) > 1:
                print('Você digitou um valor inválido, tente de novo!')
                print('\n')
                for value in values:
                    print(f'{value}')
                print('\n')
                self.resposta = input("Digite a resposta: \n").lower()
            comp = self.perguntas[i].get(self.resposta)
            questionario.atribui_pontos(questionario, comp)
    

    def atribui_pontos(self, comp):
        if comp == "gatuno":
            self.gatuno += 1
        elif comp == "guerreiro":
            self.guerreiro += 1
        elif comp == "clerigo":
            self.clerigo += 1
        elif comp == "mago":
            self.mago += 1
        elif comp == "caçador":
            self.caçador += 1
        elif comp == "mercador":
            self.mercador += 1



    def compara_valores(self):
        value = f'gatuno={self.gatuno}\nguerreiro={self.guerreiro}\nclerigo={self.clerigo}\nmago={self.mago}\ncaçador={self.caçador}\nmercador={self.mercador}'
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





    