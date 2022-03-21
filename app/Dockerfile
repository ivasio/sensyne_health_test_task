FROM python:3.8


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ls -l

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8000
