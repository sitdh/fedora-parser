from template import OERTemplate
import json

class FedoraTemplate(OERTemplate):
    '''Fedora JCR standard message'''
    FEDORA_TYPE     = "@type"
    FEDORA_ID       = "@id"
    FEDORA_VALUE    = "@value"

    FEDORA_NAMESPACE            = "http://fedora.info/definitions/v4/repository#"
    FEDORA_CREATED_URI          = FEDORA_NAMESPACE + "created" 
    FEDORA_CREATE_BY_URI        = FEDORA_NAMESPACE + "createdBy" 
    FEDORA_EXPORTS_AS_URI       = FEDORA_NAMESPACE + "exportsAs" 
    FEDORA_HAS_PARENT_URI       = FEDORA_NAMESPACE + "hasParent" 
    FEDORA_LAST_MODIFIED_URI    = FEDORA_NAMESPACE + "lastModified" 
    FEDORA_LAST_MODIFIED_BY_URI = FEDORA_NAMESPACE + "lastModifiedBy" 
    FEDORA_MIXIN_TYPES_URI      = FEDORA_NAMESPACE + "mixinTypes" 
    FEDORA_PRIMARY_TYPE_URI     = FEDORA_NAMESPACE + "primaryType" 
    FEDORA_UUID_URI             = FEDORA_NAMESPACE + "uuid" 
    FEDORA_WRITABLE_URI         = FEDORA_NAMESPACE + "writable" 
    W3_CONTAINS                 = 'http://www.w3.org/ns/ldp#contains'

    # Binary namespace
    FEDORA_DIGEST_URI               = FEDORA_NAMESPACE + "digest"
    FEDORA_HAS_FIXITY_SERVICE_URI   = FEDORA_NAMESPACE + "hasFixityService"
    FEDORA_MIME_TYPE_URI            = FEDORA_NAMESPACE + "mimeType"
    IANA_DESCRIBED_BY_URI           = 'http://www.iana.org/assignments/relation/describedby'
    LOC_HAS_ORIGINAL_NAME_URI       = 'http://www.loc.gov/premis/rdf/v1#hasOriginalName'
    LOC_HAS_SIZE_URI                = 'http://www.loc.gov/premis/rdf/v1#hasSize'
    
    FEDORA_CONTAINER_TYPE       = "fedora:Container"
    FEDORA_RESOURCE_TYPE        = "fedora:Resource"
    REPOSITORY_FOLDER_TYPE      = "nt:folder"
    REPOSITORY_RESOURCE_TYPE    = "nt:binary"

    __content_container         = None

    def content(content_container):
        if not content_container:
            return

        self.__content_container = content_container


    def parse(self, json_content=None):

        json_content = json_content if json_content else self.__content_container
        primary_content = json_content[0]

        parsed_data = {}

        parsed_data['id'] = primary_content[self.FEDORA_ID]

        parsed_data['types'] = []
        for t in primary_content[self.FEDORA_TYPE]:
            parsed_data['types'].append(t)

        # created
        parsed_data['create_time'] = primary_content[self.FEDORA_CREATED_URI][0][self.FEDORA_VALUE]

        # createdBy
        parsed_data['create_by'] = primary_content[self.FEDORA_CREATE_BY_URI][0][self.FEDORA_VALUE]

        # last modified 
        parsed_data['last_modified'] = primary_content[self.FEDORA_LAST_MODIFIED_URI][0][self.FEDORA_VALUE]

        # last modified by
        parsed_data['last_modified_by'] = primary_content[self.FEDORA_LAST_MODIFIED_BY_URI][0][self.FEDORA_VALUE]

        # mixin types
        parsed_data['mixin_types'] = []
        for ts in primary_content[self.FEDORA_MIXIN_TYPES_URI]:
            parsed_data['mixin_types'].append(ts[self.FEDORA_VALUE])

        # primary type 
        parsed_data['primary_type'] = primary_content[self.FEDORA_PRIMARY_TYPE_URI][0][self.FEDORA_VALUE]

        data = {} 
        if self.REPOSITORY_FOLDER_TYPE == parsed_data['primary_type']:
            data = self._container_parser(primary_content)
        else:
            data = self._binary_parser(primary_content)

        parsed_data.update(data)

        # UUID 
        parsed_data['uuid'] = primary_content[self.FEDORA_UUID_URI][0][self.FEDORA_VALUE]


        return parsed_data

    def _container_parser(self, primary_content):
        parsed_data = {}

        # exports as
        parsed_data['exports_by'] = primary_content[self.FEDORA_EXPORTS_AS_URI][0][self.FEDORA_ID]

        # has parent 
        parsed_data['has_parent'] = primary_content[self.FEDORA_HAS_PARENT_URI][0][self.FEDORA_ID]

        # Writable 
        parsed_data['writables'] = ('true' == primary_content[self.FEDORA_WRITABLE_URI][0][self.FEDORA_VALUE])

        # Contains 
        parsed_data['contains'] = []
        for c in primary_content[self.W3_CONTAINS]:
            parsed_data['contains'].append(c[self.FEDORA_ID])

        return parsed_data

    def _binary_parser(self, primary_content):

        parsed_data = {}

        parsed_data['digest'] = primary_content[self.FEDORA_DIGEST_URI][0][self.FEDORA_ID]

        parsed_data['has_fixity_service'] = primary_content[self.FEDORA_HAS_FIXITY_SERVICE_URI][0][self.FEDORA_ID]

        parsed_data['mime_type'] = primary_content[self.FEDORA_MIME_TYPE_URI][0][self.FEDORA_VALUE]

        parsed_data['described_by'] = primary_content[self.IANA_DESCRIBED_BY_URI][0][self.FEDORA_ID]

        parsed_data['has_original_name'] = primary_content[self.LOC_HAS_ORIGINAL_NAME_URI][0][self.FEDORA_VALUE]

        parsed_data['has_size'] = primary_content[self.LOC_HAS_SIZE_URI][0][self.FEDORA_VALUE]

        return parsed_data
