FROM python:3.9-slim
COPY /backend /app
WORKDIR /app
RUN pip install flask
RUN pip install pymongo
CMD ["python", "app.py"]

