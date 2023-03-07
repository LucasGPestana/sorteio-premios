def realizarCadastroPremios():  
  premios = []
  resposta = 'SIM'
  codProduto = 0

  while resposta == 'SIM':
      print("+" + "-----"*4 + "+")
      print(" CADASTRO DE PRÊMIOS ")
      print("+" + "-----"*4 + "+")

      nome = input("Digite o produto a ser cadastrado como prêmio: ").capitalize()

      tipo = input("Indique qual o tipo de produto a ser cadastrado como prêmio: ").capitalize()

      if nome != '' and tipo != '': # Verifica se ambos não são vazios

        codProduto += 1

        premios.append([codProduto, nome, tipo])

        while True:
          resposta = input("Deseja continuar a cadastrar prêmios (Sim/Não)? ").upper()

          if resposta == 'SIM' or resposta == 'NÃO' or resposta == 'NAO':
            break
          else:
            print("Resposta Inválida!")
      else:
        print("NOME E/OU TIPO INVÁLIDO(S)! Repita o processo novamente")
        continue

  arquivo = open('files/premios.txt', 'w')

  for index in range(len(premios)):
    arquivo.write(f"{premios[index]}\n")

  arquivo.close()
  return premios
