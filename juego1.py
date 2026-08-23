import random

piedra = 1
papel = 2
tijera = 3
lagarto = 4
spock = 5
si = 1
victoria = "sing"
victorias = "plur"

print("Bienvenido a mi primer proyecto de Python.")

print("Te presento el juego: Piedra - Papel - Tijera - Lagarto - Spock.")



print("✌️ Las Tijeras cortan el Papel 🤚")                  # Explicación normas
print("🤚 El Papel envuelve la Piedra ✊")
print("✊ La Piedra aplasta al Lagarto 🤙")
print("🤙 El Lagarto envenena a Spock 🤟")
print("🤟 Spock rompe las Tijeras ✌️")
print("✌️ Las Tijeras decapitan al Lagarto 🤙")
print(" El Lagarto se come el Papel 🤚")
print("🤚 El Papel refuta a Spock 🤟")
print("✌️ Spock vaporiza la Piedra ✊")
print("✊ La Piedra parte las Tijeras ✌️")

jugador = input("Apodo: ")

print(f"Gracias {jugador}, empezamos. ¡Suerte!")

print("⭐️================================⭐️")
print(" Piedra Papel Tijera Lagarto Spock")
print("⭐️================================⭐️")

correcto = "numero"
eleccion = 5
respuesta = 2
jug = 0
orden = 0

while respuesta != 100:
    
    while correcto != 100:                          # Bucle de Juego
        print("Elige un numero del 1 al 5: ")
        print("1) ✊")
        print("2) 🤚")
        print("3) ✌️")
        print("4) 🤙")
        print("5) ✌️")
        eleccion = int(input(" "))

        if eleccion == 1:           #Jugada del jugador
            correcto = 100
            print("- Tu jugada: ✊")
        elif eleccion == 2:
            correcto = 100
            print("- Tu jugada: 🤚")
        elif eleccion == 3:
            correcto = 100
            print("- Tu jugada: ✌️")
        elif eleccion == 4:
            correcto = 100
            print("- Tu jugada: 🤙")
        elif eleccion == 5:
            correcto = 100
            print("- Tu jugada: 🤟")
        else:
            print("Vuelve a intentarlo")


        ordenador = random.randint(1, 5)

        if ordenador == 1:      #Jugada del ordenador
            print("- Ordenador: ✊")
        elif ordenador == 2:
            print("- Ordenador: 🤚")
        elif ordenador == 3:
            print("- Ordenador: ✌️")
        elif ordenador == 4:
            print("- Ordenador: 🤙")
        elif ordenador == 5:
            print("- Ordenador: 🤟")

        if eleccion == 1 and ordenador == 1:        #Resultado
            print("¡Vaya! Parece que habéis empatado." \
        " Otra vez")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 1 and ordenador == 2:
            orden += 1
            print("¡Vaya! Has perdido, el Papel 🤚 envuelve la Piedra ✊")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 1 and ordenador == 3:
            jug += 1
            print("¡Genial! Has ganado, la Piedra ✊ parte las Tijeras ✌️")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 1 and ordenador == 4:
            jug += 1
            print("¡Genial! Has ganado, la Piedra ✊ aplasta al Lagarto 🤙")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 1 and ordenador== 5:
            orden += 1
            print("¡Vaya! Has perdido, Spock 🤟 vaporiza la Piedra ✊")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 2 and ordenador == 1:
            jug += 1
            print("¡Genial! Has ganado, el Papel 🤚 envuelve la Piedra ✊")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 2 and ordenador == 2:
            print("¡Vaya! Parece que habéis empatado." \
            " Otra vez")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 2 and ordenador == 3:
            orden += 1
            print("¡Vaya! Has perdido, las Tijeras ✌️ cortan el Papel 🤚")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 2 and ordenador == 4:
            orden += 1
            print("¡Vaya! Has perdido, el Lagarto 🤙 se come el Papel 🤚")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 2 and ordenador == 5:
            jug += 1
            print("¡Genial! Has ganado, el Papel 🤚 refuta a Spock 🤟")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")
        elif eleccion == 3 and ordenador == 1:
            orden += 1
            print("¡Vaya! Has perdido, la Piedra ✊ parte las Tijeras ✌️")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 3 and ordenador == 2:
            jug += 1
            print("¡Genial! Has ganado, las Tijeras ✌️ cortan el Papel 🤚")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 3 and ordenador == 3:
            print("¡Vaya! Parece que habéis empatado." \
                " Otra vez")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")
        elif eleccion == 3 and ordenador == 4:
            jug += 1
            print("¡Genial! Has ganado, las Tijeras ✌️ decapitan al Lagarto 🤙")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 3 and ordenador == 5:
            orden += 1
            print("¡Vaya! Has perdido, Spock 🤟 rompe las Tijeras ✌️")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 4 and ordenador == 1:
            orden += 1
            print("¡Vaya! Has perdido, la Piedra ✊aplasta al Lagarto 🤙")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 4 and ordenador == 2:
            jug += 1
            print("¡Genial! Has ganado, el Lagarto  🤙 se come el Papel 🤚")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 4 and ordenador == 3:
            orden += 1
            print("¡Vaya! Has perdido, las Tijeras ✌️ decapitan al Lagarto 🤙")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 4 and ordenador == 4:
            print("¡Vaya! Parece que habéis empatado." \
                " Otra vez")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 4 and ordenador == 5:
            jug += 1
            print("¡Genial! Has ganado, el Lagarto 🤙 envenena a Spock 🤟")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 5 and ordenador == 1:
            jug += 1
            print("¡Genial! Has ganado, Spock 🤟 vaporiza la Piedra ✊")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 5 and ordenador == 2:
            orden += 1
            print("¡Vaya! Has perdido, el Papel 🤚 refuta a Spock 🤟")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 5 and ordenador == 3:
            jug += 1
            print("¡Genial! Has ganado, Spock 🤟 rompe las Tijeras ✌️")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 5 and ordenador == 4:
            orden += 1
            print("¡Vaya! Has perdido, el Lagarto 🤙 envenena a Spock 🤟")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        elif eleccion == 5 and ordenador == 5:
            print("¡Vaya! Parece que habéis empatado." \
                " Otra vez")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")

        repetir = input("¿Quieres jugar otra vez? Escribe [1] para seguir o [2] para acabar: ")

        if repetir == "1":              #Respuesta repetición
            correcto = "numero"

        elif repetir == "2":                   #Resultado final
            correcto = 100
            respuesta = 100
            print("")
            print("📊 M A R C A D O R 📊")
            print("---------------------")
            print(f"- {jugador}: {jug} {'victoria' if jug == 1 else 'victorias'}.")
            print(f"- Ordenador: {orden} {'victoria' if orden == 1 else 'victorias'}.")
            print(f"😁 Gracias por jugar, {jugador} 😁")
            break

    

