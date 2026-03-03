
# B1
numero = int(input("Indique um número:"))

if numero >= 0:
   print("positivo")
else:
   print("negativo")

# B2
Idade = int(input("Indique a sua idade:"))

if Idade >= 18:
   print("Você é maior de idade")
else:
   print("Você é menor de idade")

# B3
num = int(input("Indique um número:"))

if num % 2:
   print("É par")
else:
   print("É impar")

# B4
num_1 = int(input("Indique o primeiro numero:"))
num_2 = int(input("Indique o segundo numero:"))

if num_1 >= num_2:
   print(f"O {num_1} é o maior")
elif num_2 >= num_1:
   print(f"O {num_2} é o maior")
else:
   print("São iguais")

# B5
password = str(input("Indique a password:"))
password_certa = ("python")

print(password == password_certa)

# I1
nota = int(input("Insira a sua nota:"))

if nota >= 18:
   print("Excelente")
elif nota >= 14:
   print("Bom")
elif nota >= 10:
   print("Suficiente")
else:
   print("Reprovado")

# I2
idade = int(input("Insira a sua idade:"))

if idade < 13:
   print("És uma criança.")

elif idade <= 17:
   print("És jovem.")

elif idade <= 64:
   print("És adulto.")
 
elif idade <= 65:
   print("És sénior")

# I3
numm = int(input("Indique um numero:"))

if numm % 5 == 0 and numm % 3 == 0:
   print("É multiplo de ambos")
elif numm % 3 == 0:
   print("multiplo de 3")
elif numm % 5 == 0:
   print("É multiplo de 5")
else:
   print("Nao é multiplo de nenhum")

# I4
user = str(input("Insire o username:"))
password = float(input("Insire a password:"))

username_correto = ("admin")
password_correta = 1234

print(user == username_correto and password == password_correta)

# I5
valor = int(input("Indique o valor:"))

if 10 <= valor <= 20 :
   print("Está entre 10 e 20")
else:
   print("Não está entre 10 e 20")

# A1
saldo_inicial = 1000
valor_a_levantar = int(input("Insira o valor a levantar:"))

if valor_a_levantar > 1000:
   print("Saldo Insuficiente")
else:
   print("Autorizado")

# A2
numero_1 = int(input("Indique o primeiro numero:"))
numero_2 = int(input("Indique o segundo numero:"))
numero_3 = int(input("Indique o terceiro numero:"))
numero_4 = int(input("Indique o quarto numero:"))

if numero_1 >= numero_2 and numero_1 >= numero_3 and numero_1 >= numero_4:
   print(f"O {numero_1} é o maior")
elif numero_2 >= numero_1 and numero_2 >= numero_3 and numero_2 >= numero_4:
   print(f"O {numero_2} é o maior")
elif numero_3 >= numero_1 and numero_3 >= numero_2 and numero_3 >= numero_4:
   print(f"O {numero_3} é o maior")
elif numero_4 >= numero_1 and numero_4 >= numero_2 and numero_4 >= numero_3:
   print(f"O maior numero é {numero_4}")
else:
   print(f"Igual")

# A3
peso = int(input("Indique o seu peso:"))
altura = float(input("Indique a sua altura:"))

IMC = peso / (altura * altura)
print(IMC)


if IMC < 18.5:
   print("Baixo peso")
elif IMC <= 24.9:
   print("Normal.")

elif IMC <= 29.9:
   print("Excesso de peso.")
 
elif IMC <= 30:
   print("Obesidade")

# A4
valor_da_compra = float(input("Insira o valor da compra"))
desconto = 0
valor_final = valor_da_compra - desconto

if valor_da_compra >= 100:
    desconto1 = valor_da_compra * 0.1
    valor_final = valor_da_compra - desconto
    print(f"O seu desconto é de {desconto} e o valor final a pagar é de {valor_final}")
elif valor_da_compra >= 50:
    desconto = valor_da_compra * 0.05
    valor_final = valor_da_compra - desconto
    print(f"O seu desconto é de {desconto} e o valor final a pagar é de {valor_final}")
else : print(f"Não tem nenhum desconto aplicado e o valor final a pagar é {valor_da_compra}")



# A5
ano = int(input("Indique um ano:"))
if ano % 4 == 0:
   print("O ano é bissexto")
else:
   print("O ano é normal")
      
      

