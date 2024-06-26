﻿"""
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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos
def load_jobs(control, filename_jobs):
    
    jobsfile = cf.data_dir + 'data/' + filename_jobs
    input_filejob = csv.DictReader(open(jobsfile, encoding='utf-8'),delimiter=";")
    for job in input_filejob:
        model.add_job(control['model'],job)
        model.carga_lista_fechas(control['model'], job)
      
    return control
# Funcion cantidad ofertas publicadas de la carga de datos
def cantidad_ofertas(datastructs):
    tamaño = model.data_size(datastructs)
    return tamaño
# Función ordenamiento por fecha de mayor a menor de las ofertas publicadas
def ofertas_ordenadas(datastructs):
    fechas_ordenadas = model.ofertas_ordenadas(datastructs["jobs"])
    return fechas_ordenadas
    
def load_skills(control, filename_skills):
    skillsfile = cf.data_dir +'data/' + filename_skills
    input_fileskill = csv.DictReader(open(skillsfile, encoding='utf-8'),delimiter=";")
    for skill in input_fileskill:
        model.add_skill(control['model'], skill)
    return control
    
def load_multilocations(control, filename_multilocations):
    multilocationsfile= cf.data_dir +'data/' + filename_multilocations
    input_filemultilocations = csv.DictReader(open(multilocationsfile, encoding='utf-8'),delimiter=";")
    for multilocations in input_filemultilocations:
        model.add_multilocations(control['model'], multilocations)
    return control

def load_employments_type(control, filename_employments_types):
    employments_typesfile= cf.data_dir +'data/' + filename_employments_types
    input_fileemployments_types = csv.DictReader(open(employments_typesfile, encoding='utf-8'),delimiter=";")
    
    for employments_types in input_fileemployments_types:
        model.add_employments_types(control['model'], employments_types)
    return control

def load_data(control, filename_jobs, filename_skills, filename_multilocations, filename_employments_types):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
    
    num_ofertas= load_jobs(control, filename_jobs)    
    num_skills = load_skills(control, filename_skills)
    num_multilocations = load_multilocations(control, filename_multilocations)
    num_employments_types = load_employments_type(control, filename_employments_types)

    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
    
    #return num_ofertas,jobsfile, num_skills, num_multilocations, num_employments_types, tiempo_total, memoria_total  

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,id_pais, num_ofertas,nivel_experiencia):
     # TODO: Modificar el requerimiento 1
    """
    Retorna el resultado del requerimiento 1
    """
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
        
    lista_final, ofertas_trabajo_pais, ofertas_trabajo_condicion= model.req_1(control,id_pais, num_ofertas,nivel_experiencia)
    
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
   
    
    return lista_final, ofertas_trabajo_pais, ofertas_trabajo_condicion, tiempo_total, memoria_total



def req_2(control, input_empresa, input_ciudad,input_cant_ofertas):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
   
    lista = model.req_2(control, input_empresa, input_ciudad,input_cant_ofertas)
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
    
    return lista
#, tiempo_total,memoria_total


def req_3(control,nombre_empresa,fecha_inicial,fecha_final):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
        
    rta=model.req_3(control["model"],nombre_empresa,fecha_inicial,fecha_final)
    
    
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
        
    return rta, tiempo_total, memoria_total



def req_4(control,id_pais, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
        
    lista_filtro, total_offers, total_companies, total_citites, max_count, max_name, min_count, min_name=model.req_4(control,id_pais, fecha_inicial, fecha_final)    
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
    

    return lista_filtro, total_offers, total_companies, total_citites, max_count, max_name, min_count, min_name, tiempo_total, memoria_total


def req_5(control, nom_ciudad, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    tamano_lista_filtrada, cant_total_empresas,  sacar_max_empresa, max_ofertas, sacar_min_empresa, min_ofertas, lista_filtrada= model.req_5(control, nom_ciudad, fecha_inicial, fecha_final)
    return tamano_lista_filtrada, cant_total_empresas,  sacar_max_empresa, max_ofertas, sacar_min_empresa, min_ofertas, lista_filtrada


def req_6(control, n_ciudades, expertisia, año):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 
    tiempo_inicial = get_time()
    memoria = True
    if memoria: 
        tracemalloc.start()
        memoria_inicial = get_memory()
        
    rta=model.req_6(control["model"], n_ciudades, expertisia, año)
    
    
    tiempo_final = get_time()
    tiempo_total = delta_time(tiempo_inicial, tiempo_final)   
    if memoria:
        memoria_final = get_memory()
        tracemalloc.stop()
        memoria_total= delta_memory(memoria_final, memoria_inicial)
        
    return rta, tiempo_total, memoria_total
    

def req_7(control, año, experticia):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req_7_list, max_name, max_count=model.req_7(data_structs, año, experticia)
    return req_7_list, max_name, max_count
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
