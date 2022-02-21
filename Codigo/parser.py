from sympy import prime
import config as cf

archivo = open(cf.data_dir + 'pruebaLinea.txt',encoding="utf-8" )

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
                    variables += [nombre]
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
        
    else:
        return 0

reservadas = ["defvar","=","move","turn","face","put","pick","move-dir","run-dirs","move-face","(skip)",
               "(defvar","(=","(move","(turn","(face","(put","(pick","(move-dir","(run-dirs","(move-face"]

variables = []

funciones = []

parentesis = {"(": 0 , ")": 0 }

main(archivo)
