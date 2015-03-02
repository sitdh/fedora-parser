from fedora.template.fedora import FedoraTemplate
from fedora.manager.manager import FedoraConnectionManager

if '__main__' == __name__:
    fedoraTemplate = FedoraTemplate()
    a = FedoraConnectionManager("http://localhost:8080/rest/hand/english/fcr:metadata", templates=[FedoraTemplate()]);

    print a.__dict__
