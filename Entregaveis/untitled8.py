# -*- coding: utf-8 -*-
"""Untitled8.ipynb
Original file is located at
    https://colab.research.google.com/drive/1sKEk0-mVS1hXaaocTtLDNMwYZNRi22wu
"""
---------------------------------------------------------------------------------------------------------
def palindromo (numero):
  "diz se um número é palindromo ou não"
  n=str(numero)

  if n==n[::-1]:
    return "É palindromo"

  else:
    return "Não é palindromo"

print(palindromo(121))
print(palindromo(55412))
---------------------------------------------------------------------------------------------------------
from sympy import primerange
"diz a soma de todos os números primos abaixo de 100"

primos = primerange(2, 100)
soma = sum(primos)
print("Soma dos primos:", soma)
---------------------------------------------------------------------------------------------------------
def maior_primo():
  "diz qual o maior divisor primo de um número"
  def primo(n):

    if n < 2:
      return False
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
    return True
  while True:
    try:
      numero = int(input("Digite um número: "))
      break
    except ValueError:

      print("Por favor, insira um número válido.")
  for i in range(numero, 1, -1):
    if numero % i == 0 and primo(i):
      return f"O maior número primo divisor é: {i}"

  return "Não há um maior número primo divisor (exceto o próprio número)."

print(maior_primo())

--------------------------------------------------------------------------------------------------------

def igual(lista):
  "verifica se o primeiro número de uma lista é igual ao último número"
  if len(lista) > 0 and lista[0] == lista[-1]:
    return "É igual."
  if not lista:
    return "A lista está vazia."
  else:
    return 'Não é igual'

print(igual([1,2,3,4,5,6,1]))
print(igual([2,3,6,4,5,9,1]))
print(igual([]))

class Drone:
  def __init__(self, nome, n_motores, qtd_camera, ano_const,peso):
    self.nome= nome
    self.n_motores= n_motores
    self.qtd_camera=qtd_camera
    self.ano_const= ano_const
    self.peso= peso

  def __str__(self):
    return f'Nome:{self.nome}.\
    Número de motores:{self.n_motores}.\
    Quantidade de Cameras:{self.qtd_camera}.\
    Ano de Construção:{self.ano_const}.\
    Peso:{self.peso}'

  def tabela(self):
    print("-" * 80)
    print(f"| {self.nome:<15} | {self.n_motores:<10} | {self.qtd_camera:<10} | {self.ano_const:<15} | {self.peso:<20} |")

  def exibir_tabela(self):
    print(f"| {'Nome':<15} | {'Motores':<10} | {'Câmeras':<10} | {'Ano Construção':<15} | {'Peso':<10} |")
    for drone in lista_drones:
      drone.tabela()

  @staticmethod
  def rankear_data(lista_drones):
      lista_drones.sort(key=lambda drone: drone.ano_const, reverse=True)
      for drone in lista_drones:
          print(drone)
      return lista_drones[:]

  def alterar_nome(self, novo):
    self.nome= novo
    return f"O Drone agora tem o nome {self.nome}"

#fazendo alguns exemplos p/ rodar
drone1 = Drone("DroneA", 4, 2,2011,11)
drone2 = Drone("DroneB", 6,1,2024, 5)
drone3 = Drone("DroneC", 8,4,2021,1)
drone4=Drone("DroneD", 6, 3, 2023, 24)
drone5=Drone("DroneE", 8, 4, 2020, 18)
drone6=Drone("DroneF", 4, 2, 2021, 25)

lista_drones = [drone1, drone2, drone3,drone4,drone5,drone6] #listei para fazer a tabela

Drone.exibir_tabela(lista_drones) #tabela


print("\nDrones Rankeados do mais novo pro mais antigo:") #cabeçalho ou índice (só consegui pensar assim)
drones_rankeados = Drone.rankear_data(lista_drones) # ativando o rankeamento, mas não coloquei em tabela não, mas se chamar a tabela ela vai estar rankeada
drone1.alterar_nome('droneNOVO') #mudando o nome do drone1

Drone.exibir_tabela(lista_drones) #a lista com a mudança do drone1, e rankeada

------------------------------------------------------------------------------------------------------------

