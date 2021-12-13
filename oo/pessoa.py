class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=26):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    mendes = Pessoa(nome='Mendes')
    madisse = Pessoa(mendes, nome='Madisse')
    print(Pessoa.cumprimentar(madisse))
    print(id(madisse))
    print(madisse.cumprimentar())
    print(madisse.nome)
    print(madisse.idade)
    for filho in madisse.filhos:
        print(filho.nome)
    madisse.sobrenome = 'Jose'
    del madisse.filhos
    madisse.olhos = 1
    del madisse.olhos
    print(madisse.__dict__)
    print(mendes.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(madisse.olhos)
    print(mendes.olhos)
    print(id(Pessoa.olhos), id(madisse.olhos), id(mendes.olhos))