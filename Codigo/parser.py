import config as cf

archivo = open(cf.data_dir + 'prueba.txt',encoding="utf-8" )

def main(archivo):
    for linea in archivo:
        respuesta = False
        checkLine = check(linea)

        if checkLine == 1:
            respuesta = True

        else:
            break

    print(respuesta)
        
        
main(archivo)