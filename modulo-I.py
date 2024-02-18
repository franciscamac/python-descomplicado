# Python Descomplicado

print("hello word! ;)")


#Imprimindo caracteres especiais 
print("\n Envia uma quebra de linha para a saída padrão\n")
print("\t imprime uma tabulação(semelhante a tecla tab\t")
print("\r equivale a pressionar um enter \r")
print("conheça o bar apóstrofo\'s")


#Separadores e quebras de linhas 
print('No meio do caminho', end='')
print(' tinha uma pedra')
print('No meio do caminho ', end='&&&&&')


#O parâmetro sep
print("A","B", "C", 0, sep="*")
print("A", "B", "C", sep='\n')


#Tipos de dados 
x=1 
print(type(x))
x ='abc'
print(type(x))
x=True
print(type(x))


# Interpolando valores em um texto
print('d% - inteiro com sinal')
print('f% - numero pontos flutuante(decimal)')
print('0 - valor na base octal')
print('x - valor de base hexadecimal')
print('s- string')
print('%%- exibe um sinal de porcentagem na posição')
# Exemplos 
print('Codigo do usuario: %d' %27)
print('15 em octal é %o' %15)
print('100 em hexadecimal é %x' %100)
print('pi com duas casas decimais é aproximadamente %.2f' %3.1415926)
print('pi com duas casas decimais é aproximadamente %.3f' %3.1415926)
nome = 'Fulano'
print('Meu nome é %s' %nome)
print('Constantes - pi: %.2f, e %.2f' %(3.1415926,2.718281))


# Formatando dados com f-strings
codigo = 27
pi=3.1415926
print(f'Código do usuario {codigo}')
print(f'15 em octal é {15:o}')
print(f'100 em hexadecimal é {100:x}')
print(f'pi com duas casas decimais é aproximadamente {pi:.2f}')
print(f'pi com duas casas decimais é aproximadamente {pi:.3f}')
nome = 'Fulano'
print(f'Meu nome é {nome}')
print(f'A média aritmética simples entre 4 e 5 é {(4+5)/2}')


# FORMATAÇÃO DO CÓDIGO
# O código identado é entendido pelo interpretador da linguagem como um bloco sobre o qual será realizada uma iteração.
# Espaços em brancos dentro de parênteses e colchetes são ignorados.
# Exemplo de como isso pode melhorar a legibilidade.
matriz_4x3 = [[21,22,23],
              [24,25,26],
              [27,28,28],
              [30,31,32]]
# É mais legível que 
matriz_4x3 = [[21,22,23],[24,25,26],[27,28,28],[30,31,32]]


# ESCOPO DE VARIÁVEIS 
# Locais: podem ser utilizadas apenas onde forem definidas
# Globais: podem ser usadas em qualquer lugar do código 
''' Exemplo de variável global'''
codigo = '123321' # Definição fora do corpo da função- variavel global
def testar():
    print(f'Dentro da função testar(), codigo={codigo}')
testar()
print(f'Fora da função testar(), codigo ={codigo}')
# O valor da variavel foi preservado entre as chamadas, dentro ou fora desta.

# Outra forma de criar uma variável global 
teste1 =123
def funcao_f():
    global teste2 # Declarando a variavel com o modificador global, faz com que ela tambem seja global.
    teste2 = 456
    for x in range(1,10):
        z = x*2
        print(f'z = {z}')
    print(f'Valor de z, após o loop: {z}')
    print(f'Valor de teste1, dentro da função: {teste1}')
    print(f'Valor de teste2, dentro da função: {teste2}')
funcao_f()
print(f'Valor de teste1, fora da função: {teste1}')
print(f'Valor de teste2, fora da função: {teste2}')
#print(f'Valor de z, após o loop: {z}') # provoca um erro ao acessar a variavel por ser uma local e não está dentro do escopo no qual foi definido 


#Operadores Logico 
def soma():
    x = 5+5
    #ou
    b=5
    b = b+5 # Ou -->  b += 5
    print(f'Soma de x é {x} e de b é {b}')
soma()
def subtracao():
    x = 5-5
    #ou
    b=5
    b = b-5 # Ou -->  b -= 5
    print(f'Subtração de x é {x} e de c é {b}')
subtracao()
def multiplicacao():
    x = 5*5
    #ou
    b=5
    b = b*5 # Ou -->  b *= 5
    print(f'Multiplicação de x é {x} e de c é {b}')
multiplicacao()
def divisao():
    x = 5/2
    #ou
    b=5
    b = b/2 # Ou -->  b /= 2
    print(f'Divisao de x é {x} e de c é {b}')
divisao()


# Precedência dos operadores aritméticos 
# 1. Expressões dentro de (parênteses)
# 2. Exponenciação 
# 3. Divisão e multiplicação na ordem em que aparecem


# Operadores de igualdades/desigualdade
# igualdade
print(5==3) # dois inteiros, porem valores diferentes
print(10==10) # dois inteiros e iguais 
print('maçã'=='maçã') # duas strings e iguais 
print('maçã'=='Maçã') # duas strings diferentes, pois python é uma linguagem case sensitive (difere maiúsculo de minúsculo)
print(2+2==4) 
print(10==10.0) # um inteiro e 1 real, porem tem o mesmo valor 
# desigualdade
print(5!=3)
print(10!=10)
print('maçã'!='maçã')
print('maçã'!='Maçã')
print(2+2!=4)
print(10!=10.0)


