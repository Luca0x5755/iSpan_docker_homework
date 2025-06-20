# Dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app", "--timeout 120"]

CMD ["sh", "-c", "if [ \"$FLASK_ENV\" = \"development\" ]; then flask run --host=0.0.0.0 --debug; else gunicorn -w 4 -b 0.0.0.0:5000 app:app --timeout 120; fi"]
