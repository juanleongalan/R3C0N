👋 Bienvenid@!

Este es un script creado en Python para la recolección de información y el escaneo de vulnerabilidades web.

🔧 Herramientas utilizadas

Las herramientas utilizadas vienen incluidas en la distribución oficial de Kali Linux.

🔧 Requisitos previos

Antes de comenzar, asegúrese de que su Kali Linux esté actualizado a la última versión ejecutando:

sudo apt update && sudo apt upgrade -y

📚 Instalación y uso

Descargue el archivo final_recon_v1.py.

Conceda permisos de ejecución:

sudo chmod +x final_recon_v1.py

Abra una terminal en el directorio donde se encuentra el archivo y ejecútelo:

./final_recon_v1.py

Ingrese el nombre de dominio cuando se le solicite.

Se mostrará un menú con diferentes herramientas de escaneo:

Puede seleccionar una por una o ejecutar todas las herramientas en secuencia.

Cada escaneo individual generará un archivo .txt con los resultados.

Si elige el escaneo completo, se creará un archivo informe_de_recoleccion.html con un resumen detallado.

📊 Herramientas utilizadas

Este script emplea las siguientes herramientas de Kali Linux para la recolección de información:

Whois - Obtiene información de registro de dominios (propietario, DNS, fechas de expiración, etc.).

Curl - Cliente de línea de comandos para transferir datos mediante HTTP, HTTPS, FTP y otros protocolos.

WhatWeb - Escáner que identifica tecnologías web usadas en un sitio (CMS, frameworks, servidores, etc.).

TheHarvester - Recolecta correos, nombres de usuario, subdominios y más desde fuentes públicas (Google, Bing, Shodan, etc.).

Subfinder - Enumerador pasivo de subdominios que recopila información de diversas fuentes.

Amass - Plataforma avanzada de reconocimiento para mapear redes y descubrir subdominios con OSINT.

SSLScan - Escanea servidores SSL/TLS para detectar configuraciones inseguras y certificados caducados.

Nuclei - Herramienta para escanear vulnerabilidades en servidores y aplicaciones web mediante plantillas YAML.

Nmap - Potente escáner de red para identificar hosts, servicios y sistemas operativos.

WAFW00F - Detecta si un sitio está protegido por un firewall de aplicaciones web (WAF) y su tipo.

🌟 Contribuciones

Si deseas mejorar este script o agregar nuevas funcionalidades, siéntete libre de hacer un pull request o reportar problemas en la sección de Issues.


🚀 Hack the Planet!
