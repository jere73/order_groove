import urllib2


class Request:

    def __init__(self):
        pass

    def makeRequest(self, url):
        html = ""
        try:

            response = urllib2.urlopen(url)
            html = response.read()

        except urllib2.URLError:
            print('The url was invalid or forbidden.')
            raise urllib2.URLError('The url was invalid or forbidden.')

        return html
