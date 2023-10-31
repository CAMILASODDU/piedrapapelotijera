import time
from time import sleep
import random 

op = ["piedra", "papel", "tijera"]
sep = "-" * 15

while True: 
    user = input ("Elije: piedra, papel o tijera: ").lower()
    sleep(0.9)
    if user not in op:
        print ("\nMovimiento no válido")
        continue
    pc = random.choice(op)
    sleep(0.9)
    print(f"\nLa  PC ha seleccionado {pc}")
    sleep(0.9)
    if user == pc:
        print (f"\nEmpate, ambos eligieron {user}")
    elif user == "piedra" and pc == "tijera":
        print(f"\nGanaste!, {user} ganas en contra de {pc}")
    elif user == "tijera" and pc == "papel":
        print(f"\nGanaste!, {user} ganas en contra de {pc}")
    elif user == "papel" and pc == "piedra":
        print (f"Ganaste!, {user} ganas en contra de {pc}")
else:
    print (f"\nPerdiste, {user} pierde contra {pc} ")
sleep(0.9)
print (f"{sep}Fin del juego{sep}")