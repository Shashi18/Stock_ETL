FROM python:3.9

ADD PipeLine.py .

ADD PullData.py .

ADD stocks.txt .

RUN pip install requests beautifulsoup4 pysqlite3

CMD ["python","./PullData.py"]
