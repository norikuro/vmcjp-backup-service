# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.administration.
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


class AuditLogs(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AuditLogsStub)


    def create(self,
               audit_log_request,
               cursor=None,
               fields=None,
               page_size=None,
               ):
        """
        This API is executed on a manager node to display audit logs from all
        nodes inside the management plane cluster. An audit log collection will
        be triggered if the local master audit log is outdated.

        :type  audit_log_request: :class:`com.vmware.nsx.model_client.AuditLogRequest`
        :param audit_log_request: (required)
        :type  cursor: :class:`long` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  fields: :class:`str` or ``None``
        :param fields: Fields to include in query results (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 100)
        :rtype: :class:`com.vmware.nsx.model_client.AuditLogListResult`
        :return: com.vmware.nsx.model.AuditLogListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error, Bad Gateway
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'audit_log_request': audit_log_request,
                            'cursor': cursor,
                            'fields': fields,
                            'page_size': page_size,
                            })
class SupportBundles(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SupportBundlesStub)


    def collect(self,
                support_bundle_request,
                override_async_response=None,
                ):
        """
        Collect support bundles from registered cluster and fabric nodes.

        :type  support_bundle_request: :class:`com.vmware.nsx.model_client.SupportBundleRequest`
        :param support_bundle_request: (required)
        :type  override_async_response: :class:`bool` or ``None``
        :param override_async_response: Override any existing support bundle async response (optional,
            default to false)
        :rtype: :class:`com.vmware.nsx.model_client.SupportBundleResult`
        :return: com.vmware.nsx.model.SupportBundleResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error, Bad Gateway
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('collect',
                            {
                            'support_bundle_request': support_bundle_request,
                            'override_async_response': override_async_response,
                            })
class _AuditLogsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'audit_log_request': type.ReferenceType('com.vmware.nsx.model_client', 'AuditLogRequest'),
            'cursor': type.OptionalType(type.IntegerType()),
            'fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/administration/audit-logs',
            request_body_parameter='audit_log_request',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'fields': 'fields',
                'page_size': 'page_size',
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'AuditLogListResult'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.administration.audit_logs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SupportBundlesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for collect operation
        collect_input_type = type.StructType('operation-input', {
            'support_bundle_request': type.ReferenceType('com.vmware.nsx.model_client', 'SupportBundleRequest'),
            'override_async_response': type.OptionalType(type.BooleanType()),
        })
        collect_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        collect_input_value_validator_list = [
        ]
        collect_output_validator_list = [
        ]
        collect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/administration/support-bundles?action=collect',
            request_body_parameter='support_bundle_request',
            path_variables={
            },
            query_parameters={
                'override_async_response': 'override_async_response',
            }
        )

        operations = {
            'collect': {
                'input_type': collect_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SupportBundleResult'),
                'errors': collect_error_dict,
                'input_value_validator_list': collect_input_value_validator_list,
                'output_validator_list': collect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'collect': collect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.administration.support_bundles',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'AuditLogs': AuditLogs,
        'SupportBundles': SupportBundles,
    }

