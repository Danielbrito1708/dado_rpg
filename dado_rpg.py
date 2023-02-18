import random

resultado_dado = "o dado foi jogado, e o resultado foi {}."

print("Escolha um dos dados \n d4[4] \n d6[6] \n d8[8] \n d10[10] \n d12[12] \n d20[20] \n d100[100]")

dado_escolhido = int(input("Qual irá escolher?"))

print(random.randint(1, int(dado_escolhido)))
