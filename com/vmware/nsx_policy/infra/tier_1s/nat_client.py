# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.tier_1s.nat.
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


class NatRules(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NatRulesStub)


    def delete(self,
               tier1_id,
               nat_id,
               nat_rule_id,
               ):
        """
        Delete NAT Rule.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  nat_id: :class:`str`
        :param nat_id: NAT id (required)
        :type  nat_rule_id: :class:`str`
        :param nat_rule_id: Rule ID (required)
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
        return self._invoke('delete',
                            {
                            'tier1_id': tier1_id,
                            'nat_id': nat_id,
                            'nat_rule_id': nat_rule_id,
                            })

    def get(self,
            tier1_id,
            nat_id,
            nat_rule_id,
            ):
        """
        Get NAT Rule.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  nat_id: :class:`str`
        :param nat_id: NAT id (required)
        :type  nat_rule_id: :class:`str`
        :param nat_rule_id: Rule ID (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyNatRule`
        :return: com.vmware.nsx_policy.model.PolicyNatRule
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
                            'tier1_id': tier1_id,
                            'nat_id': nat_id,
                            'nat_rule_id': nat_rule_id,
                            })

    def list(self,
             tier1_id,
             nat_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List NAT Rules.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  nat_id: :class:`str`
        :param nat_id: NAT id (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyNatRuleListResult`
        :return: com.vmware.nsx_policy.model.PolicyNatRuleListResult
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
                            'tier1_id': tier1_id,
                            'nat_id': nat_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier1_id,
              nat_id,
              nat_rule_id,
              policy_nat_rule,
              ):
        """
        If a NAT Rule is not already present on Tier-1 denoted by Tier-1 ID,
        create a new NAT Rule. If it already exists, update the NAT Rule.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  nat_id: :class:`str`
        :param nat_id: NAT id (required)
        :type  nat_rule_id: :class:`str`
        :param nat_rule_id: Rule ID (required)
        :type  policy_nat_rule: :class:`com.vmware.nsx_policy.model_client.PolicyNatRule`
        :param policy_nat_rule: (required)
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
        return self._invoke('patch',
                            {
                            'tier1_id': tier1_id,
                            'nat_id': nat_id,
                            'nat_rule_id': nat_rule_id,
                            'policy_nat_rule': policy_nat_rule,
                            })

    def update(self,
               tier1_id,
               nat_id,
               nat_rule_id,
               policy_nat_rule,
               ):
        """
        Update NAT Rule.

        :type  tier1_id: :class:`str`
        :param tier1_id: Tier-1 ID (required)
        :type  nat_id: :class:`str`
        :param nat_id: NAT id (required)
        :type  nat_rule_id: :class:`str`
        :param nat_rule_id: Rule ID (required)
        :type  policy_nat_rule: :class:`com.vmware.nsx_policy.model_client.PolicyNatRule`
        :param policy_nat_rule: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.PolicyNatRule`
        :return: com.vmware.nsx_policy.model.PolicyNatRule
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
        return self._invoke('update',
                            {
                            'tier1_id': tier1_id,
                            'nat_id': nat_id,
                            'nat_rule_id': nat_rule_id,
                            'policy_nat_rule': policy_nat_rule,
                            })
class _NatRulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'nat_id': type.StringType(),
            'nat_rule_id': type.StringType(),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'nat_id': 'nat-id',
                'nat_rule_id': 'nat-rule-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'nat_id': type.StringType(),
            'nat_rule_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}',
            path_variables={
                'tier1_id': 'tier-1-id',
                'nat_id': 'nat-id',
                'nat_rule_id': 'nat-rule-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'nat_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules',
            path_variables={
                'tier1_id': 'tier-1-id',
                'nat_id': 'nat-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'nat_id': type.StringType(),
            'nat_rule_id': type.StringType(),
            'policy_nat_rule': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyNatRule'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}',
            request_body_parameter='policy_nat_rule',
            path_variables={
                'tier1_id': 'tier-1-id',
                'nat_id': 'nat-id',
                'nat_rule_id': 'nat-rule-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier1_id': type.StringType(),
            'nat_id': type.StringType(),
            'nat_rule_id': type.StringType(),
            'policy_nat_rule': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyNatRule'),
        })
        update_error_dict = {
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
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-1s/{tier-1-id}/nat/{nat-id}/nat-rules/{nat-rule-id}',
            request_body_parameter='policy_nat_rule',
            path_variables={
                'tier1_id': 'tier-1-id',
                'nat_id': 'nat-id',
                'nat_rule_id': 'nat-rule-id',
            },
            query_parameters={
            }
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyNatRule'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyNatRuleListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'PolicyNatRule'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_1s.nat.nat_rules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'NatRules': NatRules,
    }

