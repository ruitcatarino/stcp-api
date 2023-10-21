# STCP API
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://spdx.org/licenses/MIT.html)

## Overview
The STCP API is an unofficial API for the STCP, offering access to real-time departure times. It is designed to work with HTTP queries made by the SMSBus application since STCP does not provide a free access API for real-time departure monitoring.

## Current Endpoints
The API is hosted on [Deta Space](https://stcpapi-1-f2965388.deta.app) and provides the following endpoint:

### `/stops/<paragem>`
- **Method:** `GET`
- **Example Request:** `https://stcpapi-1-f2965388.deta.app/stops/GGT2`
- **Response:**
  ```json
  {
    "0": ["Linha", "Destino", "Proxima"],
    "1": ["200", "BOLHAO-", "apassar-"],
    "2": ["207", "CAMPANHA-P", "15:08-1min"],
    "3": ["204", "H.S.JOAO", "15:11-4min"],
    "4": ["503", "BOAVISTAB.S", "15:12-5min"],
    "5": ["200", "BOLHAO-", "15:18-11min"]
  }
### `/docs`

![Interactive API docs](https://i.ibb.co/5YLRnqP/Screenshot-4.png)

## Installation

``` bash
git clone https://github.com/ruitcatarino/stcp-api
cd stcp-api
```

### Python
``` bash
pip3 install -r requirements.txt
uvicorn main:app
```

### Poetry
```bash
poetry run uvicorn main:app --reload
```

### Docker
```bash
docker pull ruitcatarino/stcp-api
docker run -p 8000:8000 ruitcatarino/stcp-api
```

### Docker from source
```bash
docker build -t stcp-api .
docker run -p 8000:8000 stcp-api
```

## Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [HTTPX](https://www.python-httpx.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [uvicorn](https://www.uvicorn.org/)

## Contributing

Feel free to submit a [pull request](https://github.com/ruitcatarino/stcp-api/pull/new/main) or an [issue](https://github.com/ruitcatarino/stcp-api/issues/new)!

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it in accordance with the license terms.
