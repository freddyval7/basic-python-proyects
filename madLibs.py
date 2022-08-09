# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ___________.

""" organizacion = "JuanGAY C.A"

print("Aprende a programar con " + organizacion)
print(f"Aprende a programar con {organizacion}") # f-string """

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivoPlural = input("Sustantivo plural: ")

madlib = f"Programar es tan {adj}, Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con el Campamento de Código 'El Junquito' y alcanza tus {sustantivoPlural}"

print(madlib)