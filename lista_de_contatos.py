def criar_contato():
  try:
    nome = input('Digite o nome do contato: ').strip()
    telefone = input('Digite o telefone: ').strip()

    with open('contato.txt', 'a') as contato:
      contato.write(f'{nome} - {telefone} \n')

    print(f'Contato {nome} criado com sucesso!')
  except:
    print('Erro ao criar contato')

def ver_contatos():
  try:
    with open('contato.txt', 'r') as contato:
      linhas = contato.readlines()
      for linha in linhas:
        print(linha)
  except:
    print('Erro ao listar os contatos')

def editar_nome():
  try:
    with open('contato.txt', 'r') as contato:
      contatos = contato.read()
      print(contatos)

    nome_antigo = input('Digite o nome do contato que você deseja atualizar: ').strip()

    if nome_antigo in contatos:
      nome_novo = input('Digite o novo nome do contato: ').strip()

      with open('contato.txt', 'r') as contato:
        atualizacao = contato.read()
        atualizar_contato = atualizacao.replace(nome_antigo, nome_novo)

      with open('contato.txt', 'w') as contato:
        contato.write(atualizar_contato)

        print('Nome editado com sucesso!')
    else:
      print(f'{nome_antigo} não existe na lista de contatos')

  except:
    print('Erro ao editar o contato')

def editar_numero():
  try:
    with open('contato.txt', 'r') as contato:
      contatos = list(contato.readlines())
      for linhas in contatos:
        print(linhas)

    telefone_antigo = input('Digite o numero que você deseija atualizar: ')

    for count in range(len(contatos)):
      if telefone_antigo in contatos[count]:
        telefone_novo = input('Digite o novo número: ').strip()

        with open('contato.txt', 'r') as contato:
          atualizacao = contato.read()
          atualizar_contato = atualizacao.replace(telefone_antigo, telefone_novo)

        with open('contato.txt', 'w') as contato:
          contato.write(atualizar_contato)

        print('Número editado com sucesso!')
        break
  except:
    print('Erro ao editar o número do contato')

def remover_contato():
  try:
    with open('contato.txt', 'r') as contato:
      linhas = list(contato.readlines())
      for p, linha in enumerate(linhas):
        print(f'Na posição {p}º estar o contato {linha}')

    posicao = int(input('Digite a posição do contato que você deseja remover: '))
    linhas_atualizadas = [linha for p, linha in enumerate(linhas) if p != posicao]

    with open('contato.txt', "w") as arquivo:
      arquivo.writelines(linhas_atualizadas)

    print('Nome removido com sucesso!')
  except:
    print('Erro ao remover o contato')

while True:
  try:
    opcao = int(input('''
    [0] para sair
    [1] para criar um novo contato
    [2] ver lista de contatos
    [3] para editar o nome do contato
    [4] para editar o número do contato
    [5] para remover o contato
    Digite a opção: '''))

    if opcao == 0:
      break
    elif opcao == 1:
      criar_contato()
    elif opcao == 2:
      ver_contatos()
    elif opcao == 3:
      editar_nome()
    elif opcao == 4:
      editar_numero()
    elif opcao == 5:
      remover_contato()
    else:
      print('Opção invalida!')

  except:
    print('Digite um número inteiro')
