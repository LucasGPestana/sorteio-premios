def realizarCadastroPessoas():  
  usuarios = []
  resposta = 'SIM'
  ident = 0

  while resposta == 'SIM':

      print("+" + "-----"*4 + "+")
      print("  CADASTRO DE USUÁRIO  ")
      print("+" + "-----"*4 + "+")

      ident += 1

      nome = input("Digite o seu nome: ")
      email = input("Digite seu email (Gmail): ").lower()

      if "@gmail.com" in email:
        usuarios.append([ident, nome, email])

        while True:
            resposta = input("Deseja continuar a cadastrar usuários (Sim/Não)? ").upper()
            if resposta == "SIM" or resposta == "NÃO" or resposta == "NAO":
              break
            else:
              print("Resposta inválida!")
      else:
        print("EMAIL INVÁLIDO! Repita o processo novamente!")
        continue

  arquivo = open("files/usuarios.txt", "w")

  for index in range(len(usuarios)):
      arquivo.write(f"{usuarios[index]}\n")

  arquivo.close()
  return usuarios