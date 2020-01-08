from HTMLParser import HTMLParser
from collections import Counter


class Reader(HTMLParser):
    data_container = ""

    _total_tags = 0
    _tags = {}

    def handle_data(self, data):
        self.data_container += data
        return self.data_container

    def handle_starttag(self, tag, attrs):
        self._total_tags += 1

        if tag in self._tags:
            self._tags[tag] += 1
        else:
            self._tags[tag] = 1

    def get_metrics(self):

        elements = Counter(self._tags)
        most_commons = elements.most_common(5)
        top_five = {}

        if len(most_commons) != 0:
            for i, v in most_commons:
                top_five[i] = v

        metrics = {
            'total_elements': self._total_tags,
            'top_five': top_five
        }

        return metrics
