FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /home/lookvalue/

ADD ./company ./company
ADD ./value ./value

ADD ./manage.py .

ADD requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

# ENTRYPOINT ["python", "manage.py", "runserver",  ":8000"]
ENTRYPOINT ["uwsgi", "--ini", "value/config/uwsgi/uwsgi.ini"]

# CMD ["--py-autoreload", "1"]
# CMD ["--noreload"]