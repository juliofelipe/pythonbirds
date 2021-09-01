class Pessoa:
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

  