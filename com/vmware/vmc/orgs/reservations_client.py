# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.reservations.
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


class Mw(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.reservations.mw'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MwStub)


    def get(self,
            org,
            reservation,
            ):
        """
        get the maintenance window for this SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  reservation: :class:`str`
        :param reservation: Reservation Identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.MaintenanceWindowGet`
        :return: com.vmware.vmc.model.MaintenanceWindowGet
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'reservation': reservation,
                            })

    def put(self,
            org,
            reservation,
            window,
            ):
        """
        update the maintenance window for this SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  reservation: :class:`str`
        :param reservation: Reservation Identifier (required)
        :type  window: :class:`com.vmware.vmc.model_client.MaintenanceWindow`
        :param window: Maintenance Window (required)
        :rtype: :class:`com.vmware.vmc.model_client.MaintenanceWindow`
        :return: com.vmware.vmc.model.MaintenanceWindow
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict with exiting reservation
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The reservation is not in a state that's valid for updates
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        """
        return self._invoke('put',
                            {
                            'org': org,
                            'reservation': reservation,
                            'window': window,
                            })
class _MwStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'reservation': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/reservations/{reservation}/mw',
            path_variables={
                'org': 'org',
                'reservation': 'reservation',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for put operation
        put_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'reservation': type.StringType(),
            'window': type.ReferenceType('com.vmware.vmc.model_client', 'MaintenanceWindow'),
        })
        put_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        put_input_value_validator_list = [
        ]
        put_output_validator_list = [
        ]
        put_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vmc/api/orgs/{org}/reservations/{reservation}/mw',
            request_body_parameter='window',
            path_variables={
                'org': 'org',
                'reservation': 'reservation',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'MaintenanceWindowGet'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'put': {
                'input_type': put_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'MaintenanceWindow'),
                'errors': put_error_dict,
                'input_value_validator_list': put_input_value_validator_list,
                'output_validator_list': put_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'put': put_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.reservations.mw',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Mw': Mw,
    }

