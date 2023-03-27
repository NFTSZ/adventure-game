from random import choice, randint
from time import sleep, time
from os import system, name

situacoes = ['Você encontrou uma bolsa jogada no chão.', 
    'Há um Troll valente barrando sua passagem.',
    'Há uma ponte velha no seu caminho.',
    'Um menino pergunta se você pode ajudá-lo',
    'Uma pedreira desabou, você não pode passar por aqui.',
    'Você encontrou uma nova arma: ',
    'Uma árvore grande caiu, bloqueando a passagem.',
    'Você chegou numa vila, há algumas coisas que possam ser do seu interesse aqui.',
    
    ]
cons_pontes = ['Você conseguiu passar ileso', 'A ponte estava velha demais e caiu com o seu peso, por sorte conseguiu segurar em alguns galhos']

armasz  = ['Espada de madeira ', 'Espada de ferro', 'Arco e flechas']
inventario = []
escudos = ['Escudo de madeira', 'Escudo de ferro']

cooldown_time= 180
last_used_time = 0

atk_player = 3
def_player = 5


atk_troll = randint(0, 25)
def_troll = randint(0, 25)

recomp = ''
moedas = 0

def limpa_tela():
    system('cls' if name == 'nt' else 'clear')
       
def menino():
    global moedas
    menino_precisa = randint(0, 100)
    print(f'Menino: Preciso de {menino_precisa} moedas de ouro para ajudar minha família. Por favor...')
    if moedas < menino_precisa:
        op_user = int(input('[1] Infelizmente não tenho, mas volte depois.\n>>> '))
    else:
        op_user = int(input('[1] Aqui está.   [2] Não me encha o saco!!\n>>> '))
        if op_user == 1:
            moedas -= menino_precisa
         
def armas():
    global atk_player
    global arma_nova
    if 'Espada de madeira' in arma_nova:
        atk_player = 10
    elif arma_nova == 'Espada de ferro':
        atk_player = 20
    elif arma_nova == 'Arco e flechas':
        atk_player = 18
                
def stats():
    print('-'*45)
    print(f'Coins: {moedas}            Atk: {atk_player}    Def: {def_player}')
    print('-'*45)
    
def luta():
    if atk_player >= def_troll:
        print('Você foi mais forte que o troll e não o deixou ileso')
    elif atk_troll >= def_player:
        print('Você levou muito dano, mas conseguiu fugir')
    else: 
        print('Você levou muito dano, mas conseguiu fugir')

def coins():
    global moedas
    rand = randint(0, 50)
    moedas += rand
    print(f'Você ganhou {rand} coins')
    
def menu_vila():
    print('[1] Ferreiro\n[2] Mercante\n[3] Bruxo\n[4] Sair da Vila')
    

def ferreiro():
    global moedas
    while True:
        print('-='*25)
        print('[1] Melhorar armas/armaduras  [2] Comprar minérios  [3] Voltar a vila')
        op_user = int(input('>>> '))
        #   upar armas  
        if op_user == 1:
            while True:
                if atk_player == 3:
                    print('Você não possui armas. Volte quando conseguir uma!')
                    break
                if atk_player != 3:
                    time_upar()
                    break
        #   loja de minerios
        elif op_user == 2:
            while True:
                print('[1] Ouro - 325c  [2] Prata - 232c  [3] Ferro - 103c [4] Platina - 567c  [5] Sair')
                op_user = int(input('>>> '))
                if op_user == 1:
                    if moedas >= 325:
                        moedas -= 325
                        print('Muito bom fazer negócio com você.')
                    else:
                        print('Moedas insuficientes')
                elif op_user == 2:
                    if moedas >= 232:
                        moedas -= 232
                        print('Muito bom fazer negócio com você.')
                    else:
                        print('Moedas insuficientes')
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
                    break
        # SAIR DO FERREIRO
        elif op_user == 3:
            print('Volte sempre, viajante!')
            break
        
def time_upar():
        global atk_player 
        global last_used_time       # variaveis globais (usadas dentro e fora da função)
        current_time = time()       # tempo atual
        # se o tempo atual menos o tempo da ultima vez q foi usada a opção for maior ou igual o tempo limite:
        if current_time - last_used_time >= cooldown_time: 
            last_used_time = current_time # o tempo da ultima "usagem" vai ser substituido pelo tempo atual
            # aqui vai ser gerado quantos pontos de up a arma vai receber e adicionar ao atk
            rand = randint(1, 20)
            atk_player += rand
            sleep(0.25)
            # aqui vai mostrar quanto foi upado e o tempo pra tentar novamente
            remaining_time = cooldown_time - (current_time - last_used_time)
            print(f'Sucesso! Sua arma atua subiu {rand} pontos de atk. Tente novamente em {int(remaining_time)} segundos.')
            #caso o player já tenha usado e o tempo de espera não tenha sido atingido, mostra quanto tempo falta: 
        else:
            remaining_time = cooldown_time - (current_time - last_used_time)
            print('Tente novamente em', int(remaining_time), 'minutos.')
            
def mercante():
    global moedas
    while True:
        print('-='*25)
        print('[1] Armas  [2] Escudos  [3] Voltar a vila')
        op_user = int(input('>>> '))
        # armas
        if op_user != 3 and op_user == 1:
            while True:
                print('-='*15)
                op_user = int(input('[1] Espada de Platina - 90c\n[2] Espada Flamejante  - 490c\n[3] Flechas de fogo - 68c\n[4] Voltar\n>>> '))
                if op_user == 1:
                    if moedas >= 90:
                        moedas -= 90
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 2:
                    if moedas >= 490:
                        moedas -= 490
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 3:
                    if moedas >= 68:
                        moedas -= 68
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 4:
                    break
        #   escudos
        elif op_user == 2:
            while True:
                print('[1] Escudo de madeira - 10c\n[2] Escudo de Ferro - 40c\n[3] Capa de invisibilidade - 1.000c\n[4] Voltar\n>>> ')
                op_user = int(input('>>> '))
                if op_user == 1:
                    if moedas >= 10:
                        moedas -= 10
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 2:
                    if moedas >= 40:
                        moedas -= 40
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 3:
                    if moedas >= 1000:
                        moedas -= 1000
                        print('Mercante: hehehe thank you!')
                    else:
                        print('Mercante: Você não pode comprar isso.')
                elif op_user == 4:
                    break
        # sair do mercante
        elif op_user == 3:
            print('Volte mais vezes, aventureiro.')
            break

def bruxo():
    print('Bruxo ainda não disponível, volte depois.')

           
while True:
    limpa_tela()
    stats()
    
    sit = choice(situacoes)
    print(sit)
    
    if 'Troll' in sit:
        op_user = int(input('[1] Lutar   [2] Procurar outro caminho\n>>> '))
        if op_user != 2:
            luta()
    if 'bolsa' in sit:
        op_user = int(input('[1] Pegar   [2] Deixar ali\n>>> '))
        if op_user != 2:
            coins()
    if 'ponte' in sit:
        op_user = int(input('[1] Passar   [2] Procurar outro caminho\n>>> '))
        if op_user != 2:
            print(choice(cons_pontes))
    if 'menino' in sit:
        op_user = int(input('[1] Claro que posso   [2] No que seria?   [3] Não me encha o saco!!.\n>>> '))
        if op_user != 3:
            menino()
    if 'desabou' in sit or 'caiu' in sit:
        op_user = int(input('[1] Procurar outro caminho\n>>> '))        
    if 'arma' in sit:
        arma_nova = choice(armasz)
        print(arma_nova)
        if 'Espada de madeira' in arma_nova:
            print('Atk:', 10)        
        elif 'Espada de ferro' in arma_nova:
            print('Atk:', 20)
        elif 'Arco e flechas' in arma_nova:
            print('Atk:', 18)
        op_user = op_user = int(input('[1] Pegar arma nova   [2] Manter arma atual \n>>> '))
        if op_user != 2:
            armas()
            
    if 'vila' in sit:
        op_user = int(input('[1] Dar uma olhada  [2] Continuar aventura \n>>> '))
        if op_user != 2:
            while True:
                menu_vila()
                op_user = int(input('>>> '))
                if op_user == 1:
                    print('Ferreiro: Bem vindo, viajante. Em que posso lhe ajudar?')
                    ferreiro()
                if op_user == 2:
                    print('Mercante: Olá, posso lhe oferecer algumas coisas?')
                    mercante()
                if op_user == 3:
                    bruxo()
                if op_user == 4:
                    break
    sleep(1)
