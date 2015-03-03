from fedora.template.fedora import FedoraTemplate
from fedora.manager.manager import FedoraConnectionManager

if '__main__' == __name__:
    fedoraTemplate = FedoraTemplate()

    endpoint = 'http://localhost:8080/rest'
    # endpoint = 'http://localhost:8080/rest/fcr:metadata'
    # endpoint = 'http://localhost:8080/rest/hand/english/fcr:metadata'
    parser = FedoraConnectionManager(
            endpoint,
            templates=[FedoraTemplate()]
        );
    # data = parser.retrieve_information()
    data = parser.retrieve_information(root_node=True)

    print data 
