FROM python:3
WORKDIR /app
COPY ./codigo /app
CMD ["python3", "suma.py", "5", "6"]
