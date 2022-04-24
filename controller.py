from models.LinkedList import LinkedList

def registar_pais_inicio(lista_paises, pais_novo):
    lista_paises.insert_at_start(pais_novo)
    return lista_paises
    
def registar_pais_fim(lista_paises, pais_novo):
    lista_paises.insert_at_end(pais_novo)
    return lista_paises

def registar_depois_registado(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_after_item(pais_registado, pais_novo)
    return lista_paises

def registar_antes_registado(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_before_item(pais_registado, pais_novo)
    return lista_paises

def registar_pais_index(lista_paises, pais_novo, index):
    lista_paises.insert_at_index(int(index), pais_novo)
    return lista_paises

def verificar_numero_elementos(lista_paises):
    return lista_paises.get_count()

def verificar_pais(lista_paises, pais_nome):
    if lista_paises.search_item(pais_nome) == True:
        return True
    else:
        return False

def eliminar_primeiro_pais(lista_paises):
    primeiro_pais = lista_paises.start_node.item
    lista_paises.delete_at_start()
    return primeiro_pais

def eliminar_ultimo_pais(lista_paises):
    ultimo_pais = lista_paises.get_last_node()
    lista_paises.delete_at_end()
    return ultimo_pais

def eliminar_pais_escolhido(lista_paises, pais_escolhido):
    if lista_paises.search_item(pais_escolhido) == True:
        lista_paises.delete_element_by_value(pais_escolhido)
        return True
    else:
        return False
    