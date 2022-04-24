import controller as c
from models.LinkedList import LinkedList

lista_paises = LinkedList()

def main():
    while True:
        sec_menu = input()
        menu = sec_menu.split()
        if menu[0] == "RPI":
            pais_novo = menu[1]
            RPI(lista_paises, pais_novo)
        elif menu[0] == "RPF":
            pais_novo = menu[1]
            RPF(lista_paises, pais_novo)
        elif menu[0] == "RPDE":
            pais_novo = menu[1]
            pais_registado = menu[2]
            RPDE(lista_paises, pais_novo, pais_registado)
        elif menu[0] == "RPAE":
            pais_novo = menu[1]
            pais_registado = menu[2]
            RPAE(lista_paises, pais_novo, pais_registado)
        elif menu[0] == "RPII":
            pais_novo = menu[1]
            index = menu[2]
            RPII(lista_paises, pais_novo, index)
        elif menu[0] == "VNE":
            print(f"O número de elementos são {VNE(lista_paises)}.")
        elif menu[0] == "VP":
            pais_nome = menu[1]
            verificar = VP(lista_paises, pais_nome)
            if verificar == True:
                print(f"O país {pais_nome} encontra-se na lista.")
            else:
                print(f"O país {pais_nome} não se encontra na lista.")
        elif menu[0] == "EPE":
            print(f"O país {EPE(lista_paises)} foi eliminado da lista.")
        elif menu[0] == "EUE":
            print(f"O país {EUE(lista_paises)} foi eliminado da lista.")
        elif menu[0] == "EP":
            pais_escolhido = menu[1]
            if EP(lista_paises, pais_escolhido) == True:
                print(f"O país {pais_escolhido} foi eliminado da lista.")
            else:
                print(f"O país {pais_escolhido} não se encontra na lista.")

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
