# Mimap - Mrx04programmer
<img src="https://media2.giphy.com/media/Pgnjjt9wKMpbKycPVn/giphy.gif?cid=ecf05e47fwwe5nxir7x0pvaj7ki3o5v6ehzfsesn8cvbn8c0&rid=giphy.gif&ct=s" width="300px">
### Es una herramienta dedicada al escaneo de dispositivos, tanto sus vulnerabilidades como detalles importantes, automatizando comandos de nmap según su función.
## Sus modulos disponibles son:
	* Spoofing: Genera señuelos al realizar un escaner (IP Falsa)
	* Os Detector: Detecta y muestra los detalles del Sistema operativo encontrado.
	* Normal Scan: Escaneo común para los dispositivos sin llamar la atención.
	* Intensive Scan: Modulo muy ruidoso respecto al trafico, sin embargo logra obtener resultados más acertados
	* Http (Beta no disponible): Obtiene trafico http de una ip especifica.
	* CVE Search (Beta no disponible): 
## Pre-Requisitos:
| Nombre del Servicio | Instalación |
| ------------------- | ----------- |
|  Nmap | ![apt install nmap](https://www.nmap.org)|
| python2.7 | ![apt install python](https://www.python.org)|

## Ejecución:
* Pedir ayuda de parametros:
> python mimap.py -h
* Obtener la información básica del localhost como prueba:
> python mimap.py -m scan -i 127.0.0.1 
* Listar los modulos disponibles: (LIST puede ser cualquier argumento)
> python mimap.py -l LIST


<br>
<a href="#"><img src="https://img.shields.io/badge/OS%20probado-Linux-b?style=plastic&logo=linux&color=yellow&logoColor=yellow"></a>
