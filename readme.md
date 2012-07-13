Environment Canada weather stations indexed by the StationID used in the web user interface.  See for example, "this one":http://www.climate.weatheroffice.gc.ca/climateData/monthlydata_e.html?timeframe=3&Prov=XX&StationID=10813&Year=2010&Month=10&Day=25.

Note almost no useful metadata is scraped (because it's not on web pages);
primarily intended as a feed into the "canada temperature data scraper":http://scraperwiki.com/scrapers/canada-temperature-data/.

## Identifiers and so on ##

Each station has a *webid* which is used in various URLs to get data from the
station.  It appears to be stable.  It is visible from the search results
page.

Each station has a permanent and stable identifier used by Environment Canada.
Mostly we convert these to 11-character GHCN-syle identifiers by prepending
"CAE".  And these are mostly what we use to index and key into tables.

## Tables ##

station
  List of stations, scraped from search results page.  Also contains the time
  period for which ther is data (because that is returned in the search result
  and is quite useful).

meta
  The station's metadata (name, identifier, location); unfortunately also
  mixed with metadata about the scrape from this station (like when the
  station's data was last downloaded)

series
  Derived information about the time series of each element from each station.
  Stuff like how many totaly months there are of Tmean data, and its range
  of years.

obs
  Huge table of all observations, with a row containing one monthly value
  for one element at one station.
