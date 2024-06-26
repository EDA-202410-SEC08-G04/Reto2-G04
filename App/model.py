﻿"""data_size(data_structs)
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
 
    date_str1 = data_1["published_at"]
    date_str2 = data_2["published_at"]
    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    
    date1 = dt.strptime(date_str1, format)
    date2 = dt.strptime(date_str2, format)
    
    if date1 > date2:
        return True
    else:
        return False  
    
    value= pair["value"]
def criterio_2(data_1, data_2):
    valor_1= data_1["value"]
    valor_2= data_2["value"]
    if valor_1 > valor_2:
        return True
    else:
       return False
    
def add_skill(data_structs, skill):
    """
    Función para agregar nuevos elementos a la lista
    """

    lt.addLast(data_structs['skills'], skill)
    
    return data_structs
    
    
def add_multilocations(data_structs, multilocation):
    """
    Función para agregar nuevos elementos a la lista
    """

    lt.addLast(data_structs['multilocations'], multilocation)
    
    return data_structs

def add_employments_types(data_structs, employments_types):
    """
    Función para agregar nuevos elementos a la lista
    """

    lt.addLast(data_structs['employments_types'], employments_types)
    
    return data_structs



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
    ofertas_trabajo_pais=0
    ofertas_trabajo_condicion=0
    for i in range(0, size_keys+1):
        element= lt.getElement(keys, i)
        table_element= mp.get(id_jobs, element)
        country_code_element= table_element["value"]["country_code"]
        experience_level=table_element["value"]["experience_level"]
        if country_code_element==id_pais:
            ofertas_trabajo_pais+=1
        if experience_level==nivel_experiencia:
            ofertas_trabajo_condicion+=1
        if country_code_element==id_pais and experience_level==nivel_experiencia:
            lt.addLast(lista_filtro,table_element["value"])
    listed_dates = merg.sort(lista_filtro, criterio)
    lista_final=lt.newList("ARRAY_LIST")
    for j in range(1,int(num_ofertas)+1):
        job_a_insertar=lt.getElement(listed_dates,j)
        lt.addLast(lista_final,job_a_insertar)

    return lista_final, str(ofertas_trabajo_pais), str(ofertas_trabajo_condicion)
        
 
        

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
    
    cantidad_ofertas=lt.size(req_3_ordenado)
    
    
    contador_junior=0
    contador_mid=0
    contador_senior=0
    for trabajo in lt.iterator(req_3_ordenado):
        if trabajo["experience_level"]=="junior":
           contador_junior=contador_junior+1
        if trabajo["experience_level"]=="mid":
           contador_mid=contador_mid+1
        if trabajo["experience_level"]=="senior":
           contador_senior=contador_senior+1

    print("la cantidad de ofertas es: "+str(cantidad_ofertas), "; Junior: "+ str(contador_junior)+"; mid: "+ str(contador_mid)+"; Senior: "+ str(contador_senior))
          
    return req_3_ordenado
      

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
            
    map_company=mp.newMap(numelements=17,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           cmpfunction=None)
    
    map_city=mp.newMap(numelements=17,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           cmpfunction=None)
            
    
    for offer in lt.iterator(lista_filtro):
        company_name= offer["company_name"]
        if mp.contains(map_company,company_name)==False:
            contador=1
            mp.put(map_company, company_name, contador)
        else:
            contador+=1
            mp.put(map_company,company_name, contador )
    
    for city in lt.iterator(lista_filtro):
        city_act= city["city"]
        if mp.contains(map_city, city_act)==False:
            contador=1
            mp.put(map_city, city_act, contador)
        else:
            contador+=1
            mp.put(map_city,city_act, contador)

    
    list_min_max_cities= lt.newList("ARRAY_LIST")
    cities= mp.keySet(map_city)
    for city in lt.iterator(cities):
        pair= mp.get(map_city, city)
        lt.addLast(list_min_max_cities, pair)
    ordered_values= merg.sort(list_min_max_cities, criterio_2)
    max_city=lt.lastElement(ordered_values)
    max_count=max_city["value"]
    max_name=max_city["key"]
    min_city= lt.firstElement(ordered_values)
    min_count=min_city["value"]
    min_name=min_city["key"]
    
    total_offers= lt.size(lista_filtro)
    total_companies= mp.size(map_company)
    total_citites= mp.size(map_city)
    
    
    
    return lista_filtro , total_offers, total_companies, total_citites, max_count, max_name, min_count, min_name 
        

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
        fecha_y_hora_separados=fecha_y_hora.split("-")
        fecha_trabajo=dt.strptime(fecha_y_hora_separados[0], "%Y")
        if fecha_trabajo==año_tiempo:
            if expertisia==trabajo["experience_level"] or expertisia=="indiferente":
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
    #Este mapa ciudades 2 es por si acaso necesite otro mapa 
    
    valores_ciudades={}
    
    for trabajo_lista in lt.iterator(req_6_list):
        ciudad_lista=trabajo_lista['city']    
        if ciudad_lista not in valores_ciudades:
            valor_contador=1
            valores_ciudades[ciudad_lista]=valor_contador
        elif ciudad_lista in valores_ciudades:
            valor_contador=valores_ciudades[ciudad_lista]
            valor_contador=valor_contador+1
            valores_ciudades[ciudad_lista]=valor_contador
    
            
    for llave_ciudad in valores_ciudades:
        valor_ciu=valores_ciudades[llave_ciudad]
        mp.put(mapa_ciudades,llave_ciudad,valor_ciu)   
        mp.put(mapa_ciudades_2,llave_ciudad,valor_ciu)
                    
            
    llaves_ciudades=mp.keySet(mapa_ciudades)
    mayor=0
    menor=10000
    for llave_ciudad in lt.iterator(llaves_ciudades):
        pareja_llave=mp.get(mapa_ciudades,llave_ciudad)
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
            if cantidad_sacada>mayor:
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
    
    
    
    
    
    print("El total de ciudades que cumplen con las condiciones de la consulta: "+str(numciudades))
    print("El total de empresas que cumplen con las condiciones de la consulta: "+str(cantidad_de_empresas))
    print("El total de ofertas publicadas que cumplen con las condiciones de la consulta: "+str(total_de_ofertas))
    print("Nombre de la ciudad con mayor cantidad de ofertas de empleos: "+str(mayor_ciudad_mostrar)+" y su conteo: "+str(mayor_mostrar))
    print("Nombre de la ciudad con menor cantidad de ofertas de empleos: "+str(menor_ciudad)+" y su conteo: "+str(menor))
          
    

    
    
    
    return req_6_list_n_ciudades
    
    


def req_7(data_structs, año, experticia):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    mapa= data_structs["id_jobs"]
    año_tiempo=dt.strptime(año, "%Y")
    req_7_list=lt.newList('ARRAY_LIST')
    llaves=mp.keySet(mapa)
    
    for llave in lt.iterator(llaves):
        pareja=mp.get(mapa,llave)
        trabajo=me.getValue(pareja)
        fecha_y_hora=trabajo["published_at"]
        fecha_y_hora_separados=fecha_y_hora.split("-")
        fecha_trabajo=dt.strptime(fecha_y_hora_separados[0], "%Y")
        if fecha_trabajo==año_tiempo:
            if experticia==trabajo["experience_level"] or experticia=="indiferente":
                lt.addLast(req_7_list,trabajo)
    
    
    mapa_pais=mp.newMap(numelements=17,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           cmpfunction=None)

    
    for element in lt.iterator(req_7_list):
        pais= element["country_code"]
        if mp.contains(mapa_pais, pais)==False:
            contador=1
            mp.put(mapa_pais, pais, contador)
        else:
            contador+=1
            mp.put(mapa_pais,pais, contador)

    
    list_min_max_countries= lt.newList("ARRAY_LIST")
    countries= mp.keySet(mapa_pais)
    for pais in lt.iterator(countries):
        pair= mp.get(mapa_pais, pais)
        lt.addLast(list_min_max_countries, pair)
    ordered_values= merg.sort(list_min_max_countries, criterio_2)
    max_country=lt.lastElement(ordered_values)
    max_count=max_country["value"]
    max_name=max_country["key"]
    return req_7_list, max_name, max_count
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
