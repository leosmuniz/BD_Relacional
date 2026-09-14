class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade 

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

pessoa1 = pessoa("Joaquim", "19")
pessoa2 = pessoa("Fabão", "38")

pessoa1.apresentar()
pessoa2.apresentar()