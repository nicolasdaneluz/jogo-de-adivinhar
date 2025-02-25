print("*******************")
print("Bem vindo ao jogo de Adivinhação!")
print("*******************")
numero_secreto = 42
total_de_tentativas = 3
rodada=1

while(rodada<=total_de_tentativas);
 print("tentativas {} de {}".format(rodada,total_de_tentativas))
  
chute_str = input("Digite o seu número:")
print("Você digitou:", chute_str)
chute = int(chute_str)
 
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute > numero_secreto

if (numero_secreto == chute):
    print ("Parabéns Você acertou!")
else:
    print ("Não fique triste mas você errou!Tente outra vez!")

   rodada = rodada + 1
print("Fim de Jogo!")