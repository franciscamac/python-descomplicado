# Python Descomplicado II
# Coleções: listas

# Listas
lista_carros = ['Gol','Uno','HB20','KA'] # Criando uma lista
print(f'Conteudo da lista: {lista_carros}') #Imprimindo toda a lista
print(f'O primeiro elemento da lista é {lista_carros[0]}')
print(f'O quarto elemento da lista é {lista_carros[3]}')
print(lista_carros) # São impressos na ordem em que foram armazenados, mantendo a ordem relativa entre seus elementos


# Podem crescer/diminuir de tamanho em tempo de execução
#Exemplo
carros_populares = ['Gol','uno','HB20','Ka']
superesportivos = ['Ferrari','Lamborguini','Porshe']
lista_carros = [carros_populares,superesportivos]
print(f'Conteúdo da lista de carros: {lista_carros}')


# Podendo ser acessados por indices tambem 
# Exemplo 
print(f'Carros populares: {lista_carros[0]}')
print(f'Superesportivos: {lista_carros[1]}')


# São listas bidimencionais
# Exemplo 
carros_populares = ['Gol','uno','HB20','Ka']
superesportivos = ['Ferrari','Lamborguini','Porshe']
print(f'Segundo carro popular: {lista_carros[0][1]}')
print(f'Primeiro superesportivo: {lista_carros[1][0]}')


#Inicializando e adicionando elementos dinamicamente a uma lista
# Usa-se o método append() da classe List
lista_produtos=[]
print(f'Criando uma lista de produtos vazia: {lista_produtos}')
print(f'Adicionando caneta esterográfica preta à lista: ')
lista_produtos.append('caneta esterográfica preta')
print(lista_produtos)
print(f'Adicionando caneta esterográfica azul à lista: ')
lista_produtos.append('caneta esterográfica azul')
print(lista_produtos)
print(f'Adicionando resma de papel sulfite à lista: ')
lista_produtos.append('resma de papel sulfite')
print(lista_produtos)


# Alterando os elementos de uma lista
print(f'Alterando os elementos de uma lista')
lista_produtos[2] = 'resma de papel A4'
print(lista_produtos)


# Removendo elementos de uma lista
lista_produtos.remove('resma de papel A4') # se tentar remover um objeto não existente na lista, reberá um erro.
# método pop da classe List
lista_produtos.pop() # Se nada for passado como indice ele remove o ultimo da lista
print(lista_produtos)


# Obtendo o tamanho de uma lista
print(len(lista_produtos))


# Estendendo uma lista
usuarios = []
usuarios_informatica = ['Adriano','Bruno','Carlos']
usuarios_administracao = ['Daniela','Elisa','Fernanda']
print(f'Lista vazia de usuarios: {usuarios}')
print(f'Usuarios de Informatica:{usuarios_informatica}')
print(f'Usuario de Administração: {usuarios_administracao}')
print('Unindo as listas. Primeiro testando com Informatica:c')
usuarios.extend(usuarios_informatica)
print(usuarios)
print('Agora, acrescentando a Administração:')
usuarios.extend(usuarios_administracao)
print(usuarios)


#Inserindo um elemento no meio de uma lista
#primeiro, crio uma lista com algumas ferramentas:
ferramentas = ['Alicate','Chave','Enxada']
print('Lista inicial de ferramentas: ', ferramentas)
# Agora, adiciono mais duas, de forma a manter a ordem alfabética
ferramentas.insert(2,'Chave')
print('Comprei uma chave', ferramentas)
ferramentas.insert(0,'Alicate')
print('Comprei um alicate: ', ferramentas)


# Fatiando listas 
numeros = [0,1,2,3,4,5,6,7,8,9]
print(f'Lista original: {numeros}')
primeiro_elemento = numeros[0]
print(f'Primeiro elemento: {primeiro_elemento}')
ultimo_elemento = numeros[-1]
print(f'Último elemento: {ultimo_elemento}')
penultimo_elemento = numeros[-2]
print(f'Penultimo elemento: {penultimo_elemento}')
quatro_primeiros = numeros[:4]
print(f'Quatro primeiros elementos: {quatro_primeiros}')
tres_ultimos = numeros[-3:]
print(f'Três ultimos elementos: {tres_ultimos}')
sem_os_extremos = numeros[1:-1]
print(f'Sem o primeiro e o último elementos: {sem_os_extremos}')
numeros2 = numeros[:]
print(f'Realizando uma cópia da lista inteira: {numeros2}')