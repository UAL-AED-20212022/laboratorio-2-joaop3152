import controller as c
#importar a 'class' LinkedList
from models.LinkedList import LinkedList

#atribuir uma variável global para a 'class' LinkedList
lista_paises = LinkedList()

#Função principal do programa
def main():
    while True:
        #menu com as escolhas do utilizador para executar o programa
        sec_menu = input()
        menu = sec_menu.split()
        #Registar país no início
        if menu[0] == "RPI":
            pais_novo = menu[1]
            RPI(lista_paises, pais_novo)
        #Registar país no final
        elif menu[0] == "RPF":
            pais_novo = menu[1]
            RPF(lista_paises, pais_novo)
        #Registar país depois do país já registado
        elif menu[0] == "RPDE":
            pais_novo = menu[1]
            pais_registado = menu[2]
            RPDE(lista_paises, pais_novo, pais_registado)
        #Registar país antes do país registado
        elif menu[0] == "RPAE":
            pais_novo = menu[1]
            pais_registado = menu[2]
            RPAE(lista_paises, pais_novo, pais_registado)
        #Registar país na posição pedida pelo utilizador
        elif menu[0] == "RPII":
            pais_novo = menu[1]
            index = menu[2]
            RPII(lista_paises, pais_novo, index)
        #Verificar o número de elementos/países que estão na lista_paises
        elif menu[0] == "VNE":
            print(f"O número de elementos são {VNE(lista_paises)}.")
        #Verificar se o país escolhido pelo utilizador se encontra na lista
        elif menu[0] == "VP":
            pais_nome = menu[1]
            verificar = VP(lista_paises, pais_nome)
            if verificar == True:
                print(f"O país {pais_nome} encontra-se na lista.")
            else:
                print(f"O país {pais_nome} não se encontra na lista.")
        #Eliminar o primeiro país da lista_paises
        elif menu[0] == "EPE":
            print(f"O país {EPE(lista_paises)} foi eliminado da lista.")
        #Eliminar o último país da lista_paises
        elif menu[0] == "EUE":
            print(f"O país {EUE(lista_paises)} foi eliminado da lista.")
        #Eliminar o país escolhido pelo utilizador
        elif menu[0] == "EP":
            pais_escolhido = menu[1]
            if EP(lista_paises, pais_escolhido) == True:
                print(f"O país {pais_escolhido} foi eliminado da lista.")
            else:
                print(f"O país {pais_escolhido} não se encontra na lista.")


#Funções que vão dar os returns para os prints pedidos nas funções acima 
def RPI(lista_paises, pais_novo):
    if c.registar_pais_inicio(lista_paises, pais_novo):
        return lista_paises.traverse_list()

def RPF(lista_paises, pais_novo):
    if c.registar_pais_fim(lista_paises, pais_novo):
        return lista_paises.traverse_list()

def RPDE(lista_paises, pais_novo, pais_registado):
    if c.registar_depois_registado(lista_paises, pais_novo, pais_registado):
        return lista_paises.traverse_list()

def RPAE(lista_paises, pais_novo, pais_registado):
    if c.registar_antes_registado(lista_paises, pais_novo, pais_registado):
        return lista_paises.traverse_list()

def RPII(lista_paises, pais_novo, index):
    if c.registar_pais_index(lista_paises, pais_novo, index):
        return lista_paises.traverse_list()

def VNE(lista_paises):
    return c.verificar_numero_elementos(lista_paises)

def VP(lista_paises, pais_nome):
    if c.verificar_pais(lista_paises, pais_nome) == True:
        return True
    else:
        return False

def EPE(lista_paises):
    return c.eliminar_primeiro_pais(lista_paises)

def EUE(lista_paises):
    return c.eliminar_ultimo_pais(lista_paises)

def EP(lista_paises, pais_escolhido):
    if c.eliminar_pais_escolhido(lista_paises, pais_escolhido) == True:
        return True
    else:
        return False