from os import linesep
import sqlite3



def read_local_files():
    with open('/home/sduro/Documentos/llista.txt') as f:
        for line in f:
            print (line[0:-1])
    f.close

def read_kodi_database():
    conn = sqlite3.connect('MyVideos116.db')
    print ('Database opened successfully...')
    c22='642'
    movie = '%Tenet.(2020).mkv'
    cursor = conn.execute("select * from movie where c22 like ?",(movie,))
    for row in cursor:
        print (row[2]," | ", row[28][0:4]," | ", row[24])

    print ("Done")
    conn.close()

#read_local_files()
read_kodi_database()


