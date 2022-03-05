FROM python:3.9.9 as deps
WORKDIR /home/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.9.9
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /home/app

# Not a good idea, this could be a security risk
COPY . .

ENV PORT=8000
EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN chmod +x ./run.sh

CMD ./run.sh