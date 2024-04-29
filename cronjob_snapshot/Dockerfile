FROM python:3.12-slim

RUN pip install -U pip

WORKDIR /src
ADD ./src/requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

RUN chmod -R 100 *
RUN apt-get -s remove apt
RUN rm -R /bin/cat /bin/ls /bin/pwd /bin/ln /bin/mv /bin/cp
RUN rm -Rf /var/cache/apt

CMD ["python", "main.py"]
