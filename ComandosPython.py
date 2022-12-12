#01 - Comentario de bloco
'''
idade= 19
if idade > 18:
    print("------------------ Maior de Idade")
else:
    print("xxxxxxxxxxxxxxxxxx Menor de Idade")
'''

'''
#02 - Uso de quebra de linha (\n)
print("I\né\nc\nn\ni\nc \no \nem \nDesenvolvimento \nde \nsistemas")

#03 - Variáveis
#Pode-se criar variáveis em qualquer parte de programa
#Ao declarar, nao precisa colocar tipo de dados
#Pode-se criar a variável e já atribuir valor

exemplo:
VisualG
Var:
idade: inteiro

início:
idade<- 50

Python
idade = 50
'''

'''
#Comando que mostra o tipo de dado da variável
#Comando Type
idade = 50
print('O tipo de dado da variável idade é:', type(idade))
int = números inteiros
str = textos(caracter)
float = numeros decimais
bool = true ou false (v ou f)
type = tipo da variavel
while = enquanto



#  Leitura de dados do teclado (leia) - input

#variavelQualquer = input("Mensagem pro usuário")

idade = float (input("Digite sua idade"))
print("Sua idade é:::::", idade)

#similar ao Leia(nome)

print("O tipo do dado informado é:", type(idade))
#Quando o valor de uma variável é digitada no teclado, o valor é armazenado
#como text (str), precisamos converter o tipo de dado (Casting)

print(idade/5)
'''

#Outro meio de converter o tipo de dados

'''
idade = input("Digite sua idade")
print(type(idade))
idade = int(idade)
print(type(idade))
idade = float(idade)
print(type(idade))
'''

#04 - Estrutura de Condição - IF..ELSE (Se..Então)
'''
sintaxe

if comparação:
    (TAB) ......
    ........
    ........

fim do if - continuação do algoritmo
#operadores de comparação:
#>, <, <=, >=, != (diferente), == (igual)
#conectivos
#E - and, OU - or
#Matematicos
#%Modulo(Resto da Divisão)

numero = 100
if numero<100:
    print("")
'''

'''
#elif (SENÃO SE)

idade = int(input("Digite sua idade"))

if idade<=14:
    print("Crinaça")
elif idade>14 and idade<18:
    print("Adolecente")
elif idade>=18 and idade<60:
    print("Adulto")
else:
    print("idoso")
'''

# Estrutura de Seleção (Escolha..Caso) - Match...Case
'''
Menu de opções ------
variavel = algum Valor
match varivel:
    case 1:
        (tab)......
    case 2:
        (tab)......
    case "texto qualquer":
        (tab)
    case _:
        opcão invalida
'''

'''
print("Opções ::: \n1 - X-Tudo -- \n2 - X-egg \n3 - X-Bacon")
op = int(input("Escolha seu lanche"))

match op:
    case 1:
        print("Nosso Xtudo eh bão demais")
    case 2:
        print("Sanduba de zoiião")
    case 3:
        print("Banco eh ruim demais")
    case _:
        print("Opcão invalida. Escolha um código de 1 a 3")
'''

'''
#Estrutura de repetição
#Enquanto

while condição:
    (tab)........
'''

idade = 10
while idade != 0:
    print("A idade é", idade)
    idade = int(input("Digite a idade"))

