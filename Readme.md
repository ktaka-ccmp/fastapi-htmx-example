
# A simple FastAPI example

```
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi sqlalchemy uvicorn pydantic[email] jinja2

./api01/create_data.sh

uvicorn main:app  --host 0.0.0.0 --reload
```
