# duka - Dukascopy data downloader

Finding good Forex data is difficult or expensive. Dukascopy has made available an excellent [web tool](https://www.dukascopy.com/swiss/english/marketwatch/historical/) to download tick data for a large a variety of 
Forex, CFD and commodities. This is awesome and extremely useful for people, like me, trying to study the Forex market. 
However, it takes a lot of time to download a large data set from the website because you can download only one day per time. In order to solve this issue, I created **duka**.  

**duka** is a small terminal application that can be used to download ticks for a given date range from the Dukascopy historical data feed for one or more symbols. **duka** takes advantage of python threads and coroutine in order to speed up the download. It takes roughly 10m to download tick data for  one year for a given instrument. No bad :)

Key features :
 - Ticks data with volumes
 - Candle formatting with different time-frames ( from 1 minute to 1 day )
 - CSV output
 - multi-thread support
 - Large variety of symbols

This is what **duka** looks like:

![duka](.img/Screen Shot 2016-04-10 at 20.15.51.png)

As you can see, **duka** estimates the time left until the download is completed. This is extremely useful when downloading a large data set. 


I hope you enjoy it!! 


## Installation

**duka** requires python 3.5 and request 2.0.1. It can be installed using `pip` as follows:

```
pip install duka
```

## Usage
```
 usage: duka [options]

 positional arguments:
    SYMBOLS               symbol list using format EURUSD EURGBP 

 optional arguments:
     -h           show help message and exit 
     -v           show program's version number and exit
     -d DAY       specific day format YYYY-MM-DD (default today)
     -s STARTDATE start date format YYYY-MM-DD (default today)
     -e ENDDATE   end date format YYYY-MM-DD (default today)
     -c CANDLE    use candles instead of ticks. Accepted values M1 M2 M5 M10 M15 M30 H1 H4 D1
     -f FOLDER    the dowloaded data will be saved in FOLDER (default '.')
     -t THREAD    number of threads (default 10)
     --header     include CSV header (default false)
     --local-time use local time (default GMT)
```

## Examples


- Help

   ```
   duka -h
   ```
- Download last available tick set (i.e. yesterday if not Saturday ) for `EURUSD` and `GBPUSD` 

  ```
  duka EURUSD GBPUSD 
  ```
- Download ticks for the `EURUSD` for a specific day

  ``` 
  duka EURUSD -d 2016-02-02
  ```
- Download ticks for the `EURUSD` between two dates. For example:

  ```
  duka EURUSD -s 2015-01-01 -e 2016-12-31 
  ```
  download all ticks for the 2015 year

- We can specify only the start date. The default end date will be today. For example:   
  
  ```
  duka EURUSD -s 2016-01-01
  ```
  downloads all ticks from the beginning of the year until now. 

All data is saved in the current folder. You can also specify the number of threads to be used by setting the `t` option. 
I recommend not to use too many threads because you might encounter problems opening too many connection to the server. 

## Helping 
Found a bug? Missing a feature? Open a issue and I will try to fix it as soon as possible. Pull request are also welcomed. :) 

## License

This software is licensed under the MIT License.

Copyright Giuseppe Pes, 2016.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
USE OR OTHER DEALINGS IN THE SOFTWARE.



