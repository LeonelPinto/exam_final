class Proceso:
    def __init__(self, cadena):
        cad_vac= " "
        for letra in cadena:
            cad_vac += letra
            if letra == "#":
                cad_vac = cad_vac + " "
        print(cad_vac)
    
        
prueba=input(f"Ingrese cadena: ")
cadena=str(prueba)
prueba_1=Proceso()

