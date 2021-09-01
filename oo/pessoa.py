class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá'


# >>> julio.nome
# 'Julio'
# >>> julio.idade
# 43
# >>> for filho in julio.filhos:
# ...     print(filho.nome)
# ... 
# Andre

# >>> from oo.pessoa import Pessoa
# >>> andre = Pessoa(nome='Andre')
# >>> julio = Pessoa(andre, nome='Julio')
# >>> julio.sobrenome = 'Felipe'
# >>> print(julio.__dict__)
# {'idade': 43, 'nome': 'Julio', 'filhos': [<oo.pessoa.Pessoa object at 0x000001BD4A73D340>], 'sobrenome': 'Felipe'} 
# >>> del julio.filhos
# >>> print(julio.__dict__)
# {'idade': 43, 'nome': 'Julio', 'sobrenome': 'Felipe'}
# >>> from oo.pessoa import Pessoa
# >>> Pessoa.olhos
# 2
# >>> julio = Pessoa(None, nome='Julio')
# >>> julio.__dict__
# {'idade': 43, 'nome': 'Julio', 'filhos': [None]}
# >>> julio.olhos
# 2
# >>> julio.olhos = 1
# >>> julio.__dict__
# {'idade': 43, 'nome': 'Julio', 'filhos': [None], 'olhos': 1}
# >>> del julio.olhos
# >>> julio.__dict__
# {'idade': 43, 'nome': 'Julio', 'filhos': [None]}
# >>>