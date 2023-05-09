FROM python:3.9-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r Requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]
