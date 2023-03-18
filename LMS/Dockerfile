FROM python

WORKDIR /src

COPY src /src/

COPY requirements.txt /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python main.py