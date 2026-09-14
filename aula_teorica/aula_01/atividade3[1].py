class veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print()

class carro(veiculo):
    pass
        

class moto(veiculo):
    pass

carro1 = carro("Fiat","UNO",2000)
moto1 = moto("Honda","CG",2010)

carro1.exibir_dados()
moto1.exibir_dados()
