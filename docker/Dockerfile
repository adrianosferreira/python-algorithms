FROM python:3

WORKDIR /usr/src/app

RUN wget -q https://dl-ssl.google.com/linux/linux_signing_key.pub -O- | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y -qq update && apt-get -y -qq install google-chrome-stable


RUN pip install selenium requests camelot

COPY . .

CMD [ "python", "./test.py" ]
