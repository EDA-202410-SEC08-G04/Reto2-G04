"""data_size(data_structs)
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time 
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime as dt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    data_structs = {'jobs': None,
            'skills': None,
            'employments_types': None,
            'multilocations': None,
            'id_jobs': None,
            'id_skills': None, 
            'id_employments': None,
            'id_multilocations': None}

    data_structs['jobs'] = lt.newList(datastructure='ARRAY_LIST')
    data_structs['skills'] = lt.newList(datastructure='ARRAY_LIST')
    data_structs['employments_types'] = lt.newList(datastructure='ARRAY_LIST')
    data_structs['multilocations'] = lt.newList(datastructure='ARRAY_LIST')
    
    data_structs["id_jobs"]= mp.newMap(206563, maptype='PROBING', loadfactor=0.5)
    data_structs["id_skills"]= mp.newMap(577162, maptype='PROBING', loadfactor=0.5)
    data_structs["id_employments"]= mp.newMap(259837, maptype='PROBING', loadfactor=0.5)
    data_structs["id_multilocations"] = mp.newMap(244937, maptype='PROBING', loadfactor=0.5)
    return data_structs

# Funciones para agregar informacion al modelo

def add_job(data_structs, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    id = job["id"]
    mp.put(data_structs["id_jobs"], id, job)
    
# Funciones ordenamiento carga de datos de ofertas
    
def carga_lista_fechas(data_structs, job):
    fecha = job["published_at"]
    #lt.addLast(data_structs['jobs'], fecha)
    lt.addLast(data_structs['jobs'], job)
   
def ofertas_ordenadas(lista_jobs):
    fechas_ordenadas = merg.sort(lista_jobs, criterio)
    return fechas_ordenadas 

def criterio(data_1, data_2):
    if data_1["published_at"] > data_2["published_at"]:
        return True
    else:
       return False
    
def add_skill(data_structs, skill):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    id = skill["id"]
    mp.put(data_structs["id_skills"], id, skill)
    
    
def add_multilocations(data_structs, multilocations):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    id = multilocations["id"]
    mp.put(data_structs["id_multilocations"], id, multilocations)

def add_employments_types(data_structs,  employments_types):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    id = employments_types["id"]
    mp.put(data_structs["id_employments"], id, employments_types)



# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos. 
    
    
    
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    
    jobsListSize= mp.size(data_structs["id_jobs"])
    return jobsListSize
    

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs, input_empresa, input_ciudad,input_cant_ofertas): 
    """
    """
    # TODO: Realizar el requerimiento 2
    trabajos = data_structs["id_jobs"]
    tabla_empresa =  mp.newMap(203563, maptype='CHAINING', loadfactor=0.1)
    filtro_final = lt.newList('ARRAY_LIST')
    valores_1 = mp.valueSet(trabajos)
    tamano_1 = lt.size(valores_1)
    for i in range(1, tamano_1+1):
        empresa = lt.getElement(valores_1, i)
        nom_empresa = empresa["company_name"]
        nom_inicial = empresa["title"]
        if mp.contains(tabla_empresa, nom_empresa):
           lt.addLast(bucket, empresa)
        else:
            # Si la llave no está en el mapa, crear un nuevo bucket
            bucket = lt.newList('ARRAY_LIST')
            lt.addLast(bucket, empresa)

    mp.put(tabla_empresa, nom_empresa, bucket)
        
    tamano_2 = mp.size(tabla_empresa)
    valor_empresa= mp.get(tabla_empresa,input_empresa)
    valor3 =valor_empresa['value']['elements']
    for elemento in valor3:
        valor_filtro_empresa = elemento['company_name']
        valor_filtro_ciudad = elemento['city']
        if valor_filtro_empresa == input_empresa:
           cont_empresa = +1
           if valor_filtro_ciudad  == input_ciudad:
              cont_ciudad = +1
              lt.addLast(filtro_final, elemento)       
    tamano_ff = lt.size(filtro_final)
    return filtro_final


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass
def sort_crit_req5(data_1, data_2):
    
    if data_1["published_at"] < data_2["published_at"]:
        return True
    
    elif data_1["published_at"]== data_2["published_at"]:
        if data_1["company_name"] < data_2["company_name"]:
            return True
        else: 
            return False

def req_5(data_structs, nom_ciudad, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    trabajos = data_structs["id_jobs"]
    filtro_ciudad=  mp.newMap(203563, maptype='PROBING', loadfactor=0.5)
    valores_1 = mp.valueSet(trabajos)
    tamano_1 = lt.size(valores_1)
    
    for i in range(1,tamano_1+1): #On
        elemento_x = lt.getElement(valores_1, i)
        ciudad = elemento_x["city"]
        
        if not mp.contains(filtro_ciudad, ciudad):
            lista = lt.newList('ARRAY_LIST')
            lt.addLast(lista, elemento_x)
            mp.put(filtro_ciudad, ciudad, lista )
        
        else:
            lista = me.getValue(mp.get(filtro_ciudad, ciudad))   
            lt.addLast(lista, elemento_x)
            
    
    
    fecha_i=dt.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_f=dt.strptime(fecha_final, "%Y-%m-%d")
    
    
    #valores_ciudad = mp.get(filtro_ciudad, nom_ciudad)
    valores_ciudad = lt.newList('ARRAY_LIST')
    lista_filtrada = lt.newList('ARRAY_LIST')
    llaves = mp.keySet(filtro_ciudad)

# Iterar sobre todos los elementos del mapa
    for i in range(1, mp.size(filtro_ciudad) + 1):    
       elemento = lt.getElement(llaves, i)
       if elemento == nom_ciudad:
            valor = mp.get(filtro_ciudad, elemento)
            lt.addLast(valores_ciudad, valor)
            
    tam_ciudad = lt.size(valores_ciudad)
    
    for i in range(0, tam_ciudad): 
        element = lt.getElement(valores_ciudad,i)
        fecha = element["published_at"]
        if fecha["published_at"] <= fecha_final and fecha["published_at"] >= fecha_inicial:
            lt.addLast(lista_filtrada, fecha) 
    
    tamano_lista_filtrada = lt.size(lista_filtrada)
    
    # Obtener el total de empresas que publicaron al menos una oferta en la ciudad
    
    total_empresas = []
    empresa_mayor_num ={}
    empresa_menor_num ={}
    for i in range(tamano_lista_filtrada):
        elemento = lt.getElement(lista_filtrada, i)
        nom_empresa = elemento["company_name"]
        
        if nom_empresa not in total_empresas:
            total_empresas.append(nom_empresa)

    #Empresa con mayor número de ofertas y su conteo
    
    for i in range(tamano_lista_filtrada):
        elemento = lt.getElement(lista_filtrada, i)
        nom_empresa = elemento["company_name"]
        if nom_empresa not in empresa_mayor_num:
            empresa_mayor_num[nom_empresa] = 1
        else:
            empresa_mayor_num[nom_empresa] +=1
                     
    cant_total_empresas = len(total_empresas)
    sacar_max_empresa = max(empresa_mayor_num, key=empresa_mayor_num.get)
    max_ofertas = empresa_mayor_num.get(sacar_max_empresa, 0)
    
    #Empresa con menor número de ofertas (al menos una) y su conteo
    for i in range(tamano_lista_filtrada):
        elemento = lt.getElement(lista_filtrada, i)
        nom_empresa = elemento["company_name"]
        
        if nom_empresa not in empresa_menor_num:
            empresa_menor_num[nom_empresa] = 1
        else:
            empresa_menor_num[nom_empresa] +=1
    sacar_min_empresa = min(empresa_mayor_num, key=empresa_menor_num.get)
    min_ofertas = empresa_menor_num.get(sacar_min_empresa, 0)
   
    # Ordenar ofertas cronológicamente por fecha y nombre de la empresa
   
    merg.sort(lista_filtrada, sort_crit_req5) #Onlogn
    return tamano_lista_filtrada, cant_total_empresas,  sacar_max_empresa, max_ofertas, sacar_min_empresa, min_ofertas, lista_filtrada
 



def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    
    if data_1["published_at"] < data_2["published_at"]:
        return True
    
    elif data_1["published_at"]== data_2["published_at"]:
        if data_1["company_name"] < data_2["company_name"]:
            return True
        else: 
            return False
   
    


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    
    pass
