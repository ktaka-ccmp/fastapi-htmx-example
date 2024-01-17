
# A simple FastAPI example

```
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi sqlalchemy uvicorn pydantic[email] jinja2

# Prepare necessary SQLite databases
./api01/create_data.sh
./hx02/create_data.sh

uvicorn main:app  --host 0.0.0.0 --reload
```
