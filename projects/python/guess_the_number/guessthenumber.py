import random

# Genera un número aleatorio entre 1 y 20
numero_aleatorio = random.randint(1, 20)

print("Bienvenido al juego de adivinar el número.")
print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

# Itera 5 veces para dar al usuario 5 oportunidades de adivinar
for intento in range(1, 6):
    # Pide al usuario que introduzca un número
    numero_usuario = int(input(f"Intento {intento}: Adivina el número: "))

    # Compara el número del usuario con el número aleatorio
    if numero_usuario == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en el intento {intento}!")
        break
    elif numero_usuario < numero_aleatorio:
        print("El número que buscas es más grande.")
    else:
        print("El número que buscas es más pequeño.")

# Si el usuario no ha adivinado el número en 5 intentos, muestra el número correcto
if numero_usuario != numero_aleatorio:
    print(f"Lo siento, no has adivinado el número en 5 intentos. El número correcto era {numero_aleatorio}. ¡Inténtalo de nuevo!")
