from Academia import Academia, Usuario
import random

academia = Academia()

usuarios = [ Usuario(1, academia )  for i in range(10)]
usuarios += [ Usuario(2, academia )  for i in range(2)]
random.shuffle(usuarios)

list_chaos = []

def rotina():
  for i in range(10):
    random.shuffle(usuarios)

    for user in usuarios:
      user.iniciar_execicio()
    
    for user in usuarios:
      user.finalizar_exercicio()

#testes 20
for k in range(20):
  print(f'Teste {k}')
  academia.reiniciar_o_dia()
  rotina()
  list_chaos += [academia.calcular_chaos() * 100]

print(f'{list_chaos} %')

