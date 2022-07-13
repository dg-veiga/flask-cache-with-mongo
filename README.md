## How to run

API:

```sh
git clone *project*
cd *project*
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Mongo DB:

```sh
cd *project*
docker-compose up
```

## Routes:

GET /info

```json
RESPONSE
{
    "msg": "I'm working!"
}
```

POST /insert

```json
PAYLOAD
{
    "username" string, not required
    "registry" string, not required
    "ttl": int (in minutes), required
    "data": dict, required
}
```

/retrieve

```json

```

Observations:

- django port: 8008
- mongo port: 27018
