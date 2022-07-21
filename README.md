
<h1>Mimap - Mrx04programmer </h1>
<div align="center">
<img src="https://media2.giphy.com/media/Pgnjjt9wKMpbKycPVn/giphy.gif?cid=ecf05e47fwwe5nxir7x0pvaj7ki3o5v6ehzfsesn8cvbn8c0&rid=giphy.gif&ct=s" width="200px">
<div>
<h3>Indice:</h3>
<a href="https://github.com/mrx04programmer/mimap#modules">Modulos disponibles</a><br>
<a href="https://github.com/mrx04programmer/mimap#pre">Pre-Requisitos</a><br>
<a href="https://github.com/mrx04programmer/mimap#ejecuci%C3%B3n">Ejecución</a>
</div>
</div>


Es una herramienta dedicada al escaneo de dispositivos, tanto sus vulnerabilidades como detalles importantes, automatizando comandos de nmap según su función.
<h2 id="modules">Sus modulos disponibles son:</h2>

* Spoofing: Genera señuelos al realizar un escaner (IP Falsa)
* Os Detector: Detecta y muestra los detalles del Sistema operativo encontrado.
* Normal Scan: Escaneo común para los dispositivos sin llamar la atención.
* Intensive Scan: Modulo muy ruidoso respecto al trafico, sin embargo logra obtener resultados más acertados
* Http (Beta no disponible): Obtiene trafico http de una ip especifica.
* CVE Search (Beta no disponible):
<h2 id="pre">Pre-Requisitos:</h2>

| Nombre del Servicio | Instalación |
| ------------------- | ----------- |
|  Nmap | ![apt install nmap](https://www.nmap.org)|
| python2.7 | ![apt install python](https://www.python.org)|

<h2 id="execute">Ejecución:</h2>

* Pedir ayuda de parametros:
> python mimap.py -h
* Obtener la información básica del localhost como prueba:
> python mimap.py -m scan -i 127.0.0.1
* Listar los modulos disponibles: (LIST puede ser cualquier argumento)
> python mimap.py -l LIST


<br>
<a href="#"><img src="https://img.shields.io/badge/OS%20probado-Linux-b?style=plastic&logo=linux&color=yellow&logoColor=yellow"></a>
<a href="#"><img src="https://img.shields.io/github/license/mrx04programmer/mimap?color=y&label=License&logo=gitea&style=plastic"></a>

