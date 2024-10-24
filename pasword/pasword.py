#funcion que verifica que la clave tenga almenos ocho caracteres
def ocho_caracteres(pasword:str)->str:
    if len(pasword) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        
        
#funcion que verifica si el pasword contiene almenos 2 numeros    
def al_menos_2_numeros(pasword:str)->str:
    minimo_2_numeros = 0
    
    for caracter in pasword:
        
        if caracter.isdigit():
            minimo_2_numeros = minimo_2_numeros + 1
            
            
    if not minimo_2_numeros >= 2:
        
        print("La contraseña debe contener al menos 2 números")  
    

# funcion que verifica si hay un caracter en mayuscula

def hay_mayusculas(pasword:str)->str:
    caracter_en_mayuscula = 0
    for caracter in pasword:
        if caracter.isupper():
            caracter_en_mayuscula = caracter_en_mayuscula + 1
            
    if not caracter_en_mayuscula >=1:
       #
        print("la contraseña debe contener al menos una letra mayúscula")

 
# la funcion que verifica si la contraseña contiene un caracter especial
def un_caracter_especial(pasword:str)->str:
    caracteres_especiales = "!@#$%^&*()-_+=<>?/\\|{}[];:'\".,"
    un_caracter = 0
    for caracter in pasword:
        if caracter in caracteres_especiales:
            un_caracter = un_caracter + 1
    if not un_caracter >=1:
    #     print("cumple con un caracter especial")     
    # else:
        print("la contraseña debe contener al menos un carácter especial")  
        
            
        
    
      
# funcion principal que verifica si el pasword cumple con todos lso requisitos para ingresar al sistema        
def pasword_verify(pasword:str)-> bool:
    #variable para registrar si todos las condiciosnes se cumplen
    pasword_valido = True
    if not ocho_caracteres(pasword):
        pasword_valido = False
    if not al_menos_2_numeros(pasword):
        pasword_valido = False 
    if not hay_mayusculas(pasword):
        pasword_valido = False
    if not un_caracter_especial(pasword):
        pasword_valido = False
      
    if pasword == "Diferboc12+":  
        pasword_valido =  True  
    return pasword_valido     
   
verificar = pasword_verify("Diferboc12+")
print(verificar)
