<h1> Stock Live Monitoring and Prediction </h1>

<h3> NOTE: This project is on-going and is not complete yet.</h3>
<p>
  This is a project that involves pulling stock information by scraping the stock information from Google Finance and then load in our database.
  The aim is to put a live dashboard showing the stocks of various companies. The first part of th eproject deals with a live dashboard to track
  the stocks. The second part of this project deals with stock prediction.
</p>
<img src='https://github.com/Shashi18/Stock_ETL/blob/main/Plots/Architecture.jpg' width='150%'>

<h2> What's happening here? </h2>
<hr>
<h4> Data Scraping </h4>
<p>
  We begin with scrapping data using BeautifulSoup from Google Finance every <i>n</i> minutes. I set <i>n</i> as 2. However, scrapping from the same IP would lead to an IP block. To avoid this, I use proxies and scrap from multiple servers. 
</p>
<h4> Scheduling </h4>
<p>
  For scrap scheduling, we use Cron job script that triggers the Python script stored on AWS Lambda. AWS Lambda has a timeout so our scrapping must get executed within a time frame.
</p>
<h4> Stock List </h4>
<p>
  I pull the stock list stored on AWS S3 bucket which basically can be updated as per requirements (stocks in which the user wants to invest).
</p>
<h4> Database </h4>
<p>
  After scrapping and AS Lambda gets executed, we get our incremental data which is then appended to the DynamoDB database OR SQLite Dtabase stored on an S3 bucket. This database has tables for each stock present in the stock list on S3.
</p>
<h4> Plot </h4>
<p>
  Plot the stock data obtained from the database.
</p>
<h2> Pre-Requisites </h2>

<img src='https://github.com/Shashi18/Stock_ETL/blob/main/Plots/Plot5.jpg' width='150%'>
<img src='https://github.com/Shashi18/Stock_ETL/blob/main/Plots/Plot4.jpg' width='150%'>

For this project we will be using
<ul>
  <li> Python 
     <ul>
       <li> For extraction of data from Google and loading it into our SQLite database and Pandas. </li>
    </ul>
  </li>
  <li> Docker 
    <ul>
      <li> This will used to make a container for our scripts which would be required to run the scripts on Amazon Cloud. </li>
    </ul>
  </li>
  <li> Shell 
    <ul>
      <li> This will be used to schedule our script to extract data every minute. </li>
    </ul>
  </li>
</ul>
As an alternative, we can use AWS Lambda to execute our Python script every 2 or 5 minutes and then load the incremental data into our S3 bucket.
<hr>
<h2> Part 1: Stock Live Dashboard </h2>
<h3> Working Onto It. </h3>
<p>
  For the dashboard, I'll need to revamp my front end skills. Stay tuned. 
</p>
<hr>
<h2> Part 2: Stock Prediction </h2>
In this section I'll explain the process flow for stock prediction. I initially went with Amazon stock history. The data of AMZN obtained from Yahoo Finance API. The most suitable algorithm for stock prediction must be the one that can remember the temporal structure of the time-series. LSTM(Long-Short Term Memory) is best known for this and works better than RNN by avoiding the issue of gradients. 
