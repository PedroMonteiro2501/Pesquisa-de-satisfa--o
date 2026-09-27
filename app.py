#--- Pesquisa de satisfação

#--- Variáveis de contagem
entrevistados = 50
excelente = 0
bom = 0
ruim = 0

#--- Dados da pesquisa 
for i in range(entrevistados):

    print(f"\n--- Entrevistado {i + 1} ---")

    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    opiniao = int(input("Digite a sua opinião (1-excelente, 2-bom, 3-ruim): "))

#--- Estrutura de decisão
if opiniao == 1:
    print("Você avaliou como excelente")
    excelente += 1

elif opiniao == 2:
    print("Você avaliou como bom")
    bom += 1

elif opiniao == 3:
    print("Você avaliou como ruim")
    ruim += 1

else:
    print("Opinião inválida")


#--- Resultados da pesquisa
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas BOM: {bom}")
print(f"Quantidade de respostas RUIM: {ruim}")
