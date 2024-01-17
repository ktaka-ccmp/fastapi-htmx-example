
# A FastAPI HTMX example

```
# Create Python venv
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi sqlalchemy uvicorn pydantic[email] jinja2

# Prepare necessary SQLite databases
./api01/create_data.sh
./hx02/create_data.sh

# Run server
uvicorn main:app  --host 0.0.0.0 --reload
```
# Swagger UI

Endpoints can be found in the Swagger UI.

<img src=./image/fastapi-htmx-202401180453.gif width="600px">