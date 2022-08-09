import random
import string

from palabras import palabras
from diagramaVidas import vidasDiccionarioVisual


def obtenerPalabraValida(listaDePalabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(listaDePalabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(listaDePalabras)

    return palabra.upper()



def ahorcado():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Bienvenido al Ahorcado! ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    palabra = obtenerPalabraValida(palabras)

    letrasPorAdivinar = set(palabra)
    letrasAdivinadas =  set()
    abecedario = set(string.ascii_uppercase) # No trae la ñ

    vidas = 7

    while len(letrasPorAdivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")

        # Mostrar el estado actual de la palabra.
        palabraLista = [letra if letra in letrasAdivinadas
        else "-" for letra in palabra]

        # Mostrar estado actual del ahorcado.
        print(vidasDiccionarioVisual[vidas])
 
        # Mostrar las letras separadas por un espacio.
        print(f"Palabra: {' '.join(palabraLista)}")

        letraUsuario = input("Ingrese una letra: ").upper()

        # Si la letra escogida por el usuario está en el
        # abecedario y no está en el conjunto de las letras
        # que se han ingresado, se añade la letra al conjunto de
        # letras ingresadas.
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            # Si la letra está en la palabra, se elimina del conjunto 
            # de letras por adivinar. Del contrario, se elimina una vida
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print("")
            else:
                vidas -= 1
                print(f"\nTu letra, '{letraUsuario}' no está en la palabra")
        
        #Si la letra escogida por el usuario ya fue ingresada
        elif letraUsuario in letrasAdivinadas:
            print("\nYa escogiste ésta letra. Por favor ingresa otra")
        else:
            print("\nEsta letra no es válida")
    
    # Cuando se adivinan todas las letras de la palabra o se agotaron las vidas

    if vidas == 0:
        print(vidasDiccionarioVisual[vidas])
        print("Ahorcado!, perdiste :(")
        print(f"La palabra era: {palabra}")
    else:
        print(f"Bien!, adivinaste la palabra '{palabra}'")


ahorcado()

    