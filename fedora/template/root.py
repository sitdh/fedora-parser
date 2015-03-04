from template import OERTemplate
import json

class FedoraRootNodeTemplate(OERTemplate):

    """ NEW """
    FEDORA_TYPE     = "@type"
    FEDORA_ID       = "@id"
    FEDORA_VALUE    = "@value"

    FEDORA_NAMESPACE            = "http://fedora.info/definitions/v4/repository#"

    FEDORA_EXPORTS_AS_URI                                                           = FEDORA_NAMESPACE + "exportsAs" 
    FEDORA_HAS_NODE_TYPE_URI                                                        = FEDORA_NAMESPACE + 'hasNodeType'
    FEDORA_HAS_TRANSACTION_PROVIDER_URI                                            = FEDORA_NAMESPACE + 'hasTransactionProvider'
    FEDORA_REPOSITORY_CUSTOM_REP_NAME_URI                                           = FEDORA_NAMESPACE + 'repositoryCustomRepName'
    FEDORA_REPOSITORY_IDENTIFIER_STABILITY_URI                                      = FEDORA_NAMESPACE + 'repositoryIdentifierStability'
    FEDORA_REPOSITORY_JCR_REPOSITORY_NAME_URI                                       = FEDORA_NAMESPACE + 'repositoryJcrRepositoryName'
    FEDORA_REPOSITORY_JCR_REPOSITORY_VENDOR_URI                                     = FEDORA_NAMESPACE + 'repositoryJcrRepositoryVendor'
    FEDORA_REPOSITORY_JCR_REPOSITORY_VENDOR_URL_URI                                 = FEDORA_NAMESPACE + 'repositoryJcrRepositoryVendorUrl'
    FEDORA_REPOSITORY_JCR_REPOSITORY_VERSION_URI                                    = FEDORA_NAMESPACE + 'repositoryJcrRepositoryVersion'
    FEDORA_REPOSITORY_JCR_SPECIFICATION_NAME_URI                                    = FEDORA_NAMESPACE + 'repositoryJcrSpecificationName'
    FEDORA_REPOSITORY_JCR_SPECIFICATION_VERSOIN_URI                                 = FEDORA_NAMESPACE + 'repositoryJcrSpecificationVersion'
    FEDORA_REPOSITORY_LEVEL_1_SUPPORTED_URI                                         = FEDORA_NAMESPACE + 'repositoryLevel1Supported'
    FEDORA_REPOSITORY_LEVEL_2_SUPPORTED_URI                                         = FEDORA_NAMESPACE + 'repositoryLevel2Supported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_AUTOCREATED_DEFINITIONS_SUPPORTS_URI     = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementAutocreatedDefinitionsSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_INHERITANCE_URI                          = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementInheritance'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_MULTIPLE_BINARY_PROPERTIES_SUPPORTED_URI = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementMultipleBinaryPropertiesSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_MULTIVALUED_PROPERTIES_SUPPORTED_URI     = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementMultivaluedPropertiesSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_OVERRIDES_SUPPORTED_URI                  = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementOverridesSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_PRIMARY_ITEM_NAME_SUPPORTED_URI          = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementPrimaryItemNameSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_PROPERTY_TYPES_URI                       = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementPropertyTypes'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_RESIDUAL_DEFINITIONS_SUPPORTED_URI       = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementResidualDefinitionsSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_SAME_NAME_SIBLINGS_SUPPORTED_URI         = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementSameNameSiblingsSupported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_UPDATE_IN_USE_SUPPORTED_URI              = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementUpdateInUseSuported'
    FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_VALUE_CONSTRAINTS_SUPPORTED_URI          = FEDORA_NAMESPACE + 'repositoryNodeTypeManagementValueConstraintsSupported'
    FEDORA_REPOSITORY_OPTION_ACCESS_CONTROL_SUPPORTED_URI                           = FEDORA_NAMESPACE + 'repositoryOptionAccessControlSupported'
    FEDORA_REPOSITORY_OPTION_ACTIVITIES_SUPPORTED_URI                               = FEDORA_NAMESPACE + 'repositoryOptionActivitiesSupported'
    FEDORA_REPOSITORY_OPTION_BASELINES_SUPPORTED_URI                                = FEDORA_NAMESPACE + 'repositoryOptionBaselinesSupported'
    FEDORA_REPOSITORY_OPTION_JOURNALED_OBSERVATION_SUPPORTED_URI                    = FEDORA_NAMESPACE + 'repositoryOptionJournaledObservationSupported'
    FEDORA_REPOSITORY_OPTION_LIFECYCLE_SUPPORTED_URI                                = FEDORA_NAMESPACE + 'repositoryOptionLifecycleSupported'
    FEDORA_REPOSITORY_OPTION_LOCKING_SUPPORTED_URI                                  = FEDORA_NAMESPACE + 'repositoryOptionLockingSupported'
    FEDORA_REPOSITORY_OPTION_NODE_AND_PROPERTY_WITH_SAME_NAME_SUPPORTED_URI         = FEDORA_NAMESPACE + 'repositoryOptionNodeAndPropertyWithSameNameSupported'
    FEDORA_REPOSITORY_OPTION_NODE_TYPE_MANAGEMENT_SUPPORTED_URI                     = FEDORA_NAMESPACE + 'repositoryOptionNodeTypeManagementSupported'
    FEDORA_REPOSITORY_OPTION_OBSERVATION_SUPPORTED_URI                              = FEDORA_NAMESPACE + 'repositoryOptionObservationSupported'
    FEDORA_REPOSITORY_OPTION_QUERY_SQL_SUPPORTED_URI                                = FEDORA_NAMESPACE + 'repositoryOptionQuerySqlSupported'
    FEDORA_REPOSITORY_OPTION_RETENTION_SUPPORTED_URI                                = FEDORA_NAMESPACE + 'repositoryOptionRetentionSupported'
    FEDORA_REPOSITORY_OPTION_SHAREABLE_NODES_SUPPORTED_URI                          = FEDORA_NAMESPACE + 'repositoryOptionShareableNodesSupported'
    FEDORA_REPOSITORY_OPTION_SIMPLE_VERSIONING_SUPPORTED_URI                        = FEDORA_NAMESPACE + 'repositoryOptionSimpleVersioningSupported'
    FEDORA_REPOSITORY_OPTION_TRANSACTIONS_SUPPORTED_URI                             = FEDORA_NAMESPACE + 'repositoryOptionTransactionsSupported'
    FEDORA_REPOSITORY_OPTION_UNFILED_CONTENT_SUPPORTED_URI                          = FEDORA_NAMESPACE + 'repositoryOptionUnfiledContentSupported'
    FEDORA_REPOSITORY_OPTION_UPDATE_MIXIN_NODE_TYPES_SUPPORTED_URI                  = FEDORA_NAMESPACE + 'repositoryOptionUpdateMixinNodeTypesSupported'
    FEDORA_REPOSITORY_OPTION_UPDATE_PRIMARY_NODE_TYPE_SUPPORTED_URI                 = FEDORA_NAMESPACE + 'repositoryOptionUpdatePrimaryNodeTypeSupported'
    FEDORA_REPOSITORY_OPTION_VERSIONING_SUPPORTED_URI                               = FEDORA_NAMESPACE + 'repositoryOptionVersioningSupported'
    FEDORA_REPOSITORY_OPTION_XML_EXPORT_SUPPORTED_URI                               = FEDORA_NAMESPACE + 'repositoryOptionXmlExportSupported'
    FEDORA_REPOSITORY_OPTION_XML_IMPORT_SUPPORTED_URI                               = FEDORA_NAMESPACE + 'repositoryOptionXmlImportSupported'
    FEDORA_REPOSITORY_QUERY_FULL_TEXT_SEARCH_SUPPORTED_URI                          = FEDORA_NAMESPACE + 'repositoryQueryFullTextSearchSupported'
    FEDORA_REPOSITORY_QUERY_JOINS_URI                                               = FEDORA_NAMESPACE + 'repositoryQueryJoins'
    FEDORA_REPOSITORY_QUERY_STORED_QUERIES_SUPPORTED_URI                            = FEDORA_NAMESPACE + 'repositoryQueryStoredQueriesSupported'
    FEDORA_REPOSITORY_QUERY_XPATH_DOC_ORDER_URI                                     = FEDORA_NAMESPACE + 'repositoryQueryXpathDocOrder'
    FEDORA_REPOSITORY_QUERY_XPATH_POS_INDEX_URI                                     = FEDORA_NAMESPACE + 'repositoryQueryXpathDocOrder'
    FEDORA_REPOSITORY_WRITE_SUPPORTED_URI                                           = FEDORA_NAMESPACE + 'repositoryWriteSupported'
    FEDORA_UUID_URI                                                                 = FEDORA_NAMESPACE + 'uuid'
    FEDORA_WRITABLE_URI                                                             = FEDORA_NAMESPACE + 'writable'
    W3_CONTAINS_URI                                                                 = 'http://www.w3.org/ns/ldp#contains'

    __content_container         = None

    def content(content_container):
        if not content_container:
            return

        self.__content_container = content_container

    def parse(self, json_content=None, parse_root_element=False):

        parsed_data = {}

        json_content = self.__content_container if not json_content else json_content

        primary_content = json_content[1]

        parsed_data['exports_as'] = primary_content[self.FEDORA_EXPORTS_AS_URI][0][self.FEDORA_ID]

        parsed_data['has_transaction_provinder']                                        = primary_content[self.FEDORA_HAS_TRANSACTION_PROVIDER_URI][0][self.FEDORA_ID] 
        parsed_data['repository_custom_rep_name']                                       = primary_content[self.FEDORA_REPOSITORY_CUSTOM_REP_NAME_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_identifier_stability']                                  = primary_content[self.FEDORA_REPOSITORY_IDENTIFIER_STABILITY_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_repository_name']                                   = primary_content[self.FEDORA_REPOSITORY_JCR_REPOSITORY_NAME_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_repository_vendor']                                 = primary_content[self.FEDORA_REPOSITORY_JCR_REPOSITORY_VENDOR_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_repository_vendor_url']                             = primary_content[self.FEDORA_REPOSITORY_JCR_REPOSITORY_VENDOR_URL_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_repository_version']                                = primary_content[self.FEDORA_REPOSITORY_JCR_REPOSITORY_VERSION_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_specification_name']                                = primary_content[self.FEDORA_REPOSITORY_JCR_SPECIFICATION_NAME_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_jcr_specification_versoin']                             = primary_content[self.FEDORA_REPOSITORY_JCR_SPECIFICATION_VERSOIN_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_level_1_supported']                                     = primary_content[self.FEDORA_REPOSITORY_LEVEL_1_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_level_2_supported']                                     = primary_content[self.FEDORA_REPOSITORY_LEVEL_2_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_node_type_management_autocreated_definitions_supports'] = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_AUTOCREATED_DEFINITIONS_SUPPORTS_URI][0][self.FEDORA_VALUE] 

        parsed_data['repository_node_type_management_inheritance']                          = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_INHERITANCE_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_node_type_management_multiple_binary_properties_supported'] = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_MULTIPLE_BINARY_PROPERTIES_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_multivalued_properties_supported']     = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_MULTIVALUED_PROPERTIES_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_overrides_supported']                  = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_OVERRIDES_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_primary_item_name_supported']          = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_PRIMARY_ITEM_NAME_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_property_types']                       = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_PROPERTY_TYPES_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_node_type_management_residual_definitions_supported']       = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_RESIDUAL_DEFINITIONS_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_same_name_siblings_supported']         = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_SAME_NAME_SIBLINGS_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_update_in_use_supported']              = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_UPDATE_IN_USE_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_node_type_management_value_constraints_supported']          = primary_content[self.FEDORA_REPOSITORY_NODE_TYPE_MANAGEMENT_VALUE_CONSTRAINTS_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_option_access_control_supported']                           = primary_content[self.FEDORA_REPOSITORY_OPTION_ACCESS_CONTROL_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_option_activities_supported']                               = primary_content[self.FEDORA_REPOSITORY_OPTION_ACTIVITIES_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_baselines_supported']                                = primary_content[self.FEDORA_REPOSITORY_OPTION_BASELINES_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_journaled_observation_supported']                    = primary_content[self.FEDORA_REPOSITORY_OPTION_JOURNALED_OBSERVATION_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_option_lifecycle_supported']                                = primary_content[self.FEDORA_REPOSITORY_OPTION_LIFECYCLE_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_locking_supported']                                  = primary_content[self.FEDORA_REPOSITORY_OPTION_LOCKING_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_node_and_property_with_same_name_supported']         = primary_content[self.FEDORA_REPOSITORY_OPTION_NODE_AND_PROPERTY_WITH_SAME_NAME_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_node_type_management_supported']                     = primary_content[self.FEDORA_REPOSITORY_OPTION_NODE_TYPE_MANAGEMENT_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_observation_supported']                              = primary_content[self.FEDORA_REPOSITORY_OPTION_OBSERVATION_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_query_sql_supported']                                = primary_content[self.FEDORA_REPOSITORY_OPTION_QUERY_SQL_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_retention_supported']                                = primary_content[self.FEDORA_REPOSITORY_OPTION_RETENTION_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_shareable_nodes_supported']                          = primary_content[self.FEDORA_REPOSITORY_OPTION_SHAREABLE_NODES_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_simple_versioning_supported']                        = primary_content[self.FEDORA_REPOSITORY_OPTION_SIMPLE_VERSIONING_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_transactions_supported']                             = primary_content[self.FEDORA_REPOSITORY_OPTION_TRANSACTIONS_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_unfiled_content_supported']                          = primary_content[self.FEDORA_REPOSITORY_OPTION_UNFILED_CONTENT_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_update_mixin_node_types_supported']                  = primary_content[self.FEDORA_REPOSITORY_OPTION_UPDATE_MIXIN_NODE_TYPES_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_update_primary_node_type_supported']                 = primary_content[self.FEDORA_REPOSITORY_OPTION_UPDATE_PRIMARY_NODE_TYPE_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_versioning_supported']                               = primary_content[self.FEDORA_REPOSITORY_OPTION_VERSIONING_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_xml_export_supported']                               = primary_content[self.FEDORA_REPOSITORY_OPTION_XML_EXPORT_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_option_xml_import_supported']                               = primary_content[self.FEDORA_REPOSITORY_OPTION_XML_IMPORT_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_query_full_text_search_supported']                          = primary_content[self.FEDORA_REPOSITORY_QUERY_FULL_TEXT_SEARCH_SUPPORTED_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_query_joins']                                               = primary_content[self.FEDORA_REPOSITORY_QUERY_JOINS_URI][0][self.FEDORA_VALUE]
        parsed_data['repository_query_stored_queries_supported']                            = primary_content[self.FEDORA_REPOSITORY_QUERY_STORED_QUERIES_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_query_xpath_doc_order']                                     = primary_content[self.FEDORA_REPOSITORY_QUERY_XPATH_DOC_ORDER_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_query_xpath_pos_index']                                     = primary_content[self.FEDORA_REPOSITORY_QUERY_XPATH_POS_INDEX_URI][0][self.FEDORA_VALUE] 
        parsed_data['repository_write_supported']                                           = primary_content[self.FEDORA_REPOSITORY_WRITE_SUPPORTED_URI][0][self.FEDORA_VALUE] 
        parsed_data['uuid']                                                                 = primary_content[self.FEDORA_UUID_URI][0][self.FEDORA_VALUE]
        parsed_data['writable']                                                             = primary_content[self.FEDORA_WRITABLE_URI][0][self.FEDORA_VALUE] 

        parsed_data['contains'] = []
        for k in primary_content[self.W3_CONTAINS_URI]: 
            parsed_data['contains'].append(k[self.FEDORA_ID])

        parsed_data['types'] = []
        for k in primary_content[self.FEDORA_TYPE]:
            parsed_data['types'].append(k)

        parsed_data['has_node_types'] = []
        for k in primary_content[self.FEDORA_HAS_NODE_TYPE_URI]:
            parsed_data['has_node_types'].append(k[self.FEDORA_VALUE])

        parsed_data['id'] = primary_content[self.FEDORA_ID]

        return parsed_data
