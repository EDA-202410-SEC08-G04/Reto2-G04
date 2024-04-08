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
    
    data_structs["id_jobs"]= mp.newMap(5, maptype='PROBING', loadfactor=0.5)
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

# def criterio(data_1, data_2):
#     if data_1["published_at"] > data_2["published_at"]:
#         return True
#     else:
#        return False
   
def criterio(data_1, data_2):
 
    date_str1 = data_1["published_at"]
    date_str2 = data_2["published_at"]
    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    
    date1 = dt.strptime(date_str1, format)
    date2 = dt.strptime(date_str2, format)
    
    if date1 > date2:
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
    
def add_job(data_structs, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    id = job["id"]
    mp.put(data_structs["id_jobs"], id, job)
    


def req_1(data_structs,id_pais, num_ofertas,nivel_experiencia):
    
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    lista_filtro=lt.newList("ARRAY_LIST")
    id_jobs=data_structs["id_jobs"]
    keys= mp.keySet(id_jobs)
    size_keys= lt.size(keys)
    for i in range(0, size_keys+1):
        element= lt.getElement(keys, i)
        table_element= mp.get(id_jobs, element)
        country_code_element= table_element["value"]["country_code"]
        experience_level=table_element["value"]["experience_level"]
        if country_code_element==id_pais and experience_level==nivel_experiencia:
            lt.addLast(lista_filtro,table_element["value"])
    listed_dates = merg.sort(lista_filtro, criterio)
    lista_final=lt.newList("ARRAY_LIST")
    for j in range(1,int(num_ofertas)+1):
        jod_a_insertar=lt.getElement(listed_dates,j)
        lt.addLast(lista_final,jod_a_insertar)
    
    return lista_final
        
 
        

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs, id_pais, fecha_inicial, fecha_final):
    lista_filtro = lt.newList("ARRAY_LIST")
    id_jobs = data_structs["id_jobs"]
    keys = mp.keySet(id_jobs)
    size_keys = lt.size(keys)
    for i in range(1, size_keys + 1):  
        element = lt.getElement(keys, i)
        table_element = mp.get(id_jobs, element)
        country_code_element = table_element["value"]["country_code"]
        date = table_element["value"]["published_at"]
        date_stripped = dt.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        stripped_datetime_fecha_inicial= dt.strptime(fecha_inicial, "%Y-%m-%d")
        stripped_datetime_fecha_final= dt.strptime(fecha_final, "%Y-%m-%d")

        if country_code_element == id_pais and stripped_datetime_fecha_inicial <= date_stripped <= stripped_datetime_fecha_final:
            lt.addLast(lista_filtro, table_element["value"])
            
    listed_dates = merg.sort(lista_filtro, criterio)
    return listed_dates
        

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


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
