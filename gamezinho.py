from random import choice, randint
from time import sleep

situacoes = ['Você encontrou uma bolsa de ouro jogada no chão.', 
    'Há um Troll valente barrando sua passagem.',
    'Há uma ponte velha no seu caminho.',
    'Um menino pergunta se você pode ajudá-lo',
    'Uma pedreira desabou, você não pode passar por aqui.',
    'Você encontrou uma nova arma: ',
    'Uma árvore grande caiu, bloqueando a passagem.',
    'Você chegou numa vila, há algumas coisas que possam ser do seu interesse aqui.',
    
    ]
cons_pontes = ['Você conseguiu passar ileso', 'A ponte estava velha demais e caiu com o seu peso, por sorte conseguiu segurar em alguns galhos']
armas = ['Espada de madeira ', 'Espada de ferro', 'Arco e flechas']
escudos = ['Escudo de madeira', 'Escudo de ferro']

# armadura e armas
'''esp_de_madeira = 10
esp_de_ferro = 20
arco_e_flecha = 18
esc_de_madeira = 12
esc_de_ferro = 23'''


# player
moedas = 0
atk_player = 3
def_player = 5

# troll
atk_troll = randint(0, 25)
def_troll = randint(0, 25)

# dragao
atk_drag = 52
def_drag = 68

while True:
    print('-'*45)
    print(f'Moedas: {moedas}            Ataque: {atk_player}    Defesa: {def_player}')
    print('-'*45)

    sit = choice(situacoes)
    print(sit)
    
    if 'Troll' in sit:
        op_user = int(input('[1] Lutar   [2] Procurar outro caminho\n>>> '))
        if op_user != 2:
            if atk_player >= def_troll:
                print('Você foi mais forte que o troll e não o deixou ileso')
            elif atk_troll >= def_player:
                print('Você levou muito dano, mas conseguiu fugir')
            else: 
                print('Você levou muito dano, mas conseguiu fugir')

    # SISTEMA DE MOEDAS, VAI RECEBER UMA QUANTIDADE ALEATÓRIA DE 0 A 100 CADA VEZ QUE PEGAR E ACUMULAR
    if 'ouro' in sit:
        op_user = int(input('[1] Pegar   [2] Deixar ali\n>>> '))
        rand = randint(0, 100)
        if op_user != 2:
            moedas += rand
            print(f'Você ganhou {rand} moedas de ouro')

    if 'ponte' in sit:
        op_user = int(input('[1] Passar   [2] Procurar outro caminho\n>>> '))
        if op_user != 2:
            print(choice(cons_pontes))

    # MENINO PEDE UMA QUANTIDADE ALEATÓRIA DE MOEDAS, SE TIVER, VC TEM A OPÇÃO DE DAR OU RECUSAR. VAI DIMINUIR NO NUMERO DE MOEDAS
    if 'menino' in sit:
        op_user = int(input('[1] Claro que posso   [2] No que seria?   [3] Não me encha o saco!!.\n>>> '))
        if op_user != 3:
            menino_precisa = randint(0, 100)
            print(f'Menino: Preciso de {menino_precisa} moedas de ouro para ajudar minha família. Por favor...')
            if moedas < menino_precisa:
                op_user = int(input('[1] Infelizmente não tenho, mas volte depois.\n>>> '))
            else:
                op_user = int(input('[1] Aqui está.   [2] Não me encha o saco!!\n>>> '))
                if op_user == 1:
                    moedas -= menino_precisa

    if 'desabou' in sit or 'caiu' in sit:
        op_user = int(input('[1] Procurar outro caminho\n>>> '))

    # VAI VER SE A SITUAÇÃO É SOBRE UMA ARMA, VAI MOSTRAR QUAL ARMA ENCONTRADA E SEU PODER DE ATK 
    if 'arma' in sit:
        arma_nova = choice(armas)
        print(arma_nova)
        if 'Espada de madeira' in arma_nova:
            print('Atk:', 10)        
        elif 'Espada de ferro' in arma_nova:
            print('Atk:', 20)
        elif 'Arco e flechas' in arma_nova:
            print('Atk:', 18)

        op_user = op_user = int(input('[1] Pegar arma nova   [2] Manter arma atual \n>>> '))
        # SE O PLAYER PEGAR A ARMA, O PODER DE ATK DA ARMA VAI DIRETO PRO SEU ATK
        if op_user == 1:
            if 'Espada de madeira' in arma_nova:
                atk_player = 10
            elif arma_nova == 'Espada de ferro':
                atk_player = 20
            elif arma_nova == 'Arco e flechas':
                atk_player = 18

    if 'vila' in sit:
        op_user = int(input('[1] Dar uma olhada  [2] Continuar aventura \n>>> '))
        if op_user == 1:
            while True:
                print('-'*45)
                print(f'Moedas: {moedas}            Ataque: {atk_player}    Defesa: {def_player}')
                print('-'*45)
                print('------ VILA --------\n[1] Ferreiro\n[2] Mercante\n[3] Bruxo\n[4] Sair da Vila')
                op_user = int(input('>>> '))
                if op_user != 4:

                    # FERREIRO
                    if op_user == 1:
                        print('Ferreiro: Bem vindo, viajante. Em que posso lhe ajudar?')
                        op_user = int(input('[1] Melhorar armas/armaduras  [2] Comprar minérios  [3] Voltar a vila\n>>> '))
                        while True:
                            # UPAR ARMAS
                            if op_user == 1:
                                    print('Selecione sua arma')
                                    if atk_player == 3:
                                        print('Você não possui armas. Volte quando conseguir uma!')
                                        break
                                    if atk_player == 10:
                                        op_user = int(input('[1] Espada de Madeira\n>>> '))
                                        if op_user == 1:
                                            rand = randint(0, 20)
                                        atk_player += rand
                                        print(f'Sucesso!! O atk de sua arma subiu {rand} pontos! Volte daqui uns dias para upar mais.')
                                        break
                                    if atk_player == 20:
                                        op_user = int(input('[1] Espada de Ferro\n>>> '))
                                        if op_user == 1:
                                            rand = randint(0, 20)
                                        atk_player += rand
                                        print(f'Sucesso!! O atk de sua arma subiu {rand} pontos! Volte daqui uns dias para upar mais.')
                                        break
                                    if atk_player == 18:
                                        op_user = int(input('[1] Arco e Flechas\n>>> '))
                                        if op_user == 1:
                                            rand = randint(0, 20)
                                        atk_player += rand
                                        print(f'Sucesso!! O atk de sua arma subiu {rand} pontos! Volte daqui uns dias para upar mais.')
                                        break
                            # LOJA DE MINÉRIOS DO FERREIRO
                            elif op_user == 2:
                                while True:
                                    print('[1] Ouro - 325  [2] Prata - 232  [3] Ferro - 103 [4] Platina - 567  [5] Sair')
                                    op_user = int(input('>>> '))
                                    if op_user == 1:
                                        if moedas >= 325:
                                            moedas -= 325
                                            print('Muito bom fazer negócio com você.')
                                        else:
                                            print('Moedas insuficiente')
                                    elif op_user == 2:
                                        if moedas >= 232:
                                            moedas -= 232
                                            print('Muito bom fazer negócio com você.')
                                        else:
                                            print('Moedas insuficiente')
                                    elif op_user == 3:
                                        if moedas >= 103:
                                            moedas -= 103
                                            print('Muito bom fazer negócio com você.')
                                        else:
                                            print('Moedas insuficiente')
                                    elif op_user == 4:
                                        if moedas >= 567:
                                            moedas -= 567
                                            print('Muito bom fazer negócio com você.')
                                        else:
                                            print('Moedas insuficiente')
                                    if op_user == 5:
                                        print('Volte sempre, viajante!')
                                        break
                            # SAIR DO FERREIRO
                            elif op_user == 3:
                                break
                # SAIR DA VILA
                if op_user == 4:
                    break
    sleep(1)