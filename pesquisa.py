print("Pesquisa de Satisfação TudoWeb.")
print("Sua opinião importa! Responda à pesquisa sobre o nosso atendimento.")

excelente = 0
ruim = 0

for i in range(1, 12):

    print(f"\nEntrevistado {i}")
    nome_entrevistado = input("Digite seu nome: ")
    idade_entrevistado = int(input("Digite sua idade: "))

    print("\n1- EXCELENTE | 2- BOM | 3- RUIM")
    opiniao = int(input("Insira o número que corresponde à sua opinião: "))

    if opiniao ==1:
        excelente = excelente + 1
        print("Opinião registrada!")
    elif opiniao == 3:
        ruim = ruim + 1
        print("Opinião registrada!")
    elif opiniao == 2:
        print("Opinião registrada!")
    else:
        print("Opção inválida! Por favor, insira um número válido (1, 2 ou 3).")

print("\nResultados:")
print(f"Quantidade de entrevistados que avaliaram como EXCELENTE: {excelente}")
print(f"Quantidade de entrevistados que avaliaram como RUIM: {ruim}")