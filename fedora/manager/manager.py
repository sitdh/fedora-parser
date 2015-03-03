from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import inspect
import requests, json 

class FedoraConnectionManager:

    __oer_uri = ''
    __parser_templates      = set()

    def __init__(self, uri, templates=[]):

        validator = URLValidator(verify_exists=False)

        try:
            validator(uri)

            self.__oer_uri = uri

            for t in templates:
                if 'OERTemplate' == t.__class__.__bases__[0].__name__:
                    self.__parser_templates.add(t)

        except ValidationError, e:
            pass

    """
    To retrieve OER content from assigned URI
    """
    def retrieve_information(self, root_node=False):

        request_header = {'accept': 'application/ld+json'}

        r = requests.get(self.__oer_uri, headers=request_header)
        json_response = r.json()

        parsed_data = dict();

        """ Start parsing information with assigned template """
        for template in self.__parser_templates:
            data = template.parse(
                    json_response, 
                    parse_root_element=root_node
                )
            print data
            # for key in template.__dict__.keys():
            #     val = getattr(template, key)
            #     parsed_data[key] = val

        return parsed_data
