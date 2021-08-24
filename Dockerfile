# FROM arm32v7/python:3.8
FROM python:3.9


ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.8

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code

COPY ./vaccine_tracker ./vaccine_tracker
COPY Dockerfile .
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false && \
    poetry install

CMD [ "poetry", "run", "python", "-m", "vaccine_tracker" ]
