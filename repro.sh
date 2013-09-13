#Busca y reproduce ficheros multimedia en formato lista

#directorio raiz
lista=$(ls -R /home/pi/usb/torrent/completed |egrep '..avi|..mpg')

#una vez selecionado el fichero fuerza la salida por HDMI
slc='Elige fichero:'
select file in $lista
do
if [ $file ]; then
        omxplayer -o hmdi $file
        break
else
        echo "operacion no valida"
fi
done

