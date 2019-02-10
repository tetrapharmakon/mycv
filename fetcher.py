import urllib
url = 'http://export.arxiv.org/api/query?search_query=all:loregian&start=0'
response = urllib.urlopen(url).read()
print(response)