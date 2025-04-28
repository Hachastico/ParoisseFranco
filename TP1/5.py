#Funcion que convierte un numero romano en decimal

def romano_decimal(NumRom):

    DicRom = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    
    if len(NumRom) == 0:
        return 0
    elif len(NumRom) == 1:
        return DicRom[NumRom]
    elif DicRom[NumRom[0]] < DicRom[NumRom[1]]:
        return DicRom[NumRom[1]] - DicRom[NumRom[0]] + romano_decimal(NumRom[2:])
    else:
        return DicRom[NumRom[0]] + romano_decimal(NumRom[1:])

NumRom = str(input("Inserte un numero romano para convertir a decimal: "))

print(romano_decimal(NumRom))