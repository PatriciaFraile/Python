# Crea un programa que lea los datos de un fichero de texto,
#que transforme cada fila en un diccionario y lo añada a una lista llamada personas

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run():
    claves = ['id','nombre','apellido','nacimiento']
    lista_dic = []
    try:
        with open('personas.txt', 'r', encoding='utf-8') as f:
            for linea in f:     
                dic = {}        # diccionario nuevo
                for c,v in zip(claves,linea.split(';')):  #Elimina los ; del fichero 
                    dic[c] = v.rstrip()     
                lista_dic.append(dic)       
    except Exception as e:
        print(e)
    finally:
        f.close()
    
    for d in lista_dic:     #presento resultados
        print(f"{d['id']}:{d['nombre']}:{d['apellido']}:{d['nacimiento']})")


if __name__ == '__main__':
    run()


