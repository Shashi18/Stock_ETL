FROM python:3.9

ADD PipeLine.py PullData.py stocks.txt .

RUN pip install requests beautifulsoup4 pysqlite3

CMD ["python","./PullData.py"]
