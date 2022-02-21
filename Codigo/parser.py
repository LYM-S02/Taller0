
import config as cf

archivo = open(cf.data_dir + 'pruebaLinea.txt',encoding="utf-8" )

reservadas = ["defvar","=","move","turn","face","put","pick","move-dir","run-dirs","move-face","(skip)",
               "(defvar","(=","(move","(turn","(face","(put","(pick","(move-dir","(run-dirs","(move-face"]

variables = []

funciones = []

parentesis = {"(": 0 , ")": 0 }


def main(archivo):

    for linea in archivo:
        respuesta = False
        checkLine = check(linea)

        if checkLine == 1:
            respuesta = True

        else:
            break

    print(respuesta)
        
def check(linea):
    lineaMod = linea.lstrip(' ')
    listaPalabras = lineaMod.split(" ")
    primerComando = listaPalabras[0]

    if primerComando == "(defvar":
        check = checkDefvar(listaPalabras)

    elif primerComando == "(=":
        check = checkEq(listaPalabras)

    elif primerComando == "(move":
        check = checkMove(listaPalabras)
        
    elif primerComando == "(turn":
        check = checkTurn(listaPalabras)

    elif primerComando == "(face":
        check = checkFace(listaPalabras)

    elif primerComando == "(put":
        check = checkPut(listaPalabras)

    elif primerComando == "(pick":
        check = checkPick(listaPalabras)

    elif primerComando == "(move-dir":
        check = checkMoveDir(listaPalabras)

    elif primerComando == "(run-dirs":
        check = checkRunDirs(listaPalabras)

    elif primerComando == "(move-face":
        check = checkMoveFace(listaPalabras)

    elif primerComando == "(if":
        check = checkIf(listaPalabras)

    elif primerComando == "(loop":
        check = checkLoop(listaPalabras)

    elif primerComando == "(repeat":
        check = checkRepeat(listaPalabras)

    elif primerComando == "(defun" :
        check = checkDefun(listaPalabras)


    return check

def checkDefvar(listaPalabras):
    if len(listaPalabras) == 3:
        nombre = listaPalabras[1]
        numero = listaPalabras[2]
        if nombre not in reservadas:
            ultimoChar = numero[-1]
            if ultimoChar == ")":
                numero = numero[:len(numero)-1]
                if numero.isnumeric():
                    variables.append(nombre)
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
        
    else:
        return 0

def checkEq(listaPalabras):
    if len(listaPalabras) == 3:
        nombre = listaPalabras[1]
        numero = listaPalabras[2]
        if nombre in variables:
            ultimoChar = numero[-1]
            if ultimoChar == ")":
                numero = numero[:len(numero)-1]
                if numero.isnumeric():
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkMove(listaPalabras):
    if len(listaPalabras) == 2:
        numero = listaPalabras[1]
        ultimoChar = numero[-1]
        if ultimoChar == ")":
            numero = numero[:len(numero)-1]
            if numero.isnumeric():
                return 1
            elif numero in variables:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkTurn(listaPalabras):
    if len(listaPalabras) == 2:
        direccion = listaPalabras[1]
        ultimoChar = direccion[-1]
        if ultimoChar == ")":
            direccion = direccion[:len(direccion)-1]
            if direccion == ":left" or direccion == ":right" or direccion == ":around":
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkFace(listaPalabras):
    if len(listaPalabras) == 2:
        orientacion = listaPalabras[1]
        ultimoChar = orientacion[-1]
        if ultimoChar == ")":
            orientacion = orientacion[:len(orientacion)-1]
            if orientacion == ":north" or orientacion == ":south" or orientacion == ":east" or orientacion == ":west":
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkPut(listaPalabras):
    if len(listaPalabras) == 3:
        objeto = listaPalabras[1]
        if objeto == "Balloons" or objeto == "Chips":
            numero = listaPalabras[2]
            ultimoChar = numero[-1]
            if ultimoChar == ")":
                numero = numero[:len(numero)-1]
                if numero.isnumeric():
                    return 1
                elif numero in variables:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkPick(listaPalabras):
    if len(listaPalabras) == 3:
        objeto = listaPalabras[1]
        if objeto == "Balloons" or objeto == "Chips":
            numero = listaPalabras[2]
            ultimoChar = numero[-1]
            if ultimoChar == ")":
                numero = numero[:len(numero)-1]
                if numero.isnumeric():
                    return 1
                elif numero in variables:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkMoveDir(listaPalabras):
    if len(listaPalabras) == 3:
        numero = listaPalabras[1]
        if numero in variables or numero.isnumeric():
            direccion = listaPalabras[2]
            ultimoChar = direccion[-1]
            if ultimoChar == ")":
                direccion = direccion[:len(direccion)-1]
                if direccion == ":front" or direccion == ":right" or direccion == ":left" or direccion == ":back":
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

def checkRunDirs(listaPalabras):
    longitudLista = len(listaPalabras)

def checkMoveFace(listaPalabras):
    if len(listaPalabras) == 3:
        numero = listaPalabras[1]
        if numero.isnumeric() or numero in variables:
            orientacion = listaPalabras[2]
            ultimoChar = orientacion[-1]
            if ultimoChar == ")":
                orientacion = orientacion[:len(orientacion)-1]
                if orientacion == ":north" or orientacion == ":south" or orientacion == ":west" or orientacion == ":east":
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0



main(archivo)
