sistema_do_IA = input ("qual o nome do sistema IA?: ")
performance = float(input("qual a pontuação da perfomance do sistema?:"))


if 0> performance < 39.9:
    print (" IA em Treinamento 🍼")
elif 40.0 > performance < 69.9:
    print ("IA Intermediária 🧠")
elif 70.0 > performance < 89.9:
    print("IA Otimizada 🚀")
elif 90.0 > performance < 100.0:
    print ("IA Avançada (nível Skynet) 🤯")
elif performance < 0:
    print("Erro: Pontuação inválida! ❌")
else:
    print("Erro: IA fora da escala! ⚠️")
