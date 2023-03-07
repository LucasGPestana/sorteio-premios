import cadastro_pessoas
import cadastro_premios
import envio_gmail
import random

sorteios = []
resposta = 'SIM'
usuarios = cadastro_pessoas.realizarCadastroPessoas()
premios = cadastro_premios.realizarCadastroPremios()

while resposta == 'SIM':
    
    if usuarios == [] or premios == []:  # Verifica se as listas estão vazias
       print("Não há mais usuários ou prêmios para sortear!")
       break
    
    print("+" + "-----"*3 + "+")
    print("     SORTEIO     ")
    print("+" + "-----"*3 + "+")
    usuario_escolhido = random.choice(usuarios)
    premio_escolhido = random.choice(premios)

    print("A pessoa sorteada foi: ", usuario_escolhido[1])
    print(f"O prêmio sorteado foi: {premio_escolhido[2]} {premio_escolhido[1]}")

    sorteios.append([usuario_escolhido[0], usuario_escolhido[1], premio_escolhido[2], premio_escolhido[1]])

    envio_gmail.enviarEmail(usuario_escolhido[1], usuario_escolhido[2], premio_escolhido[1], premio_escolhido[2])

    usuarios.remove(usuario_escolhido)
    premios.remove(premio_escolhido)

    while True:
      resposta = input("Deseja continuar a sortear (Sim/Não)? ").upper()
      if resposta == 'SIM' or resposta == 'NÃO' or resposta == 'NAO':
         break
      else:
         print("Resposta Inválida")

arquivo = open('files/sorteados.txt', 'w')

for index in range(len(sorteios)):
   arquivo.write(f"{sorteios[index]}\n")

arquivo.close()
