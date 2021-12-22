import os
import time

os.system("color a")
print("!Bienvenido a su asistente de  firebase")
print("Recuerde que nesecita node.js instaalado")
time.sleep(1.5)
print("")
def update():
    print("elija nuestras opciones:")
    print("1-Instalar firebase")
    print("2-Login firebase")
    print("3-subir archivos a firebase")
    print("4-Actualizar archivos en firebase")
    answer = int(input())
    if answer == 1:
        print("[+] Ejecutando código")
        print("[+] Espere...")
        time.sleep(1)
        os.system("npm install -g firebase-tools")
        print("")
        print("[+] EL código y la función fueron ejecutados con éxito")
        time.sleep(1)
        print("¿Quieres ir al menu?  y/n")
        reintento = str(input())
        if reintento == "y":
            update()
        if reintento == "n":
            print("Hasta pronto")
            time.sleep(1)
    if answer == 2:
        print("[+] Ejecutando código")
        print("[+] Espere...")
        time.sleep(1)
        os.system("firebase login")
        print("")
        print("[+] EL código y la función fueron ejecutados con éxito")
        time.sleep(1)
        print("¿Quieres ir al menu?  y/n")
        reintento = str(input())
        if reintento == "y":
            update()
        if reintento == "n":
            print("Hasta pronto")
            time.sleep(1)
    if answer == 3:
        print("[+] Ejecutando código")
        print("[+] Espere...")
        time.sleep(1)
        os.system("firebase init")
        os.system("firebase deploy")
        print("")
        print("[+] EL código y la función fueron ejecutados con éxito")
        time.sleep(1)
        print("¿Quieres ir al menu?  y/n")
        reintento = str(input())
        if reintento == "y":
            update()
        if reintento == "n":
            print("Hasta pronto")
            time.sleep(1)
    if answer == 4:
        print("[+] Ejecutando código")
        print("[+] Espere...")
        time.sleep(1)
        print("")
        os.system("cd C:\\Users\\Usuario\\github\\MyPortafolio")
        os.system("firebase deploy --only hosting")
        #os.system("")
        print("")
        print("[+] EL código y la función fueron ejecutados con éxito")
        print("¿Quieres ir al menu?  y/n")
        reintento = str(input())
        if reintento == "y":
            update()
        if reintento == "n":
            print("Hasta pronto")
            time.sleep(1)
update()
