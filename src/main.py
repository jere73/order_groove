from collections import Counter

from src.dict_output_formatter import DictOutputFormatter
from src.reader import Reader
from src.request import Request


def run():
    request1 = Request('https://www.ole.com.ar/river-plate/')
    html = request1.makeRequest()

    reader = Reader()
    reader.feed(html)
    metrics = reader.get_metrics()

    output_formatter = DictOutputFormatter(metrics)
    json = output_formatter.toJson()
    print(json)
    output_formatter.toConsole()


if __name__ == '__main__':
    run()
