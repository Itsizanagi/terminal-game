import random
import time

palavras = ('fisica', 'matematica', 'quimica')
computador = random.choice(palavras)
tentativas = 2
acertos = 0
print(' 水 '*20)
print('Jogo de palavras')
print(' 水 '*20)
print('Me chamo delta, vamos jogar? ')
jogar = str(input('Sim ou Não: ')).strip().upper()

if jogar in 'SIM':
    print('Voce tem 2 uma chance para acertar! ')
    print("\033[31mPensando aguarde....")
    time.sleep(3)
    print("\033[36mNúmero escolhido com sucesso!")
else:
    print('Poxa que pena, ate mais amigo....')
    exit()

while True:
    jogador = str(input('Qual palavra voce acha que é?'))
    if jogador == computador:
        print('Parabéns voce acertou!!')
        exit()
    else:
        print('Poxa que pena...Tente de novo')
        tentativas -= 1
        print('Agora voce tem {} chances'.format(tentativas))
        if tentativas <= 0:
            print('derrota....')
            print('A palavra era {}' . format(computador))
            break 