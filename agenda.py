AGENDA = {}

AGENDA['guilherme'] = {
    'telefone': '98889898',
    'email':'guilherme@gmail.com',
    'endereco': 'Av. 1'
}

AGENDA['stiven'] = {
    'telefone': '985544444',
    'email':'stiven@gmail.com',
    'endereco': 'Av. 2'
}


def mostrar_contatos():
   for contato in AGENDA:
       buscar_contato(contato)



def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print('######################################')

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    print()
    print('>>>>>>>>Contato {} adicionado/editado com sucesso'.format(contato))
    print()

def excluir_contato(contato):
    AGENDA.pop(contato)

    print()
    print('>>>>>>>>Contato {} excluido com sucesso'.format(contato))
    print()
def imprimir_menu():
    print('#############################################')
    print('## 1 - Mostrar todos os contatos da agenda ##')
    print('## 2 - Buscar contato                      ##')
    print('## 3 - incluir contato                     ##')
    print('## 4 - Editar contato                      ##')
    print('## 5 - Excluir contato                     ##')
    print('## 0 - Fechar agenda                       ##')
    print('#############################################')

while True:

    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3' or opcao == '4':

        contato = input('Digite o seu nome de contato: ')
        telefone = input('Digite o seu telefone de contato: ')
        email = input('Digite o seu email de contato: ')
        endereco = input('Digite o seu endereço de contato: ')

        incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '0':
        print('>>>>>Fechando Programa<<<<<')
        break
    else:
        print('>>>>>Opção Inválida<<<<<')
