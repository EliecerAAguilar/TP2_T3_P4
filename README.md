# Topicos Especiales 2
## Tarea #03

<div id="badges">
    <a href="https://www.linkedin.com/in/eliecer-aguilar-507/">
      <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
    </a>
    <a href="https://twitter.com/elieceraguilar3">
      <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
    </a>
</div>

<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>


## Problema	4.	Conexión	de	PostGis	a	Geopandas.
Escriba	un	script	en	Python	llamado	reportageo.py, que	realice	las	siguientes	funciones:  
1. Utilizando	el	conector	psycog2 conéctese	a	la	base	de	datos	de	PostgreSQL	recientemente	creada (puede	ser	
una	conexión	local	o	a	la	nube	de	Heroku).

2. Escriba	un	query	(por	ejemplo, select	*	from	Pan_provincia)	y	baje	su	resultado	a	un	dataframe	utilizando	el	
siguiente	formato:

***
df	=	geopandas.GeoDataFrame.from_postgis(sql,	conn,	geom_col='geom'	)   
***
3. Grafique	el	contenido	del	geoDataFrame.	Haga	una	captura	de	pantalla	del	query	y	de	la	respuesta	
obtenida.

***
<a href="https://academy.vertabelo.com/course/postgis/geography/geometry-vs-geography/casting-geometry-togeography" target="_blank">https://academy.vertabelo.com/course/postgis/geography/geometry-vs-geography/casting-geometry-togeography </a>
***