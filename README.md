<h1> Stock Live Monitoring and Prediction </h1>

<h3> NOTE: This project is on-going and is not complete yet.</h3>
<p>
  This is a project that involves pulling stock information by scraping the stock information from Google Finance and then load in our database.
  The aim is to put a live dashboard showing the stocks of various companies. The first part of th eproject deals with a live dashboard to track
  the stocks. The second part of this project deals with stock prediction.
</p>
<img src='https://github.com/Shashi18/Stock_ETL/blob/main/Plots/Plot3.png' width='150%'>
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

<h2> Part 1: Stock Live Dashboard </h2>
<h1> To be continued </h1>

