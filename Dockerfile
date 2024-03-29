FROM python:3.8.10-alpine

COPY . /app

RUN pip install --upgrade pip && \
    pip install --upgrade openai

WORKDIR /app

CMD ["python", "chatbot.py"]