import urllib2


class Request:

    def __init__(self, url):
        self.base_url = url

    def makeRequest(self):
        response = urllib2.urlopen(self.base_url)
        html = response.read()

        return html
