import requests
from html5print import HTMLBeautifier

suchbegriff = input('Nach welchem Suchbegriff möchten sie auf Youtube live Gaming suchen?\n').lower()

#url = 'https://www.youtube.com/gaming/live'
url = 'http://www.youtube.com/results?search_query='+suchbegriff+'&sp=EgJAAQ%253D%253D'
print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

scrape = requests.get(url, headers=headers, timeout=999)

output = open('output.txt', 'w+', encoding="utf8")
beautify = HTMLBeautifier.beautify(scrape.text, 4)
output.write(beautify)
output.close()

ids = []
labels = []
addedVIDs = []
addedLabels = []

# die Textdatei öffnen im UTF-8 Modus
with open('output.txt', encoding="utf8") as f:
    # Alle Zeilen lesen
    lines = f.readlines()
    # Durch jede Zeile loopen
    for line in lines:
        # Wenn String gefunden in einer Zeile dann..
        if 'label' in line:
            # füge diese Zeile zur ids-Liste
            labels.append(line)
    for videoId in lines:
        # Wenn String gefunden in einer Zeile dann..
        if 'addedVideoId' in videoId:
            # füge diese Zeile zur ids-Liste
            ids.append(videoId)


def labFind():
    for lab in labels:
        # Split nach dem String
        einzelID = lab.split('label')
        # Die Seite nach dem Split nutzen
        value = einzelID[1]
        # 4-Mal im String weiter gehen
        for i in range(3):
            value = value.replace(einzelID[1][i], ' ')

        # Split um " zu entfernen
        firstSplit = value.split('"')
        # Split um , zu entfernen
        secondSplit = firstSplit[0]
        # zur addedVideoIds-Liste hinzufügen
        if 'vor' in secondSplit:
            addedLabels.append(secondSplit)


def idFind():
    for id in ids:
        # Split nach dem String
        einzelID = id.split('addedVideoId')
        # Die Seite nach dem Split nutzen
        value = einzelID[1]
        # 4-Mal im String weiter gehen
        for i in range(4):
            value = value.replace(einzelID[1][i], '')

        # Split um " zu entfernen
        firstSplit = value.split('"')
        # Split um , zu entfernen
        secondSplit = firstSplit[0].split(',')
        # zur addedVideoIds-Liste hinzufügen
        addedVIDs.append(secondSplit[0])


###FINAL###

labFind()
idFind()

endProd = []
for e in range(len(addedVIDs)):
    if suchbegriff in addedLabels[e].lower():
        endProd.append(addedVIDs[e])

print('\nDie ', suchbegriff, ' ID`s lauten: \n')
for formatierung in endProd:
    print(formatierung)
print('\nEs sind insgesamt %i %s Livestreams auf Youtube live.' % (len(endProd), suchbegriff))
