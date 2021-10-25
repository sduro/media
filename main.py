import sqlite3

conn = sqlite3.connect('MyVideos116.db')
print ('Database opened successfully...')

cursor = conn.execute("select * from movie")
for row in cursor:
    print ("Title: ", row[2],"Year: ", row[28][0:4])

print ("Done")
conn.close()

   
#conn.commit()

