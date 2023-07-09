# STCP API

Unofficial API for the STCP (Serviço de Transportes Coletivos do Porto), the city's public transportation system.

It sniffs HTTP queries made by the SMSBus application because STCP does not offer its users a free access API to monitor departure times in real-time.

## Current Endpoints

All endpoints are relative to the [API hosted on Deta Space](https://stcpapi-1-f2965388.deta.app/)

### `/stops/<paragem>`

- Method: `GET`

- Example request:
  ```
  https://stcpapi-1-f2965388.deta.app/stops/GGT2
  ```

- Response:
  ```json
  {
        "0": [
            "Linha",
            "Destino",
            "Proxima"
        ],
        "1": [
            "200",
            "BOLHAO-",
            "apassar-"
        ],
        "2": [
            "207",
            "CAMPANHA-P",
            "15:08-1min"
        ],
        "3": [
            "204",
            "H.S.JOAO",
            "15:11-4min"
        ],
        "4": [
            "503",
            "BOAVISTAB.S",
            "15:12-5min"
        ],
        "5": [
            "200",
            "BOLHAO-",
            "15:18-11min"
        ]
    }
  ```

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
docker docker pull ruitcatarino/stcp-api
docker run -p 8000:8000 ruitcatarino/stcp-api
```

### Docker from source
```bash
docker build -t stcp-api .
docker run -p 8000:8000 stcp-api
```

## Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [uvicorn](https://www.uvicorn.org/)

## Contributing

Feel free to submit a [pull request](https://github.com/ruitcatarino/stcp-api/pull/new/main) or an [issue](https://github.com/ruitcatarino/stcp-api/issues/new)!

## License

The MIT License (MIT)
