from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import inspect
import requests, json 

class FedoraConnectionManager:

    __oerUri = ''
    __parserTemplates   = set()

    def __init__(self, uri, templates=[]):

        validator = URLValidator(verify_exists=False)

        try:
            validator(uri)

            self.__oerUri = uri

            for t in templates:
                if 'OERTemplate' == t.__class__.__bases__[0].__name__:
                    self.__parserTemplates.add(t)

        except ValidationError, e:
            pass

    """
    To retrieve OER content from assigned URI
    """
    def retrieve_information(self):
        request_header = {'accept': 'application/ld+json'}
        r = requests.get(self.__oerUri, headers=request_header)

        json_response = r.json()

        parsed_data = dict();

        """ Start parsing information with assigned template """
        for template in self.__parserTemplates:
            template.parse(json_response)

            for key in template.__dict__.keys():
                val = getattr(template, key)
                parsed_data[key] = val

        return parsed_data
