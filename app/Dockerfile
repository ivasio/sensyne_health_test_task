FROM python:3.8

#RUN apt-get update && apt-get install --no-install-recommends -y \
#  # dependencies for building Python packages
#  build-essential \
#  # psycopg2 dependencies
#  libpq-dev


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ls -l

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8000
