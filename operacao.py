# operacoes_bancarias_dioimport os

menu_selecionar = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair\n
\n"""


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
  
def deposito():
  global saldo
  valor_deposito = float(input("Qual valor deseja depositar: \n"))
  if valor_deposito > 0:
    saldo = valor_deposito + saldo
    print(f'Deposito realizado no valor de R$ {valor_deposito:.2f}\n')
  else:
    print("O valor informado é inválido!")
  
def saque ():
  global saldo,numero_saques, limite
  saque_solicitado = float(input("Qual valor deseja sacar: \n" ))
  
  if numero_saques < LIMITE_SAQUES:
    if saque_solicitado > 0:
      if  saque_solicitado <= limite:
       saldo = saldo - saque_solicitado
       numero_saques +=1
       print(f"valor sacado R$ {saque_solicitado:.2f}")
      else:
       print("Valor excede o limite diario")
    else:
      print("Valor invalido!")
  else:
    print ("Limite de saques excedido")
      
  
def exibir_extrato():
  global saldo, extrato, saque_solicitado
  print ("############ Extrato ############ \n")
  print (f"Seu saldo final é R$ {saldo:.2f}")
  print("###########################")

while True:
    opcao = input(menu_selecionar)
        
    match opcao:
            case 'd':
                os.system('cls')
                deposito()
            case 's':
                os.system('cls')
                saque()
            case 'e':
                os.system('cls')
                exibir_extrato()
            case 'q':
              break

            case _:
                print("Opção inválida, tente novamente.")
    
menu_selecionar()
    
      
      
