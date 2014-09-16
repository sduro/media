############################################
# Programa que usa el fichero config.cfg
# para configurar los directorios de multimedia
# Created: 15/09/2014 - sduro
# Last Modified: 
############################################

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

config = ConfigParser()
config.read("config/config.cfg")

# Cantidad de secciones
sections = config.sections() 
print("%d secciones:" % len(sections))

# Imprimimos cada una de ellas
for section in sections:
    print(section)
    
# Leemos la cantidad de temas
themes_count = config.getint("general", "temas")
print(themes_count, type(themes_count))

for section in config.sections():
    print("\n[%s]" % section)
    for item in config.items(section):
        print(item[0], ":", item[1])

# Modificamos el tema principal
config.set("general", "temas", themes_count + 1)

# Agregamos un nuevo tema (sección)
#config.add_section("TEMA3")
config.set("videos", "nom", "listado pelis")

# Removemos el ítem "votos" de la sección "TEMA2"
#config.remove_option("TEMA2", "votos")
# Guardamos los cambios
with open("config.cfg", "w") as f:
   config.write(f)
