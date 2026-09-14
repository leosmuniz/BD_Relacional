class carro:
    def __init__(self,combustivel):
        self.__combustivel = combustivel

    def abastecer(self,litros):
        self.__combustivel += litros

    def dirigir(self,distancia):
        self.__combustivel -= (distancia*0.1)

    def ver_combustivel(self):
        return self.__combustivel

carro1 = carro(0)
carro1.abastecer(50)
print(carro1.ver_combustivel())
carro1.dirigir(200)
print(carro1.ver_combustivel())