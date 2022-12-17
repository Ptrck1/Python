#Nome dos integrantes do grupo: Patrick, Renato e Gabriel
#Turma: T2

#Crie enunciados e os algoritmos que os resolvem, utilizando cada estrutura aprendida em VisualG,
#agora na linguagem Python. Vc pode criar enunciados para estruturas em separado ou um enunciado 
#e a solução com todas as estruturas em apenas um programa.

#São as estruturas:
#● Escreva e Leia (Input e Print) x
#● Se...Então...Senão (IF..Else..Elif) x
#● Conectivos E e OU (and e or) x
#● Valores Aleatórios (random.randint) x
#● Escolha ....Caso (match..case) x
#● Enquanto ..... (while) x
#● Para (for) x
#● Vetor (list) x
#● Fazer pelo menos 4 Fluxogramas


#01 - Input e Print
#Algoritmo de cadastro do restaurante, onde você vai digitar seu nome, sua idade, email e crie uma senha.

print("Faça cadastro no restaurante")
nome = str (input("Digite seu nome:"))
idade = int (input("Digite sua idade:"))
email = str (input("Digite seu email:"))
senha = str (input("Crie uma senha:"))
print("Conta criada com sucesso!!!")
print("Faça seu login")
login = str (input("Digite seu email de cadastro:"))
login = str (input("Digite sua senha de cadastro:"))
print("==========================================//=================================================")

#02 - If , Else e Elif | And e Or
#Algoritmo para verificar qual é o tipo de daltonismo da pessoa.
#Esse algoritmo serve para pessoas diagnósticadas com daltonismo, que querem saber o tipo de daltonismo.

print("Descubra qual é o seu tipo de daltonismo ")
print("Cores: \n1 - marrom \n2 - cinza  \n3 - roxo \n4 - Outra cor")
cor = int (input("Digite o numero da cor que vc enxerga:"))
if cor == 1:
    print("Você tem o tipo de daltonismo Protanopia")
elif cor == 2:
    print("Você tem o tipo de daltonismo Deuteranopia")
elif cor == 3:
    print("Você tem o tipo de daltonismo Tritanopia")
elif cor == 4:
    print("Procure um médico para ver o você tem")
print("==========================================//=================================================")


#03 - Match e case
#Algoritmo escolha o que quer comer no restaurante.

print("Bem Vindo ao restaurante")
print("Opcões: \n1 - Prato de macarrão \n2 - Fritas \n3 - Hamburguer \n4 - Prato de Alface \n5 - Não quero fazer mais o pedido")
opcões = int (input("Escolha o que você quer comer:"))
match opcões:
    case 1:
        print("Você escolheu um prato muito bom, que vem acompanhado com um molho abolonesa.")
    case 2:
        print("Você escolheu fritas muito crocantes, que vem com cheddar e bacon acompanhado.")
    case 3:
        print("Você escolheu o melhor hamburguer da cidade, que vem acompanhado com cebolas fritas.")
    case 4:
        print("Você escolheu um prato bem atípico, mais que é muito saudável e nutritivo")
    case 5:
        print("Me desculpe qualquer coisa, volte sempre!")
print("==========================================//=================================================")

#04 - While
#Algoritmo que conta quantos números pares foram digitados.

contador = 0
qtde = 0

while contador <10:
    numeros = int(input("Digite algum número:"))
    contador = contador + 1
    if (numeros%2) == 0:
      print("Esse número é par")
      qtde = qtde + 1
print ("Foram contados ", qtde, "números pares")
print("==========================================//=================================================")

#05 - For
#Algoritmo que mostra todas as combinações de roupas possíveis.

camisa = ["Preta", "Branca", "Azul"]
calça = ["Preta", "Branca", "Azul claro"]
tênis= ["Preto", "Branco", "Azul"]

for x in camisa:
    for y in calça:
        for z in tênis:
            print(x,y,z) 
print("==========================================//=================================================")

#06 - list
#Algoritmo que faz um acróstico.

my_list = ["Desenvolver", "Executar", "Sabedoria", "Emoção", "Novidade", "Valores", "Otimizar", "Liderança", "Velocidade", "Inspiração", "Modernidade", "Ético", "Notoriedade", "Trabalho", "Organização", "Dedicação", "Estabilidade", "Sofisticação", "Ideia", "Sucesso", "Tendência", "Esforço", "Money", "Ação", "Sensacional"]
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list[7])
print(my_list[8])
print(my_list[9])
print(my_list[10])
print(my_list[11])
print(my_list[12])
print(my_list[13])
print(my_list[14])
print(my_list[15])
print(my_list[16])
print(my_list[17])
print(my_list[18])
print(my_list[19])
print(my_list[20])
print(my_list[21])
print(my_list[22])
print(my_list[23])
print(my_list[24])
print("=========================//=========================")

print("A junção das primeiras letras das palavras ", my_list[1:24])
print("Resultam na frase: Desenvolvimento de Sistemas")
print("==========================================//=================================================")

