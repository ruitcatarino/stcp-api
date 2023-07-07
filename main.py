import json
import requests
import re
from bs4 import BeautifulSoup
from typing import Union
from fastapi import FastAPI

app = FastAPI()

def format_text(raw_text):
    raw_text = re.sub(u"[àáâãäå]", 'a', raw_text)
    raw_text = re.sub(u"[ÀÁÂÃÄÅ]", 'A', raw_text)
    raw_text = re.sub(u"[èéêë]", 'e', raw_text)
    raw_text = re.sub(u"[ÈÉÊË]", 'E', raw_text)
    raw_text = re.sub(u"[ìíîï]", 'i', raw_text)
    raw_text = re.sub(u"[ÌÍÎÏ]", 'I', raw_text)
    raw_text = re.sub(u"[òóôõö]", 'o', raw_text)
    raw_text = re.sub(u"[ÒÓÔÕÖ]", 'O', raw_text)
    raw_text = re.sub(u"[ùúûü]", 'u', raw_text)
    raw_text = re.sub(u"[ÙÚÛÜ]", 'U', raw_text)
    raw_text = re.sub(u"[ýÿ]", 'y', raw_text)
    raw_text = re.sub(u"[ÝŸ]", 'Y', raw_text)
    raw_text = re.sub(u"[ß]", 'ss', raw_text)
    raw_text = re.sub(u"[ñ]", 'n', raw_text)
    raw_text = re.sub(u"[Ñ]", 'N', raw_text)
    raw_text = raw_text.replace(" ", "").replace("\t", "")
    return raw_text

@app.get("/{paragem}")
def get_stops(paragem: str):

    html_response = requests.get(f'https://www.stcp.pt/pt/widget/post.php?uid=d72242190a22274321cacf9eadc7ec5f&paragem={paragem}')
    html_response = ' '.join(html_response.content.decode().rstrip().split())
    soup = BeautifulSoup(html_response, 'html.parser')
    stops = {}

    i = 0
    key = 0

    for div in soup.find_all('div', class_='floatLeft'):
        if any("Linha" in item for item in div.get('class')):
            if str(key) not in stops.keys():
                stops[str(key)] = [format_text(div.get_text())]
            else:
                stops[str(key)].append(format_text(div.get_text()))
            i+=1
            if i % 3 == 0:
                key+=1

    return(stops)