from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import inspect
import requests, json 

class FedoraConnectionManager:

    __oerUri = ''
    __parserTemplates = set()

    def __init__(self, uri, templates=[], auto_retrieved=True):

        validator = URLValidator(verify_exists=False)

        try:
            validator(uri)

            self.__oerUri = uri

            for t in templates:
                if 'OERTemplate' == t.__class__.__bases__[0].__name__:
                    self.__parserTemplates.add(t)

            if True == auto_retrieved:
                self.retrieve_information()

        except ValidationError, e:
            pass

    """
    To retrieve OER content from assigned URI
    """
    def retrieve_information(self):
        request_header = {'accept': 'application/ld+json'}
        r = requests.get(self.__oerUri, headers=request_header)

        json_response = r.json()

        """ Start parsing information with assigned template """
        for template in self.__parserTemplates:
            template.parse(json_response)
            self += template

    def __add__(self, other):
        for key in other.__dict__.keys():
            setattr(self, key, other.__dict__[key])
