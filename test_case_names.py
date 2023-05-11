import os
import glob
import pandas as pd


# Definisci il percorso della cartella
percorso_cartella = "C:\\Users\\Andrea\\Desktop\\F302G23 executed"
name_ignore = ['RESULT','MACRO','FIGURE','CONFIGURATION','AD_IELIB','OPTIONS']
# Ottieni una lista di tutti i file nella cartella
files = glob.glob(os.path.join(percorso_cartella, "*"))
list_names = []
# Stampa il nome di ogni file nella cartella
for file in files:
    if not "output" in file:
        excel_sheetNames = pd.ExcelFile(os.path.join(percorso_cartella,file)).sheet_names 
        for exc_name in excel_sheetNames:
            if exc_name.upper() not in name_ignore:
                list_names.append(exc_name)

f = open("C:\\Users\\Andrea\\Desktop\\F302G23 executed\\sheet_names.txt", "w")
i = 0
for l in list_names:
    f.writelines(l.removeprefix("TC_")+"\n")
    i = i+1

print("Total number of tests: ", i)






