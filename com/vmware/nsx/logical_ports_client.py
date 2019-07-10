# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.logical_ports.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class ForwardingPath(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ForwardingPathStub)


    def get(self,
            lport_id,
            peer_port_id,
            ):
        """
        Get networking entities between two logical ports with VIF attachment

        :type  lport_id: :class:`str`
        :param lport_id: ID of source port (required)
        :type  peer_port_id: :class:`str`
        :param peer_port_id: ID of peer port (required)
        :rtype: :class:`com.vmware.nsx.model_client.PortConnectionEntities`
        :return: com.vmware.nsx.model.PortConnectionEntities
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'lport_id': lport_id,
                            'peer_port_id': peer_port_id,
                            })
class MacTable(VapiInterface):
    """
    
    """
    LIST_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`MacTable.list`.

    """
    LIST_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`MacTable.list`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MacTableStub)


    def list(self,
             lport_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             source=None,
             transport_node_id=None,
             ):
        """
        Returns MAC table of a specified logical port. If the target transport
        node id is not provided, the NSX manager will ask the controller for
        the transport node where the logical port is located. The query
        parameter \\\\"source=cached\\\\" is not supported.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  transport_node_id: :class:`str` or ``None``
        :param transport_node_id: TransportNode Id (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortMacAddressListResult`
        :return: com.vmware.nsx.model.LogicalPortMacAddressListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'lport_id': lport_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'transport_node_id': transport_node_id,
                            })
class State(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StateStub)


    def get(self,
            lport_id,
            ):
        """
        Returns transport node id for a specified logical port. Also returns
        information about all address bindings of the specified logical port.
        This includes address bindings discovered via various snooping methods
        like ARP snooping, DHCP snooping etc. and addressing bindings that are
        realized based on user configuration.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortState`
        :return: com.vmware.nsx.model.LogicalPortState
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'lport_id': lport_id,
                            })
class Statistics(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Statistics.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Statistics.get`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatisticsStub)


    def get(self,
            lport_id,
            source=None,
            ):
        """
        Returns statistics of a specified logical port. If the logical port is
        attached to a logical router port, query parameter
        \\\\"source=realtime\\\\" is not supported.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortStatistics`
        :return: com.vmware.nsx.model.LogicalPortStatistics
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'lport_id': lport_id,
                            'source': source,
                            })
class Status(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """
    GETALL_ATTACHMENT_TYPE_VIF = "VIF"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_LOGICALROUTER = "LOGICALROUTER"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_BRIDGEENDPOINT = "BRIDGEENDPOINT"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_DHCP_SERVICE = "DHCP_SERVICE"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_METADATA_PROXY = "METADATA_PROXY"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_L2VPN_SESSION = "L2VPN_SESSION"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_ATTACHMENT_TYPE_NONE = "NONE"
    """
    Possible value for ``attachmentType`` of method :func:`Status.getall`.

    """
    GETALL_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.getall`.

    """
    GETALL_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.getall`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def get(self,
            lport_id,
            source=None,
            ):
        """
        Returns operational status of a specified logical port.

        :type  lport_id: :class:`str`
        :param lport_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortOperationalStatus`
        :return: com.vmware.nsx.model.LogicalPortOperationalStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'lport_id': lport_id,
                            'source': source,
                            })

    def getall(self,
               attachment_id=None,
               attachment_type=None,
               bridge_cluster_id=None,
               container_ports_only=None,
               cursor=None,
               diagnostic=None,
               included_fields=None,
               logical_switch_id=None,
               page_size=None,
               parent_vif_id=None,
               sort_ascending=None,
               sort_by=None,
               source=None,
               switching_profile_id=None,
               transport_node_id=None,
               transport_zone_id=None,
               ):
        """
        Returns operational status of all logical ports. The query parameter
        \\\\"source=realtime\\\\" is not supported.

        :type  attachment_id: :class:`str` or ``None``
        :param attachment_id: Logical Port attachment Id (optional)
        :type  attachment_type: :class:`str` or ``None``
        :param attachment_type: Type of attachment for logical port; for query only. (optional)
        :type  bridge_cluster_id: :class:`str` or ``None``
        :param bridge_cluster_id: Bridge Cluster identifier (optional)
        :type  container_ports_only: :class:`bool` or ``None``
        :param container_ports_only: Only container VIF logical ports will be returned if true
            (optional, default to false)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  diagnostic: :class:`bool` or ``None``
        :param diagnostic: Flag to enable showing of transit logical port. (optional, default
            to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  logical_switch_id: :class:`str` or ``None``
        :param logical_switch_id: Logical Switch identifier (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  parent_vif_id: :class:`str` or ``None``
        :param parent_vif_id: ID of the VIF of type PARENT (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  switching_profile_id: :class:`str` or ``None``
        :param switching_profile_id: Network Profile identifier (optional)
        :type  transport_node_id: :class:`str` or ``None``
        :param transport_node_id: Transport node identifier (optional)
        :type  transport_zone_id: :class:`str` or ``None``
        :param transport_zone_id: Transport zone identifier (optional)
        :rtype: :class:`com.vmware.nsx.model_client.LogicalPortStatusSummary`
        :return: com.vmware.nsx.model.LogicalPortStatusSummary
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('getall',
                            {
                            'attachment_id': attachment_id,
                            'attachment_type': attachment_type,
                            'bridge_cluster_id': bridge_cluster_id,
                            'container_ports_only': container_ports_only,
                            'cursor': cursor,
                            'diagnostic': diagnostic,
                            'included_fields': included_fields,
                            'logical_switch_id': logical_switch_id,
                            'page_size': page_size,
                            'parent_vif_id': parent_vif_id,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'switching_profile_id': switching_profile_id,
                            'transport_node_id': transport_node_id,
                            'transport_zone_id': transport_zone_id,
                            })
class _ForwardingPathStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'peer_port_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/{lport-id}/forwarding-path',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
                'peer_port_id': 'peer_port_id',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PortConnectionEntities'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_ports.forwarding_path',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _MacTableStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'transport_node_id': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/{lport-id}/mac-table',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'transport_node_id': 'transport_node_id',
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortMacAddressListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_ports.mac_table',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StateStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/{lport-id}/state',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortState'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_ports.state',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatisticsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/{lport-id}/statistics',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
                'source': 'source',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortStatistics'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_ports.statistics',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'lport_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/{lport-id}/status',
            path_variables={
                'lport_id': 'lport-id',
            },
            query_parameters={
                'source': 'source',
            }
        )

        # properties for getall operation
        getall_input_type = type.StructType('operation-input', {
            'attachment_id': type.OptionalType(type.StringType()),
            'attachment_type': type.OptionalType(type.StringType()),
            'bridge_cluster_id': type.OptionalType(type.StringType()),
            'container_ports_only': type.OptionalType(type.BooleanType()),
            'cursor': type.OptionalType(type.StringType()),
            'diagnostic': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'logical_switch_id': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'parent_vif_id': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'switching_profile_id': type.OptionalType(type.StringType()),
            'transport_node_id': type.OptionalType(type.StringType()),
            'transport_zone_id': type.OptionalType(type.StringType()),
        })
        getall_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        getall_input_value_validator_list = [
        ]
        getall_output_validator_list = [
        ]
        getall_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-ports/status',
            path_variables={
            },
            query_parameters={
                'attachment_id': 'attachment_id',
                'attachment_type': 'attachment_type',
                'bridge_cluster_id': 'bridge_cluster_id',
                'container_ports_only': 'container_ports_only',
                'cursor': 'cursor',
                'diagnostic': 'diagnostic',
                'included_fields': 'included_fields',
                'logical_switch_id': 'logical_switch_id',
                'page_size': 'page_size',
                'parent_vif_id': 'parent_vif_id',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'switching_profile_id': 'switching_profile_id',
                'transport_node_id': 'transport_node_id',
                'transport_zone_id': 'transport_zone_id',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortOperationalStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'getall': {
                'input_type': getall_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'LogicalPortStatusSummary'),
                'errors': getall_error_dict,
                'input_value_validator_list': getall_input_value_validator_list,
                'output_validator_list': getall_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'getall': getall_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_ports.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ForwardingPath': ForwardingPath,
        'MacTable': MacTable,
        'State': State,
        'Statistics': Statistics,
        'Status': Status,
    }

