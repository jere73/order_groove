from HTMLParser import HTMLParser


class Parser(HTMLParser):
    data_container = ""

    total_tags = 0
    tags = {}

    def handle_data(self, data):
        self.data_container += data
        return self.data_container

    def handle_starttag(self, tag, attrs):
        self.total_tags += 1

        if tag in self.tags:
            self.tags[tag] += 1
        else:
            self.tags[tag] = 1
