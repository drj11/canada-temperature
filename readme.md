# Environment Canada Temperature Data #

There are two scripts to do the scraping: `weather-stations`, and
`canada-temperature-data`.

`weather-stations` makes a list of weather stations (in the table *station*).
It is indexed by the StationID used in the web user interface.  See for example,
[this one](http://www.climate.weatheroffice.gc.ca/climateData/monthlydata_e.html?timeframe=3&Prov=XX&StationID=10813&Year=2010&Month=10&Day=25).
Almost no useful metadata is scraped (because it's not on web pages).

`canada-temperature-data` is a much longer process of scraping data
 from each station.  It has
been made restartable by scoring each station so it will generally avoid
scraping stations it has done recently, and prefer ones where there is
a larger amount of data that it hasn't got yet.

## Identifiers and so on ##

Each station has a *webid* which is used in various URLs to get data from the
station.  It appears to be stable.  It is visible from the search results
page.

Each station has a permanent and stable identifier used by Environment Canada.
Mostly we convert these to 11-character GHCN-syle identifiers by prepending
"CAE".  And these are mostly what we use to index and key into tables.

## Tables ##

<dt>station
<dd>List of stations, scraped from search results page.  Also contains the time
  period for which ther is data (because that is returned in the search result
  and is quite useful).

<dt>meta
<dd>The station's metadata (name, identifier, location); unfortunately also
  mixed with metadata about the scrape from this station (like when the
  station's data was last downloaded)

<dt>series
<dd>Derived information about the time series of each element from each station.
  Stuff like how many totaly months there are of Tmean data, and its range
  of years.

<dt>obs
<dd>Huge table of all observations, with a row containing one monthly value
  for one element at one station.
