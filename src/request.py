import urllib2


class Request:

    def __init__(self, url):
        self.base_url = url

    def makeRequest(self):

        try:
            response = urllib2.urlopen(self.base_url)
            html = response.read()
        except urllib2.URLError:
            raise urllib2.URLError('The url was invalid or forbidden.')

        return html
