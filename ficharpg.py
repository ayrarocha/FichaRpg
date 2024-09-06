print('''\033[2:31mDUNGEONS AND DRAGONS\033[m
\033[3:35m> FICHA RPG: \033[m''')
jogador = str(input('Qual será o seu nome? ')).title().strip()
raça = str(input('Qual será a sua raça? ')).title().strip()
classe = str(input('Qual será a sua classe? ')).title().strip()
antecedentes = str(input('Qual será o seu antecedente? ')).title().strip()
força = 0
destreza = 0
constituição = 0
inteligencia = 0
sabedoria = 0
carisma = 0
pv = 10
while True :
    print('\033[0:36m> Defina seus pontos de atributos: \033[m')
    força = int(input('Força: '))
    modforça = (força - 10) // 2
    destreza = int(input('Destreza: '))
    moddestreza = (destreza - 10) // 2
    constituição = int(input('Constituição: '))
    modconstituição = (constituição - 10) // 2
    inteligencia = int(input('Inteligência: '))
    modinteligencia = (inteligencia - 10) // 2
    sabedoria = int(input('Sabedoria: '))
    modsabedoria = (sabedoria - 10) // 2
    carisma = int(input('Carisma: '))
    modcarisma = (carisma - 10) // 2
    pv = pv + modconstituição
    while True:
        opcao = input('Você está satisfeito com os atributos? (S para finalizar, N para alterar): ').strip().upper()
        if opcao == 'S':
            break
        elif opcao == 'N':
            print('Ajuste novamente;.\n')
            break
        else:
            print('\033[31mOPÇÃO INVÁLIDA! DIGITE NOVAMENTE\033[m')

    if opcao == 'S':
        break
print('\033[2:31m==='*35)
print('\033[2:31mFICHA DO JOGADOR | RPG DUNGEONS AND DRAGONS\033[m')
print(f'''\033[2:35mNome: {jogador}
RAÇA: {raça}
CLASSE: {classe}
ANTECEDENTE: {antecedentes}\033[m''')
print('\033[2:36m==='*35)
print('\033[36mATRIBUTOS DO JOGADOR:\033[m')
print(f'''\033[2:32mPontos de Vida: {pv}
Modificador Força: +{modforça}
Modificador Destreza: +{moddestreza}
Modificador Constituição: +{modconstituição}
Modificador Inteligência: +{modinteligencia}
Modificador Sabedoria: +{modsabedoria}
Modificador Carisma: +{modcarisma}''')
print('\033[2:32m==='*35)