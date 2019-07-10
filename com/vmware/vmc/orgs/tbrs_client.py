# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.tbrs.
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


class Reservation(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.tbrs.reservation'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReservationStub)


    def post(self,
             org,
             sddc_state=None,
             ):
        """
        Retreive all reservations for all SDDCs in this org

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc_state: :class:`com.vmware.vmc.model_client.SddcStateRequest` or ``None``
        :param sddc_state: SDDCs and/or states to query (optional)
        :rtype: :class:`dict` of :class:`str` and :class:`list` of :class:`com.vmware.vmc.model_client.ReservationWindow`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Call
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('post',
                            {
                            'org': org,
                            'sddc_state': sddc_state,
                            })
class SupportWindow(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.tbrs.support_window'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SupportWindowStub)


    def get(self,
            org,
            ):
        """
        Get all available support windows

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SupportWindow`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid request
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             No support windows are available
        """
        return self._invoke('get',
                            {
                            'org': org,
                            })

    def put(self,
            org,
            id,
            sddc_id,
            ):
        """
        Move Sddc to new support window

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  id: :class:`str`
        :param id: Target Support Window ID (required)
        :type  sddc_id: :class:`com.vmware.vmc.model_client.SddcId`
        :param sddc_id: SDDC to move (required)
        :rtype: :class:`com.vmware.vmc.model_client.SupportWindowId`
        :return: com.vmware.vmc.model.SupportWindowId
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid request
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Feature does not exist
        """
        return self._invoke('put',
                            {
                            'org': org,
                            'id': id,
                            'sddc_id': sddc_id,
                            })
class _ReservationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_state': type.OptionalType(type.ReferenceType('com.vmware.vmc.model_client', 'SddcStateRequest')),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/tbrs/reservation',
            request_body_parameter='sddc_state',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'post': {
                'input_type': post_input_type,
                'output_type': type.MapType(type.StringType(), type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'ReservationWindow'))),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.tbrs.reservation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SupportWindowStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/tbrs/support-window',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for put operation
        put_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'id': type.StringType(),
            'sddc_id': type.ReferenceType('com.vmware.vmc.model_client', 'SddcId'),
        })
        put_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        put_input_value_validator_list = [
        ]
        put_output_validator_list = [
        ]
        put_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vmc/api/orgs/{org}/tbrs/support-window/{id}',
            request_body_parameter='sddc_id',
            path_variables={
                'org': 'org',
                'id': 'id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SupportWindow')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'put': {
                'input_type': put_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SupportWindowId'),
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
            self, iface_name='com.vmware.vmc.orgs.tbrs.support_window',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Reservation': Reservation,
        'SupportWindow': SupportWindow,
    }

