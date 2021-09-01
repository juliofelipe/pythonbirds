class Pessoa:
    def __init__(self, nome=None, idade=43):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá'


if __name__=='__main__':
    p = Pessoa()
    print(p.cumprimentar())
    p.nome = 'Julio'
    print(p.nome)