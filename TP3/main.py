from pessoa import Pessoa
from empregado import Empregado
from adm import Administrador
from vendedor import Vendedor
import pickle

def main():

    while True:
    

        print(" " * 12,"Menu")
        print("-" * 30)
        print("1 - Novo Empregado")
        print("2 - Lista de Empregados")

        print("3 - Editar Empregado")
        print("4 - Deletar Empregado")

        print("5 - Calcular Sálario")
        print("-" * 30)

        op = input("Op? ").lower()
        print(" ")

        match op:
            case "1":
                nome = input("Nome: ")
                morada = input("Morada: ")
                telefone = input("Telefone: ")
                idpessoa = (f'{len(Empregado.lista_empregados)+1}{telefone[0:2]}')
                new_person = Pessoa(nome, morada, telefone, idpessoa)
                Pessoa.lista_pessoas.append(new_person)
                print('1-Admistrador\n2-Vendedor')
                setor = int(input('Setor(1,2): '))
                new_empregado = Empregado(new_person.nome, new_person.morada, new_person.telefone, new_person.idpessoa, setor)
                Empregado.lista_empregados.append(new_empregado)
                save_list(Pessoa.lista_pessoas)
                save_list(Empregado.lista_empregados)
                if setor == 1:
                    new_adm = Administrador(new_empregado.nome, new_empregado.morada, new_empregado.telefone, new_empregado.idpessoa, new_empregado.codigo_setor, new_empregado.salario_base, new_empregado.imposto)
                    Administrador.lista_adms.append(new_adm)
                    save_list(Administrador.lista_adms)
                if setor == 2:
                    new_vendedor = Vendedor(new_empregado.nome, new_empregado.morada, new_empregado.telefone, new_empregado.idpessoa, new_empregado.codigo_setor, new_empregado.salario_base, new_empregado.imposto)
                    Vendedor.lista_vendedores.append(new_vendedor)
                    save_list(Vendedor.lista_vendedores)

            case "2":
                load_lista(Empregado.lista_empregados)
                print_list(Empregado.lista_empregados)
                input("\nENTER para sair ao menu")
                print(" ")



            case "3":
                print_list(Empregado.lista_empregados)


            case "5":
                print_list(Empregado.lista_empregados)
                empregado_id = input("ID do empregado: ")
                find_by_id(empregado_id)
                input("\nENTER para sair ao menu")


def find_by_id(empregado_id):
    empregado = None
    for adm in Administrador.lista_adms:
        if adm.idpessoa == empregado_id:
            empregado = adm
            break
    for vendedor in Vendedor.lista_vendedores:
        if vendedor.idpessoa == empregado_id:
            empregado = vendedor
            empregado.valor_vendas = int(input("Total de vendas: "))
            break
    if empregado:
        salario = empregado.calcular_salario()
        print(" ")
        if empregado.codigo_setor == 1:
            print(f"O Salário Liquido de {(empregado.nome).title()} é: {salario}€\nSalário Base:{empregado.salario_base}\nImposto:{empregado.imposto}\nAjuda de custo: {empregado.ajuda_de_custo}")
        if empregado.codigo_setor == 2:
            print(f"O Salário Liquido de {(empregado.nome).title()} é: {salario}€\nSalário Base:{empregado.salario_base}\nImposto:{empregado.imposto}\nValor de Vendas: {empregado.valor_vendas}€\nComissão: {empregado.comissao}")
        
    else:
        print("Empregado não encontrado.")
              
            


def save_list(list_to_save):
    if list_to_save == Empregado.lista_empregados:
        with open("empregador.pkl", "wb") as f:
            pickle.dump(Empregado.lista_empregados, f)
    elif list_to_save == Pessoa.lista_pessoas:
        with open("pessoas.pkl", "wb") as f:
            pickle.dump(Pessoa.lista_pessoas, f)
    elif list_to_save == Administrador.lista_adms:
        with open("administradores.pkl", "wb") as f:
            pickle.dump(Administrador.lista_adms, f)
    elif list_to_save == Vendedor.lista_vendedores:
        with open("vendedores.pkl", "wb") as f:
            pickle.dump(Vendedor.lista_vendedores, f)



def load_lista(load_lista):
    try:
        if load_lista == Empregado.lista_empregados:
            with open("empregador.pkl", "rb") as f:
                Empregado.lista_empregados = pickle.load(f)
        if load_lista == Pessoa.lista_pessoas:
            with open("pessoas.pkl", "rb") as f:
                Pessoa.lista_pessoas = pickle.load(f)
        if load_lista == Administrador.lista_adms:
            with open("administradores.pkl", "rb") as f:
                Administrador.lista_adms = pickle.load(f)
        if load_lista == Vendedor.lista_vendedores:
            with open("vendedores.pkl", "rb") as f:
                Vendedor.lista_vendedores = pickle.load(f)
        return load_lista       
    
    except FileNotFoundError:
        print('Lista não existe')

            
                
def print_list(list_of):
    if list_of == Empregado.lista_empregados or Pessoa.lista_pessoas or Administrador.lista_adms or Vendedor.lista_vendedores:
        
        i = 1
        print(" " * 16,"EMPREGADOS")
        print("-" * 45)
        if (len(list_of)) == 0:
            print('Não há itens nesta lista')
        else:    
            for item in list_of:
                if item.codigo_setor == 1:
                    print(f'{i} - {(item.nome).title()}| id:{item.idpessoa} | {item.codigo_setor} - Administrador')
                    i += 1
                if item.codigo_setor == 2:
                    print(f'{i} - {(item.nome).title()}| id:{item.idpessoa} | {item.codigo_setor} - Vendedor')
                    i += 1
        print("-" * 45)


if __name__ == "__main__":
    main()

