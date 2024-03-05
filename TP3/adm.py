from empregado import Empregado


class Administrador(Empregado):

    lista_adms = []

    def __init__(self, nome, morada, telefone, idpessoa, codigo_setor, salario_base, imposto, ajuda_de_custo=500):
        super().__init__(nome, morada, telefone, idpessoa, codigo_setor, salario_base, imposto)
        self.__ajuda_de_custo = ajuda_de_custo

    @property
    def ajuda_de_custo(self):
        return self.__ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        self.__ajuda_de_custo = ajuda_de_custo

    def calcular_salario(self):
        salario_liquido = super().calcular_salario() + self.__ajuda_de_custo
        return salario_liquido

    def __str__(self):
        return f"{super().__str__()}\nAjuda de Custo: {self.__ajuda_de_custo}€"

if __name__ == "__main__":

    empregado1 = Empregado("Wanna Maise", "Faro", "978654321", "12340", 1200, 10)
    adm = Administrador(empregado1.nome, empregado1.morada, empregado1.telefone, empregado1.codigo_setor, empregado1.salario_base, empregado1.imposto, 150)
    salario1 = adm.calcular_salario()

    print(adm)
    print(f"Salário Liquido: {salario1}€")