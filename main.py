from os import linesep
import sqlite3

def read_local_files():
    fitxer=[]
    with open('/home/sduro/Documentos/llista.txt') as f:
        for line in f:
            fitxer.append(line[0:-1])
            #print (line[0:-1])
    f.close
    return fitxer

def read_kodi_database():
    conn = sqlite3.connect('MyVideos116.db')
    print ('Database opened successfully...')
    pelicula_llista=[]
    cursor = conn.execute("select * from movie")

    for row in cursor:
        #print (row[2]," | ", row[28][0:4]," | ", row[24])
        pelicula=(row[24].split("/"))
        pelicula_llista.append(pelicula[5])
        #print (pelicula[5])
    fitxer=read_local_files()
    print(set(pelicula_llista) & set(fitxer))
    print ("Done")
    conn.close()

read_kodi_database()


