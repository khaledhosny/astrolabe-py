FROM python:3.12-bookworm

WORKDIR /code

RUN pip install cairocffi numpy scipy typst
