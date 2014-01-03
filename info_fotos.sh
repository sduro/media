#!/bin/bash

#Muestra la distancia focal de los ficheros imagenes.
#Hay que tener instalado el repositorio exif

filelist=$(find . -type f | grep -i '\.jpg$\|\.jpeg$\|\.JPG$\')

echo Distancia Focal
echo ----------------------

for file in $filelist; do
	distancia=$(exif $file |grep 'Distancia focal')
	echo $file $distancia
done

