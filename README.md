# ICE Portal Status Logger 🚄📊

This little python script logs the information which is presented and used in the ICE-Portal, e.g. the current speed, quality of internet connection or the geoposition. The logfile is a jsonlines-file.

The following two endpoints are used:

* https://iceportal.de/api1/rs/tripInfo/trip which contains information about the trip, e.g. the train number, start station or current delay
* https://iceportal.de/api1/rs/status which contains information about the wifi quality, geoposition and servertime

## How to install it? 💻

This project requires Python 3 and pipenv. 

1. Clone this repository

2. Run

       pipenv install

## How to use it? / Requirements 📝

1. You need to be on the wifi of a train of the Deutsche Bahn. I can assure that it works for ICE, however, ICs work probably as well.

2. Run

       pipenv run python main.py
       
The data is now logged into a file, e.g. "2019-05-22 21.18_ICE635_Bremen Hbf-Nürnberg Hbf.jsonlines"

## What to do further? 🔮

I think I am going to visualize the data to see in which areas the internet is better and in which it is worth. Furthermore, I guess it is interesting to see how fast the train is driving. 
