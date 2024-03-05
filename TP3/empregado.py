from pessoa import Pessoa

class Empregado(Pessoa):

    lista_empregados = []

    def __init__(self, nome, morada, telefone, idpessoa, codigo_setor, salario_base=1200, imposto=10):
        super().__init__(nome, morada, telefone, idpessoa)
        self.__codigo_setor = codigo_setor
        self.__salario_base = salario_base
        self.__imposto = imposto

    @property
    def codigo_setor(self):
        return self.__codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        self.__imposto = imposto

    def calcular_salario(self):
        salario_liquido = self.__salario_base - (self.__salario_base * (self.__imposto / 100))
        return salario_liquido

    def __str__(self):
        return f"{super().__str__()}\nCódigo Setor: {self.__codigo_setor}\nSalário Base: {self.__salario_base}€\nImposto: {self.__imposto}%"
    

if __name__ == "__main__":

    pessoa1 = Pessoa("Wanna Maise", "Faro", "978654321")
    empregado1 = Empregado(pessoa1.nome, pessoa1.morada, pessoa1.telefone, "12340", 1200, 10)
    
    salario1 = empregado1.calcular_salario()

    print(empregado1)
    print(f"Salário Liquido: {salario1}€")
