import csv

def cadastro_itens():
    try:
        cadastro = []
        
        item = input('Digite o item que você deseja cadastrar: ').capitalize()
        cadastro.append(item)
        quantidade = int(input(f'Digite a quantidade do item {item}: '))
        cadastro.append(quantidade)
        preco = float(input(f'Digite o preço do item {item}: '))
        cadastro.append(preco)

        with open('Armazem.csv', 'r', newline='', encoding='utf-8') as verificar_csv:
            leitor_csv = csv.reader(verificar_csv)
            for linha in leitor_csv:
                if item in linha:
                    print(f'{item} já estar cadastrado no sistema!')
                    return
        
        with open('Armazem.csv', 'a', newline='', encoding='utf-8') as cadastrar_csv:
            escritor_csv = csv.writer(cadastrar_csv)
            escritor_csv.writerow(cadastro)
        print(f'{item} cadastrado com sucesso!')
    except:
        print('Erro em salvar os dados, ou carregar os dados')
        
def consultar_itens():
    try:
        with open('Armazem.csv', 'r', newline='', encoding='utf-8') as consultar_csv:
            leitor_csv = csv.reader(consultar_csv)
            for linha in leitor_csv:
                print(linha)
    except:            
        print('Erro ao ler o arquivo')
    
def atualizar_itens():
    try:
        with open('Armazem.csv', 'r', newline='', encoding='utf-8') as atualizar_csv:
            leitor = csv.reader(atualizar_csv)
            lista = list(leitor)
            for linha in lista:
                print(', '.join(linha))

        item_antigo = input('Digite o nome do item para ser atualizado: ').capitalize()
        item_novo = input('Digite o novo nome do item: ').capitalize()
                    
        for linha in lista:
            if linha[0] == item_antigo:
                linha[0] = item_novo
            print('Nome atualizado com sucesso!')
                                        
        with open('Armazem.csv', 'w', newline='', encoding='utf-8') as atualizar_csv:
            escritor_csv = csv.writer(atualizar_csv)
            escritor_csv.writerow(lista)           
    except:
        print('Erro ao tentar atualizar o item')


while True:
    try:
        print('[0] para sair\n[1] para cadastrar\n[2] para cosultar\n[3] para atualizar')
        opcao = int(input('digite a opção: '))
         
        if opcao == 0:
            break
        elif opcao == 1:
            cadastro_itens()
        elif opcao == 2:
            consultar_itens()
        elif opcao == 3:
            atualizar_itens()
        else:
            print('Digite uma opção ou 0 para sair')
            continue
    except:
        print('Digite um número inteiro!')