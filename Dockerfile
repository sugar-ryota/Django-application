FROM ubuntu:18.04
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y locales curl python3-distutils \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip install -U pip \
    && pip install psycopg2-binary \
    && mkdir /code \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
WORKDIR /code
ADD requirements.txt /code
# requirements.txtからパッケージのインストール
RUN pip install -r requirements.txt

# サーバーを立てる場所に移動
WORKDIR /Django-application/
# これでbashとか使わずにrunするだけでサーバーが立つ
CMD  python3 manage.py runserver 0:8080

# EXPOSE 8080