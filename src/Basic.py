import urllib2
response = urllib2.urlopen('https://python.org')
html = response.read()
print(html)