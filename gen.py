import random
import time
import sys

key_1 = ''.join(random.choice('0123456789ABCDEFGHILMNOPQRSTUVZ') for i in range(4))
key_2 = ''.join(random.choice('0123456789ABCDEFGHILMNOPQRSTUVZ') for i in range(4))
key_3 = ''.join(random.choice('0123456789ABCDEFGHILMNOPQRSTUVZ') for i in range(4))
key_4 = ''.join(random.choice('0123456789ABCDEFGHILMNOPQRSTUVZ') for i in range(4))
keygen = f'\n{key_1}-{key_2}-{key_3}-{key_4}'

answer = input('Premi invio per generare una chiave: ')
if answer == (''):
    print('--------------------')
    print(keygen)
    with open('key.txt','a') as lettura:
        lettura.write(keygen)
        lettura.close()
        print('Chiave generata correttamente e inserita nel file txt!')
        time.sleep(5)