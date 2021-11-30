FROM python:3.9.0

WORKDIR /home/

RUN echo "result_LAST_1"

RUN git clone https://github.com/codemkim/Web_PET.git

WORKDIR /home/Web_PET/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=Web_main.settings.deploy && python manage.py migrate --settings=Web_main.settings.deploy && gunicorn Web_main.wsgi --env DJANGO_SETTINGS_MODULE=Web_main.settings.deploy --bind 0.0.0.0:8000"]