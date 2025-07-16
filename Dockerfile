FROM python:3.9-alpine3.13
LABEL maintainer="Celestin"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./recommendation /
WORKDIR /recommendation
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-ache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755git  /vol

ENV PATH="/py/bin:$PATH"
USER django-user

# Run migrations and collect static files
# CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
CMD python manage.py migrate && gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
