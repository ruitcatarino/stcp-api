import itertools
import re

import httpx
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


async def format_text(raw_text):
    raw_text = re.sub("[àáâãäå]", "a", raw_text)
    raw_text = re.sub("[ÀÁÂÃÄÅ]", "A", raw_text)
    raw_text = re.sub("[èéêë]", "e", raw_text)
    raw_text = re.sub("[ÈÉÊË]", "E", raw_text)
    raw_text = re.sub("[ìíîï]", "i", raw_text)
    raw_text = re.sub("[ÌÍÎÏ]", "I", raw_text)
    raw_text = re.sub("[òóôõö]", "o", raw_text)
    raw_text = re.sub("[ÒÓÔÕÖ]", "O", raw_text)
    raw_text = re.sub("[ùúûü]", "u", raw_text)
    raw_text = re.sub("[ÙÚÛÜ]", "U", raw_text)
    raw_text = re.sub("[ýÿ]", "y", raw_text)
    raw_text = re.sub("[ÝŸ]", "Y", raw_text)
    raw_text = re.sub("[ß]", "ss", raw_text)
    raw_text = re.sub("[ñ]", "n", raw_text)
    raw_text = re.sub("[Ñ]", "N", raw_text)
    raw_text = raw_text.replace(" ", "").replace("\t", "")
    return raw_text


@app.get("/stops/{paragem}")
async def get_stops(paragem: str):
    url = f"https://www.stcp.pt/pt/widget/post.php?uid=d72242190a22274321cacf9eadc7ec5f&paragem={paragem}"

    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url)
            response.raise_for_status()

            cleaned_html = " ".join(response.text.rstrip().split())
            soup = BeautifulSoup(cleaned_html, "html.parser")

            stops_lines = []

            for div in soup.find_all("div", class_="floatLeft"):
                if any("Linha" in item for item in div.get("class")):
                    stop_text = await format_text(div.get_text())
                    stops_lines.append(stop_text)

            return list(itertools.batched(stops_lines[3:], 3))
    except httpx.HTTPError as e:
        return None
