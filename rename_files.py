import os
import glob

# Definisci il percorso della cartella
percorso_cartella = "C:\\Users\\Andrea\\Desktop\\F302G23 executed"

# Ottieni una lista di tutti i file nella cartella
files = glob.glob(os.path.join(percorso_cartella, "*"))

# Stampa il nome di ogni file nella cartella
for file in files:
    if "G95" in file:
        new_name = file.replace("95","23")
        os.rename(os.path.join(percorso_cartella, file), new_name)

print("Il file è stato rinominato con successo.")