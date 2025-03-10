#!/usr/bin/env python3

import os
import sys
import subprocess
import time
import signal
import re
import socket

# Variables de control
proceso_actual = None  

# 🛑 Manejo de Ctrl + C y Ctrl + D
def handler(sig, frame):
    global proceso_actual
    print("\n\033[33m[⚠] ¿Desea salir del script? (y/n): \033[0m", end="", flush=True)
    
    try:
        choice = input().strip().lower()
    except EOFError:
        choice = 'n'
    
    if choice == 'y':
        if proceso_actual:
            proceso_actual.terminate()
        print("\033[31m[❌] Saliendo del script...\033[0m")
        sys.exit(0)
    else:
        print("\033[32m[✅] Continuando...\033[0m")

signal.signal(signal.SIGINT, handler)

# 🎨 Banner ASCII (NO MODIFICADO)
def mostrar_banner():
    banner = """
\033[31m██████  ██████  ██████  ██████  ███     ██
██   ██     ██  ██     ██    ██ ████    ██ 
██████  ██████  ██     ██    ██ ██ ██   ██
██   ██     ██  ██     ██    ██ ██   ██ ██ 
██   ██ ██████  ██████  ██████  ██     ███\033[0m
"""
    herramientas_info = """
\033[34m[🔍] Herramientas utilizadas en este script:
1 - Whois
2 - Curl
3 - WhatWeb
4 - TheHarvester
5 - Subfinder
6 - Amass
7 - SSLScan
8 - Nuclei
9 - Nmap
10 - WAFW00F
11 - Todas las herramientas
0 - Salir\033[0m
"""
    print(banner)
    print("\033[34m[🔍] Script de Auditoría Web - R3CON-ME v1.0\033[0m")
    print("\033[34m[📌] Creado por: DosZeroDayz\033[0m")
    print(herramientas_info)

mostrar_banner()

# 🖥️ Pedir URL al usuario
while True:
    try:
        DOMINIO_INPUT = input("\033[32m[+] Ingrese el dominio a escanear: \033[0m").strip()
        if DOMINIO_INPUT:
            break
        else:
            print("\033[33m[⚠] No puede dejar el dominio en blanco.\033[0m")
    except (KeyboardInterrupt, EOFError):
        print("\n\033[31m[❌] Interrupción detectada. Saliendo...\033[0m")
        sys.exit(0)

# 🔍 Normalizar dominio
def limpiar_dominio(dominio):
    dominio = re.sub(r"https?://(www\.)?", "", dominio)  
    dominio = dominio.split("/")[0]  
    return dominio

DOMINIO = limpiar_dominio(DOMINIO_INPUT)

# 🔎 Obtener la IP del dominio
def obtener_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"\033[36m[🌐] La IP de {dominio} es: {ip}\033[0m")
        return ip
    except socket.gaierror:
        print("\033[31m[❌] No se pudo obtener la IP del dominio.\033[0m")
        return None

IP_DOMINIO = obtener_ip(DOMINIO)

# 📂 Configuración de directorios
CARPETA = f"recon/{DOMINIO}"
os.makedirs(CARPETA, exist_ok=True)

# 🚀 Ejecutar herramientas individualmente o todas
def ejecutar_comando(comando, archivo_salida, herramienta):
    global proceso_actual

    print(f"\n\033[34m[+] Ejecutando {herramienta}...\033[0m")
    
    inicio = time.time()
    with open(archivo_salida, "w") as f:
        proceso_actual = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        for linea in proceso_actual.stdout:
            print(linea, end="")  
            f.write(linea)

    proceso_actual.wait()
    tiempo = round(time.time() - inicio, 2)

    print(f"\n\033[32m[✅] {herramienta} completado en {tiempo} segundos\033[0m")

# 📄 Generar informe HTML después de ejecutar todas las herramientas
def generar_informe():
    informe_html = f"{CARPETA}/informe_de_recoleccion.html"
    
    with open(informe_html, "w") as f:
        f.write(f"""<html><head><title>Informe de Recolección - {DOMINIO}</title>
        <style>
        body {{ font-family: Arial, sans-serif; background-color: #f8f9fa; padding: 20px; }}
        h1 {{ color: #ff4500; border-bottom: 2px solid #ff4500; padding-bottom: 5px; }}
        h2 {{ color: #0078D7; }}
        pre {{ background: #2e2e2e; color: #ffffff; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        </style></head><body>
        <h1>Informe de Recolección - {DOMINIO}</h1>
        <p><strong>IP del dominio:</strong> {IP_DOMINIO if IP_DOMINIO else 'No disponible'}</p>""")

        for key, value in herramientas.items():
            herramienta, archivo = value[0], f"{CARPETA}/{value[0]}.txt"
            f.write(f"<h2>{herramienta}</h2>")
            if os.path.exists(archivo):
                with open(archivo, "r") as resultado:
                    f.write(f"<pre>{resultado.read()}</pre>")
            else:
                f.write("<p>No hay resultados disponibles.</p>")

        f.write("</body></html>")

    print(f"\033[32m[✅] Informe generado: {informe_html}\033[0m")

# 🛠️ Herramientas disponibles
herramientas = {
    "1": ("Whois", f"whois {DOMINIO}"),
    "2": ("Curl", f"curl -I -s https://{DOMINIO}"),
    "3": ("WhatWeb", f"whatweb {DOMINIO}"),
    "4": ("TheHarvester", f"theHarvester -d {DOMINIO} -b all"),
    "5": ("Subfinder", f"subfinder -d {DOMINIO}"),
    "6": ("Amass", f"amass enum -d {DOMINIO}"),
    "7": ("SSLScan", f"sslscan --no-failed {DOMINIO}"),
    "8": ("Nuclei", f"nuclei -u https://{DOMINIO} -o {CARPETA}/nuclei.txt"),
    "9": ("Nmap", f"nmap -sV -O --top-ports 1000 --script vuln -v -Pn -n {IP_DOMINIO}"),
    "10": ("WAFW00F", f"wafw00f -a -v {DOMINIO}")
}

# 📌 Menú interactivo después de ingresar la URL
while True:
    try:
        print("\n\033[34m[🔍] Seleccione una opción:\033[0m")
        for key, value in herramientas.items():
            print(f"\033[32m[{key}] {value[0]}\033[0m")
        print("\033[32m[11] Todas las herramientas\033[0m")
        print("\033[31m[0] Salir\033[0m")

        opcion = input("\033[33m[⚡] Opción: \033[0m").strip()

        if opcion == "0":
            print("\033[31m[❌] Saliendo...\033[0m")
            sys.exit(0)

        elif opcion in herramientas:
            herramienta, comando = herramientas[opcion]
            ejecutar_comando(comando, f"{CARPETA}/{herramienta}.txt", herramienta)

        elif opcion == "11":
            for key, value in herramientas.items():
                ejecutar_comando(value[1], f"{CARPETA}/{value[0]}.txt", value[0])
            generar_informe()

    except KeyboardInterrupt:
        handler(None, None)
