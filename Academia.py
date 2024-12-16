import random

class Academia:
  def __init__(self):
      self.halteres = [i for i in range( 10, 50) if i % 2==0]
      self.porta_halteres = {}
      self.reiniciar_o_dia()
  
  def reiniciar_o_dia(self):
     self.porta_halteres = {i:i for i in self.halteres}
     print(f'lista halteres {self.porta_halteres}')
  
  def listar_halteres(self):
     lista = [i for i in self.porta_halteres.values() if i != 0]
     print(f'listar_halteres {lista}')
     return lista
   
  def listar_espacos(self):
     return [i for i, j in self.porta_halteres.items() if j == 0]

  def pegar_haltere(self, peso):
    halt_pos = list(self.porta_halteres.values()).index(peso)
    key_halt = list(self.porta_halteres.keys())[halt_pos]
    self.porta_halteres[key_halt] = 0
    return peso
  
  def devolver_haltere(self, Key, peso):
     if self.porta_halteres[Key] != 0:
         raise ValueError(f'Essa posição ja está ocupada {self.porta_halteres[Key]}')
     
     self.porta_halteres[Key] = peso
  
  def calcular_chaos(self):
     num_chaos = [i for i, j in self.porta_halteres.items() if i != j]
     return len(num_chaos) / len(self.porta_halteres)
  

class Usuario:
   def __init__(self, tipo, academia : Academia):
      self.tipo = tipo # 1 normal 2 bagunceiro
      self.academia = academia
      self.peso = 0
   def iniciar_execicio(self):
      lista_pesos = self.academia.listar_halteres()
      self.peso = random.choice(lista_pesos)
      self.academia.pegar_haltere(self.peso) 
   def finalizar_exercicio(self):
      espacos = self.academia.listar_espacos()
      print(f'espaços {espacos}')

      if self.tipo == 1:
         if self.peso in espacos:
            self.academia.devolver_haltere(self.peso, self.peso)
         else:
            pos = random.choice(espacos)
            self.academia.devolver_haltere(pos, self.peso)
      
      if self.tipo == 2:
         pos = random.choice(espacos)
         self.academia.devolver_haltere(pos, self.peso)