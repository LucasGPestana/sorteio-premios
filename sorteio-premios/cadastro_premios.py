def realizarCadastroPremios():  
  premios = []
  resposta = 'SIM'
  codProduto = 0

  while resposta == 'SIM':
      print("+" + "-----"*4 + "+")
      print(" CADASTRO DE PRÊMIOS ")
      print("+" + "-----"*4 + "+")
      codProduto += 1

      nome = input("Digite o produto a ser cadastrado como prêmio: ")

      tipo = input("Indique qual o tipo de produto a ser cadastrado como prêmio: ")

      premios.append([codProduto, nome, tipo])

      while True:
        resposta = input("Deseja continuar a cadastrar prêmios (Sim/Não)? ").upper()

        if resposta == 'SIM' or resposta == 'NÃO' or resposta == 'NAO':
          break
        else:
          print("Resposta Inválida!")

  arquivo = open('files/premios.txt', 'w')

  for index in range(len(premios)):
    arquivo.write(f"{premios[index]}\n")

  arquivo.close()
  return premios
