from collections import Counter

from dict_output_formatter import DictOutputFormatter
from reader import Reader
from request import Request


def run():
    request1 = Request()
    html = request1.makeRequest('http://python.org')

    reader = Reader()
    reader.feed(html)
    metrics = reader.get_metrics()

    output_formatter = DictOutputFormatter(metrics)
    output_formatter.toConsole()
    json = output_formatter.toJson()
    print(json)


if __name__ == '__main__':
    run()
