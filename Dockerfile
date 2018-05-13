FROM python:3.6

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD [ "python", "./products/web_app.py" ]