class Pessoa:
    def __init__(self, nome=None, idade=26):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Madisse')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Mendes'
    print(p.nome)
    print(p.idade)