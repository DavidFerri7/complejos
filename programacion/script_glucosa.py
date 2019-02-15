import sys
if len(sys.argv = 4):
    Glucosa_plasma = sys.argv[1]
    if Glucosa_plasma <= 72:
        print("Bajo")
    elif 72 < Glucosa_plasma <= 110:
        print("Normal")
    elif Glucosa_plasma > 110:
        print("Alto")
 
    Glucosa_sangre = sys.argv[2]
    if Glucosa_sangre <= 60:
        print("Bajo")
    
    elif 60 < Glucosa_sangre <=100:
        print("Normal")
    
    elif Glucosa_sangre > 100:
        print("Alto")
 
    Glucosa_aleatoria = int(sys.argv[3])
    if Glucosa_aleatoria <= 70:
        print("Bajo")
    
    elif 70 < Glucosa_aleatoria <= 140:
        print("Normal")

    elif Glucosa_aleatoria >= 140:
        print("Alto")
#Comprobar que solo son 3 argumentos y que son int type(variable) is...
