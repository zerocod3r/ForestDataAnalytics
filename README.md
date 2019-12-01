# Forest Data Analytics

## Ground Assist
* [Team Members](#team-members)
* [Introduction](#introduction)
* [Requirements](#requirements)
* [How to run](#how-to-run)
* [Screenshot](#screenshots)


### <a name="team-members"></a>Team Members
* Deepak Balhara <https://deepakbalhara.tech>
* Sarthak Rohilla <https://zerocod3r.github.io>


### <a name="introduction"></a>Introduction
The project is to process Forest Data provided by [MINISTRY OF AGRICULTURE AND FORESTRY, Finland](https://www.metsaan.fi/paikkatietoaineistot) and extract knowledge from these datasets by visualizing them onto an Analysis Dashboard, such that it can help solving various use case scenarios regarding conservation of forests.


### <a name="requirements"></a>Requirements
Ground Assist uses a number of open source projects to work properly.
 - [Apache Solr](http://lucene.apache.org/solr/) - big data tool for fast access data storage
 - [Banana](https://github.com/lucidworks/banana) - A port of Kibana for Apache Solr
 - [Python3](https://www.python.org/downloads/) - libraries required BeautifulSoup, geopy, django == 2.1 or later

tt
### <a name="how-to-run"></a>How to run
Ground Assist requires [Python3](https://www.python.org/downloads/) to run.

DataSets folder contains files downloaded from https://www.metsaan.fi/paikkatietoaineistot containing raw json data


Clone the repository
```sh
$ git clone https://github.com/zerocod3r/ForestDataAnalytics.git
$ cd ForestDataAnalytics
```
Install the dependencies.
```sh
$ pip3 install bs4
$ pip3 install geopy
```
Edit this file ```location-plotter/gassist/templates/index.html``` and add your Google Maps API key

Run solr server and django server with ```start-server.py``` file
```sh
$ py start-server.py
```
Visit this url to access dashboard
```http://localhost:8983/solr/banana/src/index.html#/dashboard/solr/Forest%20Data%20Analytics?server=%2Fsolr%2F```


### <a name="screenshots"></a>Screenshot
![alt text](https://raw.githubusercontent.com/zerocod3r/ForestDataAnalytics/master/analytics-ss.jpg)

**Free Software, yeah!**

