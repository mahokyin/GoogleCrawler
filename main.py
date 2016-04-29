from gscrawler import GoogleSearchCrawler
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse


def getMainSite(pURL):
    parsed_uri = urlparse(pURL)
    pURL = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return pURL

print 'Start search'

## User options
NUM_SEARCH_RESULTS = 1000                # number of search results returned
search_words = ['Create account', 'signup']  # set the keyword setting

## Create the google search class
hh = GoogleSearchCrawler(search_words)

## Set the results
hh.set_num_of_search_results(NUM_SEARCH_RESULTS)
#hh.enable_sort_date_descending()# enable sorting of date by descending. --> not enabled

## Generate the Url list based on the search item
url_list =  hh.formed_search_url()
print  url_list

## Parse the google page based on the url
hh.parse_all_search_url()
hh.consolidated_results()

for website, name in zip(hh.websiteArray, hh.webNameArray):
    mainSite = getMainSite(website)
    print mainSite
    print website
    print name
    print

print 'Total result: '
print hh.count


print 'End Search'

