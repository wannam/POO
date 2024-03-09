

class Pessoa:

    lista_pessoas = []
    
    def __init__(self, nome, morada, telefone, idpessoa):
        self.__nome = nome
        self.__morada = morada
        self.__telefone = telefone
        self.__idpessoa = idpessoa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def morada(self):
        return self.__morada

    @morada.setter
    def morada(self, morada):
        self.__morada = morada

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def idpessoa(self):
        return self.__idpessoa

    @idpessoa.setter
    def idpessoa(self, idpessoa):
        self.__idpessoa = idpessoa

    @classmethod
    def cria_anonimo(cls):
        return cls("John Doe", "Unknown", "Unknown")

    def __str__(self):
        return f"Nome: {self.__nome}\nMorada: {self.__morada}\nTelefone: {self.__telefone}\nID:{self.__idpessoa}"
    

if __name__ == "__main__":

    pessoa1 = Pessoa("Wanna Maise", "Faro", "978654321", "1")

    print(pessoa1)
##

