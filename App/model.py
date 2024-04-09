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
from datetime import datetime as dt

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
    


def comparar_fechas_pais_req_3(trabajo_1,trabajo_2):
    if trabajo_1["published_at"]<trabajo_2["published_at"]:
        return True
    
    elif trabajo_1["published_at"]==trabajo_2["published_at"]:
        return trabajo_1["country_code"]<trabajo_2["country_code"]
    
    else: 
        return False

def req_3(data_structs, nombre_empresa, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    mapa= data_structs["id_jobs"]
    fecha_i=dt.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_f=dt.strptime(fecha_final, "%Y-%m-%d")
    llaves=mp.keySet(mapa)
    req_3_list=lt.newList('ARRAY_LIST')
    
    for llave in lt.iterator(llaves):
        pareja=mp.get(mapa,llave)
        job=me.getValue(pareja)
        fecha_y_hora=job["published_at"]
        fecha_trabajo=dt.strptime(fecha_y_hora, "%Y-%m-%dT%H:%M:%S.%fZ")
        if job["company_name"]==nombre_empresa:
            if fecha_trabajo>=fecha_i and fecha_trabajo<=fecha_f:
                lt.addLast(req_3_list,job)
                
    req_3_ordenado=se.sort(req_3_list,comparar_fechas_pais_req_3)
                
    """cantidad_de_ofertas=lt.size(req_3_list)
    
    contador_junior=0
    contador_mid=0
    contador_senior=0
    for trabajo in lt.iterator(req_3_list):
        if trabajo["experience_level"]=="junior":
           contador_junior=contador_junior+1
        if trabajo["experience_level"]=="mid":
           contador_mid=contador_mid+1
        if trabajo["experience_level"]=="senior":
           contador_senior=contador_senior+1"""
        
    
    return req_3_ordenado
        
   

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


def req_6(data_structs, n_ciudades, expertisia, año):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    mapa= data_structs["id_jobs"]
    año_tiempo=dt.strptime(año, "%Y")
    req_6_list=lt.newList('ARRAY_LIST')
    llaves=mp.keySet(mapa)
    
    for llave in lt.iterator(llaves):
        pareja=mp.get(mapa,llave)
        trabajo=me.getValue(pareja)
        fecha_y_hora=trabajo["published_at"]
        fecha_trabajo=dt.strptime(fecha_y_hora, "%Y-%m-%dT%H:%M:%S.%fZ")
        if fecha_trabajo==año_tiempo:
            if expertisia==trabajo["experience_level"]:
                lt.addLast(req_6_list,trabajo)
    
    mapa_ciudades=mp.newMap(numelements=17,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           cmpfunction=None)
    
    mapa_ciudades_2=mp.newMap(numelements=17,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           cmpfunction=None)
    
     
    for llave in lt.iterator(llaves):
        pareja=mp.get(mapa,llave)
        trabajo=me.getValue(pareja)   
        for job in lt.iterator(req_6_list):
            ciudad= job['city']
            if trabajo["city"]==ciudad:
                if mp.contains(mapa_ciudades,ciudad)==False:
                    valor_contador=1
                    mp.put(mapa_ciudades,ciudad,valor_contador)
                    mp.put(mapa_ciudades_2,ciudad,valor_contador)
                    pareja_actualizar=mp.get(mapa_ciudades,ciudad)
                    pareja_actualizar_2=mp.get(mapa_ciudades,ciudad)
                elif mp.contains(mapa_ciudades,ciudad)==True:
                    valor_contador=valor_contador+1
                    me.setValue(pareja_actualizar,valor_contador)
                    me.setValue(pareja_actualizar_2,valor_contador)
                    
                    
    
        
    
    
    
    
    llaves_ciudades=mp.keySet(mapa_ciudades)
    mayor=0
    menor=10000
    for llave_ciudad in lt.iterator(llaves_ciudades):
        pareja_llave=mp.get(mapa,llave_ciudad)
        cantidad=me.getValue(pareja_llave)
        ciudad_sacada_mostrar=me.getKey(pareja_llave)
        if cantidad>mayor:
            mayor_ciudad_mostrar=ciudad_sacada_mostrar
            mayor_mostrar=cantidad
        if cantidad<menor:
            menor_ciudad=llave_ciudad
            menor=cantidad
    
        

            
    
    
        
        
    lista_ciudades_mas=[]        
    
    i=0
    while i<n_ciudades:
        mayor=0
        llaves_ciudades=mp.keySet(mapa_ciudades)    
        for llave_ciudad in lt.iterator(llaves_ciudades):
            pareja_llave=mp.get(mapa_ciudades,llave_ciudad)
            cantidad_sacada=me.getValue(pareja_llave)
            ciudad_sacada=me.getKey(pareja_llave)
            if cantidad>mayor:
                mayor_ciudad_elem=ciudad_sacada
                mayor=cantidad_sacada
        pareja_elem=mp.get(mapa_ciudades,mayor_ciudad_elem)
        ciu_ele=me.getKey(pareja_elem)
                
        lista_ciudades_mas.append(mayor_ciudad_elem)
        mp.remove(mapa_ciudades,ciu_ele)
        
                
            
        i=i+1

    
    numciudades=len(lista_ciudades_mas)
    
    
    
    req_6_list_n_ciudades=lt.newList('ARRAY_LIST')
    
    for trabajo in lt.iterator(req_6_list):
        if trabajo["city"] in lista_ciudades_mas:
            lt.addLast(req_6_list_n_ciudades,trabajo)
        
    
    lst_empresa=[]
    
    for trabajo in lt.iterator(req_6_list_n_ciudades):
        empresa=trabajo["company_name"]
        if empresa not in lst_empresa:
            lst_empresa.append(empresa)
    
    cantidad_de_empresas=len(lst_empresa)
        

    total_de_ofertas=lt.size(req_6_list_n_ciudades)
    
    salario_promedio=None 
    
    
    
    rta="Numero de ciudades a consultar: "+str(numciudades)+ ", Cantidad de empresas: "+ str(cantidad_de_empresas)+ ", Cantidad de ofertas: "+str(total_de_ofertas)+", La ciudad con mas ofertas es: "+str(mayor_ciudad_mostrar) +" Y tiene un total de ofertas de "+ str(mayor_mostrar)+", La ciudad con menor cantidad de ofertas es "+ str(menor_ciudad)+" y tiene un total de ofertas de "+ str(menor) 
    
    return rta   
    
    


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
