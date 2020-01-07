import requests
from html5print import HTMLBeautifier

suchbegriff = input('Nach welchem Suchbegriff möchten sie auf Youtube live suchen?\n').lower()

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

videoId = []

with open('output.txt', 'r', encoding="utf8") as f:
    data = f.readlines()
    for ids in data:
        if '"addedVideoId": "' in ids:
            videoId.append(ids)

###FINAL###

print(f'\nDie {suchbegriff} ID`s lauten: \n')
print(''.join(videoId).replace(' ', '').replace('"addedVideoId":"', '').replace('"', '').replace(',', ''))
print(f'\nEs sind insgesamt {len(videoId)} {suchbegriff} Livestreams auf Youtube live.')
