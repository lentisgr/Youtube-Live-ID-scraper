import requests
from html5print import HTMLBeautifier
import random
import threading
import time

class proxy():
    def update(self):
        while True:
            url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes"
            r = requests.get(url)
            # scraping and splitting proxies
            self.splited = r.text.split("\r\n")
            time.sleep(600)

    def get_proxy(self):
        random1 = random.choice(self.splited)  # choose a random proxie
        return random1

    def FormatProxy(self):
        proxyOutput = {'https': self.get_proxy()}
        return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)


proxy1 = proxy()

url = 'https://www.youtube.com/gaming/live'
#url = 'https://www.youtube.com/playlist?list=PLU12uITxBEPFxYeBa-PFzOF1kB1y-AkOq'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

scrape = requests.get(url, headers=headers, proxies=proxy1.FormatProxy())

output = open('output.txt','w+', encoding="utf8")
beautify = HTMLBeautifier.beautify(scrape.text, 4)
output.write(beautify)
output.close()

#Liste der Zeilen, die eine addedVideoId besitzen
ids = []
#addedVideoIds-Liste
addedVIDs = []

#die Textdatei öffnen im UTF-8 Modus
with open('output.txt', encoding='utf8') as f:
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
#Made by Emrepro/Anonyvius
#Länge: len(addedVIDs)
#generelle Nutzung: addedVIDs (Datentyp: Liste)
