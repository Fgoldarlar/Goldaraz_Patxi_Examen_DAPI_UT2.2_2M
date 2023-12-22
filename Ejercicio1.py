def LeerDocumento(LibroCuentas):
    """Esta función leerá la información de un fiichero y la guardará en una
    variable del tipo lista
    Parametros:
     - Fichero a leer (LibroCuentas.txt)
    Salida:
    - Devuelve una lista con los datos del fichero
    """

    with open("LibroCuentas.txt","r") as file:
        osasuna = file.readlines()
    return osasuna




def IdentificarPagado(lista):
    """Esta función creará un fichero llamado "pagado.txt" donde se 
    escribiran todas las lineas donde en la lista de entrada aparezca la
    palabra "PAGADO"
    Parametros:
        - Recibe una lista
    Salida:
        - Esta función no devuelve nada
    """
    import os
    if os.path.isfile("lista.txt"):
        with  open ("Lista.txt","w") as file:
            indargorri = file.readlines()
            if indargorri == "PAGADO":
                file.write(indargorri)
            else:
                print("Nadie ha pagado nada!!")


            



    