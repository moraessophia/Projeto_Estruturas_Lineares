import os
os.system('cls')

votos = []

print("Candidatos")
print("1. Ana")
print("2. Bruno")
print("3. Carlos")

while True:
    voto = input('Digite o nome do candidato (ou "fim"): ').lower()

    if voto == "fim":
        break

    if voto in ["ana","bruno","carlos"]:
        votos.append(voto)
    else:
        print('\nVoto Inválido! \nDigite um candidato registrado.')

ana = votos.count("ana")
bruno = votos.count("bruno")
carlos = votos.count("carlos")

print("\nResultado da votação:")
print(f"Ana: {ana}")
print(f"Bruno: {bruno}")
print(f"Carlos: {carlos}")

maior = max(ana, bruno, carlos)

if [ana, bruno, carlos].count(maior) > 1:
    print('Houve empate entre os candidatos')
else:
    if maior == ana:
        print('Vencedor: Ana!')
    elif maior == bruno:
        print('Vencedor: Bruno!')
    else:
        print('Vencedor: Carlos!')