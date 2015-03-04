from fedora.template.fedora import FedoraTemplate
from fedora.template.root import FedoraRootNodeTemplate 
from fedora.manager.manager import FedoraConnectionManager

if '__main__' == __name__:
    fedoraTemplate = FedoraTemplate()

    # endpoint = 'http://localhost:8080/rest'
    # endpoint = 'http://localhost:8080/rest/fcr:metadata'
    endpoint = 'http://localhost:8080/rest/hand/english/fcr:metadata'

    # template = FedoraRootNodeTemplate()
    template = FedoraTemplate()

    parser = FedoraConnectionManager(
            endpoint,
            templates=[template]
        );
    # data = parser.retrieve_information()
    data = parser.retrieve_information()

    print data 
