"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, tamaño_archivo):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    #data, tiempo, memoria =controller.load_data(data_structs,control, (tamaño_archivo + '-jobs.csv'), (tamaño_archivo + '-skills.csv'), (tamaño_archivo + '-employments_types.csv'), (tamaño_archivo + '-multilocations.csv'))
    #return data, tiempo, memoria
    
    controller.load_data(control, (tamaño_archivo + '-jobs.csv'), (tamaño_archivo + '-skills.csv'), (tamaño_archivo + '-employments_types.csv'), (tamaño_archivo + '-multilocations.csv'))
    
    #return data,jobsfile


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,nombre_empresa,fecha_inicial,fecha_final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    jobs=controller.req_3(control,nombre_empresa,fecha_inicial,fecha_final)
    
    
    headers ={"Fecha de publicación": [],
              "Título de la oferta": [],
              "Empresa que publica": [],
              "Nivel experticia": [],
              "País de la oferta": [],
              "Ciudad de la oferta": [],
              "Tamaño de la empresa de la oferta":[],
              "Tipo de lugar de trabajo de la oferta":[],
              "Disponible a contratar ucranianos":[]}
    for job in lt.iterator(jobs): 
        headers["Fecha de publicación"].append(job['published_at'])
        headers["Título de la oferta"].append(job['title'])
        headers["Empresa que publica"].append(job['company_name'])
        headers["Nivel experticia"].append(job['experience_level'])
        headers["País de la oferta"].append(job['country_code'])
        headers["Ciudad de la oferta"].append(job['city'])
        headers["Tamaño de la empresa de la oferta"].append(job['company_size'])
        headers["Tipo de lugar de trabajo de la oferta"].append(job['workplace_type'])
        headers["Disponible a contratar ucranianos"].append(job['open_to_hire_ukrainians'])
        
    return headers 


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control, n_ciudades, expertisia, año):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    return controller.req_6(control, n_ciudades, expertisia, año)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
#control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    control= new_controller()
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            inputs_2= input("Escriba el tamaño de los archivos a cargar(small, medium, large, 10-por, etc)")
            print("Cargando información de los archivos ....\n")
            #carga, tiempo, memoria = load_data(control, inputs_2,data_structs)
            carga = load_data(control, inputs_2)
            datastructs = control["model"]
            tamaño = controller.cantidad_ofertas(datastructs)
            print ("El total de ofertas publicadas cargadas es: ", tamaño)
            orden = controller.ofertas_ordenadas(datastructs)
            
            # imprime las primeras 3 ofertas y las 3 ultimas ofertas
            tres_p_u = []
            for i in range(1, 4):
                elemento = lt.getElement(orden, i)
                tres_p_u.append(elemento)
                
            n = tamaño -2     
            for i in  range(n,tamaño+1):
                elemento = lt.getElement(orden, i)
                tres_p_u.append(elemento)
                
            headers ={"Fecha de publicación": [],
                "Título de la oferta": [],
                "Nombre de la empresa": [],
                "Nivel de experticia de la oferta": [],
                "País de la oferta": [],
                "Ciudad de la oferta": []}
            for job in tres_p_u: 
                headers["Fecha de publicación"].append(job['published_at'])
                headers["Título de la oferta"].append(job['title'])
                headers["Nombre de la empresa"].append(job['company_name'])
                headers["Nivel de experticia de la oferta"].append(job['experience_level'])
                headers["País de la oferta"].append(job['country_code'])
                headers["Ciudad de la oferta"].append(job['city'])
            print(tabulate(headers, headers='keys'))
            #print ("memoria total: ", memoria)
            #print ("tiempo total: ", tiempo)
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            nombre_empresa=input("Escribe el nombre de la empresa que quieres consultar: ")
            fecha_inicial=input("Escribe La fecha inicial del periodo a consultar en el formato YYYY-MM-DD: ")
            fecha_final=input("Escribe La fecha final del periodo a consultar en el formato YYYY-MM-DD: ")
            print ("Estas son las N ofertas de trabajo según el nombre de la empresa y la fecha de publicación:" )
            resultado_req_3=print_req_3(control,nombre_empresa,fecha_inicial,fecha_final)
            print(tabulate(resultado_req_3,headers='keys',tablefmt="grid"))
            

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            n_ciudades=int(input("Escribe la cantidad de ciudades que quiere consultar: "))
            expertisia=input("Escriba el nivel de experiencia a consultar(junior, mid, senior): ")
            año=(input("Escribe el año que te gustaria consultar: "))
            print("Estas son las N ciudades con mayor número de oferta de trabajo segun la experticia seleccionada en el año seleccionado: " )
            resultado_req_6=print_req_6(control,n_ciudades, expertisia, año)
            print(resultado_req_6)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
