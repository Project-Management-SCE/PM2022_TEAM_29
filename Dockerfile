FROM python:3.7.2-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
