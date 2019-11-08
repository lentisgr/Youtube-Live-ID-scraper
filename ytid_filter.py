#Liste der Zeilen, die eine addedVideoId besitzen
ids = []
#addedVideoIds-Liste
addedVIDs = []

#die Textdatei öffnen im UTF-8 Modus
with open('output.txt', encoding="utf8") as f:
    #Alle Zeilen lesen
    lines = f.readlines()
    #Durch jede Zeile loopen
    for line in lines:
        #Wenn String gefunden in einer Zeile dann..
        if 'addedVideoId' in line:
            #füge diese Zeile zur ids-Liste
            ids.append(line)

#durch jede ID-Zeile der ids-Liste loopen
for id in ids:
    #Split nach dem String
    einzelID = id.split('addedVideoId')
    #Die Seite nach dem Split nutzen
    value = einzelID[1]
    #4-Mal im String weiter gehen
    for i in range(4):
        value = value.replace(einzelID[1][i],'')

    #Split um " zu entfernen
    firstSplit = value.split('"')
    #Split um , zu entfernen
    secondSplit = firstSplit[0].split(',')
    #zur addedVideoIds-Liste hinzufügen
    addedVIDs.append(secondSplit[0])



print('Die \"addedVideoId\"\'s lauten:')
#Ergebnis printen
print(addedVIDs)
print('Und es sind insgesamt %i ID\'s!' % len(addedVIDs))

#Länge: len(addedVIDs)
#generelle Nutzung: addedVIDs (Datentyp: Liste)
