# Listas
temp = []
princ = []
# Quartos do posto B
quarto7 = []
lencol7 = []
bata7 = []
fronha7 = []
quarto8 = []
lencol8 = []
bata8 = []
fronha8 = []
quarto9 = []
lencol9 = []
bata9 = []
fronha9 = []
quarto10 = []
lencol10 = []
bata10 = []
fronha10 = []
quarto11 = []
lencol11 = []
bata11 = []
fronha11 = []
quarto12 = []
lencol12 = []
bata12 = []
fronha12 = []
quarto13 = []
lencol13 = []
bata13 = []
fronha13 = []
quarto14 = []
lencol14 = []
bata14 = []
fronha14 = []
quarto15 = []
lencol15 = []
bata15 = []
fronha15 = []
quarto16 = []
lencol16 = []
bata16 = []
fronha16 = []
quarto17 = []
lencol17 = []
bata17 = []
fronha17 = []
quarto18 = []
lencol18 = []
bata18 = []
fronha18 = []
quarto19 = []
lencol19 = []
bata19 = []
fronha19 = []
quarto20 = []
lencol20 = []
bata20 = []
fronha20 = []
quarto21 = []
lencol21 = []
bata21 = []
fronha21 = []
quarto22 = []
lencol22 = []
bata22 = []
fronha22 = []
postob = [quarto7, quarto8, quarto9, quarto10, quarto11, quarto12, quarto13, quarto14, quarto15, quarto16, quarto17, quarto18, quarto19, quarto20, quarto21, quarto22]
postoc = []
postod = []
postoe = []
terreo = []
# Menu Principal
while True:
    posto = str(input(
'''Qual o POSTO?
[1] POSTO B
[2] POSTO C
[3] POSTO D
[4] POSTO E
[5] TERREO
[6] RELATORIO
Opção: '''))
    # Menu dos quartos
    if posto == '1':
        quarto = int(input('QUAL O QUARTO? obs(do 7 a 22): '))
        if quarto == 7:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel7 = str(input('Nome do responsável: '))
                lencol7.append([lencoltemp, responsavel7])
                quarto7.append([lencol7, bata7, fronha7])
                print(lencol7)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel7 = str(input('Nome do responsável: '))
                bata7.append([batatemp, responsavel7])
                quarto7.append([lencol7, bata7, fronha7])
                print(bata7)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel7 = str(input('Nome do responsável: '))
                fronha7.append([fronhatemp, responsavel7])
                quarto7.append([lencol7, bata7, fronha7])
                print(fronha7)
        if quarto == 8:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel8 = str(input('Nome do responsável: '))
                lencol8.append([lencoltemp, responsavel8])
                quarto8.append([lencol8, bata8, fronha8])
                print(lencol8)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel8 = str(input('Nome do responsável: '))
                bata8.append([batatemp, responsavel8])
                quarto8.append([lencol8, bata8, fronha8])
                print(bata8)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel8 = str(input('Nome do responsável: '))
                fronha8.append([fronhatemp, responsavel8])
                quarto8.append([lencol8, bata8, fronha8])
                print(fronha8)
        if quarto == 9:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel9 = str(input('Nome do responsável: '))
                lencol9.append([lencoltemp, responsavel9])
                quarto9.append([lencol9, bata9, fronha9])
                print(lencol9)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel9 = str(input('Nome do responsável: '))
                bata9.append([batatemp, responsavel9])
                quarto9.append([lencol9, bata9, fronha9])
                print(bata9)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel9 = str(input('Nome do responsável: '))
                fronha9.append([fronhatemp, responsavel9])
                quarto9.append([lencol9, bata9, fronha9])
                print(fronha9)
        if quarto == 10:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel10 = str(input('Nome do responsável: '))
                lencol10.append([lencoltemp, responsavel10])
                quarto10.append([lencol10, bata10, fronha10])
                print(lencol10)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel10 = str(input('Nome do responsável: '))
                bata10.append([batatemp, responsavel10])
                quarto10.append([lencol10, bata10, fronha10])
                print(bata10)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel10 = str(input('Nome do responsável: '))
                fronha10.append([fronhatemp, responsavel10])
                quarto10.append([lencol10, bata10, fronha10])
                print(fronha10)
        if quarto == 11:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel11 = str(input('Nome do responsável: '))
                lencol11.append([lencoltemp, responsavel11])
                quarto11.append([lencol11, bata11, fronha11])
                print(lencol11)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel11 = str(input('Nome do responsável: '))
                bata11.append([batatemp, responsavel11])
                quarto11.append([lencol11, bata11, fronha11])
                print(bata11)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel11 = str(input('Nome do responsável: '))
                fronha11.append([fronhatemp, responsavel11])
                quarto11.append([lencol11, bata11, fronha11])
                print(fronha11)
        if quarto == 12:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel12 = str(input('Nome do responsável: '))
                lencol12.append([lencoltemp, responsavel12])
                quarto12.append([lencol12, bata12, fronha12])
                print(lencol12)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel12 = str(input('Nome do responsável: '))
                bata12.append([batatemp, responsavel12])
                quarto12.append([lencol12, bata12, fronha12])
                print(bata12)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel12 = str(input('Nome do responsável: '))
                fronha12.append([fronhatemp, responsavel12])
                quarto12.append([lencol12, bata12, fronha12])
                print(fronha12)
        if quarto == 13:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel13 = str(input('Nome do responsável: '))
                lencol13.append([lencoltemp, responsavel13])
                quarto13.append([lencol13, bata13, fronha13])
                print(lencol13)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel13 = str(input('Nome do responsável: '))
                bata13.append([batatemp, responsavel13])
                quarto13.append([lencol13, bata13, fronha13])
                print(bata13)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel13 = str(input('Nome do responsável: '))
                fronha13.append([fronhatemp, responsavel13])
                quarto13.append([lencol13, bata13, fronha13])
                print(fronha13)
        if quarto == 14:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel14 = str(input('Nome do responsável: '))
                lencol14.append([lencoltemp, responsavel14])
                quarto14.append([lencol14, bata14, fronha14])
                print(lencol14)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel14 = str(input('Nome do responsável: '))
                bata14.append([batatemp, responsavel14])
                quarto14.append([lencol14, bata14, fronha14])
                print(bata14)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel14 = str(input('Nome do responsável: '))
                fronha14.append([fronhatemp, responsavel14])
                quarto14.append([lencol14, bata14, fronha14])
                print(fronha14)
        if quarto == 15:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel15 = str(input('Nome do responsável: '))
                lencol15.append([lencoltemp, responsavel15])
                quarto15.append([lencol15, bata15, fronha15])
                print(lencol15)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel15 = str(input('Nome do responsável: '))
                bata15.append([batatemp, responsavel15])
                quarto15.append([lencol15, bata15, fronha15])
                print(bata15)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel15 = str(input('Nome do responsável: '))
                fronha15.append([fronhatemp, responsavel15])
                quarto15.append([lencol15, bata15, fronha15])
                print(fronha15)
        if quarto == 16:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel16 = str(input('Nome do responsável: '))
                lencol16.append([lencoltemp, responsavel16])
                quarto16.append([lencol16, bata16, fronha16])
                print(lencol16)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel16 = str(input('Nome do responsável: '))
                bata16.append([batatemp, responsavel16])
                quarto16.append([lencol16, bata16, fronha16])
                print(bata16)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel16 = str(input('Nome do responsável: '))
                fronha16.append([fronhatemp, responsavel16])
                quarto16.append([lencol16, bata16, fronha16])
                print(fronha16)
        if quarto == 17:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel17 = str(input('Nome do responsável: '))
                lencol17.append([lencoltemp, responsavel17])
                quarto17.append([lencol17, bata17, fronha17])
                print(lencol17)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel17 = str(input('Nome do responsável: '))
                bata17.append([batatemp, responsavel17])
                quarto17.append([lencol17, bata17, fronha17])
                print(bata17)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel17 = str(input('Nome do responsável: '))
                fronha17.append([fronhatemp, responsavel17])
                quarto17.append([lencol17, bata17, fronha17])
                print(fronha17)
        if quarto == 18:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel18 = str(input('Nome do responsável: '))
                lencol18.append([lencoltemp, responsavel18])
                quarto18.append([lencol18, bata18, fronha18])
                print(lencol18)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel18 = str(input('Nome do responsável: '))
                bata18.append([batatemp, responsavel18])
                quarto18.append([lencol18, bata18, fronha18])
                print(bata18)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel18 = str(input('Nome do responsável: '))
                fronha18.append([fronhatemp, responsavel18])
                quarto18.append([lencol18, bata18, fronha18])
                print(fronha18)
        if quarto == 19:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel19 = str(input('Nome do responsável: '))
                lencol19.append([lencoltemp, responsavel19])
                quarto19.append([lencol19, bata19, fronha19])
                print(lencol19)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel19 = str(input('Nome do responsável: '))
                bata19.append([batatemp, responsavel19])
                quarto19.append([lencol19, bata19, fronha19])
                print(bata19)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel19 = str(input('Nome do responsável: '))
                fronha19.append([fronhatemp, responsavel19])
                quarto19.append([lencol19, bata19, fronha19])
                print(fronha19)
        if quarto == 20:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel20 = str(input('Nome do responsável: '))
                lencol20.append([lencoltemp, responsavel20])
                quarto20.append([lencol20, bata20, fronha20])
                print(lencol20)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel20 = str(input('Nome do responsável: '))
                bata20.append([batatemp, responsavel20])
                quarto20.append([lencol20, bata20, fronha20])
                print(bata20)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel20 = str(input('Nome do responsável: '))
                fronha20.append([fronhatemp, responsavel20])
                quarto20.append([lencol20, bata20, fronha20])
                print(fronha20)
        if quarto == 21:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel21 = str(input('Nome do responsável: '))
                lencol21.append([lencoltemp, responsavel21])
                quarto21.append([lencol21, bata21, fronha21])
                print(lencol21)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel21 = str(input('Nome do responsável: '))
                bata21.append([batatemp, responsavel21])
                quarto21.append([lencol21, bata21, fronha21])
                print(bata21)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel21 = str(input('Nome do responsável: '))
                fronha21.append([fronhatemp, responsavel21])
                quarto21.append([lencol21, bata21, fronha21])
                print(fronha21)
        if quarto == 22:
            opcao = str(input(
'''O QUE VOCÊ QUER CADASTRAR?
[1] LENÇOL
[2] BATA
[3] FRONHA
Opção: '''))
            if opcao == '1':
                lencoltemp = int(input('Insira a quantidade: '))
                responsavel22 = str(input('Nome do responsável: '))
                lencol22.append([lencoltemp, responsavel22])
                quarto22.append([lencol22, bata22, fronha22])
                print(lencol22)
            elif opcao == '2':
                batatemp = int(input('Insira a quantidade: '))
                responsavel22 = str(input('Nome do responsável: '))
                bata22.append([batatemp, responsavel22])
                quarto22.append([lencol22, bata22, fronha22])
                print(bata22)
            elif opcao == '3':
                fronhatemp = int(input('Insira a quantidade: '))
                responsavel22 = str(input('Nome do responsável: '))
                fronha22.append([fronhatemp, responsavel22])
                quarto22.append([lencol22, bata22, fronha22])
                print(fronha22)
    if posto == '6':
        print(f'Posto B: Quarto7 = Lençol:{lencol7} - Bata:{bata7} - Fronha:{fronha7}, quarto8 = Lençol:{lencol8} - Bata:{bata8} - Fronha:{fronha8}, quarto9 = Lençol:{lencol9} - Bata:{bata9} - Fronha:{fronha9}, quarto10 = Lençol:{lencol10} - Bata:{bata10} - Fronha:{fronha10}, quarto11 = Lençol:{lencol11} - Bata:{bata11} - Fronha:{fronha11}, quarto12 = Lençol:{lencol12} - Bata:{bata12} - Fronha:{fronha12}, quarto13 = Lençol:{lencol13} - Bata:{bata13} - Fronha:{fronha13}, quarto14 = Lençol:{lencol14} - Bata:{bata14} - Fronha:{fronha14}, quarto15 = Lençol:{lencol15} - Bata:{bata15} - Fronha:{fronha15}, quarto16 = Lençol:{lencol16} - Bata:{bata16} - Fronha:{fronha16}, quarto17 = Lençol:{lencol17} - Bata:{bata17} - Fronha:{fronha17}, quarto18 = Lençol:{lencol18} - Bata:{bata18} - Fronha:{fronha18}, quarto19 = Lençol:{lencol19} - Bata:{bata19} - Fronha:{fronha19}, quarto20 = Lençol:{lencol20} - Bata:{bata20} - Fronha:{fronha20}, quarto21 = Lençol:{lencol21} - Bata:{bata21} - Fronha:{fronha21}, quarto22 = Lençol:{lencol22} - Bata:{bata22} - Fronha:{fronha22}')
