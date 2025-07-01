lista_funcionarios = []
id_global = 5251073

def decoração(titulo, funcao): # Decoração do menu
    tamanho = 20 - int(len(titulo) / 2)
    print()
    print("-" * tamanho + titulo + "-" * tamanho)
    funcao()
    print(40 * "-")
    print()

def cadastrar_funcionario(id): # cadastra funcionario
    nome = input("Digite o nome do funcionario: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    lista = {"id": id, "nome": nome, "setor": setor, "salario": salario} # Criação do dicionário
    lista_funcionarios.append(lista.copy()) # Adicionando o dicionário na lista

def consultar_funcionarios(): # consulta funcionarios
    while True:
        try:
            resposta = int(input("1 - Consultar Todos\n2 - Consultar por Id\n3 - Consultar por Setor\n4 - Retornar\nResposta: ")) 
            if resposta not in [1, 2, 3, 4]: # Validação
                print("Opção inexistente")
                continue
            elif resposta == 1: # Mostrando todos os funcionários
                for funcionario in lista_funcionarios:
                    print(f"\nId: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: R${funcionario['salario']:.2f}\n")
            elif resposta == 2:
                try:
                    encontrado = False
                    id = int(input("Digite o id do funcionário: "))
                    for funcionario in lista_funcionarios: # Procurando o funcionário por id na lista
                        if funcionario["id"] == id:
                            print(f"\nId: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: R${funcionario['salario']:.2f}\n")
                            encontrado = True
                    if not encontrado: # Validação
                        print("Id não encontrado")
                except ValueError: # Tratamento de erro
                    print("Id inválido")
            elif resposta == 3: # Consulta por setor
                encontrado = False
                setor = input("Digite o setor do funcionário: ")
                for funcionario in lista_funcionarios: # Procurando o setor por funcionário na lista
                    if funcionario["setor"] == setor:
                        print(f"\nId: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: R${funcionario['salario']:.2f}\n")
                        encontrado = True
                if not encontrado: # Validação
                    print("Setor não encontrado")
            else:
                break
        except ValueError: # Tratamento de erro
            print("Opção inválida")
            continue
        
def remover_funcionario(): # remove funcionario
    while True:
        try:
            encontrado = False
            id = int(input("Digite o id do funcionário que deseja remover: "))
            # Procurando o funcionário na lista
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id: 
                    lista_funcionarios.remove(funcionario)
                    print("Funcionário removido com sucesso")
                    encontrado = True
                    return
            if not encontrado: # Validação
                print("Id não encontrado")
        except ValueError: # Tratamento de erro
            print("Id inválido")
            continue

# Programa principal
print("-Bem-vindo ao Sistema da Maryanne Kaffer-")
while True: # Menu
    try:
        print("-" * 13 + "Menu Principal" + "-" * 13)
        resposta = int(input("1 - Cadastrar Funcionário\n2 - Consultar Funcionário\n3 - Remover Funcionário\n4 - Encerrar Programa\nResposta: "))
        print("-" * 40)
        if resposta not in [1, 2, 3, 4]: # Validação
            print("Opção inexistente")
            continue
        # Validando as opções
        elif resposta == 1:
            decoração("Cadastrar Funcionário", lambda: cadastrar_funcionario(id_global))
            id_global += 1
        elif resposta == 2:
            decoração("Consultar Funcionário", lambda: consultar_funcionarios())
        elif resposta == 3:
            decoração("Remover Funcionário", lambda: remover_funcionario())
        else:
            break
    except ValueError: # Tratamento de erro
        print("Opção inválida")
        continue