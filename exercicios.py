
#funções:

def numero_par_ou_impar(numero):
    return numero % 2 == 0


numero = int(input('Informe um número inteiro qualquer: '))

if numero_par_ou_impar(numero):
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')


#mensagens:
nome = input('Qual é o seu nome? ')
print(f'Olá {nome}, muito prazer.')

#datas:

from datetime import datetime

data_atual = datetime.now()
print(data_atual.date())
