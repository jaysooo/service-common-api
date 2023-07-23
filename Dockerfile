from python:3.11-alpine

# set env
WORKDIR /usr/src
# source copy
COPY ./app ./app

ENV PYTHONPATH /usr/src/app

# package install
RUN pip install --upgrade pip && pip install --no-cache-dir -r ./app/requirements.txt

EXPOSE 9000

CMD python -m uvicorn app.main:app --reload --host=0.0.0.0 --port 9000

