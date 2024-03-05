from empregado import Empregado

class Vendedor(Empregado):

    lista_vendedores = []

    def __init__(self, nome, morada, telefone, idpessoa, codigo_setor, salario_base, imposto, valor_vendas=0, comissao=10):
        super().__init__(nome, morada, telefone, idpessoa, codigo_setor, salario_base, imposto)
        self.__valor_vendas = valor_vendas
        self.__comissao = comissao

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        self.__valor_vendas = valor_vendas

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def calcular_salario(self):
        salario_liquido = super().calcular_salario() + (self.__valor_vendas * (self.__comissao / 100))
        return salario_liquido

    def __str__(self):
        return f"{super().__str__()}\nValor de Vendas: {self.__valor_vendas}€\nComissão: {self.__comissao}%"


if __name__ == "__main__":

    empregado1 = Empregado("Wanna Maise", "Faro", "978654321", "12340", 1200, 10)
    vendedor1 = Vendedor(empregado1.nome, empregado1.morada, empregado1.telefone, empregado1.codigo_setor, empregado1.salario_base, empregado1.imposto, 400, 10)
    salario1 = vendedor1.calcular_salario()

    print(vendedor1)
    print(f"Salário Liquido: {salario1}€")