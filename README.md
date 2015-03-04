# JCR Message Parser

This parser was tested on Fedora commons version 4.1

## How to Use

Fedora commons is a flexible repository the user can implemene many of data schema to describe an object that was stored in the repository. So, The parser should have the flexibility to parse the data of object.

```python
from fedora.template.fedora import FedoraTemplate
from fedora.template.dublincore import DublinCoreTemplate
from fedora.template.manager import FedoraConnectionManager

endpoint = 'http:://example.com/rest/part/to/object'

pareser = FedoraConnectionManager(
            endpoint,
            templates=[ 
                FedoraTemplate(),       
                DublinCoreTemplate() 
            ]
        )

parsed_data = parser.retrieve_information()

print parsed_data
```

```FedoraTemplate``` accept both of types ```nt:resource``` and ```nt:folder``` in ```#primaryType``` 
