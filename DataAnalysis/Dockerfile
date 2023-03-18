FROM python

COPY src /src

WORKDIR /src

COPY requirements.txt /src/
COPY setup.sh /src

RUN apt-get update

RUN pip install -r requirements.txt
RUN bash setup.sh

CMD python main.py