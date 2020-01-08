import json


class DictOutputFormatter:
    pass

    def __init__(self, dict):
        self.dict = dict

    def toConsole(self):

        print('HTML Elements in web page are {}'.format(self.dict['total_elements']))
        print('The top five most used elements are ')
        for i, v in self.dict['top_five'].iteritems():
            print(str(i) + ' => ' + str(v))

    def toJson(self):
        app_json = json.dumps(self.dict)
        return app_json

