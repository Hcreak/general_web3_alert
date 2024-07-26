FROM ghcr.io/celestiaorg/celestia-app:latest AS celestia-app

FROM python:3.9

COPY --from=celestia-app /bin/celestia-appd /bin/celestia-appd

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
ADD *.py ./

CMD python3 -u celestia_balance.py