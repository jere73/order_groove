from request import Request
from src.parser import Parser


def run():
    request1 = Request('https://www.ole.com.ar/river-plate/')
    html = request1.makeRequest()

    parser1 = Parser()
    parser1.feed(html)

    print(parser1.tags)


if __name__ == '__main__':
    run()
