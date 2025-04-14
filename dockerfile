FROM python:3.11-slim

RUN mkdir app

COPY scripts/ /app

WORKDIR /app

RUN pip install -r requirements.txt 

CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]

