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

    """Object Id: @id"""
    object_id                   = ""
    """Object Type: @type"""
    object_types                = set()
    create_time                 = None 
    """User who create this object"""
    create_by                   = "" 
    """Export type"""
    exports_as                  = None
    """Parent URI"""
    has_parent                  = "" 
    last_modified               = None
    last_modified_by            = ""
    mixin_types                 = set() 
    primary_type                = "" 
    uuid                        = "" 
    writable                    = False
    contains                    = set() 

    # for binary information
    digest                      = ''
    has_fixity_service          = ''
    mime_type                   = ''
    described_by                = ''
    has_original_name           = ''
    has_size                    = ''

    def __init__(self):
        pass

    def parse(self, json_content=None):
        if None == json_content:
            return

        primary_content = json_content[0];

        self.object_id = primary_content[self.FEDORA_ID]
        for t in primary_content[self.FEDORA_TYPE]:
            self.object_types.add(t)

        # created
        self.create_time = primary_content[self.FEDORA_CREATED_URI][0][self.FEDORA_VALUE]

        # createdBy
        self.create_by = primary_content[self.FEDORA_CREATE_BY_URI][0][self.FEDORA_VALUE]

        # last modified 
        self.last_modified = primary_content[self.FEDORA_LAST_MODIFIED_URI][0][self.FEDORA_VALUE]

        # last modified by
        self.last_modified_by = primary_content[self.FEDORA_LAST_MODIFIED_BY_URI][0][self.FEDORA_VALUE]

        # mixin types
        for ts in primary_content[self.FEDORA_MIXIN_TYPES_URI]:
            self.mixin_types.add(ts[self.FEDORA_VALUE])

        # primary type 
        self.primary_type = primary_content[self.FEDORA_PRIMARY_TYPE_URI][0][self.FEDORA_VALUE]
        if self.REPOSITORY_FOLDER_TYPE == self.primary_type:
            self._container_parser(primary_content)
        else:
            self._binary_parser(primary_content)

        # UUID 
        self.uuid = primary_content[self.FEDORA_UUID_URI][0][self.FEDORA_VALUE]
        pass

    def _container_parser(self, primary_content):
        # exports as
        self.exports_by = primary_content[self.FEDORA_EXPORTS_AS_URI][0][self.FEDORA_ID]

        # has parent 
        self.has_parent = primary_content[self.FEDORA_HAS_PARENT_URI][0][self.FEDORA_ID]

        # Writable 
        self.writables = ('true' == primary_content[self.FEDORA_WRITABLE_URI][0][self.FEDORA_VALUE])

        # Contains 
        for c in primary_content[self.W3_CONTAINS]:
            self.contains.add(c[self.FEDORA_ID])

    def _binary_parser(self, primary_content):

        self.digest = primary_content[self.FEDORA_DIGEST_URI][0][self.FEDORA_ID]

        self.has_fixity_service = primary_content[self.FEDORA_HAS_FIXITY_SERVICE_URI][0][self.FEDORA_ID]

        self.mime_type = primary_content[self.FEDORA_MIME_TYPE_URI][0][self.FEDORA_VALUE]

        self.described_by = primary_content[self.IANA_DESCRIBED_BY_URI][0][self.FEDORA_ID]

        self.has_original_name = primary_content[self.LOC_HAS_ORIGINAL_NAME_URI][0][self.FEDORA_VALUE]

        self.has_size = primary_content[self.LOC_HAS_SIZE_URI][0][self.FEDORA_VALUE]

    def __getattr__(self):
        return ['a', 'b']
