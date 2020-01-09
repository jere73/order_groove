import json


class DictOutputFormatter:
    pass

    def __init__(self, dict):
        self.dict = dict

    def toConsole(self):

        if self.dict['total_elements'] != 0:

            print('HTML Elements in web page are {}'.format(self.dict['total_elements']))
            print('The top five most used elements are ')

            for i in self.dict['top_five']:
                print(i)
        else:
            print('NO elements.')

    def toJson(self):

        if self.dict['total_elements'] != 0:
            app_json = json.dumps(self.dict)
            return app_json
        else:
            return {}

