print("*******************")
print("Bem vindo ao jogo de Adivinhação!")
print("*******************")

numero_secreto = 42

chute_str = input("Digite o seu número:")
print("Você digitou:", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print ("Parabéns Você acertou!")
else:
    print ("Não fique triste mas você errou!Tente outra vez!")

print("Fim de Jogo!")