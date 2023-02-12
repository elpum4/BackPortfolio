FROM python:3.9

ARG SECRET_KEY
ARG DATABASE_URL

ENV DATABASE_URL=${DATABASE_URL}
ENV SECRET_KEY=${SECRET_KEY}

WORKDIR /usr/src/app

COPY . .
RUN echo '/usr/src' > /usr/local/lib/python3.9/site-packages/dependencies.pth
RUN pip install -r setup/requirements.txt

CMD ["uwsgi", "--ini", "/usr/src/app/app.ini"]
