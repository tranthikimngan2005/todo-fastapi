# FastAPI Todo API

Simple Todo REST API built with FastAPI.

## Features

- FastAPI backend
- CRUD Todo API
- JWT Authentication
- Request logging middleware
- Docker support

## Run locally

Create virtual environment:

python -m venv venv

Activate:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

## Run with Docker

Build image:

docker build -t fastapi-todo .

Run container:

docker run -p 8000:8000 fastapi-todo

Open:

http://localhost:8000/docs