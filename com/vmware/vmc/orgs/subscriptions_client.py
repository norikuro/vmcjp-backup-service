# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.subscriptions.
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


class OfferInstances(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.subscriptions.offer_instances'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OfferInstancesStub)


    def list(self,
             org,
             region,
             product_type,
             product=None,
             type=None,
             ):
        """
        List all offers available for the specific product type in the specific
        region

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  region: :class:`str`
        :param region: Region for the offer (required)
        :type  product_type: :class:`str`
        :param product_type: Type of the product in offers. \*This has been deprecated\*. Please
            use product & type parameters (required)
        :type  product: :class:`str` or ``None``
        :param product: The product that you are trying to purchase, eg. host. This needs
            to be accompanied by the type parameter (optional)
        :type  type: :class:`str` or ``None``
        :param type: The type/flavor of the product you are trying it purchase,eg. an
            \\\\`r5.metal\\\\` host. This needs to be accompanied by the
            product parameter. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.OfferInstancesHolder`
        :return: com.vmware.vmc.model.OfferInstancesHolder
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request. Type of the product not supported.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'region': region,
                            'product_type': product_type,
                            'product': product,
                            'type': type,
                            })
class Products(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.subscriptions.products'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProductsStub)


    def list(self,
             org,
             ):
        """
        List of all the products that are available for purchase.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SubscriptionProducts`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal server error
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class _OfferInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'region': type.StringType(),
            'product_type': type.StringType(),
            'product': type.OptionalType(type.StringType()),
            'type': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions/offer-instances',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'region': 'region',
                'product_type': 'product_type',
                'product': 'product',
                'type': 'type',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'OfferInstancesHolder'),
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
            self, iface_name='com.vmware.vmc.orgs.subscriptions.offer_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ProductsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions/products',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionProducts')),
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
            self, iface_name='com.vmware.vmc.orgs.subscriptions.products',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'OfferInstances': OfferInstances,
        'Products': Products,
    }

