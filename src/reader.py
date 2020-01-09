from HTMLParser import HTMLParser
from collections import Counter


class Reader(HTMLParser):
    data_container = ""

    _tags_open = {}
    _tags_close = {}
    _tags_start_end = {}
    _total_tags = 0
    _real_tags = {}

    def handle_data(self, data):
        self.data_container += data
        return self.data_container

    def handle_starttag(self, tag, attrs):
        if tag in self._tags_open:
            self._tags_open[tag] += 1
        else:
            self._tags_open[tag] = 1

    def handle_endtag(self, tag):
        if tag in self._tags_close:
            self._tags_close[tag] += 1
        else:
            self._tags_close[tag] = 1

    def handle_startendtag(self, tag, attrs):
        self._total_tags += 1

        if tag in self._tags_start_end:
            self._tags_start_end[tag] += 1
        else:
            self._tags_start_end[tag] = 1

    def get_metrics(self):

        for i in self._tags_open:
            if i in self._tags_close and self._tags_open[i] == self._tags_close[i]:
                self._total_tags += 1
                self._real_tags[i] = self._tags_open[i]

        self._real_tags.update(self._tags_start_end)

        elements = Counter(self._real_tags)
        most_commons = elements.most_common(5)

        metrics = {
            'total_elements': self._total_tags,
            'top_five': most_commons
        }

        return metrics
